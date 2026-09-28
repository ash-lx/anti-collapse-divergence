---
name: anti-collapse-divergence
description: Use for brainstorming, ideation, divergent exploration, reframing, option generation, hypotheses, creative/design directions, or auditing fake breadth across product, GTM, content, coding, analytics, research, and operations. Escapes obvious answer families, transfers mechanisms from fresh source worlds, and checks whether ideas differ in how they work rather than just their labels. Do not use for simple factual lookup, routine execution, or one convergent recommendation.
---

# Anti-Collapse Divergence

Version: 2.3

## Purpose

Create **real breadth**, not a longer list of same-shaped ideas.

Generate mechanism-level frames first, at the level the user requested. Concrete tactics, execution, copy, code, experiments, or recommendations come later only when asked. A brief example that reveals how an idea works is allowed; a full implementation plan is not needed. The target failure mode is normal LLM fake-breadth: many surface options that secretly collapse into a few familiar bubbles.

Core loop:

```text
clarify only if needed
-> ban obvious bubbles
-> generate fresh source ontologies
-> avoid cliché ontology mappings
-> produce mechanism-DNA frames
-> selectively ground unclear mechanisms
-> compare closest frames, with fresh-context review when appropriate
-> use heuristic checker flags as candidates for review
-> repair confirmed collisions, preserve useful unresolved fragments
-> optional mechanism-aware landing
```

## When to use

Use this skill for requests asking for:

- brainstorming, ideation, lateral thinking, reframing, divergent thinking, weird-but-plausible options
- GTM, distribution, product strategy, positioning, content angles, research hypotheses, analytics questions, coding/architecture approaches, UX directions, operating-model ideas
- “think broader,” “escape obvious choices,” “give me many directions,” “ADHD-like exploration,” “don’t converge,” or “audit whether these ideas are secretly the same”

Do not use it for:

- simple factual answers
- calculations, citations, diagnosis, or verification-only tasks
- routine implementation plans
- cases where the user explicitly wants one decisive convergent answer

## Non-negotiable definitions

### Mechanism

A **mechanism** is what makes the frame work, change something, or fail:

```text
actor -> trigger -> carrier/artifact -> pressure/vector -> reinforcing loop or failure condition
```

A mechanism is **not** a channel, topic, metaphor, feature, tactic, vibe, or clever label.

Adapt the comparison to the task. In stories or design, the relevant difference may be how action, form, attention, or meaning changes the experience. Do not force every creative idea into a business adoption loop.

### Same-mechanism test

Two frames collide if swapping their labels/ontologies leaves the causal story basically unchanged.

Operational test:

```text
If actor, trigger, carrier, pressure/vector, and payoff can be swapped without changing how the frame spreads, works, or fails, the frames share a mechanism.
```

Three shared mechanism-DNA fields are a reason to inspect a pair, not a duplicate verdict. Compare the complete causal path at the task's level of detail. Ask what change in conditions would make one work, unfold, or fail differently from the other. One decisive dependency can distinguish two frames; many renamed fields may leave the mechanism unchanged. A shared family is not itself a collision.

Compare the closest-looking pair, not only easy contrasts. If the supplied detail cannot support a distinction, mark it `unresolved`; do not invent one or discard a promising fragment just to make the set look clean.

## Operating rules

1. **Mechanism over labels.** A valid frame changes how it works or the experience it produces. A channel, wording, or format change counts only when it changes that mechanism.
2. **No judge theater.** Report the review actually performed. Fresh-context review is another judgment, not verification of creativity. Reading files, saving an answer, or invoking an unrelated tool does not make a self-audit tool-assisted.
3. **No final without collision table.** Every Standard/Wide/Weird/Repair output must include a collision table before any handoff or top picks.
4. **Repair confirmed collisions.** Review flags first. Confirmed duplicates must be repaired, merged, or explicitly preserved as deliberate variants; unresolved fragments can remain visibly unresolved. Variants do not count separately toward a requested number of distinct mechanisms.
5. **Invert answer keys.** Domain adapters are not menus to copy. Use them to identify likely bubbles, then mutate away from them.
6. **Rotate ontologies.** Do not keep reusing the same “spicy” worlds unless they produce different mechanism DNA.
7. **Avoid cliché mappings.** For each source ontology, name the obvious mapping and then avoid or mutate it.
8. **Delay compression.** Do not rank or recommend until the divergent set has been generated and collision-checked. If the check is not fresh-context, mark the landing `provisional`.
9. **Respect domain facts.** If facts are missing, label assumptions or ask one lightweight clarification.
10. **Frames first, detail as needed.** Stop at frames unless the user asks for more. Use a small concrete instance only when needed to expose a missing causal link or material dependency.

## Clarification protocol

Ask a clarifying question only when missing context would materially change the mechanism space. Do not ask a broad questionnaire.

Ask at most **one** self-contained question with choices, a recommended default, and brief pushback. This is a narrow divergence-shaping question, not a project-planning gate. If a broader `way-of-working`/project-alignment skill is active, let it own consequential alignment; this skill only asks the one choice needed to set the search space. Use this shape:

```markdown
### One choice before I branch

**What I know:** [target/domain/constraints]
**What changes the divergence:** [the missing variable]

A. [Option label] — [what this optimizes]
B. [Option label] — [what this optimizes]
C. [Option label] — [what this optimizes]
D. Use my default — I will assume [default]

**Recommended:** [A/B/C/D], because [short reason].
**Pushback:** [tempting path] may be weak because [risk].
```

Good clarification variables:

- domain/subdomain: GTM vs content vs architecture vs analytics vs research
- target user, buyer, audience, system, dataset, codebase, literature, or decision context
- desired weirdness: safe / balanced / alien
- output mode: pure divergence / repair audit / divergence + landing
- constraints that ban whole mechanism families

If the user already gave enough to proceed, do not ask. State assumptions and run the workflow.

## Default workflow

### 1. Scope snap

```markdown
**Divergence target:** [what we are exploring]
**Domain:** [GTM/content/coding/analytics/research/product/ops/etc.]
**Mode:** [compact/standard/wide/weird/repair]
**Known constraints:** [what must be respected]
**Assumptions:** [only if needed]
```

### 2. Bubble ban

List the obvious clusters the model would normally produce. These are banned unless transformed into a different mechanism.

```markdown
## Banned obvious bubbles
- [Bubble]: banned because [why it would collapse exploration]
```

Use 4-6 bubbles for Compact, 6-10 for Standard, 8-12 for Wide/Weird.

### 3. Fresh menu, then inversion

Before producing frames, name likely go-to mechanisms for this exact problem, then forbid copying them as-is.

```markdown
## Likely model attractors to mutate away from
| Attractor | Why the model will reach for it | Mutation requirement |
|---|---|---|
```

Domain adapters in `references/domain-adapters.md` are **collision warnings**, not suggested answers.

### 4. Pick divergence axes

Choose axes that force different search paths. Load `references/domain-adapters.md` when the task is domain-specific.

Universal axes:

- actor / initiator
- power holder / gatekeeper
- trigger moment
- carrier artifact / workflow / medium
- emotional or incentive engine
- pressure/vector
- reinforcing loop
- failure mode

### 5. Generate source ontologies

Select source ontologies from the problem, not from a fixed favorite list. Load `references/ontology-bank.md` only when 12+ frames, strange frames, or cross-domain breadth are requested.

```markdown
| Ontology | Cliché mapping to avoid | Mutated search direction |
|---|---|---|
```

Rule: if an ontology produces a cliché mapping, either mutate it or replace the ontology.

### 6. Generate mechanism-DNA frames

```markdown
| # | Frame | Ontology | Mechanism | Actor | Trigger | Carrier | Pressure/vector | Why non-obvious | Failure mode |
|---|---|---|---|---|---|---|---|---|
```

Keep frames compact. The table is a thinking aid, not a mandatory per-idea form: respect the user's requested format and count. Do not turn the brainstorm into tactics yet.

#### Selective grounding

When a practical idea's plausibility is unclear, trace one ordinary instance: starting situation -> what changes -> result. Check any resource, permission, access, capacity, expertise, or handoff the mechanism depends on. If it is not established, name the dependency briefly beside the idea; state a shared dependency once for the set. Do not quietly assume it exists.

Skip this extra explanation when the mechanism is already concrete. For fiction and expressive work, show the action or experience; do not append generic production requirements such as “needs good acting” or “requires editing.” This is a diagnostic check, not an early feasibility veto: retain a promising incomplete idea as `unresolved` rather than inventing the missing bridge.

### 7. Collision judge gate

Run a collision check before any handoff. Report **review provenance**, not a numeric score or a creativity certificate.

Review statuses:

| Status | Allowed when | What it means |
|---|---|---|
| `reviewed: fresh-context judge` | A separate context/subagent/model call reviewed this version of the frames without the generation rationale; its cited evidence was checked against those frames | Independent context used; judgment can still be wrong |
| `provisional: tool-assisted self-audit` | A relevant comparison tool actually ran on this set and returned results, followed by same-context review | Name the tool and input briefly; heuristic support only |
| `provisional: self-audit only` | Only model reasoning reviewed the set, including when a tool was skipped or failed | No independent or tool-based comparison occurred |

For Standard/Wide/Weird/Repair runs, use a fresh-context judge whenever the environment supports separate calls/subagents. Compact may use self-audit. If no independent context is available, state that briefly and continue provisionally. None of these statuses certifies originality, usefulness, or factual truth.

Fresh-context judge instructions:

- Use `references/judge-protocol.md`. Give the judge only the target, constraints, mechanism definition, and current frames with stable IDs. Keep one set per review packet; judge sets separately before comparing them.
- Hide ontology/cute labels if possible so it judges mechanism DNA, not style.
- Ask it to inspect the nearest pairs and distinguish duplicates, related-but-distinct frames, and unresolved cases. Require frame IDs and short source excerpts for contested judgments; check those against the actual frames before accepting a repair. Do not accept a claim about one set based on an idea from another.
- Ask it to name confirmed repair candidates and give an ordinal spread verdict: `strong / usable / weak / collapsed`.
- Do **not** ask for or trust a 0-100 spread score.

Local checker role:

- `scripts/check_frame_collisions.py` is **heuristic triage**. Flags require semantic review, not automatic repair. A clean result does not certify distinctness.
- It can over-group different ideas with shared actors/artifacts, or miss the same mechanism expressed with different vocabulary. It is optional support, not a substitute for comparing the frames.

Collision table:

```markdown
## Collision check
| Closest pair / family | Frame IDs | Duplicate, distinct, or unresolved — why? | Action |
|---|---|---|---|
```

Spread targets (heuristics, not calibrated proof):

- Aim for no more than 3 frames in one causal family unless the user requested depth there. Family membership alone does not justify deleting distinct frames.
- Aim for at least 70% distinct mechanisms, supported by pair comparisons rather than field counts or a local 0-100 score. Do not count unresolved frames as proven distinct or invent differences to meet this target.
- If the output is Wide/Weird, at least 20-30% should be stranger-but-plausible, not merely polished.
- State the review actually performed and any unresolved collisions.

### 8. Repair pass

If a collision is confirmed, repair, merge, or mark deliberate variants before finalizing. A checker or judge flag alone is not confirmation.

```markdown
## Repaired frames
| Replaced/merged frame | Collision problem | New frame | New mechanism DNA change | Why it is more distinct |
|---|---|---|---|---|
```

Repair rule: change the causal dependency or progression that made the frames equivalent. Explain the decisive difference; changing three field labels is neither necessary nor sufficient. Recheck replacements against the retained set, especially their closest neighbors. A review of the previous version does not cover newly repaired frames; report the review used on the final set.

### 9. Optional landing

Only land when asked or when the request implies action. Landing must preserve mechanism spread.

```markdown
## Mechanism-aware landing
| Pick | Frame | Engine covered | Why this one | Cheapest next test / next move |
|---|---|---|---|---|
```

Default landing set:

- **Highest-upside distinct engines:** 3
- **Most practical distinct engines:** 3
- **One weird bet:** 1
- **Do not pursue yet:** 1-2, with reason

Never select three frames from the same hidden engine just because they sound good.

## Output modes

Use the smallest mode that satisfies the request. Requested counts and formats take precedence over these defaults. Keep scaffolding brief, especially for Compact or creative prose.

### Compact

- 4-6 banned bubbles
- 6-8 frames
- lightweight collision check with a closest-pair explanation and accurate review status
- repair only if duplication is obvious

### Standard

- 6-10 banned bubbles
- 10-14 frames
- collision check required
- repair required if needed

### Wide

- 8-12 banned bubbles
- 16-24 frames
- fresh ontology table
- fresh-context collision judge for independent review
- if unavailable, output must be labeled provisional
- repair pass required

### Weird

- 8-12 banned bubbles
- 10-18 frames
- at least 50% unusual ontologies
- cliché ontology mappings must be named and mutated

### Repair audit

Use when the user gives outputs from another model.

- cluster hidden sameness
- identify fake breadth
- keep strongest frames
- regenerate colliding frames
- optionally land the strongest distinct engines

## Reference files

- `references/domain-adapters.md` — domain-native axes and collision warnings for GTM, content, coding, analytics, research, product, and operations.
- `references/collision-taxonomies.md` — domain-native hidden-cluster patterns. Use for judging, not as an answer menu.
- `references/judge-protocol.md` — fresh-context judge prompt and non-numeric spread verdict rubric.
- `references/clarifying-questions.md` — one-question A/B/C companion gate examples.
- `references/ontology-bank.md` — source worlds for cross-domain exploration.
- `references/worked-example.md` — end-to-end example with collision detection, repair, and landing.
- `references/eval-rubric.md` — evaluation rubric and trigger tests.
- `assets/output-template.md` — reusable output skeleton.
- `assets/clarifying-question-template.md` — lightweight question template for ambiguous runs.
- `assets/compact-prompt.md` — copy-paste fallback for models without skill support.
- `scripts/check_frame_collisions.py` — heuristic, lexicon-bound collision checker; flags candidates for review and cannot certify either collisions or distinctness.

## Common failure modes

- **Listicle collapse:** many rows, same mechanism.
- **Designer bubble:** the skill’s own adapters become a new answer key.
- **Judge theater:** self-review or weak scripts create false confidence.
- **Score worship:** treating a 0-100 spread score as calibrated when cluster reasoning is what matters.
- **Cliché metaphor:** “games = leaderboard,” “religion = ritual,” “luxury = expensive.”
- **Tactic leakage:** channels, tasks, campaigns, features, or code too early.
- **Premature synthesis:** ranking before spread exists.
- **Hallucinated grounding:** pretending to know facts not provided.
- **Cute nonsense:** novelty without causal path.
- **No landing:** divergent fragments with no mechanism-aware handoff when action is requested.

## Minimal examples

Good GTM frame:

> **Upstream certification mandate:** the decision-receiver rejects unaudited memos, forcing upstream writers to attach reasoning-audit proof before approval.

Bad GTM frame:

> “Do LinkedIn content and founder-led growth.”

Good coding frame:

> **Customs checkpoint:** every incoming file is quarantined, inspected, rejected with reasons, and given chain-of-custody metadata before entering production tables.

Bad coding frame:

> “Use queues, retries, microservices, and tests.”

Good analytics frame:

> **Expectation debt:** churn rises because acquisition promises create an obligation the product experience cannot later cash.

Bad analytics frame:

> “Segment churn by cohort, region, and plan.”
