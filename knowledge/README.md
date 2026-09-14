# Canonical Knowledge

Subdirectories contain canonical objects defined in `docs/ontology.md`.

```text
sources/        provenance artifacts and origins
observations/   minimally interpreted records
claims/         atomic assertions that can change or conflict
concepts/       durable ideas, definitions, and models
summaries/      derivative orientation across multiple objects
hypotheses/     propositions to test or monitor
decisions/      actual choices made
questions/      unresolved questions worth preserving
entities/       stable referents such as people, teams, products, and institutions
contributions/  audit events recording who contributed material changes and when
```

Prefer updating an existing object over creating duplicates. Use Markdown links and small metadata fields to express useful many-to-many relationships.

`source_ids` answer **where knowledge came from**. `contribution_ids` answer **who added or materially changed it in the shared context base, when, and through what agent/tool**. See `docs/provenance.md`.