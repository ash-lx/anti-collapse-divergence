# Clarifying Questions for Divergence Runs

Use this only when one missing answer would materially change the mechanism search.

This is a **companion gate**, not a separate planning methodology. It borrows the lightweight A/B/C decision shape, but it must stay narrow: choose the search direction, then run anti-collapse divergence.

## Rules

- Ask at most one question before branching.
- Offer concrete choices and a recommended default.
- Include the context inside the question so the user does not need to remember prior discussion.
- Ask about mechanism-shaping variables, not implementation details.
- If a broader project or way-of-working skill is active, let that skill own consequential product/research/implementation alignment. This skill only shapes the brainstorm.
- If the user gave enough context, do not ask. State the default and proceed.

## Template

```markdown
### One choice before I branch

**What I know:** [target/domain/constraints]
**What changes the divergence:** [missing variable that changes the mechanism search]

A. [Option label] — [what this optimizes]
B. [Option label] — [what this optimizes]
C. [Option label] — [what this optimizes]
D. Use my default — I will assume [default]

**Recommended:** [A/B/C/D], because [short reason].
**Pushback:** [tempting path] may be weak because [risk].
```

## Common question shapes

### Breadth temperature

```markdown
### One choice before I branch

**What I know:** You want divergent frames, not standard ideas.
**What changes the divergence:** Whether I should bias toward usable near-term directions or stranger mechanism discovery.

A. Practical weird — non-obvious but still executable soon.
B. Alien search — optimize for surprising mechanisms first, practicality later.
C. Split run — half practical weird, half alien, then collision-check both.
D. Use my default — I will run C.

**Recommended:** C, because it protects useful weirdness without collapsing into safe options.
**Pushback:** Pure practical often becomes polished normal advice; pure alien can become cute nonsense.
```

### GTM power holder ambiguity

```markdown
### One choice before I branch

**What I know:** This is a GTM/distribution brainstorm.
**What changes the divergence:** Whether adoption is pulled by the user, buyer, receiver, or gatekeeper.

A. User-led pull — end users adopt first.
B. Buyer/gatekeeper-led pull — a power holder mandates or funds adoption.
C. Artifact-led spread — the output travels between people and creates demand.
D. Use my default — I will run C unless the product is clearly self-serve only.

**Recommended:** D, because artifact-led spread often reveals mechanisms that channel lists miss.
**Pushback:** Assuming user-led pull too early can hide the real economic pressure.
```

### Coding / architecture ambiguity

```markdown
### One choice before I branch

**What I know:** You want architecture options before implementation.
**What changes the divergence:** Whether the core risk is bad inputs, state drift, scale, developer workflow, or migration safety.

A. Failure-mode search — branch by what can go wrong.
B. Boundary search — branch by where contracts and validation should live.
C. State-ownership search — branch by who owns truth and how drift is repaired.
D. Use my default — I will run A+B+C and repair collisions.

**Recommended:** D, because architecture brainstorms collapse when they start from components instead of system physics.
**Pushback:** Starting with “queues/retries/microservices” is usually implementation vocabulary, not real divergence.
```

### Research ambiguity

```markdown
### One choice before I branch

**What I know:** You want research angles.
**What changes the divergence:** Whether the search should vary theory, mechanism, unit of analysis, or contribution type.

A. Theory divergence — different lenses and constructs.
B. Mechanism divergence — same phenomenon, different causal explanations.
C. Unit-of-analysis divergence — different places where the phenomenon lives.
D. Use my default — I will run B with A as secondary.

**Recommended:** D, because mechanism divergence produces stronger non-colliding research frames than topic buckets.
**Pushback:** Pure theory shopping can become impressive but ungrounded.
```
