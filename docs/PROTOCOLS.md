# Protocols

This file is the normative contract for `theoretical-physics-knowledge-network`.

See also:

- `docs/L2_RETRIEVAL_PROTOCOL.md`
- `docs/PAPER_INGESTION_QUALITY_PROTOCOL.md`
- `docs/TOPIC_REGRESSION_SUITE_PROTOCOL.md`

## P0. Repository Role

The repository is a standalone theoretical-physics knowledge kernel.

It must remain:

- independent from Obsidian as the source of truth;
- independent from AITP runtime orchestration;
- compatible with typed `L2` retrieval;
- readable to humans through generated portal projections.

## P1. Canonical Storage Protocol

Only the following paths are canonical:

- `sources/`
- `units/`
- `edges/`

The following are not canonical:

- `indexes/`
- `portal/`
- `human-mirror/`

Generated projections must never be hand-edited as the authoritative source.

`human-mirror/` may be hand-edited for human readability, but it must never supersede the canonical backend.

## P2. Unit Protocol

Every reusable knowledge object must:

- live in exactly one JSON file under the matching `units/<family>/` directory;
- carry a stable typed id such as `concept:weyl-node`;
- expose explicit scope, regime, assumptions, dependencies, and source anchors;
- expose explicit mathematical content whenever the source contains it;
- record formalization and validation status;
- stay small enough to serve retrieval rather than only archival storage.

Mathematical-content rule:

- a formal unit must not hide its key equation, operator relation, invariant formula, boundary condition, or classification formula only inside `summary`;
- when the source presents a concrete displayed equation or a canonical compact formula, store it in structured `math_expressions`;
- when the source introduces symbols that are reused downstream, store them in `symbols`;
- `representation` is an interpretive prose gloss, not a substitute for the equation itself;
- if a unit is genuinely structural and the source does not give it a standalone formula, the unit must still expose formalization links to nearby equations, quantities, models, derivations, or theorems instead of remaining pure prose.

Derivation-detail rule:

- theorem-like, proof-like, equivalence-like, and derivation-like units must preserve as much of the source derivation spine as the source actually gives;
- do not compress a multi-step source argument into a one-sentence summary when the source provides intermediate equations, auxiliary constructions, limiting arguments, or change-of-variable steps;
- whenever a nontrivial conclusion depends on an intermediate formula, that intermediate formula should appear explicitly in `math_expressions` or in an adjacent typed `derivation_step` / `proof_fragment` unit;
- a detailed derivation should make visible: the starting statement, each nontrivial intermediate step, the identity or assumption used at that step, and the final conclusion;
- if one typed unit would become too wide for retrieval, split the derivation into chained neighboring units rather than collapsing the steps into prose;
- if the source itself skips steps, mark that honestly in prose or scope notes; do not fabricate unsupported intermediate formulas.

## P3. Source Anchor Protocol

Every promoted unit must anchor to at least one public source location.

Anchors must resolve to:

- a known `source_id`;
- a known section id in that source manifest;
- known equation labels or figure ids when such labels are claimed.

If a source claim cannot be anchored, it is not yet canonical.

## P4. Edge Protocol

All graph relations must live in `edges/edges.jsonl`.

Relations must use the finite vocabulary already declared by the repository.

If a relation feels missing, first test whether the knowledge should instead be encoded in:

- the unit summary;
- a warning unit;
- a bridge unit;
- a derivation unit.

Do not expand relation types casually.

## P5. Projection Protocol

`indexes/` and `portal/` are deterministic projections from the canonical store.

Required generated surfaces are:

- `indexes/unit_index.jsonl`
- `indexes/edge_index.jsonl`
- `indexes/source_anchor_index.jsonl`
- `indexes/symbol_index.jsonl`
- `indexes/formalization_index.jsonl`
- `indexes/domain_index.json`
- `portal/Topological-Phases-Of-Matter/**`

## P6. Change Protocol

For any canonical change:

1. edit canonical files only;
2. run `python3 scripts/kb.py check`;
3. run `python3 scripts/kb.py build`;
4. inspect the generated portal and indexes as projections, not as the source of truth.

## P7. Script Minimality Protocol

Python is allowed here only for two repository-local duties:

- enforcing written protocols;
- building deterministic projections.

The minimal script surface is:

- `scripts/kb.py`

Any additional Python script needs a strong reason tied to one of the two duties above.

## P8. L2 Bridge Protocol

If knowledge arrives from an AITP `L2` workflow, it must enter this repository through a promotion bridge rather than a runtime dump.

That means:

- `L2` queries repository indexes first;
- `L2` decides update-vs-create explicitly for typed objects;
- only promoted, source-grounded units enter `sources/`, `units/`, and `edges/`;
- runtime notes stay upstream unless and until they are canonicalized;
- `human-mirror/` stays secondary to typed objects.

The operational contract for this bridge lives in `docs/L2_BRIDGE_PROTOCOL.md`.

## P9. Topic Regression Protocol

If a branch is being treated as a reusable topic rather than a one-off paper parse, it should maintain:

- a stable regression suite with question ids;
- regression pass logs with `pass` / `partial` / `fail` outcomes;
- explicit writeback from partial/fail results into queues, local note expansion, or `L0` follow-up.

The operational contract lives in `docs/TOPIC_REGRESSION_SUITE_PROTOCOL.md`.
