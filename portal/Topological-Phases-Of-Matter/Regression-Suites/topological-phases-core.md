# Topological Phases Core Regression Suite

- Suite ID: `regression_suite:topological-phases-core`
- Topic: `topological-phases-of-matter/core`
- Source Map: [Topological Phases Core Source Network](../Source-Maps/topological-phases-core.md)

## Summary
Topic-level regression surface covering the current flagship theorem families for lattice no-go, Hall-response / Chern-number equivalence, and Jackiw-Rebbi edge modes, now also auditing leaf-level Lean-facing plans on the flagship theorem spines together with explicit runtime-gap-to-topic-queue bridges for the still-open cited-source branches.

## Benchmark Governance

- Contamination status: `internal-only`
- Declared use: `workflow_regression`
- Notes: This suite is curated inside the same topic branch that it evaluates. It is authoritative for internal protocol closure and promotion readiness, but it is not a clean external benchmark for autoformalization claims.

## Questions
- [Define A Weyl Node With Its Assumptions](../Regression-Questions/define-weyl-node-with-assumptions.md)
- [Reconstruct The Local Weyl Linearization](../Regression-Questions/reconstruct-local-weyl-linearization.md)
- [Prove Nielsen-Ninomiya By Stokes](../Regression-Questions/prove-nielsen-ninomiya-by-stokes.md)
- [Explain The Berry-Flux Version Of The Node Charge](../Regression-Questions/explain-berry-flux-version-of-node-charge.md)
- [Separate Anomaly Intuition From The Lattice Proof](../Regression-Questions/separate-anomaly-intuition-from-lattice-proof.md)
- [Identify Lecture Two And Three Prerequisites For The Edge-Mode Proof](../Regression-Questions/identify-lecture-two-and-three-prerequisites-for-edge-mode-proof.md)
- [Justify Large-Gauge Quantization Before Hall-Response Equivalence](../Regression-Questions/justify-large-gauge-quantization-before-hall-response-equivalence.md)
- [Reconstruct The Hall-Response / Chern-Number Equivalence](../Regression-Questions/reconstruct-hall-response-chern-number-equivalence.md)
- [Compute The Haldane Chern Number From Dirac-Mass Signs](../Regression-Questions/compute-haldane-chern-number-from-dirac-mass-signs.md)
- [Separate Local Lecture Two Proof From Cited-Source Fusion Gap](../Regression-Questions/separate-local-lecture-two-proof-from-cited-source-fusion-gap.md)
- [Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Regression-Questions/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)
- [Show Callan-Harvey Inflow Cancels The Boundary Anomaly](../Regression-Questions/show-callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Derive Boundary Chirality After Doubling And Folding](../Regression-Questions/derive-boundary-chirality-after-doubling-and-folding.md)
- [Separate Local Edge-Mode Proof From Cited-Source Fusion Gap](../Regression-Questions/separate-local-edge-mode-proof-from-cited-source-fusion-gap.md)

## Oracles
- [Oracle For Defining A Weyl Node With Assumptions](../Question-Oracles/define-weyl-node-with-assumptions.md)
- [Oracle For Reconstructing The Local Weyl Linearization](../Question-Oracles/reconstruct-local-weyl-linearization.md)
- [Oracle For Proving Nielsen-Ninomiya By Stokes](../Question-Oracles/prove-nielsen-ninomiya-by-stokes.md)
- [Oracle For The Berry-Flux Version Of The Node Charge](../Question-Oracles/explain-berry-flux-version-of-node-charge.md)
- [Oracle For Separating Anomaly Intuition From The Lattice Proof](../Question-Oracles/separate-anomaly-intuition-from-lattice-proof.md)
- [Oracle For Identifying Lecture Two And Three Prerequisites](../Question-Oracles/identify-lecture-two-and-three-prerequisites-for-edge-mode-proof.md)
- [Oracle For Large-Gauge Quantization Before Hall-Response Equivalence](../Question-Oracles/justify-large-gauge-quantization-before-hall-response-equivalence.md)
- [Oracle For Reconstructing The Hall-Response / Chern-Number Equivalence](../Question-Oracles/reconstruct-hall-response-chern-number-equivalence.md)
- [Oracle For Computing The Haldane Chern Number From Dirac-Mass Signs](../Question-Oracles/compute-haldane-chern-number-from-dirac-mass-signs.md)
- [Oracle For Separating Local Lecture Two Proof From Cited-Source Fusion Gap](../Question-Oracles/separate-local-lecture-two-proof-from-cited-source-fusion-gap.md)
- [Oracle For Deriving The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Question-Oracles/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)
- [Oracle For Showing Callan-Harvey Inflow Cancels The Boundary Anomaly](../Question-Oracles/show-callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Oracle For Deriving Boundary Chirality After Doubling And Folding](../Question-Oracles/derive-boundary-chirality-after-doubling-and-folding.md)
- [Oracle For Separating Local Edge-Mode Proof From Cited-Source Fusion Gap](../Question-Oracles/separate-local-edge-mode-proof-from-cited-source-fusion-gap.md)

## Focus Units
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Weyl-Node No-Go Consistency Family](../Theorem-Families/weyl-node-no-go-consistency.md)
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Weyl-Node No-Go Cross-Source Fusion Record](../Source-Fusion-Records/weyl-node-no-go-cross-source-fusion.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](../Proof-Fragments/continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Domain-Wall Edge-Mode Consistency Family](../Theorem-Families/domain-wall-edge-mode-consistency.md)
- [A Massive Two Plus One Dimensional Dirac Fermion Induces A Half-Level Chern-Simons Term](../Theorems/half-level-cs-term-from-massive-dirac-fermion.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Boundary Dirac Mode From Negative Bulk Mass](../Derivation-Steps/boundary-dirac-mode-from-negative-bulk-mass.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Two TKNN / Haldane Archival Enrichment Remains To Be Curated](../Open-Gaps/lecture-two-tknn-equivalence-proof-not-yet-curated.md)
- [Jackiw-Rebbi / Callan-Harvey Archival Enrichment Remains To Be Curated](../Open-Gaps/jackiw-rebbi-domain-wall-proof-not-yet-curated.md)
- [Fractional Quantum Hall Topological Order Is Not Yet Curated](../Open-Gaps/fractional-quantum-hall-topological-order-not-yet-curated.md)
- [FQHE Wilson-Loop Algebra Is Not Yet Curated](../Open-Gaps/fqhe-wilson-loop-algebra-not-yet-curated.md)
- [FQHE Torus Ground-State Degeneracy Is Not Yet Curated](../Open-Gaps/fqhe-torus-ground-state-degeneracy-not-yet-curated.md)
- [FQHE Fractional Charge And Statistics Are Not Yet Curated](../Open-Gaps/fqhe-fractional-charge-and-statistics-not-yet-curated.md)

## Recorded Runs
- [regression_run:topological-phases-core-2026-03-19](../Regression-Logs/topological-phases-core-2026-03-19.md) | status=`mixed`
- [regression_run:topological-phases-core-2026-03-20](../Regression-Logs/topological-phases-core-2026-03-20.md) | status=`mixed`
- [regression_run:topological-phases-core-2026-03-20-archival-bridge](../Regression-Logs/topological-phases-core-2026-03-20-archival-bridge.md) | status=`mixed`
- [regression_run:topological-phases-core-2026-03-20-proof-grade-closure](../Regression-Logs/topological-phases-core-2026-03-20-proof-grade-closure.md) | status=`mixed`
- [regression_run:topological-phases-core-2026-03-21-leaf-formalization-audit](../Regression-Logs/topological-phases-core-2026-03-21-leaf-formalization-audit.md) | status=`pass`
- [regression_run:topological-phases-core-2026-03-21-lecture-one-cited-recovery](../Regression-Logs/topological-phases-core-2026-03-21-lecture-one-cited-recovery.md) | status=`pass`
