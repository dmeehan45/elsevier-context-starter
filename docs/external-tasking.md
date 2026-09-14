# External Task Handoff

This repository is a persistent context source. It is **not** an execution environment, permission system, sandbox, scheduler, or durable agent runner.

The purpose of this contract is to let an agent prepare useful context for work that will execute somewhere else, and then safely ingest the evidence and findings that come back.

## Boundary

The repository owns:

- canonical knowledge and provenance;
- retrieval of relevant context;
- freshness/conflict information;
- reusable knowledge workflows under `skills/`;
- a portable context packet for an external task;
- a portable return contract for findings/evidence;
- canonicalization of approved or policy-safe results.

The external runtime owns:

- authentication and identity;
- credentials and secrets;
- tool availability and connectors;
- browser/shell/network/filesystem access;
- sandboxing and isolation;
- model selection and orchestration;
- approvals and human-in-the-loop controls;
- scheduling, retries, checkpoints, and resumability;
- compliance enforcement and audit controls outside this repository.

The repository must not weaken, override, or attempt to reproduce those runtime controls.

## Core flow

```text
user / scheduler / external system
             │
             ▼
      task intent or objective
             │
             ▼
   prepare-task-context skill
             │
             ▼
      TASK CONTEXT PACKET
     (derived, not canonical)
             │
             ▼
      EXTERNAL RUNTIME
  inherits its own permissions,
  tools, sandbox, and approvals
             │
             ▼
          RUN REPORT
   findings + evidence + limits
             │
             ▼
    ingest-task-results skill
             │
             ▼
  canonical context + provenance
```

This boundary should remain valid if the runtime later becomes Claude Code, an OpenAI agent, Microsoft Agent Framework, an internal enterprise runner, a local autonomous harness, or something not yet chosen.

## Task context packet

A task context packet is a **derived view** of the repository prepared for one external task. It is not canonical knowledge and should not become a second memory store.

A good packet contains only what the external worker needs to understand the task and the current context:

- objective;
- questions or verification targets;
- relevant canonical object IDs and concise current state;
- known conflicts or uncertainty;
- freshness concerns;
- source/evidence references that matter;
- expected evidence/result shape;
- return instructions.

A packet should not contain credentials, connector configuration, allowed domains, browser policies, network rules, model settings, or assumed tool names. The external runtime decides whether and how it can execute the work within its own controls.

If the task requires a capability that is not present, the runtime should report the gap rather than reinterpret the packet as permission to obtain or bypass that capability.

## Run report

The return artifact from an external task should separate four things:

1. **Observed** — what the worker directly saw, measured, read, or verified.
2. **Inferred** — conclusions drawn from those observations.
3. **Unresolved** — what could not be verified, accessed, or reconciled.
4. **Proposed context changes** — candidate confirmations, refinements, supersessions, contradictions, new claims, questions, or source records.

The report should also preserve execution provenance when available:

- run identifier;
- runtime/agent identity;
- execution time/window;
- evidence references;
- sources/systems actually inspected;
- material access or capability limitations.

Do not require the repository to understand vendor-specific trace formats. A runner may retain richer traces/checkpoints elsewhere; the return report should expose only the durable information needed for knowledge interpretation and provenance.

## Evidence rule

An autonomous result is not authoritative merely because an agent produced it.

When results come back:

- preserve direct evidence where permitted;
- distinguish the investigated system/source from the agent's interpretation;
- treat unsupported agent synthesis as synthesis/hypothesis, not established fact;
- compare findings to existing scope, time, and contribution lineage;
- use `skills/conflicts.md` when the new result does not cleanly agree with canonical knowledge.

## Writeback rule

External workers should not need direct write access to canonical knowledge.

The preferred portable pattern is:

1. external runtime receives a context packet;
2. external runtime performs work under its own controls;
3. external runtime returns a run report/evidence bundle;
4. a repository-aware agent follows `skills/ingest-task-results.md`;
5. normal source, conflict, contribution, and validation rules apply.

A trusted future runner may combine steps 3–5, but it must preserve the same semantic boundary. Execution authority does not automatically imply authority to reverse canonical knowledge.

## Reusable task skills

Task-specific procedural knowledge may live under `skills/` when it is genuinely portable across runtimes. Examples could eventually include:

- user-flow investigation;
- product-surface audit;
- knowledge freshness verification;
- source verification;
- context-base pruning;
- competitive scan.

A task skill should describe **how to reason about and report the work**, not how to configure a particular browser, connector, identity, sandbox, or enterprise permission set.

If a procedure only works because of one runtime's proprietary capability, keep that adapter/configuration in that runtime rather than making it part of the canonical repository contract.

## Path A now, durable runner later

For now, this repository supports the protocol manually or through whatever capable agent is available:

- prepare context;
- hand it to an external runtime;
- receive evidence/results;
- ingest results through the existing knowledge lifecycle.

A future durable runner can automate those transitions without changing the knowledge model. The runner should adapt to this contract, not become the source of truth for the context base.
