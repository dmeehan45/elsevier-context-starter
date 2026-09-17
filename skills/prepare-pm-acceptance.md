# Skill: Prepare PM Acceptance

Use this after implementation verification when a PM needs to evaluate a candidate change in staging or another pre-release environment.

## Goal

Prepare a small, evidence-oriented acceptance plan that distinguishes product behavior from environment/configuration validity.

OpenSpec requirements/scenarios from the target project are the primary acceptance contract. This context base supplies relevant user/client/domain/evaluation context.

## Procedure

1. **Identify the change and candidate.** Record the OpenSpec change and the build/commit/version intended for acceptance.
2. **Read approved change artifacts.** Retrieve the actual requirements/scenarios and any consequential design assumptions from the target project.
3. **Retrieve contextual constraints.** From this repository, retrieve only relevant client/user variation, accepted decisions, evaluation concepts, and known system/environment constraints.
4. **Derive acceptance journeys.** Turn material requirements/scenarios into a small set of user-visible checks. Preserve the specified behavior; do not invent new requirements.
5. **Define the oracle.** For each journey, state what observable evidence constitutes pass/fail and which parts require domain/product judgment.
6. **Establish environment validity.** Identify the configuration fields that could materially change the result: build identity, flags, client/tenant, permissions, fixtures/data, services/integrations, and AI model/prompt/retrieval/evaluator versions when applicable.
7. **Classify environment state.** `valid`, `valid_with_limitations`, or `invalid`.
8. **Stop invalid tests.** If an environment issue invalidates a scenario, mark it blocked/environment-invalid rather than failing the product requirement.
9. **Execute/record acceptance.** Capture expected vs observed behavior and useful evidence.
10. **Separate exploratory findings.** New observations that are not failures of an approved scenario become exploratory findings/product questions.
11. **Recommend durable learning.** After acceptance, identify only findings worth preserving in canonical team context.

## Environment validity prompts

Use only applicable prompts. Do not demand fields irrelevant to the change.

- What build/commit/version is deployed?
- Are all dependent PRs/services deployed?
- Which feature flags or experiment cohort apply?
- Which client/tenant and role/permission configuration is active?
- Which data/fixtures are being used?
- Which integration/service endpoints are active?
- Are there known differences from production that affect this behavior?
- For AI behavior: which model, prompt/system instruction, retrieval index/source, tool configuration, evaluator/scorer, and experiment configuration apply?
- Does stochastic behavior require repeated runs or an aggregate acceptance rule?

## Result semantics

Scenario outcomes:

- `pass` — observed behavior satisfies the acceptance oracle;
- `fail` — environment is valid and observed behavior violates the approved scenario;
- `blocked` — the scenario cannot currently be executed;
- `environment_invalid` — the environment cannot support a trustworthy conclusion;
- `needs_product_decision` — behavior exposes an ambiguity not resolved by the approved artifacts.

Do not collapse `environment_invalid` into `fail`.

## Output

Use `../templates/staging-acceptance-check.md` when a written record is useful.

Keep the plan proportional. A small change should not generate a massive UAT document.
