# Hall-Response / Chern-Number Equivalence Family

- ID: `theorem_family:hall-response-chern-number-equivalence`
- Type: `theorem_family`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Canonical theorem family for the integer Hall response: it groups the response-theory, the traced-curvature-to-projector TKNN bridge, the many-body formulation, and the now-explicit graphene/Haldane lattice bridge while keeping the remaining original-paper archival enrichment explicit.

## Scope
Family-level grouping for the Lecture Two flagship theorem and its neighbors.

## Regime
Cross-source reusable theorem family.

## Assumptions
- `The same gapped integer Hall phase is being described from response, band, and many-body viewpoints.`

## Representation
Family object for the Hall-response / Chern-number theorem branch.

## Source Anchors
- `lecture-two/proof-of-the-equivalence | Witten's local family spine.`
- `paper/projector-curvature-identity | eqs: occupied-bundle-curvature-form | Original microscopic source for the occupied-bundle curvature density used in the local TKNN bridge.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | Condensed-matter realization and reinterpretation of the same family through the valley-mass Chern-number criterion.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Notation Family](../Notation-Families/hall-response-chern-number-notation.md)

## Related Units
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Lecture Two TKNN / Haldane Archival Enrichment Remains To Be Curated](../Open-Gaps/lecture-two-tknn-equivalence-proof-not-yet-curated.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)

## Supporting Obligations
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](../Proof-Obligations/filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](../Proof-Obligations/twist-angle-berry-curvature-equals-hall-level.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

## Family Members
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)

## Topic Completion Status
`promotion-ready`

## Supporting Regression Questions
- [Justify Large-Gauge Quantization Before Hall-Response Equivalence](../Regression-Questions/justify-large-gauge-quantization-before-hall-response-equivalence.md)
- [Reconstruct The Hall-Response / Chern-Number Equivalence](../Regression-Questions/reconstruct-hall-response-chern-number-equivalence.md)
- [Separate Local Lecture Two Proof From Cited-Source Fusion Gap](../Regression-Questions/separate-local-lecture-two-proof-from-cited-source-fusion-gap.md)

## Supporting Oracles
- [Oracle For Large-Gauge Quantization Before Hall-Response Equivalence](../Question-Oracles/justify-large-gauge-quantization-before-hall-response-equivalence.md)
- [Oracle For Reconstructing The Hall-Response / Chern-Number Equivalence](../Question-Oracles/reconstruct-hall-response-chern-number-equivalence.md)
- [Oracle For Separating Local Lecture Two Proof From Cited-Source Fusion Gap](../Question-Oracles/separate-local-lecture-two-proof-from-cited-source-fusion-gap.md)

## Supporting Regression Runs
- `regression_run:topological-phases-core-2026-03-20-proof-grade-closure`
- `regression_run:topological-phases-core-2026-03-21-lecture-one-cited-recovery`
- `regression_run:topological-phases-core-2026-03-21-leaf-formalization-audit`

## Split Required
`False`

## Recovery Source Refs
- `open_gap:lecture-two-tknn-equivalence-proof-not-yet-curated`
- `followup_source_task:ingest-tknn-and-haldane-for-lecture-two-equivalence`

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `hall_response_chern_number_equivalence`
- Statement kind: `theorem`

### Admissible assumptions

- Work in a gapped two-dimensional U(1)-conserving Hall phase with a nondegenerate ground state under adiabatic twists.
- Treat the response, band, and many-body constructions as three presentations of the same phase rather than as independent systems.
- Import the needed first-Chern-class and Berry-curvature integrality lemmas from a lower-level geometry library instead of reproving them in the family wrapper.

### Lean prerequisites

- [Hall-Response / Chern-Number Notation Family](../Notation-Families/hall-response-chern-number-notation.md)
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](../Proof-Obligations/filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](../Proof-Obligations/twist-angle-berry-curvature-equals-hall-level.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

### Formalization blockers

- The Berry-connection / first-Chern-class infrastructure still needs a reusable Lean-side interface for occupied-band bundles.
- The Haldane lattice-realization branch is a neighboring explanatory bridge and should not be folded into the core theorem declaration until its formal interface is sharper.

## Formal-Theory Guardrails

- Formal theory role: `trusted_target`
- Definition trust tier: `reviewed_translation`
- Statement graph role: `target_statement`
- Prerequisite closure status: `closed`
- Target statement: [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

### Statement graph parents

- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

### Statement graph children

- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)

## Faithfulness Review

- Status: `reviewed`
- Strategy: Use the family wrapper only to collect the response, band, and many-body statements already spelled out by child units, while keeping the Haldane branch as an explanatory neighbor rather than silently extending the trusted target.
- Notes: The family wrapper is faithful only because it points back to the flagship theorem and its obligations instead of replacing them with a wider informal summary.

## Comparator Audit

- Status: `passed`

### Comparator risks

- Do not let the Haldane realization or graphene bridge silently widen the trusted target beyond the k = k' = khat' equivalence itself.

## Provenance And Attribution

- Provenance kind: `mixed`

### Attribution requirements

- Retain attribution to Witten for the lecture-local theorem spine and to TKNN/Haldane for the cross-source family members that remain fused into this family.

## Retrieval Hints
- `Use when a query spans several presentations of the same integer Hall theorem family.`

## Outgoing Edges
- none

## Incoming Edges
- none
