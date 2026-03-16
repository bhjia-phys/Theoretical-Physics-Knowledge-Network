# Publishing

This directory is designed to be split into a standalone public repository.

## Recommended Name

- `theoretical-physics-knowledge-network`

## Suggested First Publish Flow

```bash
cd /path/to/theoretical-physics-knowledge-network
git init
git add .
git commit -m "Initial public skeleton for theoretical-physics-knowledge-network"
```

Then create a public remote on your hosting platform and push:

```bash
git branch -M main
git remote add origin <your-public-repo-url>
git push -u origin main
```

## Before Publishing

- read `README.md`;
- read `docs/PROTOCOLS.md`;
- read `docs/L2_RETRIEVAL_PROTOCOL.md`;
- read `docs/L2_BRIDGE_PROTOCOL.md`;
- read `docs/STANDALONE_REPO_INIT.md`;
- confirm the current example scope is acceptable for public release;
- confirm no private notes or local-only paths remain in `human-mirror/`.

## Scope Rule

This public repository should include:

- canonical typed backend objects;
- generated retrieval indexes and portal projections;
- curated public example mirror notes;
- protocol and schema docs.

This public repository should not include:

- private vault exports;
- migration archaeology from local working notes;
- unreviewed research logs;
- personal task management notes;
- machine-specific paths or credentials.
