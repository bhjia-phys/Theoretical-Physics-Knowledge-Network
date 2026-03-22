# The Punctured Brillouin Zone Boundary Sum Vanishes

- ID: `proof_fragment:punctured-brillouin-zone-boundary-sum`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Excise small balls around all bad points, integrate the exterior derivative of the pulled-back closed form over the punctured Brillouin zone, and use Stokes's theorem to obtain the vanishing total charge.

## Scope
Core proof fragment in the degree-theoretic derivation of Nielsen-Ninomiya.

## Regime
Global topological analysis on the punctured Brillouin zone.

## Assumptions
- `The Brillouin zone is compact.`
- `The set of bad points is finite and isolated.`

## Representation
Global Stokes-theorem step on the punctured Brillouin zone.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: cl | Stokes's theorem turns the punctured-zone boundary integral into the vanishing sum over node charges.`

## Mathematical Content
- `kind=display` | `label=cl` | Charge cancellation from a closed form and the boundary of the punctured Brillouin zone.
$$
0 = \int_{\mathcal B'} \mathrm d\,\widehat b^{\,*}(\eta) = \sum_\alpha \int_{S^2_\alpha}\widehat b^{\,*}(\eta) = \sum_\alpha w_\alpha
$$

## Symbols
- none

## Dependencies
- [Pullback Of The Area Form Represents The Local Degree](pullback-area-form-represents-local-degree.md)
- [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md)

## Related Units
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md)

## Step Justification
- The punctured Brillouin zone has boundary equal to the union of small spheres around the bad points.
- The pulled-back area form is closed away from the bad points.
- Stokes's theorem converts the bulk integral of an exact form to the boundary sum of local charges.

## Retrieval Hints
- `Use when a proof must show the precise Stokes step behind the lattice charge-cancellation theorem.`

## Outgoing Edges
- `supports` -> [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md): The punctured-zone Stokes argument proves the global zero-sum law.

## Incoming Edges
- none
