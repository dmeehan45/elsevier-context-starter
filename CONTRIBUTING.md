# Contributing

You do not need to understand the ontology to contribute useful knowledge.

## Easiest path

Point an agent at this repository and work in ordinary language. Good examples:

- "Research this topic and teach me what matters first."
- "Here's a link — explain what it adds to our understanding."
- "What from this is actually worth preserving?"
- "Push the recommended items."
- "This conflicts with what we already have; reconcile it."
- "QA what we have on this topic before adding more."

The agent should read `AGENTS.md` and use the relevant workflow in `skills/`.

## Manual contributions are learning-first

When a human is actively involved, the agent should not silently turn research into repository content as it goes.

The normal loop is:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

The agent should first explain the findings, keep useful source citations visible, and connect the research to what the context base already knows. Then it should recommend a small set of durable additions or updates and ask the user for a lightweight decision.

A good curation prompt sounds like:

> I recommend preserving A, B, and C because they materially improve our understanding; D looks too incidental. Want me to push the recommended set?

The human decides **meaning and relevance**. The agent handles **filing, metadata, object types, links, and routine cleanup**.

If the user has already reviewed a specific item and says "push this," that counts as approval to commit it.

## Working from URLs

A public URL can be used as the starting point for a contribution. The agent should read the page when possible, teach the user what it contributes, cite material sourced claims, compare it with existing context, then recommend what is worth preserving.

A link is a source candidate, not automatic truth and not automatic permission to save every detail on the page.

## What a good contribution does

A good contribution makes the library more useful without creating unnecessary administration. It usually does one or more of these things:

- adds a useful source or observation;
- adds or updates a scoped claim;
- clarifies a durable concept or entity;
- synthesizes several objects into a useful summary;
- records an open hypothesis, question, or actual decision;
- corrects stale or conflicting knowledge while preserving provenance.

Prefer improving an existing object over creating a near-duplicate. Prefer a few durable contributions over exhaustive capture of everything learned in a session.

## If you edit by hand

1. Put raw material that still needs processing in `intake/`.
2. Put durable canonical material in the matching `knowledge/` directory.
3. Copy the closest file from `templates/` rather than inventing new metadata.
4. Use stable kebab-case IDs.
5. Link claims to sources whenever possible.
6. Do not turn inference into fact; label hypotheses and uncertainty.
7. Run `python scripts/doctor.py` when Python is available.
8. Run `python scripts/build_indexes.py` after meaningful canonical changes.

## Git workflow

Follow the host repository's branch and review policy. In a shared repository where the policy is unknown, a small branch/pull request is safer than rewriting `main` directly. Keep semantic changes focused and understandable.

Do not force-push, rewrite history, or delete unique evidence as cleanup. When information changes, supersede or dispute the old material so the reason for the change remains recoverable.

## Public repository rule

This repository is public. Contribute public information only. Never add credentials, private connector identifiers, personal data, confidential documents, or non-public company information.

For a future private/internal copy, preserve the same operating contract but apply that environment's information-handling and access rules.