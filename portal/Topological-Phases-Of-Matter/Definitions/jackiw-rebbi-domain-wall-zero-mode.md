# Jackiw-Rebbi Domain-Wall Zero Mode

- ID: `definition:jackiw-rebbi-domain-wall-zero-mode`
- Type: `definition`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
A Jackiw-Rebbi domain-wall zero mode is a boundary-localized Dirac solution supported where a mass term changes sign, with exponential decay away from the wall and a fixed boundary chirality.

## Scope
Definition of the boundary-localized zero mode invoked in Witten Lecture Three and traced back to Jackiw-Rebbi.

## Regime
Continuum edge-mode analysis for a 2+1-dimensional Dirac fermion.

## Assumptions
- `The bulk Dirac mass changes sign across the wall.`
- `The mode is required to be normalizable in the direction transverse to the wall.`

## Representation
Boundary-localized spinor supported on a sign-changing Dirac mass profile.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: gift, zoggg, trogg | Witten's folded sign-changing-mass Dirac equation and the resulting localized mode.`
- `paper/main-result | Original source of the isolated Dirac zero-mode mechanism.`

## Mathematical Content
- `kind=display` | `label=gift` | Dirac equation with sign-changing mass profile.
$$
\left(\slashed{\partial} - m\,\operatorname{sign}(x_1)\right)\psi = 0
$$
- `kind=display` | `label=zoggg` | Localized wall profile.
$$
\psi = e^{-m|x_1|}\,\psi_{\parallel}
$$
- `kind=display` | `label=trogg` | Boundary chirality condition and reduced tangential Dirac equation.
$$
\gamma_1\psi_{\parallel} = -\psi_{\parallel},\qquad \slashed{\partial}^{\parallel}\psi_{\parallel}=0
$$

## Symbols
- none

## Dependencies
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md)

## Related Units
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks what exactly the Jackiw-Rebbi boundary mode is before asking why it exists.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md): The Jackiw-Rebbi zero-mode definition is part of the Lecture Three source map.

## Incoming Edges
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md) -> `supports`: The Lecture Three notation map fixes the Dirac and boundary-mode symbols used in the Jackiw-Rebbi definition.
