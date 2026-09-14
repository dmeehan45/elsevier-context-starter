# Portability: Clone, Mirror, and Move

The repository is designed to remain useful when copied between Git hosts or worked on entirely from a local machine.

## What is portable

The canonical system is the committed repository itself: Markdown, stable IDs, relative paths, small runner-agnostic examples, and standard-library Python helpers. It does not require a hosted database, a specific Git provider, a specific agent runtime, or a durable runner.

Avoid making canonical knowledge depend on:

- absolute paths from one computer;
- symlinks;
- uncommitted local files;
- credentials or connector secrets;
- one vendor's hidden memory;
- one runtime's permission model;
- generated indexes or task packets that cannot be rebuilt.

## Runtime portability is a boundary, not a configuration

The repository should travel between execution environments without carrying their security configuration with it.

When a runtime uses the context base, it inherits that runtime's own:

- identity/authentication;
- tool and connector grants;
- browser/shell/network/filesystem permissions;
- sandbox rules;
- human approval requirements;
- model/orchestration controls;
- compliance and audit policy;
- scheduler/checkpoint state.

Do not commit those controls here merely to make another environment behave the same way. The portable contract is semantic: relevant context can be handed out, evidence/results can be handed back, and canonical knowledge follows the same lifecycle afterward.

See `docs/external-tasking.md`.

## Normal local clone

A standard clone should be enough:

```bash
git clone <repository-url>
cd <repository-directory>
python scripts/doctor.py
```

The helper scripts locate the repository relative to their own files, so the clone can live in any local directory.

## Copying to a new private/internal repository

For the common case where this public starter becomes the basis of an internal context base:

```bash
git clone <public-repository-url> internal-context-base
cd internal-context-base
git remote rename origin public-upstream
git remote add origin <approved-internal-repository-url>
git push -u origin main
```

Before adding non-public material, verify that `origin` is the approved private/internal destination. If there is any risk that tooling might push internal branches to the public remote, remove `public-upstream` after the initial transfer. Public framework updates can always be reviewed and copied deliberately later.

The important boundary is directional: **public material may be promoted into the internal copy; internal material must never be synchronized back into the public repository.**

## Full mirror

A Git mirror preserves branches, tags, and history. Use it only when the destination is intended to receive the entire source repository and you understand that `--mirror` updates/deletes destination refs to match the source.

```bash
git clone --mirror <source-url>
cd <repository>.git
git push --mirror <destination-url>
```

Do not automate a reverse mirror from an internal/private repository to this public starter.

## Working across several machines

Use ordinary Git pull/branch/merge practices. Canonical object IDs should remain stable even if filenames move. Resolve semantic conflicts by following `skills/conflicts.md`; do not resolve a Git merge conflict by casually deleting one side's evidence.

## Moving between agent runtimes

No runtime-specific task state is required to understand the knowledge base.

A new runtime should be able to:

1. read `AGENTS.md`;
2. retrieve canonical context;
3. prepare a capability-neutral task context packet if work will execute elsewhere;
4. return or ingest a capability-neutral run report/evidence bundle;
5. apply the normal knowledge lifecycle.

Vendor-specific traces, checkpoints, sandbox state, connector IDs, and credentials may stay behind in the runtime that owns them.

## Moving away from GitHub

Nothing in the knowledge model requires GitHub. GitLab, Azure DevOps, Bitbucket, enterprise Git, or a local-only repository can host the same structure. Host-specific pull-request and automation features are conveniences, not canonical dependencies.

## Before and after a move

When Python is available, run:

```bash
python scripts/doctor.py
```

Run it in the source working copy before migration and again in the destination. Confirm that `knowledge/`, `intake/`, `skills/`, `templates/`, `docs/`, and `AGENTS.md` are present and that your agent can read the repository from the new environment.
