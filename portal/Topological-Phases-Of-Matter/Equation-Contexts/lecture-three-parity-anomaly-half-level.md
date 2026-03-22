# Lecture Three Parity-Anomaly Half-Level Context

- ID: `equation_context:lecture-three-parity-anomaly-half-level`
- Type: `equation_context`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This equation context records Witten's continuum derivation that one massive 2+1-dimensional Dirac fermion induces a half-level Chern-Simons term, while a doubled pair with opposite masses restores an integer-gauge-invariant total.

## Scope
Equation-level context for the parity-anomaly part of the Lecture Three theorem family.

## Regime
Continuum parity-anomaly discussion in 2+1 dimensions.

## Assumptions
- `The massive Dirac fermion can be integrated out at low energies.`
- `The normalized momentum-space map controls the induced Chern-Simons term.`

## Representation
Equation context for the half-level parity anomaly and its cancellation by doubling.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: uftof, puft, PPP, quft | Witten's continuum derivation of the half-level and its doubling cancellation.`

## Mathematical Content
- `kind=display` | `label=uftof` | Effective Chern-Simons term induced by one massive Dirac fermion.
$$
\frac{\operatorname{sign}m}{2}\,\mathcal I_{\mathrm{CS}}(A)
$$
- `kind=display` | `label=puft` | Massive Dirac Hamiltonian used in the Berry-flux argument.
$$
H = \sigma_x p_x + \sigma_y p_y + m\sigma_z
$$
- `kind=display` | `label=PPP` | Momentum-space map to a hemisphere, giving half a degree.
$$
(p_x,p_y) \mapsto \left(\frac{p_x}{\sqrt{p_x^2+p_y^2+m^2}},\frac{p_y}{\sqrt{p_x^2+p_y^2+m^2}},\frac{m}{\sqrt{p_x^2+p_y^2+m^2}}\right)
$$
- `kind=display` | `label=quft` | Two opposite masses cancel the half-level anomaly.
$$
\frac{1}{2}(\operatorname{sign}m+\operatorname{sign}(-m))=0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `m` | Dirac mass whose sign determines the induced half level |

## Dependencies
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md)

## Related Units
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Single Massive Dirac Fermion Induces Half Level](../Proof-Obligations/single-massive-dirac-fermion-induces-half-level.md)
- [Doubling Cancels Parity Anomaly Before Boundary Sign Flip](../Proof-Obligations/doubling-cancels-parity-anomaly-before-boundary-sign-flip.md)

## Retrieval Hints
- `Open this when an answer must explain the half-level carefully rather than only invoking 'parity anomaly'.`

## Outgoing Edges
- none

## Incoming Edges
- none
