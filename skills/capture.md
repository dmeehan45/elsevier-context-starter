# Skill: Capture to Knowledge Base

Use this workflow when a human wants material considered for durable team context.

## Core principle

For interactive work, **teach before writing**. Low administration means the agent handles filing and metadata; it does not mean removing the user from deciding what is relevant.

The default manual loop is:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

If the user has already explicitly approved a specific item for capture, that approval can satisfy the curate step.

## Procedure

1. **Understand the input.** Identify source, subject, time, scope, and whether the material is direct evidence, a report, synthesis, hypothesis, decision, question, or entity context.
2. **Retrieve before writing.** Search for existing concepts, entities, claims, summaries, sources, and semantic equivalents.
3. **Teach first when the user is still learning.** Explain the important findings, why they matter, how they connect to existing context, and what remains uncertain. Keep source citations visible for externally derived claims when the runtime supports them.
4. **Recommend what is worth preserving.** Separate candidate knowledge into: recommend preserving, optional, and do not preserve. Explain relevance briefly; do not ask the user to choose filenames or metadata.
5. **Ask for a lightweight decision.** For example: "I recommend pushing A, B, and C; D feels incidental. Want me to push the recommended set?" Accept shorthand such as "push recommended," "A and C," "all," or "none."
6. **Preserve provenance.** If the raw material itself matters, save it under `intake/` or create/update a source record under `knowledge/sources/`.
7. **Extract only durable information.** Ignore conversational filler, research scaffolding, and redundant wording.
8. **Update before creating.** Amend canonical material when the information belongs to an existing object. Create a new object only when it has a distinct identity or retrieval purpose.
9. **Keep assertions appropriately atomic.** Put volatile or disputable assertions in claims. Put explanations and definitions in concepts/summaries.
10. **Link provenance.** Connect claims/observations to their sources. Never manufacture a source ID, citation, URL, author, or date.
11. **Check conflicts.** Compare new assertions with existing claims. Use `skills/conflicts.md` for meaningful mismatches.
12. **Validate.** Run `scripts/validate_kb.py` and `scripts/build_indexes.py` when the environment permits.

## When the input is a URL

A dropped link is a request to work with the source, not automatic permission to canonicalize everything on the page.

1. Open/read the page when your environment permits it.
2. Identify the publisher/organization, title, author if available, publication/update date if available, and URL.
3. Prefer an original/primary source when the page points to one and retrieving it is reasonable.
4. Teach the user what the source contributes, with citations close to material sourced claims.
5. Compare it with relevant existing context.
6. Recommend the small set of durable additions or updates worth preserving.
7. Ask before writing unless the user explicitly authorized automatic capture.

If the page cannot be accessed, say so; do not infer its contents from the URL or title.

## Expected response before writing

The user should receive value even if nothing is committed. A good manual response includes:

- the important findings and their significance;
- visible citations/links for externally derived claims;
- relevant conflicts, caveats, or changes to prior understanding;
- a concise recommendation of what should and should not enter the context base;
- one lightweight approval question.

## After approval

Canonicalize the approved set, then tell the user succinctly what was added or updated and surface only unresolved consequential conflicts/questions.

## Automated exception

Scheduled or unattended sweeps follow `skills/sweep.md` and may apply low-risk changes under their configured review policy. They do not need to simulate a teaching conversation when no human is present.

## Guardrail

This repository is public. Only capture information appropriate for a public repository.