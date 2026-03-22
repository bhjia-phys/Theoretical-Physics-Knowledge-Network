# Oracle For Deriving Boundary Chirality After Doubling And Folding

- ID: `question_oracle:derive-boundary-chirality-after-doubling-and-folding`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the Lecture Three proof-order question from parity anomaly to the chiral wall mode.

## Scope
Detailed answer key for the Lecture Three proof-order derivation question.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must preserve the order of the local proof and the role of each intermediate equation.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: uftof, quft, gift, zoggg, trogg | The answer must traverse the entire local proof chain.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Derive Boundary Chirality After Doubling And Folding](../Regression-Questions/derive-boundary-chirality-after-doubling-and-folding.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Continuum Parity Anomaly Is Not Lattice No-Go](../Conflict-Records/continuum-parity-anomaly-is-not-lattice-no-go.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Prompt
Detailed oracle for regression_question:derive-boundary-chirality-after-doubling-and-folding.

## Failure Triggers
- Fail if the answer starts from the final wall mode and never derives the preceding chain.
- Fail if the answer confuses this continuum proof with the lattice no-go theorem.

## Mandatory Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)
- [Lecture Three Parity-Anomaly Half-Level Context](../Equation-Contexts/lecture-three-parity-anomaly-half-level.md)
- [Lecture Three Sign-Changing Mass Wall Context](../Equation-Contexts/lecture-three-sign-changing-mass-wall-equation.md)
- [Lecture Three Chiral Wall-Mode Context](../Equation-Contexts/lecture-three-chiral-wall-mode.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Mandatory Equation Labels
- `uftof`
- `quft`
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
- Derive the half-level anomaly of one massive Dirac fermion.
- Cancel it by pairing with the opposite-mass fermion.
- Fold the boundary problem into the sign-changing-mass equation.
- Use the Jackiw-Rebbi zero-mode theorem to justify the localized ansatz and its normalizability.
- Insert the localized ansatz and derive the chiral boundary equation.
- Reconnect the resulting chirality to anomaly inflow and keep the lattice no-go theorem separate.

## Mandatory Logical Moves
- The doubling step must occur before the folding step.
- The sign-changing-mass equation must be derived from the boundary problem rather than assumed.
- The chiral projection must come from substituting the wall ansatz.
- The final interpretation must invoke anomaly inflow while preserving the continuum-versus-lattice scope boundary.

## Common Failure Patterns
- Skipping the doubled starting point.
- Writing the wall-mode ansatz without deriving the folding step.
- Forgetting to reconnect the local derivation to the integer Hall boundary story.

## Grading Rubric
- Pass requires the full ordered derivation plus the anomaly-inflow interpretation and the explicit continuum-versus-lattice scope boundary.
- Partial is appropriate if one of the major intermediate steps is missing.

## Outgoing Edges
- none

## Incoming Edges
- none
