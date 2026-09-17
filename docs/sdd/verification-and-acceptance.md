# Verification, environment validity, and PM acceptance

SDD needs several kinds of evidence. They are related, but they are not interchangeable.

The most important distinction for this team is:

> OpenSpec verification is not the same thing as PM acceptance in staging.

A change can be internally consistent with its artifacts and still be unacceptable to the PM. A staging test can also produce a misleading result if the environment is not actually exercising the intended candidate build or configuration.

## Four validation layers

| Layer | Question | Typical evidence | Primary responsibility |
| --- | --- | --- | --- |
| Specification validity | Did we describe observable behavior and a usable acceptance oracle? | requirements, scenarios, explicit non-goals, examples | PM + agent |
| Implementation verification | Does the implementation match the approved OpenSpec artifacts? | task completion, automated tests, scenario coverage, design/code coherence | engineering/agent + OpenSpec Verify |
| Environment validity | Is the candidate being tested in a representative and correctly configured environment? | build/commit identity, deployment state, flags, tenant/client config, data/fixtures, integration/model versions | engineering/platform + PM |
| Product acceptance | In that valid environment, does the user-visible behavior meet the intended outcome? | executed acceptance journeys, observed results, screenshots/logs/traces where appropriate, PM/domain judgment | PM/domain reviewer |

A later layer does not repair a weak earlier layer. If acceptance criteria are vague, staging feedback will be subjective. If staging is invalid, a failed acceptance scenario does not prove the product behavior is wrong.

## 1. Specification validity

Acceptance should be designed while the behavior is being specified.

For every material externally observable behavior, the PM and agent should be able to answer:

- What condition or user action triggers the behavior?
- What observable outcome should occur?
- What important alternative/edge case must also hold?
- What evidence would convince us that the behavior is working?
- Which parts can be automated and which require human/domain judgment?

A useful trace is:

```text
problem / outcome
    -> requirement
    -> acceptance scenario
    -> test oracle
    -> automated evidence where possible
    -> staging acceptance journey
    -> observed result
```

If the team cannot describe the oracle, that is a specification problem rather than something to defer to QA.

## 2. Implementation verification

Use OpenSpec Verify according to the target project's installed workflow.

OpenSpec Verify is designed to compare implementation against planning artifacts across dimensions such as completeness, correctness, and coherence. It can inspect task completion, requirements/scenarios, tests, and adherence to design.

Treat that evidence as an implementation-level check. Do not translate "Verify passed" into "PM accepted" without performing the remaining layers required by the team's delivery policy.

## 3. Environment validity

Before executing PM acceptance scenarios, establish what is actually being tested.

Record the fields that are material to the change. Common examples include:

- deployed build / commit / version;
- whether all required PRs or services are deployed;
- feature flags and experiments;
- tenant/client identity and configuration;
- permissions / role configuration;
- test data or fixtures;
- service and integration endpoints;
- prompts, models, evaluator versions, or other AI configuration when relevant;
- dependency versions whose behavior materially affects the scenario;
- known differences from production;
- known stale caches, delayed data, or asynchronous processes that can change the result.

The exact list should come from the system being tested, not from a universal checklist.

### Environment validity outcome

Use one of three states:

- `valid` — no known environment difference is expected to invalidate the acceptance conclusion;
- `valid_with_limitations` — known differences exist, but the listed scenarios remain meaningful within stated limits;
- `invalid` — the environment cannot currently support a trustworthy acceptance conclusion.

If the environment is invalid, stop the affected acceptance test. Do not record the feature itself as accepted or rejected from that evidence.

## 4. PM acceptance

PM acceptance should exercise the agreed user-visible scenarios rather than rely on unstructured "poking around."

For each scenario, record:

- setup / preconditions;
- action or journey;
- expected result;
- observed result;
- evidence when useful;
- pass / fail / blocked;
- unexpected behavior or product questions discovered.

Exploratory testing remains valuable. Record unexpected findings separately so they are not confused with failures of the specified requirement.

## Conversational / AI-specific validity

For conversational or model-driven behavior, a staging URL alone is rarely enough to establish test validity.

Depending on the change, confirm relevant items such as:

- model and model version;
- system/prompt version;
- tool availability and configuration;
- retrieval source/index version;
- evaluator/scorer version;
- feature flags or experiment cohort;
- deterministic fixtures/seeds when applicable;
- representative input set;
- client-specific rules;
- known non-determinism and the number of repetitions needed for a meaningful conclusion.

Do not demand determinism from a stochastic system when the real acceptance criterion is statistical or distributional. In those cases, define the sample/evaluation rule before testing.

## Acceptance and OpenSpec archive

This repository does not redefine the OpenSpec archive command or its built-in semantics. The team should establish a delivery policy for when archiving is appropriate.

For product changes requiring PM acceptance, the recommended policy is:

```text
Apply complete
-> automated checks / CI complete
-> OpenSpec Verify reviewed
-> candidate deployed
-> environment valid
-> PM acceptance complete
-> archive / release according to team policy
```

If the team intentionally archives earlier, make the remaining acceptance state visible elsewhere rather than allowing archive status to imply release acceptance.

## Durable learning after acceptance

Return only durable findings to this context base. Examples:

- a client variation that should influence future specs;
- an environment constraint that repeatedly affects acceptance;
- a newly accepted product decision;
- a test/evaluation pattern that should become advisory or normative guidance;
- evidence that weakens or strengthens an existing hypothesis;
- a recurring failure mode in the SDD workflow.

Implementation-local details belong in the target codebase/OpenSpec history unless they become reusable team context.
