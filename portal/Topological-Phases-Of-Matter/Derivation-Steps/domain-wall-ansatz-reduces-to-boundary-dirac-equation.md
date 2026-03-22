# Domain-Wall Ansatz Reduces To Boundary Dirac Equation

- ID: `derivation_step:domain-wall-ansatz-reduces-to-boundary-dirac-equation`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Insert the exponentially localized ansatz into the sign-changing-mass Dirac equation and separate the transverse profile from the tangential dynamics to obtain a 1+1-dimensional chiral boundary Dirac equation.

## Scope
Core derivation step in the Jackiw-Rebbi boundary-mode proof.

## Regime
Continuum Dirac analysis near a sign-changing mass wall.

## Assumptions
- `The mode is translationally invariant along the boundary directions up to a plane wave.`
- `The wall profile depends only on the normal coordinate x_1.`

## Representation
Separation of variables between transverse wall profile and tangential boundary dynamics.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: gift, zoggg, trogg | Witten explicitly inserts the localized ansatz into the sign-changing-mass Dirac equation.`
- `paper/main-result | Original zero-mode mechanism behind the wall ansatz.`

## Mathematical Content
- `kind=display` | `label=gift` | Starting sign-changing-mass Dirac equation.
$$
\left(\slashed{\partial} - m\,\operatorname{sign}(x_1)\right)\psi = 0
$$
- `kind=display` | `label=zoggg` | Localized ansatz in the normal direction.
$$
\psi = e^{-m|x_1|}\,\psi_{\parallel}
$$
- `kind=display` | `label=trogg` | Reduced chiral boundary Dirac equation.
$$
\gamma_1\psi_{\parallel} = -\psi_{\parallel},\qquad \slashed{\partial}^{\parallel}\psi_{\parallel}=0
$$

## Symbols
- none

## Dependencies
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md)
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)

## Related Units
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Step Inputs
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)

## Step Justification
- The sign-changing mass fixes the decaying transverse profile.
- After factoring out the wall profile, the remaining spinor obeys a reduced Dirac equation tangent to the boundary.
- The gamma_1 eigenvalue condition fixes the boundary chirality.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `domain_wall_ansatz_reduces_to_boundary_dirac_equation`
- Statement kind: `lemma`

### Admissible assumptions

- Work with the continuum sign-changing-mass Dirac equation and a separated wall ansatz.
- Treat the gamma-matrix conventions as fixed by the local notation family rather than reproving representation independence inside the lemma.

### Lean prerequisites

- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)

### Formalization blockers

- The current KB does not yet provide a reusable Lean-side abstraction for gamma-matrix manipulations in the domain-wall reduction.
- Normalizability is still split into a neighboring lemma and is not encoded as a postcondition of this reduction step.

## Retrieval Hints
- `Use when a derivation answer must show how the wall ansatz actually produces the boundary Dirac equation.`

## Outgoing Edges
- `supports` -> [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md): The domain-wall ansatz reduces the boundary problem to the tangential Dirac equation used in the theorem.

## Incoming Edges
- none
