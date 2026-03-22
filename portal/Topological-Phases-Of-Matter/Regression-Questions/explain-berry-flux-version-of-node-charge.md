# Explain The Berry-Flux Version Of The Node Charge

- ID: `regression_question:explain-berry-flux-version-of-node-charge`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can explain the Berry-curvature route from local geometry to node charge and then to the same global zero-sum law.

## Scope
Bridge question between local Berry geometry and global charge cancellation.

## Regime
Topic regression for the Witten Lecture One exemplar.

## Assumptions
- `The answer should stay on the Berry-curvature route, not fall back to only the degree-language route.`

## Representation
Bridge-style regression prompt.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zif, wif, nna | The answer should expose the local flux formula and the global dF=0 sum rule.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md)

## Related Units
- [Oracle For The Berry-Flux Version Of The Node Charge](../Question-Oracles/explain-berry-flux-version-of-node-charge.md)

## Prompt
Explain how Witten's Berry-curvature construction turns an isolated Weyl node into an integer charge and then reproduces the Nielsen-Ninomiya sum rule.

## Question Family
`bridge`

## Pass Conditions
- The answer writes the Berry-flux charge formula on a small surrounding sphere.
- The answer states that dF = 0 away from the bad points.
- The answer explains how Stokes's theorem on the punctured zone recovers the global zero-sum law.

## Primary Retrieval Paths
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md)

## Retrieval Hints
- `Use in regression runs to test whether the KB can navigate from Berry geometry to global topology.`

## Outgoing Edges
- `tests` -> [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md): The regression question tests the Berry-curvature route to the charge and zero-sum law.

## Incoming Edges
- [Oracle For The Berry-Flux Version Of The Node Charge](../Question-Oracles/explain-berry-flux-version-of-node-charge.md) -> `oracles`: This oracle records the proof requirements for the Berry-flux question.
