# Universal Agent Contract

This repository is a persistent context base for humans and agents. Treat it as shared organizational memory: useful and curated, but never unquestionable.

This contract is vendor-neutral. Follow it whether you are running in a coding agent, chat agent, enterprise platform, autonomous harness, local model, or a future runtime not anticipated here.

## Bootstrap protocol

When a user points you at this repository with little or no additional instruction:

1. Read `README.md` and this file.
2. Identify your actual capabilities: repository read/search/write, shell, Git operations, external-source access, and any runtime-specific tools.
3. Do not assume capabilities or permissions you do not have.
4. Explain the repository simply when needed: it is a shared knowledge library that turns sourced information into updateable context for humans and agents.
5. Start with `generated/CONTEXT_MAP.md` when available or targeted search; retrieve only the relevant canonical material under `knowledge/` rather than loading the whole corpus.
6. Read the relevant workflow under `skills/` before changing canonical knowledge or preparing an external-task handoff.

If you have read-only access, you may still answer from the library and propose exact changes. Never claim that files were changed, committed, pushed, inspected, or verified unless they actually were.

## Common user intents

- **"What does the context base say about X?"** Retrieve canonical material and answer with epistemic distinctions intact.
- **"Research/explain X."** Teach the user first; do not silently write findings while they are still learning.
- **A user drops a URL.** Read it if possible, explain what it contributes with citations, compare it with existing context, then recommend what is worth preserving.
- **"Push this into the knowledge base."** Follow `skills/capture.md` and the information-boundary gate.
- **"Sweep these sources."** Follow `skills/sweep.md`.
- **"What needs to be rechecked / keep this current."** Follow `skills/review-freshness.md`.
- **"Is this appropriate to store/share here?"** Follow `skills/check-information-boundary.md`.
- **"QA/clean up the knowledge base."** Follow `skills/maintain.md`.
- **"These two things conflict."** Follow `skills/conflicts.md`.
- **"Prepare context for another agent/task."** Follow `skills/prepare-task-context.md` and `docs/external-tasking.md`.
- **"Ingest what that agent found."** Follow `skills/ingest-task-results.md`.
- **"How should I retrieve/contextualize this corpus?"** Follow `docs/retrieval-architecture.md`.
- **"Help me work through this product change using SDD/OpenSpec."** Follow `skills/sdd-pm-companion.md` and `docs/sdd/pm-workflow.md`.
- **"Is this one spec/change or should we split it?"** Follow `skills/review-change-scope.md`.
- **"Prepare PM acceptance for staging."** Follow `skills/prepare-pm-acceptance.md` and `docs/sdd/verification-and-acceptance.md`.
- **"How do I contribute/use/move this?"** Use `README.md`, `CONTRIBUTING.md`, `docs/agent-interop.md`, and `docs/portability.md`.

## Manual learning contract: teach before curating

When a human is actively researching with you, optimize for their learning before optimizing for repository growth.

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

### Investigate

Retrieve relevant existing context and examine the new sources. Separate direct source content from synthesis or inference.

### Teach

Explain the important findings, why they matter, and how they connect. Surface uncertainty, contradictions, and changes to prior understanding. Keep citations visible for externally derived claims whenever the runtime supports citations or links.

### Curate with the user

Recommend a small set of durable additions/updates and distinguish **recommend preserving**, **optional**, and **do not preserve**. Ask for one lightweight decision. Do not ask the user to choose filenames, object types, metadata, or folder locations.

Accept shorthand such as **"push recommended," "all," "A and C,"** or **"none."** If the user has already reviewed a specific item and says **"push this"**, that can satisfy the curation step.

### Commit after approval

Canonicalize only the approved set unless automatic capture was explicitly authorized in advance. A curation approval is not a sensitivity/destination approval: run `skills/check-information-boundary.md` when the material is non-public or potentially sensitive.

Scheduled/unattended sweeps may apply low-risk changes under `skills/sweep.md`, but automation may not self-approve `HUMAN_CONFIRM` information-boundary cases.

Low administration means agents own clerical work; humans stay involved in meaning and relevance.

## Retrieval contract

This repository uses progressive disclosure rather than full-corpus loading.

```text
context map → orientation objects → specific claims/questions/decisions → evidence/provenance
```

Canonical folders stay partitioned by epistemic type. Query/use-case-specific views are generated and disposable.

When available, use `generated/CONTEXT_MAP.md` to choose a retrieval path. Expand to `generated/INDEX.md` or repository search only as needed. See `docs/retrieval-architecture.md`.

For SDD work, also use `generated/SDD_CONTEXT_MAP.md` when available. It is a workflow-oriented routing view, not a separate source of truth. Do not classify the whole corpus by OpenSpec stage; retrieve dynamically for the decision being made. See `docs/sdd/context-routing.md`.

## Spec-driven-development contract

This repository supports SDD but does not replace the target project's planning/execution workflow.

When the target project uses OpenSpec:

1. use this repository to retrieve relevant product/domain/client/decision context;
2. preserve the authority distinction in `docs/ontology.md` — descriptive evidence is not automatically a requirement;
3. before proposal, use `skills/review-change-scope.md` when scope is uncertain or broad;
4. let the installed OpenSpec workflow control schema selection, artifact instructions/dependencies, blocked/ready state, apply, verify, sync, and archive semantics;
5. do not hand-create a parallel proposal/spec/design/tasks lifecycle in this repository;
6. do not treat generated OpenSpec artifacts as PM-approved merely because they exist;
7. do not silently narrow specified behavior during implementation; route consequential changes back to the appropriate planning artifact;
8. distinguish OpenSpec implementation verification from environment validity and PM product acceptance;
9. use `skills/prepare-pm-acceptance.md` for staging acceptance when product review is required;
10. after the change, preserve only durable learning in canonical context rather than copying implementation-local detail.

A useful operating loop is:

```text
context -> explore -> scope review -> OpenSpec propose/artifact review
-> apply -> verify -> environment validity -> PM acceptance -> archive/learn
```

This is an operating model around OpenSpec, not a redefinition of OpenSpec. If the installed OpenSpec version or target repository's explicit workflow conflicts with guidance here, preserve the controlling OpenSpec/user/runtime behavior and surface the conflict.

## Freshness contract

Current-state knowledge may carry `last_reviewed`, `volatility`, and `review_after` metadata.

- `review_after` is a review target, not a schedule.
- the external runner decides when to execute work;
- a recent edit is not proof of freshness;
- do not advance `last_reviewed` without genuine verification;
- use `skills/review-freshness.md` and `generated/FRESHNESS_QUEUE.md` when available.

## Information-boundary contract

Runtime permissions are authoritative, but repository writes and handoffs have an additional destination check.

Before persisting or exporting non-public, authenticated, restricted, personal, regulated, or potentially highly confidential material, follow `skills/check-information-boundary.md`.

If the result is `HUMAN_CONFIRM`, do not store the candidate in canonical knowledge, `intake/`, or an external task packet until a human explicitly confirms that the destination and intended audience are appropriate. Human confirmation cannot override an environment, policy, contractual, or legal restriction.

Never store credentials/secrets in durable team context.

## External task handoff

This repository is a **context source and return destination**, not the execution environment for external tasks.

When work will execute in another runtime:

1. follow `skills/prepare-task-context.md`;
2. create a derived task context packet with only relevant canonical context, verification targets, known conflicts/freshness, and the expected return shape;
3. run the information-boundary check before widening access to potentially sensitive context;
4. do **not** prescribe or store credentials, connector configuration, browser implementation, network policy, sandbox policy, model choice, approval rules, or scheduler state;
5. let the external runtime inherit and enforce its own identity, permissions, tools, sandbox, compliance controls, and human approvals;
6. expect findings back in a capability-neutral run report/evidence bundle;
7. follow `skills/ingest-task-results.md` before changing canonical knowledge.

The task context packet is not canonical knowledge and does not grant permissions. If the external runtime lacks a needed capability, it should report that limitation rather than bypass it.

A future durable runner may automate this handoff, but the runner must adapt to this semantic contract rather than becoming the source of truth for the context base.

## Citation behavior

For externally researched material:

- cite material claims close to the claim they support when the runtime permits;
- prefer primary sources when available and appropriate;
- consider source authority and scope rather than treating publication as truth;
- never manufacture URLs, source names, dates, authors, or citation details;
- when comparing research to the repository, name relevant canonical objects/files rather than pretending the repository is an external source.

## Before answering from the knowledge base

1. Use the compact retrieval map or targeted search before the full index.
2. Prefer specific sources, observations, and claims over broad summaries when evidence matters.
3. Preserve epistemic distinctions: hypothesis, observation, synthesis, and established claim are not interchangeable.
4. When freshness matters, inspect source dates, `last_reviewed`, `review_after`, status, supersession, and contribution lineage.
5. Surface credible conflicts rather than averaging them away.
6. Do not treat repeated copies of one upstream assertion as independent evidence.

## Write protocol

Before changing canonical knowledge:

1. retrieve existing objects about the same subject and aliases;
2. classify new material using `docs/ontology.md`;
3. update before creating;
4. check the information boundary for non-public/potentially sensitive content;
5. preserve source provenance without manufacturing metadata;
6. classify the relationship as confirm, refine, supersede, contradict, reframe, or orthogonal;
7. preserve meaningful history;
8. set/update freshness metadata for current-state knowledge when useful;
9. for every material semantic write, create one contribution event under `knowledge/contributions/` and link affected objects through `contribution_ids`;
10. preserve human handling confirmation in the contribution when the boundary gate required it;
11. validate and rebuild generated views when the environment permits;
12. report briefly what changed and surface only unresolved consequential issues.

Raw input may be messy. Canonical knowledge should be concise, scoped, retrievable, and appropriate for its destination.

## Contribution provenance

Source provenance and contribution provenance are different. See `docs/provenance.md`.

A source answers **where the information came from**. A contribution answers **who decided to add/change it in shared context, when, and through which agent/tool**.

For a material write:

- identify the contributor from authenticated/session context when available;
- if a human contributor is unknown and attribution matters, ask once rather than guessing;
- use a stable actor label such as `person:...`, `team:...`, or `automation:...`;
- record the executing repository writer separately, such as `agent:chatgpt` or `agent:claude-code`;
- include materially changed objects in the contribution's `object_ids` and backlink via `contribution_ids`;
- do not create contribution events for formatting, typos, generated indexes, or other non-semantic maintenance.

For external investigations, the investigating runtime belongs in the run/source provenance. The agent that actually canonicalizes the result belongs in contribution provenance unless they are the same system.

Legacy objects without contribution metadata remain valid. Backfill only when reliable evidence supports attribution.

## Canonicalization rules

- Prefer atomic claims for assertions likely to change, conflict, or need provenance.
- Keep broader explanations and reusable models in concepts and summaries.
- A fact is a sufficiently supported claim, not an immutable type.
- Repetition is not independent confirmation.
- Agent inference remains synthesis/hypothesis unless evidence supports promotion.
- Do not silently erase earlier evidence; use status, `supersedes`, `contradicts`, sources, and contribution history.
- Clear temporal updates can usually be applied automatically; consequential semantic reversals require review.

## Capability-specific behavior

**Local clone + shell:** edit repository-relative paths, run `python scripts/doctor.py` and `python scripts/build_indexes.py` when appropriate, and use normal Git hygiene.

**Git hosting/API write access but no shell:** make the same semantic file changes through the repository API. Perform documented checks semantically and say when executable validation was not run.

**Read-only repository access:** answer, prepare context packets, or propose a patch. Do not claim to have written anything.

**Agent platform with its own memory/search:** that memory is a cache/retrieval aid, not canonical truth. Durable team knowledge belongs here only through the repository lifecycle.

**External task runtime:** inherit the runtime's own controls. Do not treat repository instructions as authorization to use tools, systems, or data the runtime has not granted.

See `docs/agent-interop.md` for adapter guidance.

## Git and collaboration safety

- Respect the host repository's branch/review policy.
- If write policy is unknown in a shared repository, prefer a branch/pull request when possible.
- Do not force-push, rewrite history, delete unique provenance, or change remotes without explicit instruction.
- Keep commits semantically understandable.
- Never commit secrets, credentials, tokens, private connector identifiers, or machine-specific absolute paths.
- Do not make canonical behavior depend on uncommitted local files.

## Portability rules

Canonical knowledge must survive a plain Git clone or mirror:

- use stable repository-relative paths and stable object IDs;
- avoid symlinks and machine-specific paths;
- do not require a specific agent vendor, hosted database, or proprietary memory layer;
- treat generated files and task context packets as rebuildable;
- keep platform-specific adapters and runtime controls outside canonical knowledge.

## Maintenance behavior

Follow `skills/maintain.md` periodically or after large sweeps. Automatically repair low-semantic-risk problems. Human review is reserved for semantic merges, consequential contradictions, unclear source authority, destructive changes, and sensitive destination decisions that cannot safely be inferred.

## Public repository safety

This repository is currently public. Only clearly public information may be added here. If material is non-public, confidential, proprietary, personal, or otherwise restricted, do not write it here; use the approved private/internal copy instead. Human confirmation does not override this public boundary.
