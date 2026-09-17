# Staging Acceptance Check

Use this as a lightweight record for product acceptance after implementation verification. Delete sections that are not relevant.

## Change / Candidate

- OpenSpec change:
- Candidate build / commit / version:
- Environment:
- Reviewer:
- Date:

## Environment Validity

Record only fields material to the behavior being tested.

- Expected build/configuration:
- Observed build/configuration:
- Required feature flags / experiments:
- Client / tenant / role:
- Test data / fixtures:
- Relevant services / integrations:
- Relevant AI model / prompt / retrieval / evaluator configuration:
- Known differences from production:
- Other material constraints:

**Environment state:** `valid | valid_with_limitations | invalid`

**Limitations / reason:**

If the environment is invalid for a scenario, do not convert the result into a product failure.

## Acceptance Scenarios

### Scenario: <name>

- Requirement / OpenSpec reference:
- Preconditions / setup:
- User action / journey:
- Expected observable result:
- Evidence / oracle:
- Observed result:
- Result: `pass | fail | blocked | environment_invalid | needs_product_decision`
- Notes / evidence links:

## Exploratory Findings

Record unexpected observations that are not failures of an approved acceptance scenario.

- Finding:
  - Why it matters:
  - Follow-up question/change if any:

## Acceptance Decision

- `accepted`
- `accepted_with_known_limitations`
- `revisions_needed`
- `acceptance_blocked`

Rationale:

## Candidate Durable Learning

Only list findings that may belong in shared team context beyond this change.

- New decision / constraint / client variation / reusable pattern / hypothesis update:
