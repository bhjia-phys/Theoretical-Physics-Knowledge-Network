# Berry Connection

- ID: `concept:berry-connection`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
The Berry connection is the U(1) connection on the line bundle of occupied states over regular momentum space, encoding phase transport of eigenstates along paths.

## Scope
Lecture One U(1) Berry connection for a two-band problem with one filled state.

## Regime
Adiabatic geometry of a gapped band subspace away from bad points.

## Assumptions
- `The occupied state is isolated from the empty state over the region of interest.`
- `A smooth local phase choice exists away from singularities.`

## Dependencies
- [Complex Line Bundle Of Filled States](complex-line-bundle-of-filled-states.md)

## Related Units
- [Berry Curvature](berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zb | Parallel transport of phase is the defining geometric picture.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md): The Berry-connection unit is part of the current Lecture One source map.
- `depends_on` -> [Complex Line Bundle Of Filled States](complex-line-bundle-of-filled-states.md): The Berry connection lives on the occupied-state line bundle.

## Incoming Edges
- [Berry Curvature](berry-curvature.md) -> `depends_on`: Curvature is defined from the connection.

## Failure Modes
- `At bad points the bundle is singular and the U(1) connection is not globally defined.`

## Formal Targets
- `aitp-l2`
- `lean`
