# Projector Formula For The TKNN Chern Number

- ID: `proof_fragment:projector-formula-for-the-tknn-chern-number`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
For the occupied-band projector P(p), the microscopic Hall integer k' is the Brillouin-zone integral of i Tr(P[\partial_{p_1}P,\partial_{p_2}P]) / 2\pi, which is the first Chern number of the filled-band bundle.

## Scope
Source-grade TKNN fragment that upgrades the band-theory side of the Lecture Two theorem from a verbal bundle statement to an explicit formula.

## Regime
Single-particle band-topology formulation of the integer quantum Hall invariant.

## Assumptions
- `The occupied-band projector is smooth over the whole two-dimensional Brillouin torus.`
- `The filled subspace remains gapped from the empty bands.`

## Representation
Explicit projector-level realization of the band Chern invariant used inside the Lecture Two Hall-response family.

## Source Anchors
- `paper/projector-curvature-identity | eqs: occupied-bundle-curvature-form | Original source of the quantized Hall invariant, rendered here through the traced-curvature identity and the occupied-projector formula.`
- `lecture-two/relation-to-band-topology | Witten states the TKNN integer as the first Chern class of the filled-band bundle.`

## Mathematical Content
- `kind=display` | Projector onto the occupied Bloch subspace.
$$
P(p)=\sum_{a=1}^{n}|u_a(p)\rangle\langle u_a(p)|
$$
- `kind=display` | Local non-abelian Berry connection and curvature on the filled bundle.
$$
\mathcal A_{ab}=\langle u_a,\mathrm du_b\rangle,\qquad \mathcal F=\mathrm d\mathcal A+\mathcal A\wedge\mathcal A
$$
- `kind=display` | Projector formula for the TKNN invariant and its equality to the first Chern number.
$$
k'=\frac{i}{2\pi}\int_{\mathcal B}\operatorname{Tr}\!\left(P[\partial_{p_1}P,\partial_{p_2}P]\right)\,\mathrm d^2p=\int_{\mathcal B}\frac{\operatorname{Tr}\,\mathcal F}{2\pi}
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `P(p)` | spectral projector onto the filled bands at momentum p |
| `\mathcal A` | Berry connection on a local occupied-state frame |
| `\mathcal F` | Berry curvature two-form of the occupied-state bundle |

## Dependencies
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry-Curvature Trace Equals Projector Commutator](berry-curvature-trace-equals-projector-commutator.md)

## Related Units
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)

## Step Justification
- Differentiate P squared equals P to show that dP only mixes occupied and empty states.
- Expand Tr(P[dP,dP]) in a local orthonormal occupied frame.
- Recognize the resulting expression as the trace of the non-abelian Berry curvature.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `projector_formula_for_tknn_chern_number`
- Statement kind: `lemma`

### Admissible assumptions

- Work with a smooth finite-rank occupied projector over the two-dimensional Brillouin torus.
- Treat Brillouin-zone orientation and measure conventions as fixed global background data.

### Lean prerequisites

- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry-Curvature Trace Equals Projector Commutator](berry-curvature-trace-equals-projector-commutator.md)

### Formalization blockers

- A reusable Lean representation of the Brillouin torus as an oriented compact two-manifold is still missing.
- The integration layer needed to turn the local curvature density into a global integer invariant is not yet connected to the present bundle notes.

## Retrieval Hints
- `Use when the answer must show the actual TKNN integrand rather than only saying first Chern class.`

## Outgoing Edges
- none

## Incoming Edges
- none
