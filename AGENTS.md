# Agent Contract

This repository is a persistent context base for humans and agents. Treat it as shared organizational memory, not as a scratchpad and not as an unquestionable source of truth.

## Before answering from the knowledge base

1. Search canonical material under `knowledge/` before relying on generated indexes.
2. Prefer the most specific relevant source, observation, or claim over a broad summary.
3. Preserve epistemic distinctions. A hypothesis is not a claim; an observation is not automatically an explanation; a summary is not primary evidence.
4. When the answer depends on freshness, inspect `last_reviewed`, source dates, and supersession links.
5. If material conflicts exist, surface them rather than averaging them away.

## When the user says "push this into the knowledge base"

Follow `skills/capture.md`.

The default is **no administrative questions**. Infer filenames, types, links, and metadata when reasonably possible. Ask the user only when ambiguity would materially change meaning, a consequential conflict cannot be resolved from evidence, or the requested action would delete/merge important knowledge.

## Canonicalization rules

- Raw input may be messy. Canonical knowledge should be concise and retrievable.
- Update an existing canonical page when the new information belongs there. Do not create a new file merely because the new wording differs.
- Prefer atomic claims for assertions likely to change, conflict, or need provenance.
- Keep broader explanatory material in concepts and summaries.
- Do not convert repeated mentions into stronger truth. Repetition is not independent evidence.
- Do not convert an agent inference into an established claim without supporting evidence.
- Do not erase history when information changes. Use `supersedes`, `contradicts`, status changes, and source links.
- Obvious temporal updates may be canonicalized automatically. Material contradictions should be added to the review queue and surfaced to the user.

## Provenance

Every durable assertion should be traceable to at least one of:

- a source artifact,
- a direct observation,
- a named human report captured as a source/observation,
- or an explicitly labeled synthesis/hypothesis.

Never fabricate citations, dates, people, source identifiers, or confidence.

## Retrieval behavior

When using this context base:

- retrieve narrowly first, then expand through links;
- cite or name the relevant canonical files when useful;
- distinguish established claims from disputed, stale, or provisional ones;
- prefer primary/internal sources over summaries when answering factual questions;
- use summaries for orientation, not as a substitute for evidence when evidence matters.

## Maintenance behavior

Follow `skills/maintain.md` for periodic sweeps. Most low-risk cleanup should happen without human intervention. Human review is reserved for semantic merges, consequential contradictions, unclear authority, and destructive changes.

## Public starter safety

Until this repository is moved into an approved private/internal environment, do not ingest confidential Elsevier information or any other non-public company information.