# Winding Number

- ID: `quantity:winding-number`
- Type: `quantity`
- Domain: `topological-phases-of-matter`
- Subdomain: `topological-charge`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
The winding number is the integer degree assigned to an isolated bad point by the normalized map from an enclosing sphere in momentum space to the target sphere.

## Scope
Lecture One point-node charge in degree and Berry-flux language.

## Regime
Topological classification of isolated point nodes.

## Assumptions
- `The enclosing surface avoids other singularities.`

## Dependencies
- none

## Related Units
- [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: wn, nwn, wnn | The same integer appears as a degree and as a flux.`

## Outgoing Edges
- none

## Incoming Edges
- [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md) -> `uses`: The equation defines the winding number as a degree.

## Failure Modes
- `If the enclosed region contains multiple nodes, the value is only the total charge.`

## Formal Targets
- `aitp-l2`
- `lean`
