# Dirac Point In Two Dimensions

- ID: `concept:dirac-point-in-2d`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `dirac-materials`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
A two-dimensional Dirac point is a linear band crossing in 2D whose generic persistence usually requires extra symmetry or special tuning rather than only codimension counting.

## Scope
Lecture One discussion of why 2D crossings are less generic than 3D Weyl crossings.

## Regime
Two-dimensional Bloch-band systems.

## Assumptions
- `The problem is two-dimensional.`
- `The crossing is analyzed near the Fermi level.`

## Dependencies
- [Band Crossing](band-crossing.md)

## Related Units
- [Generic 2D Dirac Points Require Symmetry Protection](../Claims/generic-2d-dirac-points-require-symmetry-protection.md)
- [Crossing Away From The Fermi Energy Is Not Yet A Clean Weyl Semimetal](../Warnings/crossing-away-from-fermi-energy-is-not-yet-a-clean-weyl-semimetal.md)

## Source Anchors
- `lecture-one/two-dimensions | eqs: twod | Lecture One contrasts the 2D and 3D genericity stories.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md): The 2D Dirac-point unit is part of the current Lecture One source map.
- `contrasts_with` -> [Weyl Node](weyl-node.md): Lecture One contrasts generic 2D Dirac crossings with generic 3D Weyl crossings.

## Incoming Edges
- [Band Crossing](band-crossing.md) -> `explains`: A two-dimensional Dirac point is another dimension-specific form of band crossing.
- [Generic 2D Dirac Points Require Symmetry Protection](../Claims/generic-2d-dirac-points-require-symmetry-protection.md) -> `derived_from`: The claim packages the stability lesson of the 2D Dirac-point concept.

## Failure Modes
- `Without symmetry protection, a small perturbation often gaps the crossing.`

## Formal Targets
- `aitp-l2`
