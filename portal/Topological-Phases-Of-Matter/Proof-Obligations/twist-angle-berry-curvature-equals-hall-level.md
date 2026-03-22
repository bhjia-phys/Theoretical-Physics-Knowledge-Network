# Twist-Angle Berry Curvature Equals The Hall Level

- ID: `proof_obligation:twist-angle-berry-curvature-equals-hall-level`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that the Berry curvature on the twist-angle torus is constant and integrates to the same integer k that controls the macroscopic Hall response.

## Scope
Many-body Berry-curvature obligation in the Lecture Two equivalence proof.

## Regime
Many-body adiabatic-transport formulation.

## Assumptions
- `The twist angles alpha_1 and alpha_2 are periodic coordinates on a torus.`
- `The one-derivative adiabatic term correctly captures the Berry connection.`

## Representation
Bounded proof obligation for the many-body Berry-curvature route to the Hall-response level.

## Source Anchors
- `lecture-two/proof-of-the-equivalence | eqs: mizz, roff, coff, plizz | Witten's twist-angle Berry-phase proof of the many-body Chern number.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Chern-Simons Level Produces Quantized Hall Current](chern-simons-level-produces-quantized-hall-current.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)
- [Lecture Two Twist-Angle Berry Curvature Context](../Equation-Contexts/lecture-two-twist-angle-berry-curvature.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Dependency Graph](../Dependency-Graph-Snapshots/lecture-two-hall-response-chern-number-proof.md)

## Pass Conditions
- The answer introduces the twist-angle torus and the adiabatic reduced action.
- The answer writes the Berry connection or covariant derivatives on the torus.
- The answer derives the constant Berry curvature and integrates it to obtain \widehat{k}' = k.

## Mandatory Logical Moves
- Treat alpha_1 and alpha_2 as adiabatic parameters.
- Read off the Berry connection from the one-derivative action.
- Integrate the resulting curvature over the full torus.

## Common Failure Patterns
- Stating the twist-angle result without the Berry-connection step.
- Confusing the many-body torus with the Brillouin torus.
- Forgetting that the final integral yields the same integer k.

## Grading Rubric
- Full credit requires the Berry connection, Berry curvature, and torus integral.
- Partial credit is appropriate if the answer mentions twisted boundary conditions but omits the geometric calculation.

## Retrieval Hints
- `Use when the many-body derivation must be explicit and formula-bearing.`

## Outgoing Edges
- none

## Incoming Edges
- none
