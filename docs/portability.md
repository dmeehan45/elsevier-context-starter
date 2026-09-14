# Portability: Clone, Mirror, and Move

The repository is designed to remain useful when copied between Git hosts or worked on entirely from a local machine.

## What is portable

The canonical system is the committed repository itself: Markdown, stable IDs, relative paths, small JSON configuration examples, and standard-library Python helpers. It does not require a hosted database, a specific Git provider, or a specific agent runtime.

Avoid making canonical knowledge depend on:

- absolute paths from one computer;
- symlinks;
- uncommitted local files;
- credentials or connector secrets;
- one vendor's hidden memory;
- generated indexes that cannot be rebuilt.

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

## Moving away from GitHub

Nothing in the knowledge model requires GitHub. A GitLab, Azure DevOps, Bitbucket, enterprise Git server, or local-only repository can host the same structure. Host-specific pull-request and automation features are conveniences, not canonical dependencies.

## Before and after a move

When Python is available, run:

```bash
python scripts/doctor.py
```

Run it in the source working copy before migration and again in the destination. Then confirm that `knowledge/`, `intake/`, `skills/`, `templates/`, `docs/`, and `AGENTS.md` are present and that your agent can read the repository from the new environment.