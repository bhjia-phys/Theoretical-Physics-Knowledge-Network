# TKNN Invariant As First Chern Class Of The Filled-Band Bundle

- ID: `definition:tknn-invariant-as-first-chern-class-of-filled-band-bundle`
- Type: `definition`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
For a gapped two-dimensional band insulator, the TKNN invariant is the first Chern number of the filled-band bundle over the Brillouin torus, equivalently written through the occupied-projector formula and the Berry curvature of the occupied states.

## Scope
Definition of the single-particle topological invariant used in Witten Lecture Two and in TKNN.

## Regime
Gapped two-dimensional band insulators.

## Assumptions
- `The two-dimensional band structure is fully gapped over the whole Brillouin zone.`
- `The occupied-state subspaces vary smoothly with momentum.`

## Representation
First Chern number of the occupied-state bundle over the two-dimensional Brillouin torus.

## Source Anchors
- `lecture-two/relation-to-band-topology | Witten defines k' as the first Chern class of the occupied-state bundle over the Brillouin torus.`
- `paper/projector-curvature-identity | eqs: occupied-bundle-curvature-form | Primary source for the geometric Hall-conductance invariant written through occupied-bundle curvature.`

## Mathematical Content
- Single-particle Hall invariant defined from the Berry curvature of the filled bands.
$$
k' = c_1(\mathcal H'_p) = \int_{\mathcal B} \frac{\operatorname{Tr}\,F}{2\pi}
$$
- `label=occupied-bundle-curvature-form` | Equivalent projector formula for the same first Chern number.
$$
k'=\frac{i}{2\pi}\int_{\mathcal B}\operatorname{Tr}\!\left(P[\partial_{p_1}P,\partial_{p_2}P]\right)\,\mathrm d^2p
$$
- Rank-one specialization when a single filled band is present.
$$
k' = \int_{\mathcal B}\frac{F}{2\pi}
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `k'` | band-theory TKNN invariant |
| `\mathcal H'_p` | occupied-state subbundle of the full Bloch Hilbert bundle |
| `\mathcal B` | two-dimensional Brillouin torus |
| `F` | Berry curvature of the occupied-state bundle |
| `P` | projector onto the occupied subspace |

## Dependencies
- [Complex Line Bundle Of Filled States](../Concepts/complex-line-bundle-of-filled-states.md)
- [Berry Connection](../Concepts/berry-connection.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

## Related Units
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Failure Modes
- `If the bulk gap closes anywhere on the Brillouin torus, the occupied-state bundle and its Chern number cease to be well-defined.`

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `tknn_invariant_as_first_chern_class`
- Statement kind: `definition`

### Admissible assumptions

- Work with a smooth gapped occupied-state bundle over the two-dimensional Brillouin torus.
- Treat the multi-band case through the occupied projector or traced curvature rather than through one global abelian gauge.

### Lean prerequisites

- [Complex Line Bundle Of Filled States](../Concepts/complex-line-bundle-of-filled-states.md)
- [Berry Connection](../Concepts/berry-connection.md)
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)

### Formalization blockers

- A reusable Lean-side interface for smooth Bloch bundles over the Brillouin torus is still missing.
- The passage from local Berry-connection charts to a global first-Chern-class representative is not yet packaged as a lower-level geometry lemma.

## Formal-Theory Guardrails

- Formal theory role: `trusted_target`
- Definition trust tier: `reviewed_translation`
- Statement graph role: `prerequisite`
- Prerequisite closure status: `closed`

### Statement graph parents

- [Complex Line Bundle Of Filled States](../Concepts/complex-line-bundle-of-filled-states.md)
- [Berry Connection](../Concepts/berry-connection.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)

### Statement graph children

- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Faithfulness Review

- Status: `reviewed`
- Strategy: Keep the canonical definition equal to Witten's k' and the TKNN occupied-bundle Chern number, while exposing the projector formula explicitly for the multi-band case.
- Notes: The KB adds explanatory wording about rank-one versus multi-band presentations, but the invariant itself remains the same first Chern number.

## Comparator Audit

- Status: `passed`

### Comparator risks

- Do not weaken the definition into a rank-one-only statement when the source also supports the traced-curvature and projector formulations.

## Provenance And Attribution

- Provenance kind: `mixed`

### Attribution requirements

- Retain attribution to both Witten Lecture Two and the original TKNN paper when citing this canonical definition.
- Do not present the projector formula as KB-internal invention; it is a source-derived equivalent expression.

## Retrieval Hints
- `Use when a query asks for the precise microscopic invariant behind the integer Hall response.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture Two Source Map](../Source-Maps/witten-topological-phases-lecture-two.md): The TKNN definition is part of the Lecture Two source map.
- `supports` -> [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md): The TKNN definition provides the microscopic Chern-number side of the Hall-response theorem.

## Incoming Edges
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md) -> `supports`: The Lecture Two notation map fixes the Hall-response and Berry-curvature symbols used in the TKNN definition.
