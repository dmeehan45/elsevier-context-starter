# Skill: Maintain the Context Base

Run periodically or after a large ingestion sweep.

## Goal

Keep the corpus coherent without turning maintenance into a human job.

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
- accidental deletion of earlier contribution links when an object is updated.

Legacy objects created before contribution provenance was introduced are valid without backfilled contribution records. Backfill only when reliable Git/source/session evidence supports the attribution.

### Freshness

- claims whose subject is time-sensitive but has not been reviewed within its expected freshness window;
- active claims contradicted by a newer superseding claim;
- stale external market information still represented as current.

### Structure

- invalid or missing IDs/types/status values;
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

Do not silently merge concepts, reverse established claims, delete unique evidence, or invent missing contributor history. Queue those for review.

## Anti-churn rule

A maintenance run is successful even if it changes nothing. Do not rewrite prose, reorder metadata, or rename objects merely to make the repository look maintained.