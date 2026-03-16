# Weyl Node

- ID: `concept:weyl-node`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
A Weyl node is an isolated three-dimensional two-band crossing whose linearized Hamiltonian is a Weyl Hamiltonian and whose local topological charge is nonzero.

## Scope
Lecture One treatment of local two-band crossings and their topological charge.

## Regime
Low-energy expansion near an isolated 3D crossing.

## Assumptions
- `The crossing is isolated in three-dimensional momentum space.`
- `A two-band local reduction is valid near the node.`

## Dependencies
- [Band Crossing](band-crossing.md)
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md)
- [Chirality Sign](../Quantities/chirality-sign.md)

## Related Units
- [Chirality Of A Weyl Node](chirality-of-weyl-node.md)
- [Berry Curvature](berry-curvature.md)
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md)
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)

## Source Anchors
- `lecture-one/three-dimensions | eqs: xpa, perd | The local 2x2 Hamiltonian determines the Weyl cone and its handedness.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md): The Weyl-node unit is part of the current Lecture One source map.
- `bridges_to` -> [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md): The local crossing picture is bridged to the Berry-flux picture.
- `depends_on` -> [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md): The local Weyl-node description is built from the 2x2 Pauli-vector Hamiltonian.
- `explains` -> [Chirality Of A Weyl Node](chirality-of-weyl-node.md): Chirality is a property of an isolated Weyl node.
- `warned_by` -> [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md): A local Weyl-node description should not be mistaken for a full lattice model.

## Incoming Edges
- [Band Crossing](band-crossing.md) -> `explains`: A Weyl node is a special isolated three-dimensional band crossing.
- [Isolated 3D Two-Band Crossings Are Weyl Nodes](../Claims/isolated-3d-two-band-crossings-are-weyl-nodes.md) -> `derived_from`: The claim is the theorem-style restatement of the Weyl-node local analysis.
- [Dirac Point In Two Dimensions](dirac-point-in-2d.md) -> `contrasts_with`: Lecture One contrasts generic 2D Dirac crossings with generic 3D Weyl crossings.
- [Fermi Arc](fermi-arc.md) -> `depends_on`: Fermi arcs are boundary signatures of bulk Weyl-node topology.
- [Nielsen-Ninomiya Theorem](nielsen-ninomiya-theorem.md) -> `depends_on`: The theorem constrains sets of Weyl nodes in a lattice band structure.
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md) -> `explains`: The Pauli-vector decomposition is the universal local language for Weyl nodes.

## Failure Modes
- `If the determinant of the linearization vanishes, the simple Weyl description can fail.`
- `Global lattice consistency is not fixed by the local cone alone.`

## Formal Targets
- `aitp-l2`
- `lean`
