# Skill: Maintain the Context Base

Run periodically or after a large ingestion sweep.

## Goal

Keep the corpus coherent, fresh, retrievable, and appropriately bounded without turning maintenance into a human job.

## Checks

### Identity and duplication

- duplicate IDs;
- likely alias concepts/entities;
- files that substantially duplicate another canonical page;
- accidental singular/plural or spelling variants.

### Source provenance

- established claims without source/observation support;
- broken source IDs;
- summaries that make strong assertions no longer supported by linked canonical knowledge;
- circular agent-generated sourcing.

### Contribution provenance

- broken `contribution_ids` or `object_ids`;
- contribution events that reference no material canonical object;
- contribution events whose `object_ids` do not link back through `contribution_ids` when the affected object uses the new provenance contract;
- material semantic changes made after the provenance contract was introduced but lacking a contribution event;
- contributor or `recorded_by` values that were guessed rather than supported by session/platform context;
- accidental deletion of earlier contribution links when an object is updated;
- incomplete handling-confirmation metadata when a sensitivity gate required explicit human destination approval.

Legacy objects created before contribution provenance was introduced are valid without backfilled contribution records. Backfill only when reliable Git/source/session evidence supports the attribution.

### Freshness

- objects whose `review_after` date is due or overdue;
- fast/moderate objects with no explicit review target;
- claims whose subject is time-sensitive but has not been reviewed within its expected freshness window;
- active claims contradicted by a newer superseding claim;
- stale external market information still represented as current;
- summaries that are newer than none of the underlying evidence and may therefore create a false impression of freshness;
- `last_reviewed` dates that appear to have been advanced without a genuine verification event.

Use `skills/review-freshness.md` for semantic freshness work rather than mechanically resetting dates.

### Retrieval quality

- summaries that no longer orient toward the strongest current evidence;
- duplicate concepts/entities that make search ambiguous;
- commonly used topics with no clear summary/entity/concept entry point;
- generated context maps that have become too large or noisy to function as progressive-disclosure routing;
- broken or missing generated indexes;
- retrieval paths that force agents to read broad amounts of unrelated context to answer common questions.

See `docs/retrieval-architecture.md`.

### Information boundary

- material copied from non-public sources without an evident destination check;
- credentials, secrets, personal/regulated data, or other content that should not live in shared context;
- potentially highly confidential material with no explicit human destination confirmation where one was required;
- source records/raw excerpts that duplicate much more sensitive content than is needed for retrieval;
- public-repository content that is not clearly public.

Do not broaden access as part of cleanup. Follow `skills/check-information-boundary.md` when eligibility is uncertain.

### Structure

- invalid or missing IDs/types/status values;
- invalid freshness/handling metadata;
- broken internal links;
- orphaned canonical files;
- unknown relationship targets;
- ontology categories proliferating without clear retrieval value.

### Conflict

- unresolved contradiction links;
- claims marked established while credible contradicting evidence is active;
- multiple active claims that cannot all be true within the same scope/time;
- conflict prompts that omit available source/contributor lineage.

## Automatic repairs

Automatically fix low-semantic-risk problems such as filenames, obvious aliases, broken generated indexes, metadata normalization, and links after a safe rename.

Do not silently merge concepts, reverse established claims, delete unique evidence, invent missing contributor history, reset freshness dates, or approve sensitive information boundaries. Queue those for review.

## Anti-churn rule

A maintenance run is successful even if it changes nothing. Do not rewrite prose, reorder metadata, or rename objects merely to make the repository look maintained.
