# Stokes's Theorem Implies Net Zero Charge

- ID: `derivation:stokes-theorem-implies-net-zero-charge`
- Type: `derivation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Because the relevant form is closed on the punctured Brillouin zone, integrating its exterior derivative over the punctured region and applying Stokes's theorem yields that the sum of boundary charges around all bad points is zero.

## Scope
Lecture One degree-theoretic and Berry-curvature proofs of chirality cancellation.

## Regime
Global topological analysis on the punctured Brillouin zone.

## Assumptions
- `The Brillouin zone is compact.`
- `Bad points are isolated and excised to form the punctured region.`

## Dependencies
- [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)

## Related Units
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: weta, wnn, cl | The theorem is derived from a closed form on the punctured Brillouin zone.`
- `lecture-one/the-berry-connection | eqs: wif, nna | The Berry-curvature proof has the same Stokes structure.`

## Outgoing Edges
- `derived_from` -> [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md): The Stokes-theorem derivation uses the degree formulation of node charge.

## Incoming Edges
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md) -> `depends_on`: The current exemplar theorem entry is supported by the Stokes-theorem derivation.

## Failure Modes
- `The simple derivation must be reformulated for non-isolated node sets.`

## Formal Targets
- `aitp-l2`
- `lean`
