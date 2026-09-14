# Skill: Prepare Task Context

Use this when work will execute in another agent/runtime and that worker needs context from this repository.

## Goal

Produce the smallest useful context packet for the external task without assuming anything about that runtime's permissions, tools, sandbox, connectors, or execution model.

## Procedure

1. **Clarify the objective semantically.** Identify what the worker is being asked to understand, verify, map, compare, inspect, or report.
2. **Retrieve narrowly.** Search canonical knowledge for the relevant entities, concepts, claims, sources, summaries, questions, and contribution lineage.
3. **Expose current state.** Summarize what the context base currently believes, including scope, confidence, freshness, and known disagreement.
4. **Identify verification targets.** Call out claims that are stale, provisional, disputed, incomplete, or especially important to confirm.
5. **Preserve references.** Include stable canonical IDs and relevant source/evidence references so returned findings can be reconciled with the same objects.
6. **Define the expected return shape.** Ask for observed findings, evidence, inference, unresolved gaps, and proposed context changes.
7. **Do not prescribe runtime mechanics.** Do not specify credentials, tool names, browser implementation, network access, sandbox configuration, model, scheduling, or permission rules unless the external environment itself supplied those details as part of the task.
8. **Keep the packet derived.** Do not treat the packet as canonical knowledge. It may be regenerated whenever needed.

## Context selection

Prefer relevance over completeness. Include enough context to prevent the external worker from rediscovering known facts or missing known conflicts, but do not dump the whole repository.

Useful inclusions:

- concise task objective;
- specific questions/verification targets;
- canonical IDs and short summaries;
- current statuses/confidence;
- dates relevant to freshness;
- known conflicts and previous contributors when material;
- sources that should be considered;
- expected evidence/output structure.

Avoid:

- unrelated background;
- credentials or secrets;
- connector IDs that only work in one environment;
- assumed tool availability;
- instructions to bypass runtime restrictions;
- copied generated indexes when direct canonical objects are available.

## Capability-neutral wording

Write the packet in terms of outcomes, not tools.

Prefer:

> Determine the learner-visible steps from assignment launch through completion and provide evidence for each observed state.

Over:

> Open Chrome, use credential X, click these selectors, and save screenshots to path Y.

The runtime may choose a browser, API, connector, or other compliant mechanism. If it cannot perform the task, it should report the limitation.

## Handoff

Use `templates/task-context-packet.md` as a lightweight shape when a structured packet is helpful.

The packet should direct the external worker to return results consistent with `templates/run-report.md`.

See `docs/external-tasking.md` for the boundary between this repository and the execution environment.
