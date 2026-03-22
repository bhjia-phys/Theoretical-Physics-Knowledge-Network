# Lecture Three Chiral Wall-Mode Context

- ID: `equation_context:lecture-three-chiral-wall-mode`
- Type: `equation_context`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This equation context records the exponentially localized wall ansatz, the gamma_1 chirality projection, and the reduced tangential Dirac equation that together produce the chiral boundary mode.

## Scope
Equation-level context for the localized chiral wall mode.

## Regime
Domain-wall zero-mode derivation.

## Assumptions
- `The physical edge mode must be normalizable away from the wall.`

## Representation
Equation context for the chiral wall mode supported by the sign-changing mass.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: zoggg, trogg | Localized ansatz and reduced boundary Dirac equation.`

## Mathematical Content
- `kind=display` | `label=zoggg` | Exponentially localized wall profile.
$$
\widehat\psi = e^{-m|x_1|}\,\psi_{\parallel}
$$
- `kind=display` | `label=trogg` | Boundary chirality projection and reduced tangential Dirac equation.
$$
\gamma_1\psi_{\parallel} = -\psi_{\parallel},\qquad \slashed{\partial}^{\parallel}\psi_{\parallel}=0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `\psi_{\parallel}` | boundary-localized spinor after factoring out the wall profile |
| `\gamma_1` | normal gamma matrix fixing the chirality of the wall mode |

## Dependencies
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md)

## Related Units
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Domain-Wall Ansatz Imposes Chiral Boundary Equation](../Proof-Obligations/domain-wall-ansatz-imposes-chiral-boundary-equation.md)
- [Normalizable Wall Mode Requires Mass Sign Change](../Proof-Obligations/normalizable-wall-mode-requires-mass-sign-change.md)

## Retrieval Hints
- `Use when an answer must reconstruct the actual wall-mode ansatz and chirality condition.`

## Outgoing Edges
- none

## Incoming Edges
- none
