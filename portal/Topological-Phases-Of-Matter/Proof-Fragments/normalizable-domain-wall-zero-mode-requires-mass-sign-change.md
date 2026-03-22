# Normalizable Domain-Wall Zero Mode Requires Mass Sign Change

- ID: `proof_fragment:normalizable-domain-wall-zero-mode-requires-mass-sign-change`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Gluing two opposite-mass fermions across a boundary is equivalent to a single fermion with a sign-changing mass; once the mass profile changes sign, the exponentially localized boundary mode becomes normalizable and furnishes the missing chiral edge excitation.

## Scope
Normalizability and existence part of the Lecture Three Jackiw-Rebbi proof chain.

## Regime
Folded continuum description of a boundary in the integer quantum Hall problem.

## Assumptions
- `The boundary condition can be folded into a sign-changing-mass problem on all of space.`
- `The edge mode must decay away from the boundary to count as a boundary excitation.`

## Representation
Folded-wall proof fragment that turns boundary consistency into a sign-changing-mass zero-mode problem.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: plift, ulift, nuft, obeys, gift, zoggg, trogg | Witten folds the boundary condition into a sign-changing-mass Dirac equation and then extracts the boundary mode.`
- `paper/main-result | Original anomaly-inflow source for the physical meaning of the chiral wall mode.`

## Mathematical Content
- `kind=display` | `label=plift` | Boundary condition gluing the two opposite-mass fermions.
$$
\left.\psi'\right|_{x_1=0}=\gamma_1\left.\psi\right|_{x_1=0}
$$
- `kind=display` | `label=gift` | Folded sign-changing-mass Dirac equation.
$$
\left(\slashed{\partial} - m\,\operatorname{sign}(x_1)\right)\widehat\psi = 0
$$
- `kind=display` | `label=zoggg` | Normalizable boundary-localized profile.
$$
\widehat\psi = e^{-m|x_1|}\,\psi_{\parallel}
$$

## Symbols
- none

## Dependencies
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](parity-anomaly-half-level-from-massive-dirac-fermion.md)

## Related Units
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Step Justification
- Before the mass flip, the doubled system has zero total Chern-Simons level and no edge excitation.
- After the mass flip, the folded fermion sees a sign-changing mass profile across the boundary.
- That sign change makes the exponential wall profile decaying on both sides, hence normalizable.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `normalizable_domain_wall_zero_mode_requires_mass_sign_change`
- Statement kind: `lemma`

### Admissible assumptions

- Work with the folded sign-changing-mass Dirac problem in the continuum.
- Treat the exponential profile extracted from the wall ansatz as the candidate zero-mode envelope.

### Lean prerequisites

- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](parity-anomaly-half-level-from-massive-dirac-fermion.md)

### Formalization blockers

- The analytic normalizability estimate for the wall profile is not yet abstracted into a reusable Lean theorem.
- The folded-boundary construction is still represented as a local physics reduction rather than a fully explicit formal equivalence.

## Retrieval Hints
- `Use when a proof answer must explain why the wall mode exists as a physical boundary excitation rather than merely writing its ansatz.`

## Outgoing Edges
- `supports` -> [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md): Normalizability explains why a sign change in the Dirac mass is required for the chiral wall mode.

## Incoming Edges
- none
