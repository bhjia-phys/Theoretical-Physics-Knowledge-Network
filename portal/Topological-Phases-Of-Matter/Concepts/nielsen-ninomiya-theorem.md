# Nielsen-Ninomiya Theorem

- ID: `concept:nielsen-ninomiya-theorem`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
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

## Dependencies
- [Weyl Node](weyl-node.md)
- [Winding Number](../Quantities/winding-number.md)
- [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md)

## Related Units
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md)

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: nwn, wnn, cl | The sum rule is proved by degree theory and Stokes's theorem.`
- `lecture-one/the-berry-connection | eqs: nna | The same theorem is recovered from Berry curvature.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md): The Nielsen-Ninomiya unit is part of the current Lecture One source map.
- `depends_on` -> [Stokes's Theorem Implies Net Zero Charge](../Derivations/stokes-theorem-implies-net-zero-charge.md): The current exemplar theorem entry is supported by the Stokes-theorem derivation.
- `depends_on` -> [Weyl Node](weyl-node.md): The theorem constrains sets of Weyl nodes in a lattice band structure.

## Incoming Edges
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md) -> `motivates`: Continuum anomaly intuition motivates the lattice no-go theorem.
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md) -> `derived_from`: The claim is the direct operational statement of the theorem.

## Failure Modes
- `The simple statement changes for non-isolated crossings or for continuum models without lattice compactness.`

## Formal Targets
- `aitp-l2`
- `lean`
