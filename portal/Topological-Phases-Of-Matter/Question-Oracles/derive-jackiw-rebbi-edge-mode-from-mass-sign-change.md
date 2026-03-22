# Oracle For Deriving The Jackiw-Rebbi Edge Mode From Mass Sign Change

- ID: `question_oracle:derive-jackiw-rebbi-edge-mode-from-mass-sign-change`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the Lecture Three boundary-mode derivation question.

## Scope
Detailed answer key for the Jackiw-Rebbi / parity-anomaly boundary-mode theorem family.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must keep the continuum edge-mode proof distinct from the lattice Nielsen-Ninomiya theorem.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: uftof, gift, zoggg, trogg | The answer must reconstruct both the half-level anomaly and the wall-mode derivation.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Regression-Questions/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Domain-Wall Edge-Mode Consistency Family](../Theorem-Families/domain-wall-edge-mode-consistency.md)
- [Domain-Wall Edge-Mode Cross-Source Fusion Record](../Source-Fusion-Records/domain-wall-edge-mode-cross-source-fusion.md)
- [Continuum Parity Anomaly Is Not Lattice No-Go](../Conflict-Records/continuum-parity-anomaly-is-not-lattice-no-go.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Prompt
Detailed oracle for regression_question:derive-jackiw-rebbi-edge-mode-from-mass-sign-change.

## Failure Triggers
- Fail if the answer states only that Jackiw-Rebbi was cited without reconstructing the mode.
- Fail if the answer identifies the continuum edge-mode proof with the lattice no-go proof.
- Fail if the answer treats anomaly inflow as a slogan and never writes the cancellation equation.
- Fail if the answer omits why the wall profile is normalizable.

## Mandatory Units
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Mandatory Equation Labels
- `uftof`
- `gift`
- `zoggg`
- `trogg`

## Supporting Obligations
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

## Derivation Spine
- State the half-level parity anomaly of one massive 2+1-dimensional Dirac fermion.
- Explain why doubling with the opposite mass gives a trivial boundary-free starting point.
- Flip one mass sign, fold the boundary problem into a sign-changing-mass Dirac equation, and write the localized ansatz.
- Invoke the Jackiw-Rebbi zero-mode theorem to justify the exponential wall profile and its normalizability.
- Derive the boundary chirality condition and reduced tangential Dirac equation.
- Write the Callan-Harvey cancellation equation matching the edge anomaly to the bulk variation.
- Explain that anomaly inflow requires the resulting chiral wall mode as the boundary degree of freedom of the consistent integer Hall system.

## Mandatory Logical Moves
- Keep the doubled starting point explicit before the sign flip.
- Derive the sign-changing-mass equation from folding rather than assuming it.
- Use the explicit bulk-plus-boundary cancellation equation when invoking anomaly inflow.
- Reconnect the local wall mode to the consistent integer Hall boundary story.

## Common Failure Patterns
- Jumping directly to the wall ansatz without the folding step.
- Citing Jackiw-Rebbi or anomaly inflow by name without using their actual theorem content.
- Invoking anomaly inflow without the explicit Callan-Harvey cancellation equation.
- Forgetting the anomaly-cancellation role of doubling.
- Confusing the continuum edge-mode derivation with the lattice no-go theorem.

## Grading Rubric
- Pass requires the ordered local derivation together with explicit use of the Jackiw-Rebbi zero-mode and anomaly-inflow ingredients.
- Partial is appropriate if one major intermediate step is omitted.

## Outgoing Edges
- `oracles` -> [Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Regression-Questions/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md): This oracle records the derivation requirements for the Jackiw-Rebbi edge-mode question.

## Incoming Edges
- none
