# Lecture Two Large-Gauge Holonomy Shift Context

- ID: `equation_context:lecture-two-large-gauge-holonomy-shift`
- Type: `equation_context`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This equation context records why Witten's unit-flux background on S^2 times S^1 and the large gauge shift of the temporal holonomy are enough to force the Chern-Simons level to be integral.

## Scope
Equation-level context for the large-gauge argument preceding the Hall-response theorem.

## Regime
Closed-manifold Chern-Simons quantization argument.

## Assumptions
- `The background gauge field is compact.`
- `The path integral only depends on the action modulo 2pi.`

## Representation
Equation context for the holonomy-shift argument that upgrades Chern-Simons gauge invariance into integrality of k.

## Source Anchors
- `lecture-two/quantization-of-the-chern-simons-coupling | eqs: unitf, nifty, prif | Witten's S^2 times S^1 large-gauge background that makes the level quantization explicit.`

## Mathematical Content
- `kind=display` | `label=unitf` | One unit of magnetic flux is inserted through the spatial two-sphere.
$$
\int_{S^2}\frac{F}{2\pi}=1
$$
- `kind=display` | `label=nifty` | The Chern-Simons functional evaluates to the temporal holonomy angle.
$$
\mathcal I_{\mathrm{CS}} = \frac{1}{4\pi}\int_{S^2\times S^1}\epsilon^{ijk}A_i\partial_jA_k = s
$$
- `kind=display` | `label=prif` | A large gauge transformation shifts the holonomy by 2pi without changing the physical configuration.
$$
s \to s + 2\pi
$$
- `kind=display` | Because the action is only defined modulo 2pi, the coefficient k must be integral.
$$
e^{ik\mathcal I_{\mathrm{CS}}} \text{ is gauge invariant } \Rightarrow k \in \mathbb Z
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `s` | temporal holonomy angle on the S^1 factor |
| `k` | Chern-Simons level multiplying the effective action |

## Dependencies
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

## Related Units
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)

## Retrieval Hints
- `Open this before answering why k is an integer instead of merely asserting it.`

## Outgoing Edges
- none

## Incoming Edges
- none
