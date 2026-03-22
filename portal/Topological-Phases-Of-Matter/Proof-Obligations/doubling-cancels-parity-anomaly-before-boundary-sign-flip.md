# Doubling Cancels Parity Anomaly Before Boundary Sign Flip

- ID: `proof_obligation:doubling-cancels-parity-anomaly-before-boundary-sign-flip`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that two Dirac fermions with opposite masses contribute opposite half levels, so the doubled boundary-free starting point has zero total Chern-Simons level before one mass sign is flipped.

## Scope
Second proof obligation in the Lecture Three theorem family.

## Regime
Consistency setup for the integer Hall boundary discussion.

## Assumptions
- `The doubled system is considered before introducing the domain wall.`

## Representation
Bounded proof obligation for the anomaly-free doubled starting point.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: quft | Witten's explicit cancellation of the two opposite half levels.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Single Massive Dirac Fermion Induces Half Level](single-massive-dirac-fermion-induces-half-level.md)
- [Lecture Three Parity-Anomaly Half-Level Context](../Equation-Contexts/lecture-three-parity-anomaly-half-level.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Boundary Folding Produces Sign-Changing Mass Dirac Equation](boundary-folding-produces-sign-changing-mass-dirac-equation.md)

## Pass Conditions
- The answer states that the two masses have opposite sign.
- The answer shows that the two half-level contributions cancel.
- The answer explains why this gives a trivial starting point before the boundary sign flip.

## Mandatory Logical Moves
- Pair the two opposite-mass fermions.
- Sum their half-level contributions.
- Interpret the zero total level as the pre-domain-wall reference configuration.

## Common Failure Patterns
- Jumping straight to the domain wall without explaining the anomaly-free doubled starting point.
- Treating the single-fermion half level as already gauge invariant.

## Grading Rubric
- Full credit requires the cancellation step and its role in setting up the boundary problem.
- Partial credit is appropriate if the answer knows there are two fermions but does not explain why their total level vanishes.

## Retrieval Hints
- `Use when the derivation must keep the doubled setup explicit.`

## Outgoing Edges
- none

## Incoming Edges
- none
