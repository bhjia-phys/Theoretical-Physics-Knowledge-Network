# Sign-Changing Dirac Mass Supports Chiral Edge Mode

- ID: `theorem:sign-changing-dirac-mass-supports-chiral-edge-mode`
- Type: `theorem`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
A 2+1-dimensional Dirac system whose mass changes sign across a boundary supports a boundary-localized chiral mode; source-grade Jackiw-Rebbi zero-mode and anomaly-inflow results now make the continuum edge-mode consistency story explicit locally.

## Scope
Flagship Lecture Three theorem joining the parity anomaly, Jackiw-Rebbi wall mode, and anomaly-inflow consistency.

## Regime
Continuum edge-mode realization of the integer quantum Hall boundary theory.

## Assumptions
- `The bulk effective action is the integer-level Chern-Simons term after doubling.`
- `The folded boundary problem is equivalent to a sign-changing-mass Dirac equation.`

## Representation
Canonical theorem family for the continuum edge-mode realization of the integer Hall boundary.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: plof, uftof, quft, gift, zoggg, trogg | Witten's continuum proof of edge-mode consistency from the parity anomaly and a sign-changing mass.`
- `paper/isolated-zero-mode | eqs: soliton-dirac-zero-mode | Original zero-mode ingredient, now represented by a dedicated source-grade theorem in the KB.`
- `paper/anomaly-cancellation | eqs: bulk-topological-variation, inflow-balance | Original anomaly-inflow ingredient, now represented by a dedicated source-grade theorem in the KB.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | Lattice realization of the same continuum consistency story.`

## Mathematical Content
- `kind=display` | `label=uftof` | One massive Dirac fermion carries a half-level parity anomaly.
$$
\frac{\operatorname{sign}m}{2}\,\mathcal I_{\mathrm{CS}}(A)
$$
- `kind=display` | `label=gift` | Boundary problem rewritten as a sign-changing-mass Dirac equation.
$$
\left(\slashed{\partial} - m\,\operatorname{sign}(x_1)\right)\widehat\psi = 0
$$
- `kind=display` | `label=trogg` | Chiral boundary mode localized at the wall.
$$
\widehat\psi = e^{-m|x_1|}\,\psi_{\parallel},\qquad \gamma_1\psi_{\parallel} = -\psi_{\parallel},\qquad \slashed{\partial}^{\parallel}\psi_{\parallel}=0
$$

## Symbols
- none

## Dependencies
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](anomaly-inflow-requires-chiral-edge-modes.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Dirac Mode From Negative Bulk Mass](../Derivation-Steps/boundary-dirac-mode-from-negative-bulk-mass.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)

## Related Units
- [Domain-Wall Edge-Mode Consistency Family](../Theorem-Families/domain-wall-edge-mode-consistency.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Domain-Wall Edge-Mode Cross-Source Fusion Record](../Source-Fusion-Records/domain-wall-edge-mode-cross-source-fusion.md)
- [Continuum Parity Anomaly Is Not Lattice No-Go](../Conflict-Records/continuum-parity-anomaly-is-not-lattice-no-go.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)
- [Topological Phases Core Source Network](../Source-Maps/topological-phases-core.md)
- [Former Parity-Anomaly Versus Lattice-No-Go Scope Gap (Closed)](../Open-Gaps/parity-anomaly-motivates-but-does-not-prove-lattice-no-go.md)

## Proof Obligations
- [Single Massive Dirac Fermion Induces Half Level](../Proof-Obligations/single-massive-dirac-fermion-induces-half-level.md)
- [Doubling Cancels Parity Anomaly Before Boundary Sign Flip](../Proof-Obligations/doubling-cancels-parity-anomaly-before-boundary-sign-flip.md)
- [Boundary Folding Produces Sign-Changing Mass Dirac Equation](../Proof-Obligations/boundary-folding-produces-sign-changing-mass-dirac-equation.md)
- [Domain-Wall Ansatz Imposes Chiral Boundary Equation](../Proof-Obligations/domain-wall-ansatz-imposes-chiral-boundary-equation.md)
- [Normalizable Wall Mode Requires Mass Sign Change](../Proof-Obligations/normalizable-wall-mode-requires-mass-sign-change.md)
- [Edge Mode Restores Consistency With Integer Bulk Response](../Proof-Obligations/edge-mode-restores-consistency-with-integer-bulk-response.md)

## Equation Contexts
- [Lecture Three Parity-Anomaly Half-Level Context](../Equation-Contexts/lecture-three-parity-anomaly-half-level.md)
- [Lecture Three Sign-Changing Mass Wall Context](../Equation-Contexts/lecture-three-sign-changing-mass-wall-equation.md)
- [Lecture Three Chiral Wall-Mode Context](../Equation-Contexts/lecture-three-chiral-wall-mode.md)

## Dependency Graph Snapshot
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)

## Topic Completion Status
`promotion-ready`

## Supporting Regression Questions
- [Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Regression-Questions/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)
- [Show Callan-Harvey Inflow Cancels The Boundary Anomaly](../Regression-Questions/show-callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Derive Boundary Chirality After Doubling And Folding](../Regression-Questions/derive-boundary-chirality-after-doubling-and-folding.md)
- [Separate Local Edge-Mode Proof From Cited-Source Fusion Gap](../Regression-Questions/separate-local-edge-mode-proof-from-cited-source-fusion-gap.md)

## Supporting Oracles
- [Oracle For Deriving The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Question-Oracles/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)
- [Oracle For Showing Callan-Harvey Inflow Cancels The Boundary Anomaly](../Question-Oracles/show-callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Oracle For Deriving Boundary Chirality After Doubling And Folding](../Question-Oracles/derive-boundary-chirality-after-doubling-and-folding.md)
- [Oracle For Separating Local Edge-Mode Proof From Cited-Source Fusion Gap](../Question-Oracles/separate-local-edge-mode-proof-from-cited-source-fusion-gap.md)

## Supporting Regression Runs
- `regression_run:topological-phases-core-2026-03-20-proof-grade-closure`
- `regression_run:topological-phases-core-2026-03-21-leaf-formalization-audit`

## Split Required
`False`

## Recovery Source Refs
- `open_gap:jackiw-rebbi-domain-wall-proof-not-yet-curated`
- `followup_source_task:ingest-callan-harvey-and-jackiw-rebbi-for-edge-mode-proof`
- `conflict_record:continuum-parity-anomaly-is-not-lattice-no-go`

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `sign_changing_dirac_mass_supports_chiral_edge_mode`
- Statement kind: `theorem`

### Admissible assumptions

- Work in the continuum doubled 2+1-dimensional Dirac model with a folded boundary producing a sign-changing mass profile.
- Treat the parity-anomaly half level, Jackiw-Rebbi zero mode, and anomaly-inflow cancellation as explicit local sublemmas.

### Lean prerequisites

- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](anomaly-inflow-requires-chiral-edge-modes.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)

### Formalization blockers

- A reusable Lean-side analytic interface for domain-wall Dirac operators and localized zero modes is still missing.
- The continuum edge-mode theorem is still intentionally separated from the distinct lattice regularization story and needs a formal bridge layer if those branches are to be combined.

## Formal-Theory Guardrails

- Formal theory role: `trusted_target`
- Statement graph role: `target_statement`
- Prerequisite closure status: `closed`

### Statement graph parents

- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](anomaly-inflow-requires-chiral-edge-modes.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)

### Statement graph children

- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)

## Faithfulness Review

- Status: `reviewed`
- Strategy: Keep the trusted theorem limited to the continuum bulk-boundary consistency statement proved from sign-changing mass, Jackiw-Rebbi localization, and anomaly inflow, while leaving the lattice no-go branch outside the theorem.
- Notes: The KB expands the argument into source-grade subclaims but keeps the trusted target theorem at the same scope as the source.

## Comparator Audit

- Status: `passed`

### Comparator risks

- Do not let the continuum theorem drift into a claim about lattice charge cancellation or species doubling.

## Provenance And Attribution

- Provenance kind: `mixed`

### Attribution requirements

- Retain attribution to Witten for the theorem statement and to Jackiw-Rebbi / Callan-Harvey for the explicit neighboring source-grade ingredients.

## Retrieval Hints
- `Use when a query asks for the flagship Lecture Three boundary-mode theorem, including how the bulk topological term and edge mode fit together.`

## Outgoing Edges
- `anchored_in_source` -> [Topological Phases Core Source Network](../Source-Maps/topological-phases-core.md): The edge-mode theorem is one of the flagship families anchored in the topic-level source network.
- `anchored_in_source` -> [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md): The flagship edge-mode theorem is part of the Lecture Three source map.

## Incoming Edges
- [Ingest Callan-Harvey And Jackiw-Rebbi For The Edge-Mode Proof](../Followup-Source-Tasks/ingest-callan-harvey-and-jackiw-rebbi-for-edge-mode-proof.md) -> `routes_to`: The Callan-Harvey / Jackiw-Rebbi recovery task is meant to re-enter the canonical edge-mode theorem family.
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md) -> `supports`: The domain-wall ansatz reduces the boundary problem to the tangential Dirac equation used in the theorem.
- [Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Regression-Questions/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md) -> `tests`: The regression question tests whether the edge-mode theorem can be reconstructed explicitly.
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md) -> `supports`: Normalizability explains why a sign change in the Dirac mass is required for the chiral wall mode.
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md) -> `motivates`: The half-level parity anomaly explains why the boundary mode must appear in the consistent doubled system.
