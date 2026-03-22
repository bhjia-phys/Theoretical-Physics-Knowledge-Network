# Berry Curvature Closedness Repeats The Same Stokes Sum

- ID: `proof_fragment:berry-curvature-closedness-repeats-stokes-sum`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Away from the singular points, the Berry curvature is closed; applying Stokes's theorem on the punctured Brillouin zone gives the same zero-sum law as the degree-theory proof.

## Scope
Lecture One proof fragment that recovers Nielsen-Ninomiya from Berry curvature.

## Regime
Berry-geometric proof on the punctured Brillouin zone.

## Assumptions
- `The Berry connection is defined away from the bad points.`
- `The node set is isolated so the punctured Brillouin zone is smooth.`

## Representation
Berry-curvature proof fragment paralleling the degree-theory Stokes argument.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: wif, nna | Witten rederives the same global sum rule from dF=0 away from the bad points.`

## Mathematical Content
- `kind=display` | `label=wif` | Berry curvature is closed away from the singular locus.
$$
\mathrm dF = 0
$$
- `kind=display` | `label=nna` | The Berry-curvature boundary sum reproduces charge cancellation.
$$
0 = \int_{\mathcal B'} \mathrm d\!\left(\frac{F}{2\pi}\right) = \sum_\alpha \int_{S^2_\alpha}\frac{F}{2\pi}
$$

## Symbols
- none

## Dependencies
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)

## Related Units
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md)

## Step Justification
- Closedness of F away from bad points makes the punctured-zone bulk integral vanish.
- The boundary spheres around the bad points capture the Berry-flux charges.
- Summing those boundary integrals gives the zero-total-charge statement.

## Retrieval Hints
- `Use when a derivation answer must give the Berry-curvature route to Nielsen-Ninomiya.`

## Outgoing Edges
- `supports` -> [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md): The Berry-curvature route independently supports the same theorem.

## Incoming Edges
- [Explain The Berry-Flux Version Of The Node Charge](../Regression-Questions/explain-berry-flux-version-of-node-charge.md) -> `tests`: The regression question tests the Berry-curvature route to the charge and zero-sum law.
