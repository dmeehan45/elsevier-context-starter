# OpenSpec integration boundary

Use OpenSpec as the planning and implementation workflow in repositories that adopt it. Use this context base as a selectively retrieved source of product/team knowledge around that workflow.

Do not duplicate the context corpus into `openspec/config.yaml`, and do not create a parallel artifact lifecycle here.

## Thin adapter principle

A target project's OpenSpec configuration should contain only enough stable guidance to tell the planning/implementation agent how to use shared team context.

Conceptual example:

```yaml
context: |
  Shared team/product context exists outside this repository.
  Do not load that corpus in full.
  Retrieve only context relevant to the current product capability,
  affected user/client scope, and decision being made.

  Treat descriptive context as evidence, advisory context as guidance,
  and normative context as an applicable constraint within its stated scope.

rules:
  proposal:
    - Ground the problem and scope in relevant evidence and accepted decisions.
    - Surface material unresolved questions rather than silently assuming answers.
  specs:
    - Keep externally observable behavior testable.
    - Do not promote descriptive research into a requirement without a product decision.
  design:
    - Consult applicable architecture, design-system, client-variation, and evaluation guidance.
  tasks:
    - Include meaningful verification steps and preserve explicit acceptance behavior.

operations:
  apply:
    guidance:
      - Retrieve implementation-relevant shared context when it changes how the approved artifacts should be implemented.
      - If implementation reveals a change to specified behavior, surface it and update planning artifacts rather than silently narrowing scope.
```

This is an example, not a file to copy blindly. Adapt it to the version/schema installed in the target repository and validate it against current OpenSpec documentation/CLI behavior.

## What stays under OpenSpec control

OpenSpec remains authoritative for:

- schema selection;
- artifact dependencies and instructions;
- change state;
- proposal/spec/design/task locations;
- apply blocked/ready/completion behavior;
- verification behavior;
- sync/archive semantics.

This context base must not instruct an agent to bypass an OpenSpec blocked state or reinterpret an artifact as complete.

## What this context base adds

The shared context layer provides:

- product/domain/customer evidence;
- hypotheses and open questions;
- accepted decisions and constraints;
- reusable design/implementation/evaluation patterns when the team has actually established them;
- client/segment variation;
- workflow coaching for PMs;
- scope and delivery-slicing recommendations;
- environment-validity and PM-acceptance guidance.

## Explore

A conversational agent may use this repository heavily during exploration, but should still inspect the target project's existing OpenSpec specs and code when they are relevant to current behavior.

Exploration is not authorization to implement. When the PM is ready to formalize the change, hand planning to the target project's installed OpenSpec workflow.

## Proposal / artifact generation

Retrieve context for the decision being made and pass it to the agent as working context. Do not paste large source documents into OpenSpec artifacts merely so the implementation agent can see them.

Artifacts should contain the product intent, requirements, design choices, and implementation tasks that belong to the change. Evidence remains linked/retrievable from the context base.

## Apply

Apply should primarily consume the approved OpenSpec artifacts and the target codebase. Retrieve shared context only where it constrains or materially informs implementation.

## Verify and PM acceptance

Do not overload OpenSpec Verify with a separate PM-acceptance meaning. Use OpenSpec Verify for artifact/implementation consistency and use the workflow in `verification-and-acceptance.md` for environment validity and product acceptance.

## Future shared OpenSpec stores

OpenSpec's cross-repository store/reference mechanisms may eventually be useful for genuinely shared **normative specs** such as accessibility, platform contracts, or client-configuration requirements.

Do not convert descriptive research into OpenSpec specs merely to make it referenceable. Adopt shared stores only when repeated team usage demonstrates a real need and the installed OpenSpec version supports the intended behavior reliably.
