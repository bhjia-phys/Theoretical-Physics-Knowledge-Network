# Design Alignment

## AITP L2 Compatibility

This repository mirrors the same backend assumptions used by the current AITP `L2` design:

- typed object store rather than note blobs;
- explicit edge layer;
- deterministic retrieval-facing indexes;
- source-grounded reusable units with compact summaries;
- promotion based on content quality gates rather than schema completeness alone.

The repo is independent from the AITP runtime, but the contracts are shaped so it can later act as an external `L2` backend or seed corpus.

## Paper-Quality Lesson

Paper ingestion is only useful if the resulting notes are actually understandable.

This repository therefore treats the following as first-class quality targets:

- self-interrogation after note writing;
- detailed derivation visibility when the source supports it;
- explicit context links across a paper's argument spine;
- automatic `L0` follow-up when a cited background result is needed to make the note truly clear.

## LeanCat Lesson

LeanCat emphasizes metadata-rich, statement-level objects instead of only broad topic notes.

This repository adopts the same general lesson:

- granular objects;
- stable ids;
- explicit difficulty or maturity style metadata;
- clear future formalization targets.

That is why each unit records `formalization_status` and can point toward later Lean-facing targets without pretending that the current object is already a theorem statement.

## physlib Lesson

`physlib` argues for physics-organized documentation and reusable modules that remain readable to physicists.

This repository keeps the same principle on the human-facing side:

- topic-first navigation in `portal/`;
- concise summaries;
- equations and models surfaced alongside concepts instead of hidden behind implementation details.

## Zettelkasten Lesson

The human portal is intentionally zettelkasten-like:

- many small notes;
- dense local links;
- cross-cutting navigation.

The difference is structural:

- in a classic zettelkasten, the notes themselves are often the source of truth;
- here the typed units and edges are the source of truth, and the note-like portal is generated from them.
