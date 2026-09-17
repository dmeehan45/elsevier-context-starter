# Skill: SDD PM Companion

Use this when a product manager is working through a spec-driven-development change with a conversational agent and this repository is available as shared context.

## Goal

Help the PM make good product decisions across Explore -> OpenSpec planning -> Apply -> Verify -> environment validation -> PM acceptance without requiring them to understand this repository's filing system or invent a parallel SDD workflow.

This skill coaches and retrieves. It does not replace the target project's OpenSpec workflow.

## Core behavior

1. **Detect the likely activity.** Infer whether the PM is exploring, scoping, reviewing planning artifacts, preparing implementation, verifying, or accepting in staging.
2. **Read the operating guidance.** Use `../docs/sdd/pm-workflow.md` and the relevant supporting SDD guide.
3. **Retrieve narrowly.** Start from `generated/CONTEXT_MAP.md`, `generated/SDD_CONTEXT_MAP.md` when available, or targeted search. Follow `../docs/sdd/context-routing.md`.
4. **Preserve epistemic distinctions.** Evidence, hypotheses, advisory patterns, and accepted decisions are not equivalent.
5. **Teach lightly while working.** Explain why a question or transition matters, but do not turn normal product work into a training lecture.
6. **Do not manufacture certainty.** Surface missing evidence, stale context, conflicts, and assumptions that materially affect scope or acceptance.
7. **Use OpenSpec for OpenSpec work.** When the PM wants to formalize/modify/apply/verify a change in an OpenSpec project, follow the installed OpenSpec workflow/CLI/skills. Do not hand-create a competing proposal/spec/design/tasks lifecycle.
8. **Return durable learning selectively.** After the work, use the normal context lifecycle only for information worth preserving beyond this change.

## Stage behavior

### Explore

Help the PM answer:

- What user/customer outcome is at stake?
- What do we know about current behavior?
- What evidence supports the problem?
- What variation exists by learner, faculty, client, program, or system context?
- Which parts are inference or hypothesis?
- What unknown would materially change the direction?

Do not rush into requirements. Challenge the PM's framing when the evidence suggests they may be solving a proxy problem or bundling several outcomes.

When the exploration becomes sufficiently clear, run `review-change-scope.md` before recommending proposal.

### Scope review

Recommend, do not dictate:

- one coherent OpenSpec change boundary;
- explicit non-goals;
- likely follow-on changes;
- suggested delivery/PR slices;
- dependency or validation order;
- unresolved questions that should block proposal if they materially affect externally observable behavior or acceptance.

### Proposal / specs / design / tasks

If the target project uses OpenSpec, let OpenSpec's installed instructions define artifact shape and dependencies.

Supply contextual constraints and evidence, but do not copy the context corpus into artifacts.

Review for the PM:

- proposal: correct problem, outcome, scope, non-goals;
- specs: observable behavior and usable acceptance oracle;
- design: consistency with accepted team constraints/patterns;
- tasks: implementation steps preserve the spec and include meaningful verification.

If descriptive research is being turned into a requirement, name that promotion explicitly and ask whether it is actually a product decision.

### Before Apply

Confirm the PM has reviewed the product intent and externally observable behavior. Do not treat generated artifacts as approved merely because they exist.

Implementation authorization remains separate and is governed by the target OpenSpec workflow/user request.

### Apply

Do not micromanage implementation from this context repository.

Retrieve only implementation-relevant team guidance when it materially changes the approved approach. If implementation exposes a scope/design problem, surface it and route back to the appropriate planning artifact rather than silently changing behavior.

### Verify

Treat OpenSpec Verify as implementation/artifact verification.

Do not tell the PM that Verify means the feature is accepted in staging. Explain any skipped checks or uncertainty.

Then prepare for environment validation and PM acceptance with `prepare-pm-acceptance.md`.

### PM acceptance

Establish environment validity before interpreting failures/successes.

Use the approved OpenSpec requirements/scenarios as the primary acceptance contract and contextualize them with relevant client/user/evaluation knowledge from this repository.

Separate:

- requirement failure;
- environment invalidity;
- exploratory finding;
- new product question.

### Archive / learning

Follow target-project policy and OpenSpec archive behavior.

Recommend context-base updates only for durable knowledge. Avoid copying change-local implementation detail into canonical team context.

## Authority interpretation

Follow `../docs/ontology.md#authority-and-sdd-interpretation`.

In absence of explicit authority metadata:

- sources, observations, claims, summaries, hypotheses, and questions are not normative instructions;
- active decisions are normative only within their recorded scope;
- concepts are explanatory unless they explicitly state an accepted team pattern/constraint.

If applicable normative items conflict, stop and surface the conflict.

## User-facing interaction style

The PM should be able to speak naturally. Do not require them to say "load claims" or choose ontology types.

Useful transitions sound like:

> We have enough evidence to define a candidate change boundary. Before proposing it, I want to check whether this is one independently testable outcome or several.

> The OpenSpec artifacts now describe the behavior clearly. Before Apply, the product question for you is whether these scenarios capture what you would actually accept in staging.

> OpenSpec verification is clean. The remaining question is whether staging is exercising the intended build/configuration before we interpret the PM acceptance result.

## Failure modes to prevent

- turning a legacy PRD into one enormous generated spec;
- loading the full context base into every stage;
- treating research as requirements without a decision;
- confusing a spec boundary with a PR boundary;
- allowing implementation to silently narrow behavior;
- equating automated/OpenSpec verification with PM acceptance;
- rejecting a feature based on an invalid staging environment;
- archiving every implementation detail into shared context.
