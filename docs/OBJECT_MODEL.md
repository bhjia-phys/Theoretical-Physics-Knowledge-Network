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
- `notation`
- `assumption`
- `regime`
- `theorem`
- `proof_fragment`
- `derivation_step`
- `definition`
- `example`
- `caveat`
- `equivalence`
- `symbol_binding`

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
- `math_expressions`
- `model_refs`
- `equation_refs`
- `quantity_refs`
- `failure_modes`
- `formal_targets`
- `retrieval_hints`
- `symbols`

## Auto-Canonical Metadata (Optional)

For AITP auto-promotion and canonicalization workflows, units may also carry:

- `canonical_layer`
- `review_mode`
- `review_artifacts`
- `coverage`
- `consensus`
- `merge_lineage`
- `conflict_status`
- `conflict_refs`
- `equivalence_refs`

These fields are optional and backward-compatible with older unit files.
`review_artifacts` and `merge_lineage` are stored as flat string lists so the
backend stays easy to diff, grep, and re-index.

## Source Anchors

`source_anchors` connect reusable units back to public source structure.

Each anchor may specify:

- `source_id`
- `section`
- `equation_labels`
- `figure_ids`
- `notes`

This is the key bridge between human reading and machine retrieval.

## Derivation Granularity

Derivation-heavy knowledge should be modeled at the finest granularity that still remains reusable.

That means:

- if a proof or derivation has several nontrivial intermediate moves, prefer a chain of `derivation_step`, `proof_fragment`, `equivalence`, and `theorem` units over a single compressed summary object;
- each derivation-bearing unit should ideally expose the start formula, the nontrivial transformation or argument, and the resulting formula;
- when a source supplies a recognizable equation chain, `math_expressions` should preserve that chain rather than only the endpoint;
- if the source omits a step, record the omission honestly instead of inventing it.

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
