# Scope and delivery slicing for SDD

This guide helps a PM and agent decide whether an idea belongs in one OpenSpec change, several changes, or one change implemented through several delivery slices.

The goal is not to optimize for document size. It is to preserve one coherent product outcome with a meaningful acceptance boundary.

## Default heuristic

A single OpenSpec change should usually represent:

> the smallest coherent behavioral change that delivers independently testable value.

That means the work should have a clear user/customer outcome and a coherent answer to: "How will we know this change is acceptable?"

## Signals that work probably belongs together

Keep work in one change when most of the following are true:

- requirements serve the same primary outcome;
- the same user/client scope is affected;
- acceptance criteria depend on the behaviors working together;
- the work shares a rollout/rollback decision;
- splitting would produce an unusable or misleading intermediate product state;
- uncertainty is similar across the major parts of the work.

## Signals that the agent should recommend a split

Recommend separate OpenSpec changes when one or more of these are material:

- two pieces create independently useful product outcomes;
- they could reasonably ship or be rolled back separately;
- they have materially different acceptance criteria;
- they affect different clients, segments, or user roles in ways that change the contract;
- one portion is well understood while another still requires substantial discovery;
- one portion introduces a distinct capability rather than extending the same behavior;
- completing one portion provides evidence needed to decide whether the next should exist;
- a broad change contains multiple high-risk areas whose failures would be easier to isolate separately.

Do not split merely because many files will change. Do not keep work together merely because it originated in one PRD.

## Distinguish change scope from pull-request scope

The OpenSpec change expresses a product/behavioral outcome. Pull requests are implementation/review units.

One OpenSpec change may reasonably produce several PRs.

Example:

```text
OpenSpec change
Recognize semantically valid assessment-question variants

Suggested delivery slices

PR 1 - evaluation baseline
- add representative failing cases
- establish current behavior
- no production behavior change

PR 2 - behavior change
- update scoring path
- add automated scenario coverage
- protect rollout if needed

PR 3 - observability / configuration
- add telemetry or client-specific configuration if the design requires it
```

These are recommendations. Engineering should be free to alter PR boundaries after inspecting the code, as long as the implementation still satisfies the approved spec and preserves useful validation checkpoints.

## What makes a useful delivery slice

Prefer slices that are:

- reviewable without understanding an enormous diff;
- independently verifiable where possible;
- ordered so early work reduces uncertainty for later work;
- safe to merge without silently changing specified behavior;
- explicit about dependencies;
- capable of leaving the codebase in a coherent state.

A useful sequence often looks like:

```text
test/evaluation oracle
-> enabling refactor or interface
-> behavior change
-> integration / telemetry / rollout work
```

Do not force this sequence when it does not fit the architecture.

## Scope-review questions for the agent

Before recommending `/openspec-propose`, answer:

1. What user/customer outcome is being changed?
2. What is the current behavior or current product contract?
3. What is explicitly out of scope?
4. Could any major portion deliver value independently?
5. Do major portions have different acceptance boundaries?
6. Is there unresolved uncertainty that should be explored before specification?
7. Is there a dependency that should be implemented or validated first?
8. Does the work require materially different client/segment behavior?
9. What would make the change too broad to reason about or accept confidently?

## Recommended output

The agent should return a recommendation in this shape:

```text
Recommended OpenSpec boundary
- <one-sentence behavioral outcome>

Keep inside this change
- ...

Recommend separate/follow-on changes
- ...

Why
- acceptance boundary: ...
- coupling: ...
- uncertainty: ...

Suggested delivery slices
1. ...
2. ...

Dependencies / validation checkpoints
- ...

Unresolved question that could change this recommendation
- ...
```

Avoid false precision such as fixed requirement counts, line counts, or story-point thresholds. Use behavioral coherence and testability as the primary signals.
