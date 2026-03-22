# Normalizable Wall Mode Requires Mass Sign Change

- ID: `proof_obligation:normalizable-wall-mode-requires-mass-sign-change`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that the exponential wall profile is normalizable only because the mass changes sign across the boundary, so the mode decays away from the wall on both sides.

## Scope
Fifth proof obligation in the Lecture Three theorem family.

## Regime
Physical existence criterion for the wall mode.

## Assumptions
- `A genuine boundary excitation must be square-integrable in the normal direction.`

## Representation
Bounded proof obligation for the physical normalizability of the wall mode.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: gift, zoggg, trogg | The wall profile is normalizable only when the mass flips sign.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Domain-Wall Ansatz Imposes Chiral Boundary Equation](domain-wall-ansatz-imposes-chiral-boundary-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Lecture Three Chiral Wall-Mode Context](../Equation-Contexts/lecture-three-chiral-wall-mode.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Pass Conditions
- The answer explains why the sign-changing mass makes the exponential profile decay on both sides.
- The answer states that normalizability is what makes the mode a physical boundary excitation.

## Mandatory Logical Moves
- Inspect the wall profile away from the boundary on both sides.
- Use the mass sign flip to show both tails decay rather than one exploding.
- Interpret the result as normalizability of the edge mode.

## Common Failure Patterns
- Writing the exponential profile without checking whether it is normalizable.
- Saying a wall mode exists without explaining why the sign change matters.

## Grading Rubric
- Full credit requires an explicit normalizability argument tied to the mass sign change.
- Partial credit is appropriate if the answer states the mode but omits why it decays.

## Retrieval Hints
- `Use when a derivation must justify that the boundary mode is physically admissible.`

## Outgoing Edges
- none

## Incoming Edges
- none
