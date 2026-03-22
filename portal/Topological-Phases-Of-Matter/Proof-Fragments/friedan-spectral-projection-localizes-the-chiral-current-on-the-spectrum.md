# Friedan Spectral Projection Localizes The Chiral Current On The Spectrum

- ID: `proof_fragment:friedan-spectral-projection-localizes-the-chiral-current-on-the-spectrum`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: `topological-phases/weyl-node-no-go`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Friedan rewrites the lattice no-go theorem in terms of the charge-filtered spectral projection S(p)=Theta(K(p)-p^0)P_Q(p) and an antisymmetrized trace current whose support collapses onto the spectrum and whose local form depends only on the nearby spectral projector.

## Scope
Friedan's spectral-projection reformulation of the lattice chiral current behind the Nielsen-Ninomiya theorem.

## Regime
Rigorous lattice proof route on energy-momentum space.

## Assumptions
- `The lattice Hamiltonian K(p) and the charge projector P_Q(p) vary smoothly with momentum.`
- `A generic point on the spectrum lies on a single nearby eigenvalue branch k(p) with local spectral projector P_0(p).`

## Representation
Spectral-projector current formula that makes the lattice proof local in energy-momentum space while keeping the theorem global in momentum-space topology.

## Source Anchors
- `paper/spectral-projection-chiral-current | eqs: spectral-projection-S, chiral-index-from-low-energy-current | Friedan defines the charge-filtered spectral projection and the conserved chiral current.`
- `paper/localization-near-spectrum | eqs: local-current-from-spectral-projection | Near a generic eigenvalue branch the current localizes to a delta-function spectral-projector formula.`

## Mathematical Content
- `kind=display` | `label=spectral-projection-S` | Charge-filtered spectral projection onto eigenstates whose energy is at least p^0.
$$
S(p)=\Theta\!\bigl(K(p)-p^0\bigr)P_Q(p)
$$
- `kind=display` | Projector calculus identity used to show that the chiral current vanishes away from the spectrum.
$$
\partial_\nu S = S(\partial_\nu S)(1-S) + (1-S)(\partial_\nu S)S
$$
- `kind=display` | `label=local-current-from-spectral-projection` | Local generic-branch form of Friedan's chiral current; the dimensional normalization is fixed by the Chern-character convention.
$$
j_Q^\mu(p) \propto \delta\!\bigl(k(p)-p^0\bigr)\,\epsilon^{\mu\nu_1\cdots\nu_d}(\partial_{\nu_1}k)\,\mathrm{tr}\!\bigl(P_0\,\partial_{\nu_2}P_0\cdots\partial_{\nu_d}P_0\bigr)
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `S(p)` | charge-filtered spectral projection used to define the lattice chiral current |
| `P_Q(p)` | projector onto the chosen irreducible charge sector |
| `P_0(p)` | local spectral projector onto the generic eigenvalue branch k(p) |
| `j_Q^\mu(p)` | chiral current in energy-momentum space for charge Q |

## Dependencies
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)

## Related Units
- [The Punctured Brillouin Zone Boundary Sum Vanishes](punctured-brillouin-zone-boundary-sum.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](berry-curvature-closedness-repeats-stokes-sum.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Weyl-Node No-Go Cross-Source Fusion Record](../Source-Fusion-Records/weyl-node-no-go-cross-source-fusion.md)

## Step Justification
- The charge-filtered spectral projection packages the lattice Hamiltonian and internal symmetry sector into one projector-valued object on energy-momentum space.
- Projector calculus forces every antisymmetrized trace term to contain S(1-S), so the current vanishes wherever S is smooth, namely away from the spectrum.
- Near a generic spectral branch the current collapses to a delta-function expression controlled only by the local spectral projector P_0 and the branch derivative \partial k.

## Retrieval Hints
- `Use when an answer must explain the rigorous cited-paper route rather than only Witten's punctured-zone Stokes sketch.`

## Outgoing Edges
- none

## Incoming Edges
- none
