# Universal Agent Contract

This repository is a persistent context base for humans and agents. Treat it as shared organizational memory: useful and curated, but never unquestionable.

This file is intentionally vendor-neutral. Follow it whether you are running in a coding agent, chat agent, enterprise agent platform, local open-source model, autonomous harness, or a future system not anticipated here.

## Bootstrap protocol

When a user points you at this repository with little or no additional instruction:

1. Read `README.md` and this file.
2. Identify your capabilities: read/search, write/edit, shell execution, Git operations, pull requests, external-source access.
3. Do not assume capabilities you do not have.
4. If the user asks what this is, explain it in simple language: this is a shared knowledge library where raw inputs can be turned into sourced, updateable context for humans and agents.
5. For a task, retrieve only the relevant canonical material under `knowledge/`; do not ingest the whole repository into the answer by default.
6. Read the relevant workflow under `skills/` before changing canonical knowledge.

If you have read-only access, you may still answer from the library and propose exact changes. Never claim that files were changed, committed, or pushed unless they actually were.

## Common user intents

- **"What does the context base say about X?"** Retrieve canonical material and answer with epistemic distinctions intact.
- **"Push this into the knowledge base."** Follow `skills/capture.md`.
- **"Sweep these sources."** Follow `skills/sweep.md`.
- **"QA/clean up the knowledge base."** Follow `skills/maintain.md`.
- **"These two things conflict."** Follow `skills/conflicts.md`.
- **"How do I contribute/use/move this?"** Use `README.md`, `CONTRIBUTING.md`, `docs/agent-interop.md`, and `docs/portability.md`.

The default is **low administration for the user**. Infer filenames, types, links, and routine metadata when reasonably possible. Ask only when ambiguity materially changes meaning, a consequential conflict cannot be resolved from evidence, or the requested action would destroy/merge important knowledge.

## Before answering from the knowledge base

1. Search canonical material under `knowledge/` before relying on generated indexes.
2. Prefer the most specific relevant source, observation, or claim over a broad summary.
3. Preserve epistemic distinctions. A hypothesis is not a claim; an observation is not automatically an explanation; a summary is not primary evidence.
4. When freshness matters, inspect source dates, `last_reviewed`, status, and supersession links.
5. If credible material conflicts, surface the conflict rather than averaging it away.
6. Do not treat repeated copies of one upstream assertion as independent evidence.

## Write protocol

Before changing canonical knowledge:

1. Retrieve existing objects about the same subject and obvious aliases.
2. Classify the new material using `docs/ontology.md`.
3. Update before creating. A wording difference is not a new object.
4. Preserve provenance. Do not manufacture source IDs, people, citations, dates, confidence, or authority.
5. Check whether the new information confirms, refines, supersedes, contradicts, reframes, or is orthogonal to existing material.
6. Preserve meaningful history when the current view changes.
7. Validate the result when your environment permits it.
8. Tell the user briefly what changed and surface only unresolved consequential issues.

Raw input may be messy. Canonical knowledge should be concise, scoped, and retrievable.

## Canonicalization rules

- Prefer atomic claims for assertions likely to change, conflict, or need provenance.
- Keep broader explanations and reusable models in concepts and summaries.
- A fact is represented as a sufficiently supported claim, not as an immutable type.
- Repetition is not independent confirmation.
- Agent inference must remain labeled as synthesis/hypothesis unless evidence supports promotion.
- Do not silently erase earlier evidence. Use status, `supersedes`, `contradicts`, and source links.
- Clear temporal updates can usually be applied automatically; consequential semantic reversals require review.

## Capability-specific behavior

**Local clone + shell:** edit repository-relative paths; run `python scripts/doctor.py` and `python scripts/build_indexes.py` when appropriate; use normal Git hygiene.

**Git hosting/API write access but no shell:** make the same file changes through the repository API. Perform validation semantically if scripts cannot run, and say that executable checks were not run.

**Read-only repository access:** answer and propose a patch/change set. Do not create a parallel memory store unless the user requests one.

**Agent platform with its own memory/search:** that memory is a retrieval aid, not canonical truth. Durable team knowledge belongs in this repository if the user asks to preserve it here.

See `docs/agent-interop.md` for adapter guidance.

## Git and collaboration safety

- Respect the repository's existing branch/review policy.
- If write policy is unknown in a shared repository, prefer a branch/pull request when your tooling supports it.
- Do not force-push, rewrite history, delete unique provenance, or change remotes without explicit instruction.
- Keep commits focused enough that another human or agent can understand the semantic change.
- Never commit secrets, credentials, access tokens, private connector identifiers, or machine-specific absolute paths.
- Do not make canonical behavior depend on uncommitted local files.

## Portability rules

Canonical knowledge must survive a plain Git clone or mirror:

- use stable repository-relative paths and stable object IDs;
- avoid symlinks and machine-specific paths;
- do not require a specific agent vendor, hosted database, or proprietary memory layer;
- treat generated files as rebuildable;
- keep platform-specific adapters optional and subordinate to this contract.

## Maintenance behavior

Follow `skills/maintain.md` periodically or after large sweeps. Automatically repair low-semantic-risk problems. Human review is reserved for semantic merges, consequential contradictions, unclear source authority, and destructive changes.

## Public repository safety

This repository is currently public. Only public information may be added here. If the material is non-public, confidential, proprietary, personal, or otherwise restricted, do not write it to this repository; use the approved private/internal copy instead.