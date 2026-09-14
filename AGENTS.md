# Universal Agent Contract

This repository is a persistent context base for humans and agents. Treat it as shared organizational memory: useful and curated, but never unquestionable.

This file is intentionally vendor-neutral. Follow it whether you are running in a coding agent, chat agent, enterprise agent platform, local open-source model, autonomous harness, or a future system not anticipated here.

## Bootstrap protocol

When a user points you at this repository with little or no additional instruction:

1. Read `README.md` and this file.
2. Identify your capabilities: read/search, write/edit, shell execution, Git operations, pull requests, external-source access.
3. Do not assume capabilities you do not have.
4. If the user asks what this is, explain it simply: this is a shared knowledge library where sourced information can be turned into updateable context for humans and agents.
5. For a task, retrieve only the relevant canonical material under `knowledge/`; do not ingest the whole repository into the answer by default.
6. Read the relevant workflow under `skills/` before changing canonical knowledge.

If you have read-only access, you may still answer from the library and propose exact changes. Never claim that files were changed, committed, or pushed unless they actually were.

## Common user intents

- **"What does the context base say about X?"** Retrieve canonical material and answer with epistemic distinctions intact.
- **"Research/explain X."** Teach the user first; do not silently write research findings while they are still learning.
- **A user drops a URL.** Read the page if possible, explain what it contributes with citations, compare it with existing context, then recommend what is worth preserving.
- **"Push this into the knowledge base."** Follow `skills/capture.md`. If the user has already reviewed the material, this can count as approval to write it.
- **"Sweep these sources."** Follow `skills/sweep.md`.
- **"QA/clean up the knowledge base."** Follow `skills/maintain.md`.
- **"These two things conflict."** Follow `skills/conflicts.md`.
- **"How do I contribute/use/move this?"** Use `README.md`, `CONTRIBUTING.md`, `docs/agent-interop.md`, and `docs/portability.md`.

## Manual learning contract: teach before curating

When a human is actively researching with you, optimize for their learning before optimizing for repository growth.

Use this default loop:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

### 1. Investigate

Retrieve relevant existing context and examine the new sources. Separate direct source content from your synthesis or inference.

### 2. Teach

Explain the important findings, why they matter, and how they connect. Surface uncertainty, contradictions, and changes to prior understanding. Keep citations visible for externally derived claims whenever the runtime supports citations or links.

The response should be useful even if nothing is eventually saved.

### 3. Curate with the user

Recommend a small set of durable additions/updates and explain why they are relevant. Distinguish:

- **recommend preserving**;
- **optional**;
- **do not preserve**.

Then ask for one lightweight decision. Do not ask the user to choose filenames, object types, metadata, or folder locations.

Accept shorthand such as **"push recommended," "all," "A and C,"** or **"none."**

### 4. Commit after approval

Canonicalize only the approved set, unless the user clearly authorized automatic capture in advance.

This approval loop applies to interactive manual research. Scheduled/unattended sweeps may apply low-risk changes under `skills/sweep.md` because no human may be present to teach in real time.

The default is still **low administration for the user**: agents own clerical work; humans stay involved in meaning and relevance.

## Citation behavior

For externally researched material:

- cite material claims close to the claim they support when the runtime allows it;
- prefer primary sources when available and appropriate;
- do not present a source's assertion as independent fact without considering authority and scope;
- do not manufacture URLs, source names, publication dates, authors, or citation details;
- when comparing new research to the repository, name the relevant canonical object/file rather than pretending the repository is an external source.

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
7. For every material semantic write, create one contribution event under `knowledge/contributions/` and link affected canonical objects through `contribution_ids`.
8. Validate the result when your environment permits it.
9. Tell the user briefly what changed and surface only unresolved consequential issues.

Raw input may be messy. Canonical knowledge should be concise, scoped, and retrievable.

## Contribution provenance

Source provenance and contribution provenance are different. Preserve both. See `docs/provenance.md`.

A source answers **where the information came from**. A contribution answers **who decided to add/change it in shared context, when, and through which agent/tool**.

For a material write:

- identify the contributor from authenticated/session context when available;
- if a human contributor is unknown, ask once before the first durable write rather than guessing;
- use a stable actor label such as `person:jeff-landis`, `team:shadow-health`, or `automation:market-scan`;
- record the executing tool separately, such as `agent:chatgpt` or `agent:claude-code`;
- include every materially changed canonical object in the contribution's `object_ids`;
- append the contribution ID to each affected object's `contribution_ids`;
- do not create contribution events for typo fixes, formatting, generated indexes, or other non-semantic maintenance.

When answering questions about conflicts or history, retrieve contribution records as well as sources so you can say who contributed the current understanding and when.

Legacy objects without contribution metadata remain valid. Backfill only when reliable evidence supports the attribution.

## Canonicalization rules

- Prefer atomic claims for assertions likely to change, conflict, or need provenance.
- Keep broader explanations and reusable models in concepts and summaries.
- A fact is represented as a sufficiently supported claim, not as an immutable type.
- Repetition is not independent confirmation.
- Agent inference must remain labeled as synthesis/hypothesis unless evidence supports promotion.
- Do not silently erase earlier evidence. Use status, `supersedes`, `contradicts`, source links, and contribution history.
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