# Boundary Folding Produces Sign-Changing Mass Dirac Equation

- ID: `proof_obligation:boundary-folding-produces-sign-changing-mass-dirac-equation`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that the boundary gluing of the doubled system can be folded into a single Dirac equation on all of space with a mass term m sign(x_1).

## Scope
Third proof obligation in the Lecture Three theorem family.

## Regime
Folded whole-space reformulation of the boundary problem.

## Assumptions
- `The gluing condition at the boundary is the one used by Witten in the doubled system.`

## Representation
Bounded proof obligation for the folding step from boundary gluing to the domain-wall equation.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: plift, ulift, gift | The gluing condition is rewritten as one sign-changing-mass Dirac equation.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Doubling Cancels Parity Anomaly Before Boundary Sign Flip](doubling-cancels-parity-anomaly-before-boundary-sign-flip.md)
- [Lecture Three Sign-Changing Mass Wall Context](../Equation-Contexts/lecture-three-sign-changing-mass-wall-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)

## Pass Conditions
- The answer states the boundary gluing condition or the two opposite-mass equations.
- The answer explains the folding construction.
- The answer derives the sign-changing-mass Dirac equation.

## Mandatory Logical Moves
- State the boundary gluing condition.
- Fold the two half-space fermions into one whole-space spinor.
- Show that the resulting equation has mass term m sign(x_1).

## Common Failure Patterns
- Starting from the sign-changing-mass equation without explaining how it arises from the doubled system.
- Treating the wall equation as an unrelated ansatz.

## Grading Rubric
- Full credit requires the boundary-to-domain-wall rewrite, not only the final wall equation.
- Partial credit is appropriate if the answer quotes the wall equation but not the folding logic.

## Retrieval Hints
- `Use when the answer must show how the boundary problem becomes the Jackiw-Rebbi problem.`

## Outgoing Edges
- none

## Incoming Edges
- none
