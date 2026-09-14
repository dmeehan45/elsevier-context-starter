# Contributing

You do not need to understand the ontology to contribute useful knowledge.

## Easiest path

Point an agent at this repository and say what you want in ordinary language. Good examples:

- "Push this into the knowledge base."
- "Add the durable findings from these notes."
- "Update what we know about this company using these sources."
- "This conflicts with what we already have; reconcile it."
- "QA what we have on this topic before adding more."

The agent should read `AGENTS.md` and use the relevant workflow in `skills/`.

## What a good contribution does

A good contribution makes the library more useful without creating unnecessary administration. It usually does one or more of these things:

- adds a useful source or observation;
- adds or updates a scoped claim;
- clarifies a durable concept or entity;
- synthesizes several objects into a useful summary;
- records an open hypothesis, question, or actual decision;
- corrects stale or conflicting knowledge while preserving provenance.

Prefer improving an existing object over creating a near-duplicate.

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