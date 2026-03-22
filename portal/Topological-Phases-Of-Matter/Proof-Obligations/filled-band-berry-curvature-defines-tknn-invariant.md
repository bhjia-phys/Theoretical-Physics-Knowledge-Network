# Filled-Band Berry Curvature Defines The TKNN Invariant

- ID: `proof_obligation:filled-band-berry-curvature-defines-tknn-invariant`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Discharge the proof obligation that the microscopic Hall invariant k' is the first Chern number of the occupied-band bundle over the Brillouin torus, explicitly realized by the occupied-projector formula and the Berry curvature of the filled states.

## Scope
Microscopic Berry-curvature obligation inside the Lecture Two theorem family.

## Regime
Single-particle band-topology formulation.

## Assumptions
- `The occupied-state bundle is smooth over the Brillouin torus.`
- `The system is gapped so the filled-state projector is well-defined.`

## Representation
Bounded proof obligation for the band-theory side of the Hall-response family.

## Source Anchors
- `lecture-two/relation-to-band-topology | Witten identifies k' with the first Chern class of the filled-band bundle.`
- `paper/projector-curvature-identity | eqs: occupied-bundle-curvature-form | Original band-theory source of the traced-curvature identity and the quantized Hall invariant.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)

## Pass Conditions
- The answer identifies the occupied-band bundle over the Brillouin torus.
- The answer defines k' as the first Chern number or Berry-curvature integral of that bundle.
- The answer can explain why Tr F equals i Tr(P dP wedge dP) on a smooth occupied patch.
- The answer can write the occupied-projector formula or explain why it is equivalent to the Berry-curvature integral.
- The answer makes clear that k' is the microscopic invariant to be matched with the response coefficient.

## Mandatory Logical Moves
- Name the filled-state bundle or projector data over the Brillouin zone.
- Bridge the traced Berry curvature to the projector commutator density.
- Write the first-Chern-number integral or the equivalent occupied-projector formula.
- Interpret the resulting integer as the microscopic Hall invariant.

## Common Failure Patterns
- Mentioning TKNN without giving the bundle or Berry-curvature meaning of k'.
- Writing the projector formula without saying why it equals the traced Berry curvature.
- Quoting k' without any explicit formula for the occupied subspace.
- Treating the band invariant as already equal to k without stating what it is.

## Grading Rubric
- Full credit requires a genuine band-topology definition of k'.
- Partial credit is appropriate if the answer only says 'TKNN invariant' without defining it.

## Retrieval Hints
- `Use when the answer must include the microscopic side of the Hall-response theorem and not only the response-theory side.`

## Outgoing Edges
- none

## Incoming Edges
- none
