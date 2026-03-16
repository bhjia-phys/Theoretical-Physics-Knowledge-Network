# Contributing

## Ground Rules

- Follow `docs/PROTOCOLS.md`.
- If the work comes from an AITP `L2` flow, also follow `docs/L2_BRIDGE_PROTOCOL.md`.
- Edit canonical objects in `units/`, `edges/`, and `sources/`.
- Treat `human-mirror/` as a human-facing mirror, never as the canonical backend.
- Regenerate `indexes/` and `portal/` after canonical changes.
- Keep ids stable once published.
- Prefer one reusable unit per file.
- Do not copy large prose blocks from private notes or copyrighted sources.
- Do not add new Python automation unless a written protocol cannot be enforced or projected without it.

## Unit Authoring

Each unit should:

- have a typed id like `concept:berry-curvature`;
- state scope and assumptions explicitly;
- list dependencies and nearby related units;
- include at least one `source_anchor`;
- record `formalization_status` even if formalization has not started.

## Human Mirror Authoring

If you add or update a note in `human-mirror/`:

- decide first whether it is an object mirror or a structural control note;
- object mirrors should include `kb_unit_id` or `kb_source_map_id`;
- structural control notes may use `kb_surface` such as `human_index` or `human_control`;
- add human-oriented explanation only after the typed backbone is preserved;
- do not place migration audits, private vault archaeology, or unreviewed run notes into the public mirror.
- keep mirror filenames English and ASCII.
- use stable vault-root wiki-links under `human-mirror/`.

## Edge Authoring

Use the finite edge taxonomy in `schema/edge.schema.json`.

If two units are related only loosely, prefer a concise `summary` over inventing a new relation type.

## Generated Files

The following are generated and may be overwritten:

- `indexes/*.jsonl`
- `indexes/*.json`
- `portal/**/*.md`

## Minimal Script Policy

The repository keeps only the Python needed for:

- `scripts/kb.py`: protocol enforcement plus deterministic projection building.

## Review Standard

The review bar is:

- source-grounded;
- retrieval-friendly;
- concise enough to reuse during reasoning;
- explicit about failure modes and regime limits.

## AI-Originated Contributions

If an AI agent is promoting knowledge from an upstream `L2` workflow:

- treat the change as a `source-onboarding`, `unit-promotion`, `graph-refinement`, or `mirror-sync` packet;
- search existing typed objects before creating new ones;
- keep raw runtime state upstream rather than committing it here;
- include a PR summary that lists touched source ids, typed ids, edge ids, and mirror notes.

## Local Check

Run the repository checks before opening a pull request:

```bash
python3 scripts/kb.py check
python3 scripts/kb.py build
```
