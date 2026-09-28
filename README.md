# Anti-Collapse Divergence Skill

A portable Agent Skill for divergent brainstorming across creative work, GTM, content, coding, analytics, research, product, UX, and operations.

**Generate ideas that work differently, then check the closest pairs for hidden sameness.** The skill helps an agent move beyond a longer list of familiar answers. It supports compact exploration, broader sets, unusual directions, and audits of an existing brainstorm.

## Install with Skills CLI

Requires Node.js and npm for `npx`. From your project directory:

```bash
npx skills add ash-lx/anti-collapse-divergence --skill anti-collapse-divergence
```

Choose your agent when prompted. For a global installation targeting Codex and Claude Code:

```bash
npx skills add ash-lx/anti-collapse-divergence --skill anti-collapse-divergence -g -a codex -a claude-code
```

Preview the available skill without installing:

```bash
npx skills add ash-lx/anti-collapse-divergence --list
```

For a local checkout or an unpublished export, replace `ash-lx/anti-collapse-divergence` with the path to this folder.

The CLI follows the [Agent Skills format](https://agentskills.io/specification) and supports multiple agents. See the [official CLI documentation](https://github.com/vercel-labs/skills) for current agent support and options. Agent behavior, explicit invocation syntax, and access to separate review contexts vary by host.

## Try it

In Codex:

```text
$anti-collapse-divergence Give me six different ways a neighborhood library could make Wi-Fi available after closing. Keep it compact; compare the closest pair before recommending anything.
```

In Claude Code, use `/anti-collapse-divergence` with the same request. Other agents can select the installed skill from a relevant brainstorming request.

More examples:

- "Explore different explanations for subscription cancellations. Separate causal hypotheses from segment labels."
- "Give me ten short-film premises where the story engines differ, not just their settings."
- "Audit these ideas for hidden sameness. Preserve incomplete ideas as unresolved instead of inventing a distinction."

Modes: **Compact**, **Standard**, **Wide**, **Weird**, and **Repair audit**. Use the smallest mode that fits the request. This skill is not intended for routine execution, simple factual lookup, or a request for one immediate recommendation.

## What you get

- A portable instruction file plus supporting references and output templates.
- Optional Python checker and regression fixtures; the checker uses only the Python standard library.
- Guidance for independent review when the host supports separate contexts, and honest provisional review when it does not.

Python 3.10+ is recommended for running the optional checker and its tests. Python is not needed to read or use the core skill instructions. The skill itself requires no API key, hosted service, or Vercel deployment. Your agent may use its normal tools to complete the task you give it.

## Limits

This is a prompting workflow, not a validated measure of creativity. It does not certify originality, factual truth, practical value, or safety. A fresh-context review is another judgment. The optional lexical checker has documented false positives and false negatives; its flags are candidates for semantic review.

## Repository and discovery

This repository contains one skill at its root. Install the whole folder so the relative references, templates, and checker remain available.

According to the [Skills FAQ](https://skills.sh/docs/faq), GitHub-hosted skills become discoverable on the skills.sh leaderboard through CLI installation telemetry. Publishing the repository and appearing on the directory are separate steps; listing timing and ranking are not guaranteed by this repository. No npm package or Vercel application deployment is required for this GitHub installation route.

## Contributing

Changes that address a demonstrated failure are welcome. Include the smallest reproducible prompt or fixture, explain the expected behavior, and run the checker regression suite below. Do not treat a clean heuristic result as proof that a set of ideas is distinct.

## License

[MIT](LICENSE), copyright 2026 Ashish Alexander.

## What changed in v2.3

The core loop is preserved: ban obvious bubbles, transform familiar attractors, transfer mechanisms from fresh source worlds, compare frames, repair confirmed duplicates, and land only when requested.

This revision makes four focused changes:

1. **Selective grounding.** Expose a practical idea's missing causal link or material dependency when needed. State shared dependencies once. Do not append generic production requirements to creative premises.
2. **Causal comparison.** Three matching fields nominate a pair for review; they do not prove duplication. One decisive difference can matter. Keep promising incomplete frames visibly unresolved.
3. **Accurate review provenance.** A fresh judge means reviewed, not verified creativity. Tool-assisted self-audit requires an actual comparison tool result for this set; file reads/writes do not count. Check the judge's frame IDs and source excerpts.
4. **Honest checker flags.** The lexical detector still has both false positives and false negatives. Its output now requests review rather than prescribing repair. The scoring and clustering algorithm is unchanged.

The revision follows model-based product and story tests. Those tests supported a conditional grounding check, not a compulsory per-idea template or a claim of universal creativity gains.

## Main files

- `SKILL.md`: workflow, modes, and review rules.
- `references/judge-protocol.md`: fresh-context review prompt and source checks.
- `references/eval-rubric.md`: output and process diagnostics.
- `references/worked-example.md`: compare, preserve supported differences, and repair.
- `references/domain-adapters.md`, `collision-taxonomies.md`, `ontology-bank.md`: search aids and collision warnings, not answer menus.
- `assets/compact-prompt.md`, `output-template.md`: portable prompts and optional scaffolding.
- `evals/evals.json`: behavioral prompts and assertions.
- `evals/test_checker.py`, `evals/fixtures/`: checker regression tests and known limitations.
- `scripts/check_frame_collisions.py`: optional lexical triage.

## Manual install: Codex

For a repo-scoped skill:

```bash
mkdir -p .agents/skills
cp -R anti-collapse-divergence .agents/skills/
```

For a user-scoped skill:

```bash
mkdir -p ~/.agents/skills
cp -R anti-collapse-divergence ~/.agents/skills/
```

Invoke explicitly with:

```text
$anti-collapse-divergence Explore 20 GTM frames for ...
```

## Manual install: Claude Code

For a personal skill:

```bash
mkdir -p ~/.claude/skills
cp -R anti-collapse-divergence ~/.claude/skills/
```

For a project skill:

```bash
mkdir -p .claude/skills
cp -R anti-collapse-divergence .claude/skills/
```

Invoke explicitly with:

```text
/anti-collapse-divergence Explore 20 frames for ...
```

## Validate the checker

From the skill directory:

```bash
python3 -m unittest discover -s evals -p 'test_*.py' -v
python3 scripts/check_frame_collisions.py evals/fixtures/attestation-collapse.json
python3 scripts/check_frame_collisions.py evals/fixtures/distinct-renewal-causes.json --markdown
```

The last two commands intentionally exit **1**, meaning candidate clusters need review. The renewal example shares actor, trigger, and carrier but has different causal explanations: inability to pay versus a completed task. It must not be automatically repaired.

CLI contract:

- Exit `0`: no candidate clusters. This is not a semantic pass.
- Exit `1`: candidate clusters require review. This is not a confirmed collision.
- Exit `2`: invalid input.
- `candidate_clusters_found` is the preferred JSON flag. `certifies_collisions` and `certifies_distinctness` are always false.
- Legacy `collisions_found` remains an alias for the candidate flag, and pairwise `collision` remains a heuristic flag. Neither is a semantic verdict.
- Cluster `review_needed` is true; `repair_needed` is now null (unknown until review), replacing v2.2's automatic true.
- The positive verdict is now `review_flagged_candidates`; consumers that acted on the old repair verdict must review the actual mechanisms first.
- The `--threshold` option controls reporting of pairwise candidates; it does not change clustering or the exit code.

The fixtures document a detected overlap family, a basic diverse set, a duplicate the lexicon misses, and a distinct pair it over-groups. Passing these tests checks reporting behavior, not general semantic accuracy. Use `references/judge-protocol.md` for a source-checked review.

## Non-install fallback

Use `assets/compact-prompt.md` when pasting into a model that does not support skills.
