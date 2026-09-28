# Evaluation Rubric for Anti-Collapse Divergence

Judge breadth by the ideas and the comparisons supporting it. A completed template or a confident judge label is not proof.

## Frame diagnostics

Use these questions qualitatively. Optional local 1-5 ratings may help compare revisions, but do not require a scorecard in the user's brainstorm or present the ratings as calibrated evidence.

| Criterion | What to inspect |
|---|---|
| Mechanism clarity | Can the reader follow what changes and why, at the level the task needs? |
| Distinctness | Does the closest alternative work, unfold, or fail differently? Shared fields alone do not decide this. |
| Non-obviousness | Is the idea meaningfully transformed, rather than a familiar idea with a surprising name? |
| Domain fit | Does it respect the actual problem and constraints? |
| Selective grounding | When practical plausibility is unclear, is the material missing dependency exposed without inventing access, permission, capacity, or expertise? |
| Creative expression | For fiction/design, is the action or experience clear without generic implementation/production boilerplate? |
| Incompleteness | Are promising fragments allowed to remain unresolved without being counted as established differences? |
| Transformability | Could the idea later support action, exploration, or development appropriate to the request? |

## Set-level checks

- Obvious bubbles and likely attractors are identified and transformed before generation.
- Source ontologies change the mechanism, rather than supplying decorative costumes.
- Closest pairs are inspected, including apparently related ideas that may be distinct.
- The 70% distinctness and maximum-three-per-family targets guide inspection; they are not field-count rules or calibrated proof. Do not force repairs solely to meet a quota.
- Standard/Wide/Weird/Repair outputs include a collision table. Compact can use a brief pair comparison.
- Confirmed duplicates are repaired, merged, or retained as explicit variants. Variants do not separately satisfy a requested count of distinct mechanisms. Flags and unresolved ideas are not automatically deleted.
- The final landing, if requested, covers distinct mechanisms. Reviews of an earlier set do not cover repaired frames.
- Counts and presentation follow the user's request; workflow scaffolding does not overwhelm the ideas.
- Shared dependencies are stated once. Grounding is selective, not a repeated example/requirements template.

## Review status check

Use the exact labels defined in `references/judge-protocol.md`:

- `reviewed: fresh-context judge`: a separate context reviewed this version, and the caller checked the cited source evidence.
- `provisional: tool-assisted self-audit`: a comparison tool actually returned results for this set, then the model reviewed them. File reads/writes and unrelated tools do not qualify.
- `provisional: self-audit only`: reasoning alone, including skipped or failed comparison tools.

Check the actual tool/agent trace, not only the answer's assertion. Neither a fresh judge nor the checker verifies originality, usefulness, or factual truth. Check every contested source attribution against the right frame ID.

## Spread verdict

Use `strong / usable / weak / collapsed`, based on pair and cluster reasoning; definitions are in `references/judge-protocol.md`. Do not use a 0-100 semantic-spread score as proof.

## Checker contract

- `candidate_clusters_found: true` means review the candidate clusters, not repair automatically.
- `candidate_clusters_found: false` means this heuristic found no clusters, not that the set is diverse.
- `certifies_collisions` and `certifies_distinctness` are always false.
- `collisions_found` is a retained compatibility alias for `candidate_clusters_found`, not a semantic verdict. Cluster `repair_needed: null` means unknown until review.

The fixtures include a flagged likely-duplicate family, a basic diverse set, a paraphrased duplicate the lexicon misses, and distinct renewal causes it over-groups. The tests check this honest reporting contract; they do not establish the detector's semantic accuracy.

## Repair checks

1. Identify the causal path or progression that made the frames equivalent.
2. Keep the strongest, merge, explicitly preserve variants, or replace the redundant mechanism.
3. Explain the decisive change. Changing three fields is neither necessary nor sufficient.
4. Recheck the replacement against retained neighbors, and report the review used for the final version.

## Behavioral evals

`evals/evals.json` contains prompts and observable assertions. Run fresh contexts without giving the worker expected answers. Evaluate against actual outputs and tool traces. Repeated generations and independent source-checked comparisons are useful; a small smoke test cannot establish general creativity gains.

Should trigger: divergent GTM/content directions, architecture alternatives, causal hypotheses, research angles, creative premises, and repair audits of fake breadth.

Should clarify when the missing variable changes the search space: “Brainstorm for my startup,” “Give me broad ideas for the site,” or “Find research angles for this.” Ask one useful question, not a questionnaire.

Should not trigger: factual lookup, ordinary summarization, a normal PR description, syntax fixes, calculations, citation verification, routine rewrites, or an explicitly decisive choice between known options.
