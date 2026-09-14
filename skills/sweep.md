# Skill: Sweep Sources

Use this for periodic ingestion across a bounded set of conversations, interviews, notes, documents, feeds, or alerts.

## Goal

Find durable new knowledge and changed knowledge without creating duplicate pages or turning repeated language into false certainty.

## Procedure

1. Define the sweep boundary: sources, date range, or changed material since the previous sweep.
2. For each source, identify candidate observations, claims, concepts, hypotheses, decisions, questions, and entities.
3. Batch candidates by subject before writing. This makes cross-source agreement and conflict visible.
4. Search the canonical corpus for existing equivalents.
5. Prefer updates to existing objects over new files.
6. Treat multiple mentions from the same upstream origin as one evidence lineage, not independent confirmation.
7. Preserve meaningful provenance. Record source IDs and dates when available.
8. Run the conflict workflow for contradictions and supersession.
9. Do not rewrite stable content merely to harmonize style.
10. Finish with ontology maintenance and regenerate indexes.

## Automation behavior

A routine sweep should be safe to run unattended. It may automatically:

- add new non-conflicting observations and source records;
- enrich existing concepts and summaries;
- add provisional claims/hypotheses;
- resolve obvious aliases;
- mark clear time-based supersession;
- close a question when evidence clearly answers it.

It should queue review rather than guess when:

- authoritative sources materially conflict;
- a proposed update reverses an established claim;
- two apparently duplicate concepts may encode a meaningful distinction;
- source authority materially affects the result;
- the operation would delete unique evidence.

## External alerts

Market scans, press releases, regulatory updates, and similar external alerts should enter as sources first. Extract claims with dates and scope. External publication does not make a claim automatically true; preserve who said it.