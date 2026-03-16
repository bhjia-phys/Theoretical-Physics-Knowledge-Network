# Berry Curvature Two-Form

- ID: `quantity:berry-curvature-two-form`
- Type: `quantity`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
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

## Dependencies
- [Berry Connection](../Concepts/berry-connection.md)

## Related Units
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)

## Source Anchors
- `lecture-one/the-berry-connection | eqs: fc, wif | Lecture One identifies F/2pi with the first Chern class and notes dF=0 away from singularities.`

## Outgoing Edges
- none

## Incoming Edges
- [Berry Curvature](../Concepts/berry-curvature.md) -> `uses`: The curvature concept is represented by the two-form F.
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md) -> `uses`: The topological-charge formula integrates the Berry curvature two-form.

## Failure Modes
- `At singular points the form is not globally regular.`

## Formal Targets
- `aitp-l2`
- `lean`
