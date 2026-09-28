#!/usr/bin/env python3
"""Heuristic collision checker for anti-collapse divergence frames.

Input: JSON list of frame objects.
Expected fields may include:
- frame / name
- mechanism
- actor
- trigger
- carrier / carrier_artifact
- pressure_vector / pressure/vector / pressure / vector
- power_holder
- emotional_engine
- failure_mode

This script nominates candidate clusters using lexical, field-DNA, and
archetype overlap. Flags require semantic review, not automatic repair:
different mechanisms can share vocabulary, and duplicate mechanisms can
avoid this lexicon. Neither flags nor their absence certify a judgment.
Use `references/judge-protocol.md` for source-checked semantic review.

Exit codes: 0 = no candidate clusters, 1 = candidate clusters need review,
2 = invalid input. Legacy `collisions_found` and pairwise `collision` keys
remain heuristic flags, not confirmed collisions. `repair_needed: null`
means unknown until semantic review.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "by", "can", "for",
    "from", "has", "have", "if", "in", "into", "is", "it", "of", "on", "or",
    "that", "the", "their", "them", "then", "this", "to", "with", "without",
    "user", "users", "product", "tool", "system", "frame", "mechanism",
}

FIELD_ALIASES = {
    "frame": ["frame", "name", "label", "title"],
    "mechanism": ["mechanism", "causal_engine", "engine"],
    "actor": ["actor", "primary_actor", "adopter", "initiator"],
    "trigger": ["trigger", "trigger_moment", "cue", "moment"],
    "carrier": ["carrier", "carrier_artifact", "artifact", "workflow", "medium"],
    "pressure": ["pressure_vector", "pressure/vector", "pressure", "vector", "adoption_pressure", "distribution_vector"],
    "power_holder": ["power_holder", "beneficiary_power_holder", "beneficiary/power-holder", "beneficiary", "gatekeeper", "buyer"],
    "emotional_engine": ["emotional_engine", "emotion", "incentive_engine"],
    "failure_mode": ["failure_mode", "failure_condition", "failure", "risk"],
}

# Domain-general archetype lexicon. This is intentionally transparent so users
# can extend it for their own fields.
ARCHETYPES: dict[str, list[str]] = {
    "certification_attestation": [
        "certify", "certification", "certificate", "certified", "attest", "attestation",
        "proof", "prove", "verified", "verification", "stamp", "badge", "notary", "notarized",
        "audit proof", "clearance", "credential", "whitelist", "bill of materials", "bom",
        "diligence", "claim defense", "defence", "liability cover", "audit trail",
        "reject uncertified", "un certified", "un-certified",
    ],
    "mandated_gate": [
        "mandatory", "mandate", "required", "require", "approval", "gate", "gated",
        "checkpoint", "must", "cannot proceed", "won't advance", "process", "compliance",
        "policy", "doctrine", "sop", "standard operating", "pre filing", "pre-filing",
    ],
    "artifact_contagion": [
        "screenshot", "share", "shared", "forward", "verdict", "meme", "remix",
        "snippet", "report travels", "artifact travels", "contact event", "infect", "infection",
        "contagion", "viral", "r0", "spreads as", "circulat",
    ],
    "professional_standard": [
        "curriculum", "course", "training", "cohort", "bootcamp", "guild", "profession",
        "standard", "taxonomy", "vocabulary", "canon", "open standard", "protocol", "card id",
    ],
    "anxiety_relief_loop": [
        "anxiety", "doubt", "itch", "relief", "private", "embarrassment", "shame",
        "variable reward", "habit", "compulsive", "reassurance", "saved from", "worry",
    ],
    "enemy_movement": [
        "enemy", "movement", "activist", "insurgency", "resistance", "opponent", "villain",
        "grievance", "coalition", "counter propaganda", "propaganda", "hippo", "authority",
    ],
    "scarcity_prestige": [
        "luxury", "scarce", "scarcity", "exclusive", "exclusivity", "premium", "elite",
        "status", "rank", "prestige", "veblen", "gatekept", "price signal",
    ],
    "marketplace_sorting": [
        "marketplace", "dating", "sort", "sortable", "pool", "screen", "screening",
        "vet", "vetting", "adverse selection", "rankable", "matching", "unlock communication",
    ],
    "workflow_carrier": [
        "workflow", "file", "memo", "pull request", "pr", "ticket", "api", "intranet",
        "knowledge base", "pipeline", "handoff", "artifact", "existing flow", "desire path",
    ],
    "scoreboard_game": [
        "score", "scoreboard", "leaderboard", "rank", "achievement", "points", "pvp",
        "game", "gamif", "mastery", "ladder",
    ],
    "boundary_gate_validation": [
        "boundary", "interface", "validation", "validate", "compiler", "type-check", "type check",
        "parse", "reject invalid", "schema", "customs", "inspection", "quarantine", "sandbox",
    ],
    "ledger_history": [
        "ledger", "append-only", "append only", "event log", "audit log", "chain of custody",
        "history", "provenance", "immutable", "record", "decision log",
    ],
    "reconciliation_loop": [
        "reconcile", "reconciliation", "diff", "drift", "repair job", "sync", "mismatch",
        "eventual", "consistency", "backfill",
    ],
    "segmentation_slice": [
        "cohort", "segment", "geography", "region", "plan", "device", "persona", "breakdown",
        "dashboard", "funnel", "engagement", "metric slice",
    ],
    "expectation_mismatch": [
        "expectation", "promise", "positioning", "onboarding surprise", "sales misfit", "gap",
        "time to first win", "first win", "activation cliff",
    ],
    "trust_decay": [
        "trust decay", "trust", "reliability", "silent failure", "support delay", "pricing surprise",
        "confidence", "credibility erosion",
    ],
}


def norm(value: Any) -> str:
    text = str(value or "").lower().strip()
    text = text.replace("–", "-").replace("—", "-")
    text = re.sub(r"[^a-z0-9\s/-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", norm(text)) if len(t) > 2 and t not in STOPWORDS}


def char_ngrams(text: str, n: int = 4) -> set[str]:
    s = re.sub(r"\s+", " ", norm(text))
    if len(s) <= n:
        return {s} if s else set()
    return {s[i : i + n] for i in range(len(s) - n + 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 0.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cosine_counts(a: Iterable[str], b: Iterable[str]) -> float:
    ca: dict[str, int] = defaultdict(int)
    cb: dict[str, int] = defaultdict(int)
    for x in a:
        ca[x] += 1
    for x in b:
        cb[x] += 1
    if not ca or not cb:
        return 0.0
    dot = sum(ca[k] * cb.get(k, 0) for k in ca)
    na = math.sqrt(sum(v * v for v in ca.values()))
    nb = math.sqrt(sum(v * v for v in cb.values()))
    return dot / (na * nb) if na and nb else 0.0


def get_field(frame: dict[str, Any], field: str) -> str:
    for name in FIELD_ALIASES[field]:
        if name in frame:
            return norm(frame[name])
    return ""


def combined_text(frame: dict[str, Any]) -> str:
    fields = [get_field(frame, f) for f in FIELD_ALIASES]
    return " ".join(x for x in fields if x)


def infer_archetypes(text: str) -> list[str]:
    text_n = norm(text)
    hits: list[tuple[int, str]] = []
    for archetype, terms in ARCHETYPES.items():
        score = 0
        for term in terms:
            term_n = norm(term)
            if not term_n:
                continue
            if " " in term_n or "-" in term_n:
                if term_n in text_n:
                    score += 3
            elif re.search(rf"\b{re.escape(term_n)}", text_n):
                score += 1
        if score:
            hits.append((score, archetype))
    hits.sort(reverse=True)
    return [name for _, name in hits[:3]]


def field_similarity(f1: dict[str, Any], f2: dict[str, Any], field: str) -> float:
    a = get_field(f1, field)
    b = get_field(f2, field)
    if not a or not b:
        return 0.0
    return max(
        jaccard(tokens(a), tokens(b)),
        SequenceMatcher(None, a, b).ratio() * 0.75,
        jaccard(char_ngrams(a), char_ngrams(b)) * 0.85,
    )


def pair_similarity(f1: dict[str, Any], f2: dict[str, Any]) -> dict[str, Any]:
    t1 = combined_text(f1)
    t2 = combined_text(f2)
    token_sim = jaccard(tokens(t1), tokens(t2))
    char_sim = jaccard(char_ngrams(t1), char_ngrams(t2))
    seq_sim = SequenceMatcher(None, norm(t1), norm(t2)).ratio()

    dna_fields = ["actor", "trigger", "carrier", "pressure", "power_holder", "emotional_engine", "failure_mode"]
    field_sims = {field: field_similarity(f1, f2, field) for field in dna_fields}
    strong_field_matches = [k for k, v in field_sims.items() if v >= 0.42]

    arch1 = infer_archetypes(t1)
    arch2 = infer_archetypes(t2)
    shared_arch = sorted(set(arch1) & set(arch2))

    mechanism_sim = field_similarity(f1, f2, "mechanism")
    pressure_sim = field_sims["pressure"]
    carrier_sim = field_sims["carrier"]
    actor_sim = field_sims["actor"]
    trigger_sim = field_sims["trigger"]

    weighted = max(
        0.35 * token_sim + 0.25 * char_sim + 0.20 * seq_sim + 0.20 * mechanism_sim,
        0.25 * mechanism_sim + 0.20 * pressure_sim + 0.15 * carrier_sim + 0.15 * actor_sim + 0.15 * trigger_sim + 0.10 * min(len(shared_arch), 1),
    )

    reasons: list[str] = []
    if mechanism_sim >= 0.45:
        reasons.append("similar mechanism wording")
    if len(strong_field_matches) >= 3:
        reasons.append(f"{len(strong_field_matches)} similar mechanism-DNA fields: {', '.join(strong_field_matches)}")
    if shared_arch:
        reasons.append("shared archetype(s): " + ", ".join(shared_arch))
    if pressure_sim >= 0.45 and carrier_sim >= 0.35:
        reasons.append("similar pressure/vector and carrier")
    if token_sim >= 0.38 or char_sim >= 0.36:
        reasons.append("high lexical overlap")

    collision = False
    if mechanism_sim >= 0.62:
        collision = True
    if len(strong_field_matches) >= 3 and (mechanism_sim >= 0.30 or shared_arch):
        collision = True
    if shared_arch and pressure_sim >= 0.35 and (carrier_sim >= 0.30 or actor_sim >= 0.35 or trigger_sim >= 0.35):
        collision = True
    if weighted >= 0.48:
        collision = True

    return {
        "score": round(weighted, 3),
        "collision": collision,
        "reasons": reasons,
        "shared_archetypes": shared_arch,
        "field_sims": {k: round(v, 3) for k, v in field_sims.items()},
    }


def label(frame: dict[str, Any], i: int) -> str:
    return str(frame.get("frame") or frame.get("name") or frame.get("label") or f"frame-{i}")


def build_clusters(frames: list[dict[str, Any]], pair_results: dict[tuple[int, int], dict[str, Any]]) -> list[list[int]]:
    parent = list(range(len(frames)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for (i, j), result in pair_results.items():
        if result["collision"]:
            union(i, j)

    # Nominate overloaded archetype families even when pairwise wording differs.
    # Shared families can contain distinct mechanisms; review must decide.
    low_signal_arches = {"workflow_carrier"}
    arch_groups: dict[str, list[int]] = defaultdict(list)
    for idx, frame in enumerate(frames):
        for arch in infer_archetypes(combined_text(frame)):
            if arch not in low_signal_arches:
                arch_groups[arch].append(idx)
    for arch, idxs in arch_groups.items():
        if len(idxs) >= 3:
            first = idxs[0]
            for other in idxs[1:]:
                union(first, other)

    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(len(frames)):
        groups[find(i)].append(i)
    return [g for g in groups.values() if len(g) > 1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic collision checker for anti-collapse divergence frames")
    parser.add_argument("frames_json", help="Path to JSON list of frame objects")
    parser.add_argument("--markdown", action="store_true", help="Print markdown summary instead of JSON")
    parser.add_argument("--threshold", type=float, default=0.48, help="Reporting threshold for pairwise candidates")
    args = parser.parse_args()

    path = Path(args.frames_json)
    try:
        frames = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"Could not read JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(frames, list) or not all(isinstance(x, dict) for x in frames):
        print("Input must be a JSON list of frame objects", file=sys.stderr)
        return 2

    pair_results: dict[tuple[int, int], dict[str, Any]] = {}
    for i, j in combinations(range(len(frames)), 2):
        pair_results[(i, j)] = pair_similarity(frames[i], frames[j])

    clusters = build_clusters(frames, pair_results)

    # Deliberately do not calculate a 0-100 semantic-spread score. In practice
    # that number is easy to miscalibrate and can create false confidence.
    # Flagged clusters require review, not automatic repair. Both false
    # positives and false negatives are possible with these heuristics.
    pair_candidates = []
    for (i, j), result in pair_results.items():
        if result["collision"] or result["score"] >= args.threshold:
            pair_candidates.append({
                "frames": [label(frames[i], i + 1), label(frames[j], j + 1)],
                "similarity_signal": result["score"],
                "collision": result["collision"],
                "reasons": result["reasons"],
                "shared_archetypes": result["shared_archetypes"],
            })
    pair_candidates.sort(key=lambda x: x["similarity_signal"], reverse=True)

    cluster_payload = []
    for group in clusters:
        arch_counts: dict[str, int] = defaultdict(int)
        for idx in group:
            for arch in infer_archetypes(combined_text(frames[idx])):
                arch_counts[arch] += 1
        top_arch = sorted(arch_counts.items(), key=lambda x: (-x[1], x[0]))[:3]
        cluster_payload.append({
            "frames": [label(frames[i], i + 1) for i in group],
            "likely_meta_mechanisms": [a for a, _ in top_arch],
            "review_needed": True,
            "repair_needed": None,
        })

    result = {
        "candidate_clusters_found": bool(clusters),
        "collisions_found": bool(clusters),
        "checker_role": "heuristic triage",
        "certifies_collisions": False,
        "certifies_distinctness": False,
        "verdict": (
            "review_flagged_candidates"
            if clusters
            else "no_clusters_detected_by_heuristic_only_not_a_pass"
        ),
        "legacy_fields": {
            "collisions_found": "alias for candidate_clusters_found, not confirmed collisions",
            "pairwise_candidates[].collision": "heuristic pair flag, not a semantic verdict",
            "clusters[].repair_needed": "null means unknown until semantic review",
        },
        "limitations": [
            "can over-group distinct mechanisms sharing vocabulary or mechanism-DNA fields",
            "lexicon-bound; can miss same mechanism worded around its vocabulary",
            "no 0-100 semantic-spread score is emitted because it is not calibrated",
            "review actual causal paths before repair; fresh-context judgments also need source checks",
        ],
        "clusters": cluster_payload,
        "pairwise_candidates": pair_candidates,
    }

    if args.markdown:
        print(f"# Collision check\n")
        print("Checker role: **heuristic triage**")
        print(f"Candidate clusters found: **{str(bool(clusters)).lower()}**")
        print("Certifies collisions: **false**")
        print("Certifies distinctness: **false**")
        print("Caveat: flags require semantic review, not automatic repair; no clusters detected is not a pass.\n")
        if cluster_payload:
            print("| Candidate cluster frames | Likely families | Review needed |")
            print("|---|---|---|")
            for c in cluster_payload:
                print(f"| {', '.join(c['frames'])} | {', '.join(c['likely_meta_mechanisms']) or 'unclear'} | {c['review_needed']} |")
        if pair_candidates:
            print("\n## Pairwise candidates")
            print("| Frames | Similarity signal | Reasons |")
            print("|---|---:|---|")
            for p in pair_candidates[:20]:
                print(f"| {' ↔ '.join(p['frames'])} | {p['similarity_signal']} | {'; '.join(p['reasons']) or 'similarity threshold'} |")
    else:
        print(json.dumps(result, indent=2))

    return 1 if clusters else 0


if __name__ == "__main__":
    raise SystemExit(main())
