# Parity Anomaly Half Level From Massive Dirac Fermion

- ID: `proof_fragment:parity-anomaly-half-level-from-massive-dirac-fermion`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
A gapped 2+1-dimensional Dirac fermion induces the half-integer Chern-Simons term (sign m)/2 times I_CS; in the current KB this umbrella fragment is now factored through an explicit hemisphere-Berry-flux subfragment and a theorem-level half-level response statement.

## Scope
Continuum proof fragment that motivates the edge-mode consistency story in Witten Lecture Three.

## Regime
Continuum 2+1-dimensional parity-anomaly analysis.

## Assumptions
- `The bulk Dirac fermion is massive and can be integrated out.`
- `The resulting topological term is interpreted modulo the gauge-invariance obstruction of the half level.`

## Representation
Continuum Berry-flux argument for the half-integer Chern-Simons level of a massive Dirac fermion.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: uftof, puft, PPP, quft | Witten's Berry-flux derivation of the half-level parity anomaly.`
- `paper/main-result | Haldane's lattice realization is explicitly cited by Witten as the condensed-matter parity-anomaly model.`

## Mathematical Content
- `kind=display` | `label=uftof` | Half-level Chern-Simons term induced by integrating out one massive Dirac fermion.
$$
\frac{\operatorname{sign}m}{2}\,\mathcal I_{\mathrm{CS}}(A)
$$
- `kind=display` | `label=puft` | Massive Dirac Hamiltonian whose normalized vector gives the Berry map.
$$
H = \sigma_x p_x + \sigma_y p_y + m\sigma_z
$$
- `kind=display` | `label=PPP` | Momentum-space map to a hemisphere with degree sign(m)/2.
$$
(p_x,p_y) \mapsto \left(\frac{p_x}{\sqrt{p_x^2+p_y^2+m^2}},\frac{p_y}{\sqrt{p_x^2+p_y^2+m^2}},\frac{m}{\sqrt{p_x^2+p_y^2+m^2}}\right)
$$
- `kind=display` | `label=quft` | Doubling with opposite masses removes the half-level anomaly.
$$
\frac{1}{2}(\operatorname{sign}m + \operatorname{sign}(-m)) = 0
$$

## Symbols
- none

## Dependencies
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md)
- [Hemisphere Berry Flux Of A Massive Dirac Hamiltonian Gives Half A Chern Number](hemisphere-berry-flux-of-massive-dirac-hamiltonian-gives-half-chern-number.md)
- [A Massive Two Plus One Dimensional Dirac Fermion Induces A Half-Level Chern-Simons Term](../Theorems/half-level-cs-term-from-massive-dirac-fermion.md)

## Related Units
- [A Massive Two Plus One Dimensional Dirac Fermion Induces A Half-Level Chern-Simons Term](../Theorems/half-level-cs-term-from-massive-dirac-fermion.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Former Parity-Anomaly Versus Lattice-No-Go Scope Gap (Closed)](../Open-Gaps/parity-anomaly-motivates-but-does-not-prove-lattice-no-go.md)

## Step Justification
- The normalized Dirac vector covers only one hemisphere of the target two-sphere.
- Therefore its Berry-flux degree is one half of the integer map obtained from a full sphere.
- A second fermion with opposite mass contributes the opposite half level and restores a gauge-invariant integer total.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `parity_anomaly_half_level_from_massive_dirac_fermion`
- Statement kind: `lemma`

### Admissible assumptions

- Work with the continuum massive Dirac Hamiltonian and its occupied-band Berry map.
- Use the hemisphere-degree argument as the accepted local route to the one-half coefficient.

### Lean prerequisites

- [A Massive Two Plus One Dimensional Dirac Fermion Induces A Half-Level Chern-Simons Term](../Theorems/half-level-cs-term-from-massive-dirac-fermion.md)

### Formalization blockers

- The link between hemisphere Berry flux and the parity-odd effective action is still encoded as a physics wrapper rather than a lower-level formal theorem.
- The doubled cancellation statement has not yet been isolated as its own reusable Lean lemma.

## Retrieval Hints
- `Use when a query asks for the continuum parity-anomaly ingredient of the edge-mode story, but not when a lattice no-go proof is required.`

## Outgoing Edges
- `motivates` -> [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md): The half-level parity anomaly explains why the boundary mode must appear in the consistent doubled system.

## Incoming Edges
- none
