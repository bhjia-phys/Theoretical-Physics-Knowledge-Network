# Domain-Wall Ansatz Imposes Chiral Boundary Equation

- ID: `proof_obligation:domain-wall-ansatz-imposes-chiral-boundary-equation`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that inserting the localized wall ansatz into the sign-changing-mass Dirac equation forces a definite gamma_1 chirality and leaves a reduced tangential Dirac equation for the boundary mode.

## Scope
Fourth proof obligation in the Lecture Three theorem family.

## Regime
Localized domain-wall mode derivation.

## Assumptions
- `The wall profile depends only on x_1 and the tangential dynamics live on the boundary.`

## Representation
Bounded proof obligation for the boundary chirality condition induced by the wall ansatz.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: zoggg, trogg | The localized ansatz leads to the chiral boundary equation.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Boundary Folding Produces Sign-Changing Mass Dirac Equation](boundary-folding-produces-sign-changing-mass-dirac-equation.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Lecture Three Chiral Wall-Mode Context](../Equation-Contexts/lecture-three-chiral-wall-mode.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)

## Pass Conditions
- The answer writes the localized ansatz.
- The answer substitutes it into the sign-changing-mass equation.
- The answer derives both the gamma_1 chirality condition and the tangential Dirac equation.

## Mandatory Logical Moves
- Factor out the exponential wall profile.
- Separate the normal and tangential pieces of the Dirac equation.
- Identify the surviving chiral boundary equation.

## Common Failure Patterns
- Writing the final edge mode without showing how the chirality projection appears.
- Failing to distinguish the normal profile from the tangential spinor.

## Grading Rubric
- Full credit requires the substitution step and the explicit reduced equation.
- Partial credit is appropriate if the answer states the wall-mode form but not the derivation.

## Retrieval Hints
- `Use when the derivation must explain where the chiral boundary equation comes from.`

## Outgoing Edges
- none

## Incoming Edges
- none
