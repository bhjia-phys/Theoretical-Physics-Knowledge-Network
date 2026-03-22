# Large Gauge Invariance Quantizes The Chern-Simons Level

- ID: `proof_fragment:large-gauge-invariance-quantizes-chern-simons-level`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Place the theory on S^2 times S^1 with one unit of flux through S^2 and a constant temporal holonomy A_0 = s/beta; because the Chern-Simons action shifts by 2pi under the allowed large gauge transformation, its coefficient must be integral.

## Scope
Quantization step for the Chern-Simons level in Witten Lecture Two.

## Regime
2+1-dimensional effective topological response on a closed spacetime manifold.

## Assumptions
- `The microscopic electron field transforms under a compact U(1) gauge symmetry.`
- `The effective action is allowed to be defined only modulo 2pi in the path integral.`

## Representation
Closed-manifold large-gauge-invariance argument for integer Chern-Simons level.

## Source Anchors
- `lecture-two/quantization-of-the-chern-simons-coupling | eqs: unitf, nifty, prif | Witten's closed-manifold argument for the integrality of the Chern-Simons level.`

## Mathematical Content
- `kind=display` | `label=unitf` | Unit Dirac flux through the spatial two-sphere.
$$
\int_{S^2}\frac{F}{2\pi}=1
$$
- `kind=display` | `label=nifty` | Value of the Chern-Simons functional on the background with temporal holonomy s.
$$
\mathcal I_{\mathrm{CS}} = \frac{1}{4\pi}\int_{S^2\times S^1}\epsilon^{ijk}A_i\partial_jA_k = s
$$
- `kind=display` | `label=prif` | Allowed large gauge transformation of the temporal holonomy.
$$
s \to s + 2\pi
$$

## Symbols
- none

## Dependencies
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

## Related Units
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Step Justification
- The electron wavefunction only requires exp(i phi) to be single-valued, not phi itself.
- The path integral is unchanged when the action shifts by an integer multiple of 2pi.
- Therefore an effective action term k I_CS is gauge invariant only when k is an integer.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `large_gauge_invariance_quantizes_chern_simons_level`
- Statement kind: `lemma`

### Admissible assumptions

- Work with a compact U(1) gauge field on the closed manifold S^2 x S^1.
- Treat the large gauge transformation of the temporal holonomy as an allowed input rather than formalizing the full gauge-group homotopy theory inside this lemma.

### Lean prerequisites

- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

### Formalization blockers

- The current KB does not yet expose a reusable Lean-side library for the Chern-Simons functional on closed three-manifolds.
- The path-integral modulo-2pi convention still needs a more explicit formal wrapper than plain equality of real actions.

## Retrieval Hints
- `Use when a Hall-response explanation must justify why the Chern-Simons level is quantized before differentiating it into a current.`

## Outgoing Edges
- `supports` -> [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md): Large gauge invariance supplies the integer quantization of the Hall-response level.

## Incoming Edges
- none
