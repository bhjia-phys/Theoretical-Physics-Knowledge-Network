# Standalone Repo Init

This document describes how to turn `theoretical-physics-knowledge-network` into an independent public repository and keep it maintainable after the split.

## Target Role

The standalone repository should act as:

- a public, source-grounded theoretical-physics knowledge kernel;
- a human-readable mirror for selected domains;
- an external backend that is compatible with AITP `L2` retrieval contracts;
- a durable target for promoted knowledge, not a dump of runtime state.

## First Publish

From this directory:

```bash
git init
git add .
git commit -m "Initial public skeleton for theoretical-physics-knowledge-network"
git branch -M main
git remote add origin <your-public-repo-url>
git push -u origin main
```

## Required Repository Settings

After the first push, set:

- default branch: `main`;
- GitHub Actions enabled;
- branch protection on `main`;
- required status check: `protocol-build`;
- no direct pushes to `main` except by maintainers in emergencies.

Recommended merge policy:

- prefer squash merge for small protocol-sized changes;
- require the branch to be up to date before merge if concurrent curation becomes frequent.

## Directory Ownership

Canonical repository state lives only in:

- `sources/`
- `units/`
- `edges/`

Generated surfaces:

- `indexes/`
- `portal/`

Human-facing but non-canonical surface:

- `human-mirror/`

Support surfaces:

- `docs/`
- `schema/`
- `examples/`
- `.github/`

## Maintainer Bootstrap Checklist

Before accepting outside or AI-generated contributions:

1. read `README.md`;
2. read `docs/PROTOCOLS.md`;
3. read `docs/L2_RETRIEVAL_PROTOCOL.md`;
4. read `docs/L2_BRIDGE_PROTOCOL.md`;
5. confirm CI passes on `main`;
6. confirm generated `indexes/` and `portal/` are committed and in sync.

## Recommended Labels

If you use GitHub issues or pull requests, start with:

- `source-onboarding`
- `unit-promotion`
- `graph-refinement`
- `mirror-sync`
- `formalization`
- `docs`

These labels mirror the actual kinds of protocol-sized work in the repository.

## AI Contributor Gate

Any AI agent writing to this repository should be instructed to:

1. query `indexes/` before creating new units;
2. treat `sources/`, `units/`, and `edges/` as canonical;
3. follow `docs/L2_BRIDGE_PROTOCOL.md` when its upstream context is an AITP `L2` workflow;
4. update `human-mirror/` only as a bound mirror layer;
5. run `python3 scripts/kb.py check`;
6. run `python3 scripts/kb.py build`;
7. include the generated `indexes/` and `portal/` diff in the same change.

## Release Discipline

This repository should publish stable knowledge, not transient process state.

Do not commit:

- private vault exports;
- raw chat transcripts;
- AITP runtime snapshots;
- local machine paths;
- unanchored claims that have not yet been promoted into canonical objects.

If an upstream `L2` run cannot meet the canonical requirements yet, keep that material upstream and do not write it into this repo.
