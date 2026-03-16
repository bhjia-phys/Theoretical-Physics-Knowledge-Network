# L2 Bridge Protocol

This document defines how AITP `L2` work should be written into `open-physics-kb`.

`L2` is allowed to use this repository as an external knowledge kernel, but it must write into it through the repository protocol rather than by dumping runtime notes.

## Ownership Boundary

Treat the layers as:

- public sources: the ultimate evidence surface;
- `open-physics-kb` canonical store: the durable promoted knowledge surface;
- generated `indexes/` and `portal/`: deterministic projections;
- `human-mirror/`: explanatory mirror for people;
- AITP `L2` runtime state: upstream working memory, not repository truth.

The repository is not an archive of `L2` sessions.

## Read Before Write

Before any `L2`-driven write, the agent must read:

- `docs/PROTOCOLS.md`
- `docs/L2_RETRIEVAL_PROTOCOL.md`
- `docs/OBJECT_MODEL.md`
- this file

If the change also touches `human-mirror/`, the agent should read:

- `human-mirror/Mirror Contract.md`

## Allowed Write Modes

There are only four normal `L2` -> repo write modes:

1. `source-onboarding`
2. `unit-promotion`
3. `graph-refinement`
4. `mirror-sync`

### `source-onboarding`

Use when `L2` introduces a new public paper, lecture, book chapter, or other public source.

Required writes:

- `sources/<source-slug>/manifest.json`
- at least one `source_map` unit under `units/source-maps/`

Optional writes:

- promoted units already grounded in that source;
- human mirror source-map note.

### `unit-promotion`

Use when `L2` has isolated a reusable object that is mature enough to become canonical.

Required writes:

- one or more files under `units/<family>/`
- any necessary edge updates in `edges/edges.jsonl`

Optional writes:

- bound mirror notes in `human-mirror/`

### `graph-refinement`

Use when the main change is better relations between existing units.

Required writes:

- `edges/edges.jsonl`

Optional writes:

- unit dependency updates if the relation changes canonical prerequisites;
- mirror note updates if the human navigation should reflect the graph change.

### `mirror-sync`

Use when the canonical objects already exist and the human-facing explanation needs to catch up.

Allowed writes:

- `human-mirror/` only

Constraint:

- every object-like mirror note must preserve one-to-one binding through `kb_unit_id` or `kb_source_map_id`.

## Canonicalization Procedure

Before creating a new canonical unit, the agent must:

1. query `indexes/unit_index.jsonl`;
2. inspect likely collisions by `title`, `aliases`, `tags`, and nearby `domain`;
3. inspect `indexes/source_anchor_index.jsonl` for the relevant source sections;
4. inspect `edges/edges.jsonl` around the nearest existing objects;
5. decide explicitly whether the operation is `update-existing` or `create-new`.

If an equivalent typed object already exists, update it. Do not create a parallel duplicate.

If only a human note exists without `kb_unit_id` or `kb_source_map_id`, treat it as a hint, not as canonical truth.

## Canonical Write Rules

Every `L2`-originated canonical write must satisfy all of the following:

- every promoted unit is in exactly one JSON file;
- every promoted unit has at least one valid `source_anchor`;
- every dependency or related-unit reference resolves to an existing typed id;
- every edge uses the repository's finite relation vocabulary;
- every unit states `formalization_status`, `validation_status`, and `maturity`;
- every summary is compact enough for retrieval, not a long note dump.

What `L2` must never write directly into canonical storage:

- raw chain-of-thought or session logs;
- private notes;
- unsupported paraphrase with no public anchor;
- generated portal markdown as if it were canonical;
- ad hoc new Python tooling for one-off ingestion.

## Human Mirror Rules For L2

If `L2` updates `human-mirror/`, it must follow these rules:

- mirror notes are English-only;
- filenames should be English ASCII;
- object-like mirrors must include `kb_unit_id` or `kb_source_map_id`;
- structural notes may use `kb_surface`;
- wiki-links should use stable vault-root paths under `human-mirror/`;
- the mirror may add intuition and navigation, but must not replace source-grounded ids, assumptions, regime, or dependency structure.

## Commit Packet Contract

Each `L2`-driven pull request should be understandable as a promotion packet.

The PR description should state:

- write mode;
- public source ids touched;
- units created;
- units updated;
- edges added or changed;
- mirror notes added or changed;
- unresolved items intentionally left upstream in `L2`.

## Acceptance Gate

Before merge, the agent must run:

```bash
python3 scripts/kb.py check
python3 scripts/kb.py build
```

And confirm:

- protocol check passes;
- generated `indexes/` and `portal/` are committed;
- no private or runtime-only material entered the repo.

## Rejection Conditions

Reject the change if any of the following is true:

- the contribution is mainly a runtime memo instead of promoted knowledge;
- the source anchors do not resolve;
- the change creates a duplicate typed object;
- the mirror note pretends to be canonical without typed binding;
- generated outputs were hand-edited instead of rebuilt;
- the patch introduces extra Python automation unrelated to repository-local checking or deterministic build.
