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

Do not force all relationships into metadata. Normal Markdown links are valid. Use explicit relation fields when the relationship changes epistemic interpretation, especially `supports`, `contradicts`, and `supersedes`.

## Minimal frontmatter

Canonical pages should usually include:

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
related:
  - concept-id
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

## Confidence

Use `low`, `medium`, or `high`. Confidence is a judgment about evidence quality within the stated scope, not a probability and not a substitute for source links.

## Design rule

When unsure whether to create a new ontology category, do not. Start with a claim, concept, summary, source, observation, hypothesis, decision, question, or entity. Add new types only after recurring use demonstrates a real retrieval problem.