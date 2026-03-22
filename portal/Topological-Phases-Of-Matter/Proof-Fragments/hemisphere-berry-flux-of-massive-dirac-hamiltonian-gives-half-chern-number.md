# Hemisphere Berry Flux Of A Massive Dirac Hamiltonian Gives Half A Chern Number

- ID: `proof_fragment:hemisphere-berry-flux-of-massive-dirac-hamiltonian-gives-half-chern-number`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `parity-anomaly`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
For H=p_x sigma_x + p_y sigma_y + m sigma_z, the normalized Bloch vector covers only one hemisphere of S^2, so the occupied-band Berry flux is sign(m)/2 rather than an integer.

## Scope
Geometric substep behind the parity-anomaly half level and the Haldane lattice bridge.

## Regime
Continuum 2+1-dimensional Dirac cone viewed through Berry geometry.

## Assumptions
- `The occupied band is the negative-energy band of a single continuum massive Dirac cone.`
- `Momentum space is compactified by the point at infinity.`

## Representation
Geometric Berry-flux fragment extracting one half of a Chern number from a single massive Dirac cone.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: puft, PPP | Witten's hemisphere map explanation of the half-level parity-anomaly contribution.`
- `paper/main-result | The lattice completion of this half-integer continuum contribution is the condensed-matter motivation for the Haldane model.`

## Mathematical Content
- `kind=display` | Normalized Bloch vector of the massive Dirac Hamiltonian.
$$
\hat n(p)=\frac{(p_x,p_y,m)}{\sqrt{p_x^2+p_y^2+m^2}}
$$
- `kind=display` | Berry curvature of the occupied Dirac band.
$$
\mathcal F_{p_xp_y}=\frac{1}{2}\hat n\cdot\left(\partial_{p_x}\hat n\times\partial_{p_y}\hat n\right)=\frac{m}{2(p_x^2+p_y^2+m^2)^{3/2}}
$$
- `kind=display` | Half-integer Berry flux from the hemisphere image.
$$
\frac{1}{2\pi}\int_{\mathbb R^2}\mathcal F_{p_xp_y}\,\mathrm d p_x\,\mathrm d p_y=\frac{1}{2}\operatorname{sign}(m)
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `\hat n` | normalized Bloch vector of the two-band Dirac Hamiltonian |
| `\mathcal F` | Berry curvature of the occupied Dirac band |

## Dependencies
- [Berry Curvature](../Concepts/berry-curvature.md)

## Related Units
- [Parity Anomaly Half Level From Massive Dirac Fermion](parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [A Massive Two Plus One Dimensional Dirac Fermion Induces A Half-Level Chern-Simons Term](../Theorems/half-level-cs-term-from-massive-dirac-fermion.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)

## Step Justification
- The compactified momentum plane maps to only one hemisphere because the sign of m fixes the north-versus-south choice at the origin while infinity lands on the equator.
- The Berry-curvature integral equals the solid angle swept by the normalized Bloch vector.
- A single hemisphere contributes exactly half of the full sphere degree.

## Failure Modes
- `A full lattice model cannot stop at the half-integer result; ultraviolet completion must restore an integer total Chern number.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks where the factor of one half comes from geometrically in the parity-anomaly argument.`

## Outgoing Edges
- none

## Incoming Edges
- none
