# Boundary Dirac Mode From Negative Bulk Mass

- ID: `derivation_step:boundary-dirac-mode-from-negative-bulk-mass`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
For a Dirac fermion on a half-space, the separated ansatz psi=e^{m x_1} psi_parallel is normalizable only when m<0, yielding a boundary-localized lower-dimensional Dirac mode and giving a lecture-one precursor of the later Jackiw-Rebbi wall construction.

## Scope
Cross-lecture derivation step that links the Lecture One boundary-mode calculation to the later sign-changing-mass edge-mode family.

## Regime
Continuum half-space Dirac problem used as a precursor to the Lecture Three wall-mode construction.

## Assumptions
- `The system occupies the half-space x_1 >= 0.`
- `A Hermitian boundary condition is imposed on the bulk Dirac fermion.`

## Representation
Cross-lecture boundary-mode derivation step highlighting the normalizability test for a half-space Dirac fermion.

## Source Anchors
- `lecture-one/gapless-boundary-modes-from-dirac-fermions | eqs: molof, ogg, pogg, zuffo | Lecture One boundary-mode derivation that serves as a precursor to the later domain-wall construction.`

## Mathematical Content
- `kind=display` | `label=molof` | Hermitian boundary condition on the bulk Dirac field.
$$
\gamma_1\psi\big|_{x_1=0}=\pm\psi\big|_{x_1=0}
$$
- `kind=display` | `label=pogg` | Boundary-localized mode obtained after separation of variables.
$$
\psi=e^{m x_1}\psi_{\parallel}(x_{\parallel}),\qquad \gamma_1\psi_{\parallel}=\psi_{\parallel},\qquad \gamma\cdot\partial^{\parallel}\psi_{\parallel}=0
$$
- `kind=display` | `label=zuffo` | Doubled boundary Dirac equation in Witten's lecture-one presentation.
$$
\left(\sum_{\mu=0}^{2}\gamma^{\mu}\partial_{\mu}-i\begin{pmatrix}0&m\\-m&0\end{pmatrix}\right)\begin{pmatrix}\psi_1\\\psi_2\end{pmatrix}=0
$$

## Symbols
- none

## Dependencies
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)

## Related Units
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Former Parity-Anomaly Versus Lattice-No-Go Scope Gap (Closed)](../Open-Gaps/parity-anomaly-motivates-but-does-not-prove-lattice-no-go.md)
- [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)

## Step Justification
- The separated ansatz reduces the transverse dependence to an exponential factor whose exponent is fixed by the bulk mass.
- Normalizability on x_1 >= 0 forces the exponent to decay, which requires m<0.
- The remaining tangential equation is the lower-dimensional massless boundary Dirac equation.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallPrelude`
- Declaration: `boundary_dirac_mode_from_negative_bulk_mass`
- Statement kind: `lemma`

### Admissible assumptions

- Work in the continuum half-space Dirac problem with a fixed Hermitian boundary condition.
- Treat the separation ansatz as the accepted local reduction of the boundary-mode problem.

### Lean prerequisites

- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)

### Formalization blockers

- A reusable Lean-side library for boundary conditions on continuum Dirac operators is still missing.
- The relation between this half-space precursor and the folded wall problem is still narrative rather than formalized as a bridge lemma.

## Retrieval Hints
- `Use when the answer needs the lecture-one precursor that makes the later Jackiw-Rebbi wall mode feel less abrupt.`

## Outgoing Edges
- none

## Incoming Edges
- none
