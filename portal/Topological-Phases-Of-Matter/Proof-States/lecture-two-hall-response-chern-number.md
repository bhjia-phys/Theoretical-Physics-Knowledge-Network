# Lecture Two Hall-Response / Chern-Number Proof State

- ID: `proof_state:lecture-two-hall-response-chern-number`
- Type: `proof_state`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Current proof-state ledger for the Lecture Two flagship theorem: the local Witten derivation spine is explicit, the TKNN side is source-grade locally through the traced-curvature identity plus the projector formula, the graphene/Haldane bridge is decomposed through explicit lattice and valley-mass units, and the remaining follow-up is original-paper archival enrichment rather than a missing core proof.

## Scope
Ledger-level summary of the Hall-response / Chern-number theorem family.

## Regime
Proof-completion review state.

## Assumptions
- `The local theorem family is being audited for proof completeness and source-fusion honesty.`

## Representation
Proof-state ledger distinguishing the explicit core theorem chain from the narrower residual enrichment route.

## Source Anchors
- `lecture-two/quantization-of-the-chern-simons-coupling | Beginning of the local proof chain.`
- `lecture-two/proof-of-the-equivalence | Completion of the local proof chain.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Lecture Two Hall-Response / Chern-Number Dependency Graph](../Dependency-Graph-Snapshots/lecture-two-hall-response-chern-number-proof.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)

## Related Units
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)
- [Lecture Two TKNN / Haldane Archival Enrichment Remains To Be Curated](../Open-Gaps/lecture-two-tknn-equivalence-proof-not-yet-curated.md)
- [Ingest TKNN And Haldane For The Lecture Two Equivalence](../Followup-Source-Tasks/ingest-tknn-and-haldane-for-lecture-two-equivalence.md)

## Pass Conditions
- All local Witten-side obligations are explicit and formula-bearing.
- The TKNN route is explicit through the traced-curvature identity, the occupied-projector formula, and the Chern-class interpretation.
- The Haldane bridge is explicit through the graphene Hamiltonian, Dirac-point condition, symmetry-protection statement, and valley-mass Chern-number criterion.
- The proof state records the remaining original-paper Haldane / archival-enrichment follow-up honestly instead of overstating it as a missing core proof.

## Failure Triggers
- Fail if the theorem is described as still lacking a core TKNN source-grade fragment even though the projector formula is present.
- Fail if the projector formula is quoted without the local Berry-curvature-to-projector bridge.
- Fail if any obligation is referenced only by title without its defining equations or logical move.
- Fail if the narrower Haldane / archival-enrichment follow-up is silently erased.

## Proof Obligations
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](../Proof-Obligations/filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](../Proof-Obligations/twist-angle-berry-curvature-equals-hall-level.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

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
- Declaration: `hall_response_chern_number_proof_state`
- Statement kind: `scaffold`

### Admissible assumptions

- The theorem family is formalized as a bundle of bounded lemmas rather than as one opaque derivation block.
- The cited-source Haldane enrichment remains outside the local core scaffold.

### Lean prerequisites

- [Lecture Two Hall-Response / Chern-Number Dependency Graph](../Dependency-Graph-Snapshots/lecture-two-hall-response-chern-number-proof.md)
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](../Proof-Obligations/filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](../Proof-Obligations/twist-angle-berry-curvature-equals-hall-level.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

### Formalization blockers

- The occupied-bundle geometry package still needs a stable import surface before this proof state can become a real Lean namespace wrapper.

## Formal-Theory Guardrails

- Formal theory role: `intermediate_theory`
- Statement graph role: `temporary_scaffold`
- Prerequisite closure status: `closed`
- Target statement: [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

### Statement graph parents

- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)

### Statement graph children

- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](../Proof-Obligations/filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](../Proof-Obligations/twist-angle-berry-curvature-equals-hall-level.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

## Faithfulness Review

- Status: `bounded`
- Strategy: Treat this proof state only as a ledger of obligations and dependency structure; it is faithful precisely by refusing to replace the trusted theorem statement.
- Notes: The proof state is intentionally narrower than the theorem family and should never be cited as the theorem itself.

## Comparator Audit

- Status: `passed`

### Comparator risks

- A proof-state ledger can look complete enough to be mistaken for the theorem; keep the target theorem link explicit.

## Provenance And Attribution

- Provenance kind: `mixed`

### Attribution requirements

- Preserve the distinction between Witten's lecture-local proof spine and the cited TKNN/Haldane source enrichments when reusing this scaffold.

## Retrieval Hints
- `Use when an answer or audit needs the whole proof ledger rather than one isolated obligation.`

## Outgoing Edges
- none

## Incoming Edges
- none
