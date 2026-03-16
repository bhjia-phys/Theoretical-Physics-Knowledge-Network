# Lattice Weyl Nodes Sum To Zero Net Chirality

- ID: `claim:lattice-weyl-nodes-sum-to-zero-net-chirality`
- Type: `claim`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
In a lattice system with isolated Weyl nodes, the total chirality over the Brillouin zone vanishes; positive and negative nodes must balance globally.

## Scope
Lecture One theorem-level statement for Weyl-node sets.

## Regime
Lattice band theory with isolated point nodes.

## Assumptions
- `The Brillouin zone is compact.`
- `All bad points are isolated.`

## Dependencies
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)
- [Chirality Sign](../Quantities/chirality-sign.md)
- [Winding Number](../Quantities/winding-number.md)

## Related Units
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md)

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: cl | The global sum of the node charges is zero.`
- `lecture-one/the-berry-connection | eqs: nna | The same cancellation is recovered from the Berry-curvature formulation.`

## Outgoing Edges
- `derived_from` -> [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md): The claim is the direct operational statement of the theorem.

## Incoming Edges
- none

## Failure Modes
- `A local continuum Weyl cone does not imply this claim by itself.`

## Formal Targets
- `aitp-l2`
- `lean`
