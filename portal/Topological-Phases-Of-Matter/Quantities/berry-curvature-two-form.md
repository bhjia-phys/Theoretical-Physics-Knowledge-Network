# Berry Curvature Two-Form

- ID: `quantity:berry-curvature-two-form`
- Type: `quantity`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
The Berry curvature two-form F is the gauge-invariant curvature of the Berry connection and integrates to the first Chern number on closed surfaces.

## Scope
Lecture One curvature two-form of the occupied-state line bundle.

## Regime
Regular momentum-space region or parameter-space surface.

## Assumptions
- `The relevant band bundle is smooth on the domain.`

## Representation
Gauge-invariant curvature two-form associated with Berry transport.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: fc, wif | Lecture One identifies F/2pi with the first Chern class and notes dF=0 away from singularities.`

## Mathematical Content
- Definition of the Berry-curvature two-form in the abelian rank-one case.
$$
F = \mathrm dA
$$
- `label=fc` | The integral over a closed surface Sigma measures the first Chern number of the occupied-state line bundle restricted to Sigma.
$$
\int_{\Sigma} \frac{F}{2\pi} = c_1(\mathcal L|_{\Sigma})
$$
- `label=wif` | Closedness of the curvature away from singular sources.
$$
\mathrm dF = 0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `F` | Berry-curvature two-form |
| `A` | Berry connection one-form |
| `\Sigma` | closed oriented surface in parameter or momentum space |
| `\mathcal L` | occupied-state line bundle |

## Dependencies
- [Berry Connection](../Concepts/berry-connection.md)

## Related Units
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)

## Failure Modes
- `At singular points the form is not globally regular.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks for the geometric meaning of Berry curvature.`

## Outgoing Edges
- none

## Incoming Edges
- [Berry Curvature](../Concepts/berry-curvature.md) -> `uses`: The curvature concept is represented by the two-form F.
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md) -> `uses`: The topological-charge formula integrates the Berry curvature two-form.
