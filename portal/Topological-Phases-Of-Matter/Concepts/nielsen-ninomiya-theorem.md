# Nielsen-Ninomiya Theorem

- ID: `concept:nielsen-ninomiya-theorem`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
For a lattice band structure with isolated Weyl crossings, the sum of all node charges over the Brillouin zone is zero, forbidding a net chirality in a strictly lattice-regularized system.

## Scope
Lecture One topological and Berry-curvature derivations of chirality cancellation.

## Regime
Lattice band theory with isolated point nodes.

## Assumptions
- `The Brillouin zone is compact.`
- `Only finitely many isolated bad points occur.`

## Representation
Global topological constraint on a lattice node set.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: nwn, wnn, cl | The sum rule is proved by degree theory and Stokes's theorem.`
- `lecture-one/the-berry-connection | eqs: nna | The same theorem is recovered from Berry curvature.`

## Mathematical Content
- `kind=display` | `label=cl` | Degree-theoretic form of the theorem.
$$
\sum_{\alpha} w_\alpha = 0
$$
- `kind=display` | `label=nna` | Berry-curvature form of the theorem.
$$
\sum_{\alpha}\int_{S^2_\alpha}\frac{F}{2\pi}=0
$$

## Symbols
- none

## Dependencies
- [Weyl Node](weyl-node.md)
- [Winding Number](../Quantities/winding-number.md)
- [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Related Units
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md)
- [Former Friedan-Level Nielsen-Ninomiya Source Gap (Recovered)](../Open-Gaps/friedan-level-rigorous-nielsen-ninomiya-proof-not-yet-ingested.md)

## Failure Modes
- `The simple statement changes for non-isolated crossings or for continuum models without lattice compactness.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use for chirality cancellation, fermion doubling, and lattice no-go queries.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md): The Nielsen-Ninomiya unit is part of the current Lecture One source map.
- `depends_on` -> [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md): The current exemplar theorem entry is supported by the Stokes-theorem derivation.
- `depends_on` -> [Weyl Node](weyl-node.md): The theorem constrains sets of Weyl nodes in a lattice band structure.

## Incoming Edges
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md) -> `motivates`: Continuum anomaly intuition motivates the lattice no-go theorem.
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md) -> `derived_from`: The claim is the direct operational statement of the theorem.
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md) -> `explains`: The theorem unit provides the formal statement underlying the concept note.
