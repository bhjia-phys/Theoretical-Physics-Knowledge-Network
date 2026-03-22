# Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary

- ID: `proof_fragment:friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: `topological-phases/weyl-node-no-go`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Friedan identifies the lattice chiral index with the Chern number of the spectral bundle W over the boundary of the punctured Brillouin zone; because that boundary bounds a compact manifold, cobordism invariance forces the total chiral index to vanish.

## Scope
Friedan's Chern-character and cobordism interpretation of the total lattice chiral index.

## Regime
Characteristic-class formulation of the lattice no-go theorem.

## Assumptions
- `Zero energy occurs only at isolated Fermi points so the punctured Brillouin zone has a boundary made of small surrounding spheres.`
- `The occupied spectral subspaces form a finite-rank bundle W over the punctured Brillouin zone.`

## Representation
Characteristic-class proof fragment turning the lattice chiral index into a boundary Chern number that must vanish.

## Source Anchors
- `paper/spectral-projection-chiral-current | eqs: chiral-index-from-low-energy-current | The low-energy chiral index is the total charge of Friedan's chiral current at p^0=0.`
- `paper/chern-character-and-cobordism | eqs: spectral-bundle-curvature, cobordism-chern-number-zero | The current is reinterpreted as the top Chern character of the spectral bundle W, and the theorem becomes cobordism invariance of that Chern number.`

## Mathematical Content
- `kind=display` | `label=chiral-index-from-low-energy-current` | The lattice chiral index is the total low-energy chiral charge.
$$
I_Q = \int \mathrm d^d p\, j_Q^0(0,p)
$$
- `kind=display` | `label=spectral-bundle-curvature` | Natural covariant derivative and curvature on the spectral bundle W determined by the projector S.
$$
D = S(\mathrm d - \mathrm dS), \qquad \Omega = S(\mathrm dS\,\mathrm dS)
$$
- `kind=display` | `label=cobordism-chern-number-zero` | The boundary Chern number of the spectral bundle vanishes because \partial M bounds the punctured Brillouin-zone manifold M.
$$
I_Q = \int_{\partial M} n_\mu F_Q^{0\mu} = 0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `I_Q` | total chiral index in charge sector Q |
| `W` | spectral bundle formed by the range of S(0,p) over the punctured Brillouin zone |
| `D` | natural covariant derivative on the spectral bundle |
| `\Omega` | curvature two-form of the spectral bundle |

## Dependencies
- [Friedan Spectral Projection Localizes The Chiral Current On The Spectrum](friedan-spectral-projection-localizes-the-chiral-current-on-the-spectrum.md)

## Related Units
- [The Punctured Brillouin Zone Boundary Sum Vanishes](punctured-brillouin-zone-boundary-sum.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)

## Step Justification
- At zero energy the current measures the net right-minus-left chiral content of the low-energy lattice spectrum.
- Removing small balls around the isolated Fermi points leaves a manifold M with boundary \partial M equal to the union of enclosing spheres.
- The current is the dual of the top Chern character of the spectral bundle W on M, so the total chiral index becomes a boundary Chern number.
- Cobordism invariance of the Chern number forces any such boundary contribution to vanish, yielding the lattice no-go theorem.

## Retrieval Hints
- `Use when an answer must explain why Friedan's proof is stronger than a bare Stokes sketch: it identifies the theorem as a characteristic-class and cobordism statement.`

## Outgoing Edges
- none

## Incoming Edges
- none
