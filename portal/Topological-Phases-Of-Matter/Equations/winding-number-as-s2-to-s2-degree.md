# Winding Number As The Degree Of S2 To S2

- ID: `equation:winding-number-as-s2-to-s2-degree`
- Type: `equation`
- Domain: `topological-phases-of-matter`
- Subdomain: `topological-charge`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
The topological charge of an isolated bad point is the degree of the map from a small enclosing sphere in momentum space to the target sphere of normalized b-vectors.

## Scope
Lecture One degree-theory formulation of Weyl-node charge.

## Regime
Topological classification of isolated point nodes.

## Assumptions
- `The crossing is isolated.`
- `The enclosing sphere does not intersect any other bad point.`

## Representation
Integral formula for the degree of the normalized b-map.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: nwn, wnn | The integer is presented both as an integral density and as the pullback degree.`

## Mathematical Content
- `kind=display` | `label=wnn` | Charge as the degree of the normalized map.
$$
w_\alpha = \int_{S^2_\alpha}\widehat b^{\,*}(\eta)
$$
- `kind=display` | `label=weta` | Closed normalized area form on the target sphere.
$$
\mathrm d\eta = 0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `w(S)` | winding number on the enclosing sphere |
| `n` | normalized vector b/|b| |

## Dependencies
- [Winding Number](../Quantities/winding-number.md)
- [Two-Band Hamiltonian A Plus B Dot Sigma](two-band-hamiltonian-d-dot-sigma.md)

## Related Units
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)
- [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md)

## Failure Modes
- `If the sphere encloses multiple nodes, the integral returns the total charge rather than a single-node charge.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use for topological-charge calculations around a Weyl node.`

## Outgoing Edges
- `uses` -> [Winding Number](../Quantities/winding-number.md): The equation defines the winding number as a degree.

## Incoming Edges
- [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md) -> `derived_from`: The Stokes-theorem derivation uses the degree formulation of node charge.
