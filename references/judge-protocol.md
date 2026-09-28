# Fresh-Context Judge Protocol

Use this to review whether frames differ in how they work. A separate context can catch the generator's blind spots, but it can also misread, over-group, or attribute evidence to the wrong idea. Review is not verification of creativity.

## Review provenance

| Status | Allowed when |
|---|---|
| `reviewed: fresh-context judge` | A separate context reviewed the current frames without generation rationale, and the caller checked cited evidence against those frames. |
| `provisional: tool-assisted self-audit` | A relevant comparison tool returned results for this set, followed by same-context review. Name the tool and input. |
| `provisional: self-audit only` | Only model reasoning compared the frames. Reading/writing files does not qualify as tool-assisted comparison. A skipped or failed checker does not qualify either. |

These labels describe the process, not originality, usefulness, factual correctness, or calibrated confidence. If repair changes the set, report the review performed on the repaired version.

## Prepare the packet

- Include only the target, constraints, mechanism definition, and current frames with stable IDs.
- Hide decorative titles and ontology labels when possible; retain actual actions, dependencies, and consequences.
- Use one set per packet. For an A/B comparison, first review each set separately, then compare the reviews against the source sets. Similarity across A and B is not evidence of duplication within either set.
- Do not supply the generator's defense, favored conclusion, or earlier judge verdict.

## Judge prompt

```markdown
Review the breadth of this one set of ideas. Find both hidden sameness and false claims of sameness. Do not reward unusual labels or demand that related ideas be discarded.

Set/version ID:
[ID]

Target and constraints:
[brief]

Frames with stable IDs:
[current frames]

Definitions:
- Mechanism = what makes the frame work, change something, or fail: actor -> trigger -> carrier/artifact -> pressure/vector -> loop or failure condition.
- Adapt this to the task. In stories/design, compare how action, form, attention, or meaning changes the experience.
- Frames collide if swapping labels leaves the causal path or progression essentially unchanged.
- Shared actors, objects, settings, or three matching fields only nominate pairs for inspection. A decisive dependency or consequence can distinguish them.
- One broad family can contain distinct mechanisms. Do not invent missing details to make an incomplete frame distinct; mark it unresolved.

Tasks:
1. Inspect the nearest pairs and any overloaded families, not just obvious contrasts.
2. For each contested pair, cite both frame IDs and a short exact excerpt from each. Explain the shared path or the condition that distinguishes how they work, unfold, or fail.
3. Mark the pair duplicate / related but distinct / unresolved. Preserve supported differences. Identify material missing dependencies only when relevant; omit generic production caveats.
4. Give an ordinal spread verdict: strong / usable / weak / collapsed, with a brief reason. Do not use a 0-100 spread score or a mandatory per-frame scorecard.
5. Name confirmed merge/repair candidates and the causal change a repair would need. Do not treat new names or changing three fields as sufficient.

Return:
Set/version reviewed: [ID]

| Pair/family | Frame IDs and short source excerpts | Relationship and reason | Action |
|---|---|---|---|

Spread verdict: [strong / usable / weak / collapsed]
Reason: [based on the actual pair comparisons]
Unresolved: [if any]

Do not claim creativity has been verified. The caller must check your source attributions before accepting the review.
```

## Accepting and acting on the review

Check that cited IDs belong to this set and each excerpt is actually in that frame. Then check that the excerpt supports the claimed equivalence or distinction; matching text alone does not validate the interpretation. If evidence is mixed up, discard the affected rationale and re-review the relevant pair in isolation. Do not repeat a verdict merely because a judge stated it confidently.

Repair or merge confirmed duplicates, or preserve them as explicit variants when useful. Keep unresolved fragments visible without counting them as established breadth. Recheck replacements against retained neighbors. Neither broad family membership nor an overlapping channel alone warrants repair.

## Spread verdicts

| Verdict | Meaning |
|---|---|
| Strong | Most frames have supported differences in mechanism; nearest pairs withstand comparison. |
| Usable | Meaningful breadth, with some repairs or unresolved distinctions still needed. |
| Weak | Several frames repeat hidden mechanisms; repair before a confident landing. |
| Collapsed | Most frames re-skin the same few mechanisms; revisit axes, ontologies, and attractors. |

These are qualitative judgments, not calibrated measures. Use the skill's spread targets as prompts to inspect coverage, not reasons to manufacture differences.

## Local checker

`scripts/check_frame_collisions.py` is optional heuristic triage. A flag requests semantic review; it does not prove a collision. No flag does not prove distinctness. The lexicon can both miss paraphrased duplicates and over-group different ideas with common vocabulary. Use the same pair reasoning on flagged and unflagged neighbors.
