# Contribution Provenance

This context base preserves two different kinds of provenance because they answer different questions.

## Knowledge provenance

**Where did this information come from?**

This is represented by sources, observations, citations, `source_ids`, source dates, and fields such as `author_or_speaker`.

Example: Jeff said something in an onboarding conversation on Tuesday. Jeff and Tuesday belong to the source provenance even if someone else later records the learning.

## Contribution provenance

**Who decided to put or change this information in the shared context base, when, and through what agent/tool?**

This is represented by a `contribution` object under `knowledge/contributions/`.

A contribution is a lightweight audit event. One contribution may update several canonical objects, and one canonical object may accumulate many contributions over time.

## Contribution fields

A contribution should normally include:

```yaml
---
id: contribution-2026-09-14-jeff-shadow-health-onboarding
type: contribution
contributor: person:jeff-landis
contributed_at: 2026-09-14T14:30:00-04:00
recorded_by: agent:claude-code
interaction_type: manual
source_ids:
  - source-jeff-onboarding-2026-09-14
object_ids:
  - example-claim
  - example-concept
---
```

Use the most precise timestamp the environment can reliably provide. ISO 8601 with timezone is preferred. A date-only value is acceptable when time is unavailable.

### `contributor`

The human, team, or automated process whose contribution this represents. Prefer stable readable actor labels such as `person:jeff-landis`, `person:david-meehan`, `team:shadow-health`, or `automation:market-scan`.

Do not guess a person's identity. If a human is actively contributing and their identity is not available from the authenticated environment or conversation, ask once before the first durable write and reuse that identity for the session.

### `recorded_by`

The agent/tool that actually performed the write, for example `agent:chatgpt`, `agent:claude-code`, `agent:hermes`, `agent:microsoft`, or `human:direct-edit`.

This is not the same as the contributor. David may approve a contribution that ChatGPT writes; Jeff may be the source speaker whose statement David is preserving.

### `interaction_type`

Useful values include `manual`, `url-research`, `meeting-notes`, `document-review`, `import`, and `automated-sweep`. This is descriptive, not a rigid ontology.

### `object_ids`

The canonical objects created or materially changed by the contribution. Do not create contribution records for typo fixes, index regeneration, formatting, or other non-semantic maintenance.

## Canonical object links

Canonical objects may include:

```yaml
contribution_ids:
  - contribution-2026-09-14-jeff-shadow-health-onboarding
```

When an object is materially changed later, append the new contribution ID rather than replacing the old one. This makes the contribution history portable without depending exclusively on Git history.

## Source vs contributor example

Suppose David interviews Jeff on Tuesday and pushes the learning on Wednesday through ChatGPT.

The **source** records Jeff as `author_or_speaker` and Tuesday as `source_date`.

The **contribution** records David as `contributor`, Wednesday as `contributed_at`, and ChatGPT as `recorded_by`.

A later conflict can therefore say: "The current claim traces to something Jeff reported Tuesday and David added Wednesday. The new information disagrees. Is this a newer state, different scope, or a genuine contradiction?"

If Jeff himself was working with his own agent and approved the contribution, Jeff would be the `contributor` as well.

## Conflict behavior

Before proposing an overwrite or supersession, retrieve both source provenance and contribution provenance.

Use them in the question to the human. Prefer a prompt with concrete lineage:

> Existing claim: contributed by Jeff on 2026-09-08, based on an onboarding conversation. New evidence: product documentation updated 2026-09-14. These appear to disagree about the same scope. Should we treat the new information as a supersession, keep both as scope-specific, or mark the claim disputed?

Do not silently overwrite a meaningful human contribution merely because newer text exists.

## Legacy objects

Objects created before this contract may not have `contribution_ids`. Do not invent them.

When reliable Git history, source records, or conversation metadata make the lineage clear, an agent may backfill contribution records. Otherwise leave the legacy object as-is and say that contributor provenance is unavailable.