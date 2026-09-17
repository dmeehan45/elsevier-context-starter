# SDD Context Map

Generated routing view for product managers and agents using shared context around spec-driven development. Do not edit manually.

This is a router, not an OpenSpec artifact and not a stage taxonomy. Start from the product decision being made, retrieve the smallest useful canonical objects, and re-retrieve when the task changes.

## Operating guides

- [PM SDD workflow](../docs/sdd/pm-workflow.md)
- [Context routing](../docs/sdd/context-routing.md)
- [Scope and delivery slicing](../docs/sdd/scope-and-delivery-slicing.md)
- [Verification and acceptance](../docs/sdd/verification-and-acceptance.md)
- [OpenSpec integration boundary](../docs/sdd/openspec-adapter.md)
- [SDD PM companion skill](../skills/sdd-pm-companion.md)

## Retrieval by product decision

### Explore a product problem

Use orientation summaries first, then retrieve relevant concepts/entities, claims/observations, hypotheses/questions, decisions, and sources only as needed.

### Orientation summaries

- [Elsevier acquisition history — 2026](../knowledge/summaries/elsevier-acquisition-history-2026.md)
- [Elsevier corporate map — 2026](../knowledge/summaries/elsevier-corporate-map-2026.md)
- [Elsevier leadership influence map — 2026](../knowledge/summaries/elsevier-leadership-influence-map-2026.md)
- [Elsevier product portfolio — 2026](../knowledge/summaries/elsevier-product-portfolio-2026.md)
- [Nursing edtech buying and leadership map — 2026](../knowledge/summaries/nursing-edtech-buying-and-leadership-map-2026.md)
- [Nursing learner population and career lifecycle — 2026](../knowledge/summaries/nursing-learner-population-and-career-lifecycle-2026.md)
- [Nursing learning journey and simulation map — 2026](../knowledge/summaries/nursing-learning-journey-and-simulation-map-2026.md)
- [Nursing program archetypes and campus variation — 2026](../knowledge/summaries/nursing-program-archetypes-and-campus-variation-2026.md)
- [Nursing program technology backdrop — 2026](../knowledge/summaries/nursing-program-technology-backdrop-2026.md)
- [Nursing and Shadow Health acronym catalogue — 2026](../knowledge/summaries/nursing-shadow-health-acronym-catalogue-2026.md)
- [Nursing student technology environment — 2026](../knowledge/summaries/nursing-student-technology-environment-2026.md)
- [Shadow Health at a glance — 2026](../knowledge/summaries/shadow-health-at-a-glance-2026.md)
- [Shadow Health competitive landscape — 2026](../knowledge/summaries/shadow-health-competitive-landscape-2026.md)
- [Shadow Health history and acquisition — 2026](../knowledge/summaries/shadow-health-history-acquisition-2026.md)
- [Shadow Health marketing vs product docs — 2026](../knowledge/summaries/shadow-health-marketing-vs-product-docs-2026.md)
- [Shadow Health product audiences — 2026](../knowledge/summaries/shadow-health-product-audiences-2026.md)
- [Shadow Health SWOT — 2026](../knowledge/summaries/shadow-health-swot-2026.md)

### Open hypotheses

- [Shadow Health learner transition segmentation — 2026](../knowledge/hypotheses/shadow-health-learner-transition-segmentation-2026.md)
- [Shadow Health segmentation by program operating model — 2026](../knowledge/hypotheses/shadow-health-segmentation-by-program-operating-model-2026.md)

### Open / partial questions

- [Nursing learner population research gaps — 2026](../knowledge/questions/nursing-learner-population-research-gaps-2026.md)
- [Nursing program technology integration gaps — 2026](../knowledge/questions/nursing-program-technology-integration-gaps-2026.md)
- [Nursing program variation research gaps — 2026](../knowledge/questions/nursing-program-variation-research-gaps-2026.md)
- [Shadow Health client device telemetry — 2026](../knowledge/questions/shadow-health-client-device-telemetry-2026.md)

## Review scope / requirements

Use active decisions as applicable constraints, then retrieve claims and client/user context that could change the boundary. Descriptive evidence informs requirements but does not become normative automatically.

### Active decisions

_No active canonical decision objects are currently present. This means an SDD agent should be especially careful not to infer product requirements from research summaries/claims._

### Explicit advisory / normative guidance

_No objects are explicitly tagged advisory/normative yet. Existing active decisions would be normative within their recorded scope; other legacy records retain their normal epistemic meaning._

## Prepare PM acceptance

Primary acceptance behavior comes from the target project's approved OpenSpec requirements/scenarios. Use this context base to retrieve relevant client/user variation, accepted decisions, evaluation concepts, and known environment constraints.

Use [Prepare PM Acceptance](../skills/prepare-pm-acceptance.md) and [Staging Acceptance Check](../templates/staging-acceptance-check.md).

## Existing-data rule

No backfill is required before using the current corpus for SDD. Interpret legacy objects by type and status; see [authority and SDD interpretation](../docs/ontology.md#authority-and-sdd-interpretation). Add authority metadata only when it materially improves downstream interpretation.

## Retrieval rule

Do not load the whole repository or carry a large Explore context into Apply. Retrieve again for the next decision. Use targeted repository search when the objects above are not enough. Rebuild this view with `python scripts/build_indexes.py` after meaningful canonical changes.
