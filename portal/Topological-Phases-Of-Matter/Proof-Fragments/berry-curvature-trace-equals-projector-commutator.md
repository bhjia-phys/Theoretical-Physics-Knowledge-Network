# Berry-Curvature Trace Equals Projector Commutator

- ID: `proof_fragment:berry-curvature-trace-equals-projector-commutator`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
For a smooth occupied-state frame U and projector P = U U dagger, the traced Berry curvature satisfies Tr F_12 = i Tr(P[partial_1 P, partial_2 P]), giving the local identity behind the TKNN projector formula.

## Scope
Archival TKNN bridge between Berry-connection notation and the occupied-projector integrand.

## Regime
Local differential-geometric rewrite inside the TKNN band invariant.

## Assumptions
- `A smooth local orthonormal occupied-state frame exists on the patch under discussion.`
- `The occupied projector has constant rank on the patch.`

## Representation
Local TKNN identity making the projector commutator and the traced Berry curvature interchangeable.

## Source Anchors
- `paper/projector-curvature-identity | eqs: occupied-bundle-curvature-form | Archival geometric identity linking the Hall-conductance integrand to occupied-bundle curvature.`
- `lecture-two/relation-to-band-topology | Witten states the Hall integer as the first Chern class of the filled-band bundle.`

## Mathematical Content
- `kind=display` | Occupied frame and projector on a local patch.
$$
U^{\dagger}U=\mathbf{1},\qquad P=UU^{\dagger}
$$
- `kind=display` | Berry connection and curvature in a local occupied frame.
$$
\mathcal{A}=U^{\dagger}\,\mathrm{d}U,\qquad \mathcal{F}=\mathrm{d}\mathcal{A}+\mathcal{A}\wedge\mathcal{A}=\mathrm{d}U^{\dagger}(\mathbf{1}-P)\wedge \mathrm{d}U
$$
- `kind=display` | Identity relating the traced curvature density to the projector commutator.
$$
\operatorname{Tr}\mathcal{F}= i\,\operatorname{Tr}(P\,\mathrm{d}P\wedge \mathrm{d}P)= i\,\operatorname{Tr}\!\left(P[\partial_{p_1}P,\partial_{p_2}P]\right)\,\mathrm{d}p_1\wedge \mathrm{d}p_2
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `U` | matrix whose columns are a local orthonormal occupied-state frame |
| `P` | occupied-band projector UU dagger |
| `\mathcal{F}` | non-abelian Berry-curvature two-form of the occupied bundle |

## Dependencies
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry Connection](../Concepts/berry-connection.md)
- [Berry Curvature](../Concepts/berry-curvature.md)

## Related Units
- [Projector Formula For The TKNN Chern Number](projector-formula-for-the-tknn-chern-number.md)
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)

## Step Justification
- Differentiate U dagger U equals 1 to relate dU dagger U and U dagger dU.
- Use P = UU dagger and P squared equals P to rewrite dP in terms of transitions between occupied and empty subspaces.
- Expand Tr F in the local frame and collapse the result to i Tr(P dP wedge dP).

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `berry_curvature_trace_eq_projector_commutator`
- Statement kind: `lemma`

### Admissible assumptions

- Work on a smooth local patch with a finite-rank occupied subbundle and a local orthonormal frame U.
- Use standard matrix-valued differential-form identities instead of rederiving them from first principles in this lemma.

### Lean prerequisites

- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry Connection](../Concepts/berry-connection.md)
- [Berry Curvature](../Concepts/berry-curvature.md)

### Formalization blockers

- The Lean-side interface for matrix-valued differential forms and wedge-product trace identities is still missing.
- The passage between local frame notation U and the abstract occupied bundle is not yet packaged as a reusable formal equivalence.

## Retrieval Hints
- `Use when a derivation must show exactly how the Berry-curvature language becomes the projector formula.`

## Outgoing Edges
- none

## Incoming Edges
- none
