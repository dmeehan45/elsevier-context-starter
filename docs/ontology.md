# Ontology

The ontology is intentionally small. Its job is to preserve meaning and provenance, not to make every piece of information fit a rigid taxonomy.

## Core object types

### Source

An artifact or origin from which knowledge came: document, webpage, meeting, interview, transcript, dataset, announcement, email, research paper, system output, or similar.

A source can support many observations and claims. A claim can have many sources.

### Observation

A minimally interpreted record of something reported, seen, measured, or directly stated.

Examples: "The interviewee said X," "the dashboard showed Y," or "the document defines Z this way."

Observations preserve what was encountered without requiring the repository to endorse the implication.

### Claim

An atomic assertion about the world that can be supported, disputed, become stale, or be superseded.

A claim may be extracted directly from a source or synthesized from multiple observations. Claims are the right unit for information likely to change or conflict.

A **fact** is represented as a claim with `status: established`, sufficient evidence, an appropriate confidence level, and current scope. This avoids treating facts as immutable.

### Concept

A durable idea, definition, model, mechanism, framework, or vocabulary item. Concepts explain what something means and connect related knowledge.

Concept pages may reference many claims without duplicating them.

### Summary

A human- or agent-readable synthesis across multiple objects. Summaries optimize orientation and retrieval. They are derivative and should link back to relevant evidence.

### Hypothesis

A proposition worth testing or watching. It may be informed by evidence but is not yet treated as established.

### Decision

A choice the team has actually made, ideally including date, scope, rationale, and the evidence or constraints that informed it. Decisions are not the endpoint of all knowledge; they are just one object type in the network.

### Question

An unresolved question that matters enough to preserve. Questions may be answered, partially answered, parked, or reopened.

### Entity

A stable referent such as a person, team, product, institution, customer segment, standard, market, system, or organization. Entity pages help agents resolve names and collect links without turning every entity into a narrative document.

### Contribution

A lightweight audit event recording who caused one or more canonical objects to be created or materially changed, when that contribution occurred, and what agent/tool performed the write.

Contribution records preserve **repository provenance**. They do not replace source provenance. One contribution can affect many objects, and one object can have many contributions over time.

Use contribution records for material semantic changes, not typo fixes, formatting, index generation, or other non-semantic maintenance.

See `docs/provenance.md`.

## Relationships

Use links only when they add retrieval or interpretive value. The preferred relation vocabulary is:

- `about`
- `related`
- `supports`
- `contradicts`
- `supersedes`
- `derived_from`
- `informs`
- `answers`
- `part_of`
- `contribution_ids`

Do not force all relationships into metadata. Normal Markdown links are valid. Use explicit relation fields when the relationship changes epistemic interpretation, especially `supports`, `contradicts`, and `supersedes`.

## Minimal frontmatter

A normal canonical claim may include:

```yaml
---
id: stable-kebab-case-id
type: claim
status: active
confidence: medium
created: 2026-09-14
last_reviewed: 2026-09-14
source_ids:
  - source-id
contribution_ids:
  - contribution-id
related:
  - concept-id
---
```

A contribution record should normally include:

```yaml
---
id: contribution-2026-09-14-example
type: contribution
contributor: person:example-user
contributed_at: 2026-09-14T14:30:00-04:00
recorded_by: agent:example-agent
interaction_type: manual
source_ids: []
object_ids:
  - stable-kebab-case-id
---
```

Only fields that matter should be present. Agents maintain frontmatter so humans rarely need to.

## Status vocabulary

For claims:

- `provisional` — plausible but not yet sufficiently supported
- `active` — current working claim
- `established` — strong enough to rely on within its stated scope
- `disputed` — credible conflicting evidence exists
- `superseded` — replaced by a newer claim while retained for history
- `stale` — freshness is insufficient for current reliance
- `rejected` — investigated and not supported

For hypotheses: `open`, `supported`, `weakened`, `rejected`, `promoted`.

For questions: `open`, `partial`, `answered`, `parked`.

For decisions: `active`, `revisited`, `superseded`, `reversed`.

Contribution records do not need a lifecycle status by default; they are append-only audit events. Correct a mistaken contribution record explicitly rather than silently changing its meaning.

## Confidence

Use `low`, `medium`, or `high`. Confidence is a judgment about evidence quality within the stated scope, not a probability and not a substitute for source links.

## Authority and SDD interpretation

`authority` is an optional interpretation hint for workflows such as spec-driven development. It does **not** create a new object type or make an assertion more true.

Use only when the distinction materially improves downstream behavior:

- `descriptive` — evidence, research, current-state understanding, or synthesis about what appears to be true;
- `advisory` — an accepted recommendation, reusable pattern, or preferred practice that should normally guide work but is not itself a product requirement;
- `normative` — an accepted decision, constraint, contract, or standard that should govern applicable work within its recorded scope.

Do not mass-tag old objects merely to satisfy SDD. Existing records remain usable with these defaults:

- sources, observations, claims, summaries, hypotheses, and questions are descriptive/non-normative unless explicitly stated otherwise;
- an active decision is normative only within the scope actually recorded in that decision;
- a concept is explanatory/descriptive unless it explicitly records an accepted team pattern or constraint;
- contribution records are provenance and carry no product authority.

An SDD agent must not promote descriptive evidence into a requirement silently. If evidence suggests a new rule, the PM/team should make that product or technical decision explicitly and record it in the appropriate OpenSpec artifact; preserve a canonical decision here only when it is durable team context beyond the individual change.

When two applicable normative records conflict, surface the conflict rather than choosing one by recency or confidence alone.

## Contributor identity

Contributor labels are stable actor identifiers rather than authority claims. Prefer readable prefixes such as:

- `person:jeff-landis`
- `person:david-meehan`
- `team:shadow-health`
- `automation:market-scan`

`recorded_by` identifies the executing agent/tool separately, such as `agent:chatgpt`, `agent:claude-code`, or `human:direct-edit`.

Do not infer a human identity from writing style or content. If contributor identity matters and is unavailable, ask once before the first material write.

## Design rule

When unsure whether to create a new ontology category, do not. Start with a claim, concept, summary, source, observation, hypothesis, decision, question, entity, or contribution. Add new types only after recurring use demonstrates a real retrieval problem.