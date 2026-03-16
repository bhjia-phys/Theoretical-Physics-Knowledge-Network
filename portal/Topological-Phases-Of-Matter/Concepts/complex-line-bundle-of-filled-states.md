# Complex Line Bundle Of Filled States

- ID: `concept:complex-line-bundle-of-filled-states`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
For a two-band system with one filled band, the occupied state at each regular momentum defines a one-dimensional complex vector space; together these fibers form the line bundle on which the Berry connection lives.

## Scope
Lecture One geometric reformulation of the occupied-state phase problem.

## Regime
Punctured regular momentum space B'.

## Assumptions
- `Exactly one band is filled in the local two-band discussion.`
- `Bad points are removed from the base space.`

## Dependencies
- none

## Related Units
- [Berry Connection](berry-connection.md)
- [Berry Curvature](berry-curvature.md)

## Source Anchors
- `lecture-one/the-berry-connection | The line-bundle picture underlies the Berry connection construction.`

## Outgoing Edges
- none

## Incoming Edges
- [Berry Connection](berry-connection.md) -> `depends_on`: The Berry connection lives on the occupied-state line bundle.

## Failure Modes
- `For multiple filled bands the geometry becomes non-abelian rather than a line bundle.`

## Formal Targets
- `aitp-l2`
- `lean`
