# Berry Flux Equals Topological Charge

- ID: `equation:berry-flux-topological-charge`
- Type: `equation`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
For an isolated bad point, the integral of Berry curvature over a small surrounding sphere equals the integer topological charge of the node.

## Scope
Lecture One Berry-curvature restatement of node charge.

## Regime
Abelian Berry geometry of an isolated node.

## Assumptions
- `The Berry connection is defined on the punctured sphere around the node.`

## Representation
Surface-flux formula for node charge in terms of Berry curvature.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zif, wif, nna | The flux formula and dF=0 turn local geometry into a global sum rule.`

## Mathematical Content
- `label=zif` | Berry-flux formula for the local node charge.
$$
w_\alpha = \int_{S^2_\alpha}\frac{F}{2\pi}
$$
- `label=wif` | Berry curvature is closed away from the bad points.
$$
\mathrm dF = 0
$$
- `label=nna` | Global charge-cancellation law obtained by summing the local fluxes on a compact punctured Brillouin zone.
$$
\sum_{\alpha}\int_{S^2_\alpha}\frac{F}{2\pi}=0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `F` | Berry curvature two-form |
| `S^2_\alpha` | small sphere surrounding the isolated node labeled by alpha |
| `w_\alpha` | integer charge of the bad point |

## Dependencies
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)
- [Winding Number](../Quantities/winding-number.md)

## Related Units
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md)
- [Berry Flux Gives Node Charge](../Derivations/berry-flux-gives-node-charge.md)
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Failure Modes
- `The simple abelian formula changes when multiple occupied bands require a non-abelian treatment.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when translating geometric Berry data into topological charge.`

## Outgoing Edges
- `explains` -> [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md): Berry flux supplies the same sign and integer data as local chirality.
- `uses` -> [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md): The topological-charge formula integrates the Berry curvature two-form.

## Incoming Edges
- [Berry-Flux Diagnosis Of Node Charge](../Methods/berry-flux-diagnosis-of-node-charge.md) -> `uses`: The diagnostic method is the operational use of the flux formula.
