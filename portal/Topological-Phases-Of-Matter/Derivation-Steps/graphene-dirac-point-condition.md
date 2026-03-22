# Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0

- ID: `derivation_step:graphene-dirac-point-condition`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `haldane-model`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
The graphene band crossings occur exactly when the off-diagonal entry of the nearest-neighbor Hamiltonian vanishes, so 1+e^{i alpha}+e^{i beta}=0 and the two symmetry-related Dirac points follow immediately.

## Scope
Reusable derivation step that locates the two graphene Dirac points used in the Haldane bridge.

## Regime
Honeycomb-lattice Dirac-point analysis prior to the Haldane perturbation.

## Assumptions
- `The starting point is the nearest-neighbor graphene Hamiltonian with no symmetry-breaking mass terms.`
- `Band crossings are identified by the vanishing of the determinant of the traceless two-band Hamiltonian.`

## Representation
Ordered lattice derivation step locating the two graphene Dirac points.

## Source Anchors
- `lecture-three/haldanes-model-of-graphene | eqs: theq, omeq | Witten's explicit solution of the graphene band-touching condition.`

## Mathematical Content
- `kind=display` | `label=theq` | Condition for the off-diagonal entry of the graphene Hamiltonian to vanish.
$$
1+e^{i\alpha}+e^{i\beta}=0
$$
- `kind=display` | `label=omeq` | The two symmetry-related solutions locating the Dirac points.
$$
e^{i\alpha}=\frac{1}{2}\left(-1\pm\sqrt{-3}\right)=e^{-i\beta}
$$

## Symbols
- none

## Dependencies
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)

## Related Units
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Lecture Two TKNN / Haldane Archival Enrichment Remains To Be Curated](../Open-Gaps/lecture-two-tknn-equivalence-proof-not-yet-curated.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)

## Step Inputs
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)

## Step Justification
- For a traceless two-band Hamiltonian, a band crossing occurs exactly when the off-diagonal hopping amplitude vanishes.
- Setting 1+e^{i alpha}+e^{i beta} to zero gives a quadratic equation for e^{i alpha}.
- The two resulting roots are exchanged by the honeycomb lattice symmetries and define the two Dirac points.

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when the Haldane bridge needs the explicit derivation of where the graphene Dirac cones sit.`

## Outgoing Edges
- none

## Incoming Edges
- none
