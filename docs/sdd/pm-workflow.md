# Product management workflow for spec-driven development

This guide is for product managers moving from a large-PRD / Jira-handoff workflow into spec-driven development (SDD) with OpenSpec and conversational agents.

The context base supports the workflow; it does not replace OpenSpec. When a target project uses OpenSpec, OpenSpec's current schema, artifact instructions, blocked/ready state, and apply/verify behavior remain controlling. This repository helps the PM and agent retrieve relevant team knowledge, reason about scope, and perform acceptance work around that workflow.

## The mental model

Traditional handoff often looks like:

```text
large PRD -> Jira decomposition -> developer handoff -> implementation -> PM staging test
```

The intended SDD loop is smaller and more iterative:

```text
team context
    |
    v
EXPLORE
understand the problem, evidence, unknowns, and candidate boundary
    |
    v
PROPOSE
proposal -> specs -> design -> tasks
    |
    v
REVIEW THE PLAN
PM confirms intent, externally observable behavior, non-goals, and acceptance criteria
    |
    v
APPLY
implementation follows the approved artifacts
    |
    v
VERIFY
artifact <-> implementation consistency and automated evidence
    |
    v
VALIDATE THE ENVIRONMENT
confirm the candidate build/configuration is meaningful to test
    |
    v
PM ACCEPTANCE
exercise the agreed user-visible scenarios and record evidence
    |
    v
ARCHIVE + LEARN
preserve the change history; return durable learning to team context when useful
```

Do not treat this as a rigid phase gate. OpenSpec is intentionally fluid: implementation can reveal a design problem and send the team back to update planning artifacts. The important rule is that changes to intent or specified behavior are made explicit rather than silently absorbed during implementation.

## What the PM owns

The PM remains accountable for:

- the problem and intended user/customer outcome;
- which evidence is relevant and which assumptions remain uncertain;
- the product boundary and meaningful non-goals;
- externally observable requirements and acceptance criteria;
- consequential client/segment variations;
- review of the proposed artifacts before implementation;
- product acceptance in a valid environment;
- deciding whether newly learned information is durable enough to enter shared context.

The PM does **not** need to choose repository filenames, manually search the whole context base, decide every technical implementation task, or define exact pull-request boundaries.

## What the conversational agent should own

The agent should:

- identify the likely SDD stage from the conversation;
- retrieve the smallest relevant context from this repository;
- distinguish evidence, inference, advisory patterns, and accepted decisions;
- surface conflicts and important unknowns;
- recommend a coherent OpenSpec change boundary before proposal;
- flag acceptance criteria that do not yet have a usable oracle;
- recommend implementation/delivery slices without presenting them as mandates;
- hand planning work to OpenSpec rather than inventing a parallel artifact workflow;
- distinguish OpenSpec verification from environment validity and PM acceptance;
- help capture durable post-change learning through the normal context lifecycle.

See `../../skills/sdd-pm-companion.md` for the agent contract.

## How to use the context base during each stage

### Explore

Start broad enough to understand the problem, but do not load the full corpus.

Prefer:

```text
relevant summaries / concepts / entities
-> claims + observations
-> hypotheses + unresolved questions
-> prior decisions
-> source evidence when confidence matters
```

The goal is to clarify the problem and candidate boundary, not to produce a spec immediately.

A useful exploration should be able to state:

- the user/customer outcome;
- current behavior or current understanding;
- evidence supporting the problem;
- important contradictions or gaps;
- affected product/capability/client scope;
- candidate change boundaries;
- the next question that would materially change the proposal.

### Before proposing

Run the scope review in `../../skills/review-change-scope.md`.

The default question is:

> What is the smallest coherent behavioral change that delivers independently testable value?

The agent should recommend a boundary and explain likely follow-on work. The PM chooses whether the recommendation matches the intended product outcome.

### Proposal / specs / design / tasks

Use OpenSpec's own workflow and artifact instructions. The context base supplies evidence and constraints; it does not replace OpenSpec templates or state.

PM review should focus on:

- **proposal:** is the problem/outcome and boundary right?
- **specs:** are externally observable behaviors precise and testable?
- **design:** are consequential implementation decisions consistent with team constraints and known patterns?
- **tasks:** does the implementation plan preserve the specified behavior, and are meaningful validation steps included?

Avoid converting descriptive research into requirements without a product decision. See `../ontology.md#authority-and-sdd-interpretation`.

### Apply

Implementation is driven by the approved OpenSpec artifacts. Use relevant team context only where it changes implementation choices: architecture decisions, design-system rules, accessibility requirements, evaluation practices, client variation, telemetry, release constraints, or other accepted guidance.

If implementation reveals that specified behavior must be changed, update the planning artifacts rather than silently narrowing the implementation.

### Verify

OpenSpec Verify is an implementation-consistency check. It can assess task completeness, requirement/scenario coverage, and coherence with design. It is **not** proof that the staging environment is valid or that the PM has accepted the end-user behavior.

See `verification-and-acceptance.md`.

### Environment validation and PM acceptance

Before PM acceptance, establish that the environment represents the candidate being evaluated. Then exercise the agreed acceptance scenarios and capture observable evidence.

Use `../../skills/prepare-pm-acceptance.md` and `../../templates/staging-acceptance-check.md`.

### Archive and learn

Archive the OpenSpec change according to the target project's workflow after the team's completion/acceptance policy is satisfied.

Do not copy every implementation detail into this context base. Preserve only durable learning, such as:

- a new accepted product or client decision;
- a newly discovered constraint;
- a reusable implementation/evaluation pattern;
- an invalidated hypothesis;
- evidence that materially changes an existing claim;
- a recurring workflow failure worth preventing in future work.

Use the normal `INVESTIGATE -> TEACH -> CURATE -> COMMIT` lifecycle for those additions.

## Transition from the old workflow

A useful mapping is:

| Previous artifact/activity | SDD equivalent |
| --- | --- |
| PRD problem/context | Explore evidence + proposal `Why` |
| PRD scope | Proposal + explicit non-goals |
| Requirements | OpenSpec requirements and scenarios |
| Technical approach section | Design artifact |
| Jira decomposition | OpenSpec tasks + recommended delivery slices |
| Developer handoff | Explicit Apply request after plan review |
| Developer QA | Automated tests + OpenSpec Verify |
| PM staging test | Environment validity + PM acceptance |
| Historical PRD/Jira record | Archived OpenSpec change + selected durable context |

The behavioral change is not "write a smaller PRD." It is to keep intent legible across a chain of smaller artifacts, each with a specific job and a reviewable feedback loop.

## First-team adoption

For first use, prefer one small, real, low-risk change and complete the whole lifecycle. OpenSpec includes an onboarding workflow for this reason. Heavy narration is useful for the first few changes; it should decrease as the team builds fluency.

Do not customize the OpenSpec schema merely to make the process feel familiar. Use the default workflow until repeated real work demonstrates a gap that cannot be solved with context, artifact rules, examples, or team guidance.
