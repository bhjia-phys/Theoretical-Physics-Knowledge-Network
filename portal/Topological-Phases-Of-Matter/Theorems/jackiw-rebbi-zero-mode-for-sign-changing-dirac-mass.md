# Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass

- ID: `theorem:jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass`
- Type: `theorem`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
If a Dirac mass profile changes sign across an interface, then the Dirac operator admits a normalizable wall-localized zero mode whose envelope is the exponential of minus the mass integral.

## Scope
Reusable source-grade zero-mode theorem behind the Lecture Three domain-wall derivation.

## Regime
Continuum Dirac operator with a one-dimensional sign-changing mass profile.

## Assumptions
- `The asymptotic masses at x_1 to plus and minus infinity have opposite sign.`
- `The tangential momentum is tuned to the interface zero-mode branch when solving the transverse localization problem.`

## Representation
Source-grade zero-mode theorem extracted from the sign-changing-mass Dirac equation.

## Source Anchors
- `paper/isolated-zero-mode | eqs: soliton-dirac-zero-mode | Original source of the sign-changing-mass zero-mode mechanism.`
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: gift, zoggg, trogg | Witten uses the Jackiw-Rebbi mechanism in the folded Hall-boundary problem.`

## Mathematical Content
- `kind=display` | Dirac equation with a wall-dependent mass profile.
$$
\left(\gamma^1\partial_1+\gamma^{\parallel}\cdot p_{\parallel}-m(x_1)\right)\psi=0
$$
- `kind=display` | Projected wall ansatz.
$$
\psi(x_1,x_{\parallel})=f(x_1)\psi_{\parallel}(x_{\parallel}),\qquad \gamma_1\psi_{\parallel}=-\psi_{\parallel}
$$
- `kind=display` | Normalizable envelope when the mass flips sign.
$$
f(x_1)=\exp\!\left(-\int_0^{x_1}m(y)\,\mathrm dy\right)
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `m(x_1)` | Dirac mass profile across the interface |
| `f(x_1)` | transverse localization envelope of the zero mode |
| `\psi_{\parallel}` | spinor tangent to the interface |

## Dependencies
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)

## Related Units
- [Domain-Wall Edge-Mode Consistency Family](../Theorem-Families/domain-wall-edge-mode-consistency.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Domain-Wall Edge-Mode Cross-Source Fusion Record](../Source-Fusion-Records/domain-wall-edge-mode-cross-source-fusion.md)

## Topic Completion Status
`promotion-ready`

## Supporting Regression Questions
- [Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Regression-Questions/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)
- [Derive Boundary Chirality After Doubling And Folding](../Regression-Questions/derive-boundary-chirality-after-doubling-and-folding.md)

## Supporting Oracles
- [Oracle For Deriving The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Question-Oracles/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)
- [Oracle For Deriving Boundary Chirality After Doubling And Folding](../Question-Oracles/derive-boundary-chirality-after-doubling-and-folding.md)

## Supporting Regression Runs
- `regression_run:topological-phases-core-2026-03-20-proof-grade-closure`
- `regression_run:topological-phases-core-2026-03-21-leaf-formalization-audit`

## Split Required
`False`

## Recovery Source Refs
- `open_gap:jackiw-rebbi-domain-wall-proof-not-yet-curated`
- `followup_source_task:ingest-callan-harvey-and-jackiw-rebbi-for-edge-mode-proof`

## Failure Modes
- `If the mass does not change sign, the exponential profile fails to decay on both sides and this zero-mode construction is not normalizable.`

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `jackiw_rebbi_zero_mode_for_sign_changing_dirac_mass`
- Statement kind: `theorem`

### Admissible assumptions

- Work with a continuum Dirac operator whose mass profile has opposite asymptotic signs on the two sides of the interface.
- Treat the tangential zero-mode branch and the wall ansatz as accepted setup data for the theorem.

### Lean prerequisites

- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)

### Formalization blockers

- The analytic existence statement for localized zero modes of sign-changing-mass Dirac operators is not yet packaged as a reusable Lean theorem.
- The relation between the local zero mode and the later anomaly-carrying chiral boundary theory remains a separate bridge theorem.

## Retrieval Hints
- `Use when the answer must reconstruct the actual Jackiw-Rebbi mode instead of citing the paper name only.`

## Outgoing Edges
- none

## Incoming Edges
- none
