# Skill: Review Change Scope

Use this before creating or materially expanding an OpenSpec proposal when a PM needs help deciding whether the work is one coherent change, several changes, or one change with multiple implementation slices.

## Goal

Recommend a product/behavioral boundary that is small enough to reason about and accept confidently without fragmenting tightly coupled behavior into artificial micro-specs.

The recommendation is advisory. The PM owns product intent; engineering may later adjust implementation/PR boundaries.

## Procedure

1. **State the intended outcome.** Express the user/customer behavior being changed in one sentence.
2. **Retrieve relevant context.** Use summaries, active decisions, claims about affected users/clients, hypotheses, questions, and known constraints. Do not load the full corpus.
3. **Separate outcomes from implementation.** Identify independently valuable behavioral outcomes before discussing files or pull requests.
4. **Check acceptance coupling.** Ask whether the major parts share one acceptance boundary or can be judged independently.
5. **Check rollout coupling.** Determine whether portions could reasonably ship/rollback separately.
6. **Check uncertainty.** Is one portion still exploratory enough that specifying it now would manufacture certainty?
7. **Check population/client variation.** Different external contracts may warrant distinct changes even when implementation overlaps.
8. **Identify dependencies.** Prefer an order that reduces uncertainty and leaves useful validation checkpoints.
9. **Recommend a boundary.** Keep one coherent outcome inside the current change; name likely follow-ons explicitly.
10. **Recommend delivery slices separately.** Suggest PR/implementation slices only after the product change boundary is clear.

## Split signals

A split recommendation becomes stronger when:

- a sub-part is independently useful;
- it has different acceptance criteria;
- it can ship/rollback independently;
- it affects a materially different user/client contract;
- one portion is much less understood than another;
- one change provides evidence needed to decide whether another should exist;
- combined scope would make failure attribution or PM acceptance materially harder.

Do not split merely because many code files will change. Do not keep work together merely because it came from one PRD or Jira epic.

## Delivery-slice guidance

Suggested slices should be reviewable, dependency-aware, and independently verifiable where practical.

Common patterns include:

```text
evaluation/test oracle
-> enabling interface/refactor
-> behavioral implementation
-> integration / observability / rollout
```

This is a pattern, not a required sequence.

Do not ask the PM to define exact source-code PR boundaries when the agent/engineering team can make a better recommendation from the target codebase.

## Output contract

Return:

```text
Recommended OpenSpec boundary
- <one-sentence outcome>

Keep inside this change
- ...

Recommend separate/follow-on changes
- ...

Rationale
- acceptance coupling: ...
- rollout coupling: ...
- uncertainty: ...
- client/user variation: ...

Suggested delivery/PR slices
1. ...
2. ...

Dependencies / validation checkpoints
- ...

Unresolved question that could change the recommendation
- ...
```

If the work is already appropriately scoped, say so and explain why rather than inventing a split.
