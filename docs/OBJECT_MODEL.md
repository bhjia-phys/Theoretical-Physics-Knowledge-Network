# Object Model

## Source Of Truth

The kernel has three canonical surfaces:

- `sources/`: public source manifests;
- `units/`: reusable typed knowledge objects;
- `edges/`: typed relations between units.

Everything else is a projection.

The operational rules that constrain these surfaces live in `docs/PROTOCOLS.md`.

## Unit Families

Current unit families:

- `concept`
- `equation`
- `quantity`
- `claim`
- `derivation`
- `method`
- `model`
- `warning`
- `bridge`
- `source_map`

Each unit carries both human-readable fields and retrieval-facing fields.

## Required Common Fields

- `id`
- `type`
- `title`
- `summary`
- `domain`
- `tags`
- `aliases`
- `assumptions`
- `regime`
- `scope`
- `dependencies`
- `related_units`
- `source_anchors`
- `formalization_status`
- `validation_status`
- `maturity`
- `created_at`
- `updated_at`

## Physics-Specific Fields

Units may also carry:

- `symmetries`
- `representation`
- `model_refs`
- `equation_refs`
- `quantity_refs`
- `failure_modes`
- `formal_targets`
- `retrieval_hints`
- `symbols`

## Source Anchors

`source_anchors` connect reusable units back to public source structure.

Each anchor may specify:

- `source_id`
- `section`
- `equation_labels`
- `figure_ids`
- `notes`

This is the key bridge between human reading and machine retrieval.

## Edge Layer

Edges are stored separately from units so the graph can be rebuilt, audited, or re-indexed without rewriting unit files.

Current relation vocabulary:

- `depends_on`
- `defines`
- `uses`
- `explains`
- `motivates`
- `specializes`
- `generalizes`
- `contrasts_with`
- `derived_from`
- `supports`
- `warned_by`
- `bridges_to`
- `formalizes_toward`
- `anchored_in_source`

## Projection Surfaces

- `indexes/` are deterministic retrieval surfaces for agents and scripts.
- `portal/` is a zettelkasten-like human projection with dense links and summaries.

The portal is intentionally secondary to the typed object store.
