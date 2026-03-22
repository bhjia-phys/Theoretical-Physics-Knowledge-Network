# Pullback Of The Area Form Represents The Local Degree

- ID: `proof_fragment:pullback-area-form-represents-local-degree`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `topological-charge`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
The local charge of an isolated node is the degree of the normalized map from a small sphere in momentum space to the target sphere, computed by pulling back the normalized area form.

## Scope
Local proof fragment that identifies the charge with a pullback integral.

## Regime
Degree-theoretic description of an isolated point node.

## Assumptions
- `The enclosing sphere does not intersect any other bad point.`
- `The normalized map is well-defined on the sphere.`

## Representation
Local degree formula for the charge of an isolated node.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: wnn, weta | Witten's charge formula is the degree of the normalized map to the target two-sphere.`

## Mathematical Content
- `kind=display` | `label=wnn` | Charge as the degree of the normalized map \widehat b.
$$
w_\alpha = \int_{S^2_\alpha} \widehat b^{\,*}(\eta)
$$
- `kind=display` | `label=weta` | Closedness of the normalized area form on the target sphere.
$$
\mathrm d\eta = 0
$$

## Symbols
- none

## Dependencies
- [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md)
- [Winding Number](../Quantities/winding-number.md)

## Related Units
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [The Punctured Brillouin Zone Boundary Sum Vanishes](punctured-brillouin-zone-boundary-sum.md)

## Step Justification
- Normalizing the Pauli-vector coefficients defines a map from the enclosing sphere to S^2.
- The pullback of the normalized area form measures how many times the domain sphere wraps the target sphere.
- This integer is the local charge of the bad point.

## Retrieval Hints
- `Use when a proof must move from the local Weyl cone to the degree-theoretic notion of charge.`

## Outgoing Edges
- `supports` -> [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md): The local degree formula supplies the local charge notion used in the theorem.

## Incoming Edges
- none
