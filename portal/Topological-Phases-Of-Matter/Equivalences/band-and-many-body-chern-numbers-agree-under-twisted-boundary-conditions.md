# Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions

- ID: `equivalence:band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions`
- Type: `equivalence`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
The single-particle TKNN invariant k' and the many-body twist-angle invariant \widehat{k}' are two organizations of the same Berry-curvature calculation in the gapped integer quantum Hall system.

## Scope
Witten's equivalence between the TKNN invariant and the twist-angle many-body invariant.

## Regime
Comparison between single-particle band topology and many-body adiabatic transport.

## Assumptions
- `The finite-volume ground state is obtained by filling the gapped occupied bands.`
- `Twist-angle adiabatic transport can be defined on the ground-state line bundle.`

## Representation
Equivalence between the Brillouin-zone Chern number and the twist-angle many-body Chern number.

## Source Anchors
- `lecture-two/relation-to-band-topology | eqs: zudo | The finite-volume shifted-momentum picture reorganizes the band-theory calculation.`
- `lecture-two/proof-of-the-equivalence | eqs: plizz | Witten identifies the many-body twist-angle invariant with the same integer.`
- `paper/main-result | Original microscopic invariant side of the equivalence.`

## Mathematical Content
- `kind=display` | The occupied-band invariant and the twist-angle many-body invariant agree.
$$
k' = \widehat{k}'
$$

## Symbols
- none

## Dependencies
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)

## Related Units
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `band_chern_number_eq_many_body_chern_number_under_twists`
- Statement kind: `theorem`

### Admissible assumptions

- Work in a gapped integer Hall phase where the many-body ground state is obtained by filling the occupied bands and remains nondegenerate under adiabatic twists.
- Use the determinant-line-bundle identification between filled-band data and the many-body ground-state bundle as a permitted wrapper statement.

### Lean prerequisites

- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)

### Formalization blockers

- A clean Lean-side interface between the filled-band determinant line and the many-body ground-state bundle is still missing.
- Finite-volume and thermodynamic-limit comparison lemmas are not yet separated from the wrapper equivalence statement.

## Retrieval Hints
- `Use when a query asks why the TKNN invariant can be reformulated without assuming a single-particle band description.`

## Outgoing Edges
- `supports` -> [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md): The many-body twisted-boundary equivalence closes the equality between microscopic and macroscopic invariants.

## Incoming Edges
- none
