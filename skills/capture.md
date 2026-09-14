# Skill: Capture to Knowledge Base

Use this workflow when the user says "push this into the knowledge base," "remember this in the context base," or provides material whose explicit purpose is durable team context.

## Goal

Turn messy input into useful canonical knowledge with minimal user administration.

## Procedure

1. **Understand the input.** Identify source, subject, time, scope, and whether the material is direct evidence, a report, a synthesis, a hypothesis, a decision, or a question.
2. **Preserve provenance when useful.** If the raw material itself matters, save it under `intake/` or create/update a source record under `knowledge/sources/`.
3. **Retrieve before writing.** Search for existing concepts, entities, claims, summaries, and semantic equivalents.
4. **Extract only durable information.** Ignore conversational filler and redundant wording.
5. **Update before creating.** Amend canonical material when the information belongs to an existing object. Create a new object only when it has a distinct identity or retrieval purpose.
6. **Keep assertions appropriately atomic.** Put volatile or disputable assertions in claims. Put explanations and definitions in concepts/summaries.
7. **Link provenance.** Connect claims/observations to their sources. Never manufacture a source ID.
8. **Check conflicts.** Compare new assertions with existing claims. Use `skills/conflicts.md` when there is a meaningful mismatch.
9. **Minimize human review.** Resolve naming, filenames, routine dedupe, and clear temporal updates automatically. Ask only about consequential ambiguity.
10. **Regenerate navigation.** Run `scripts/validate_kb.py` and `scripts/build_indexes.py` when the environment permits.

## Expected response

After a successful capture, tell the user succinctly what was added or updated and surface only unresolved conflicts/questions. Do not require them to inspect metadata or perform filing work.

## Guardrail

If this repository is still public, do not capture non-public Elsevier material. Tell the user to perform the capture in the approved private/internal clone instead.