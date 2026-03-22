# Theoretical Physics Knowledge Network

Theoretical Physics Knowledge Network is a protocol-first, schema-backed theoretical-physics knowledge base.

This public skeleton is built around one core architectural split:

- the canonical backend is a typed object store meant to remain compatible with AITP `L2` retrieval;
- the human-facing layer is a curated mirror that stays structurally compatible with the backend without becoming the source of truth.

## Repository Role

This repository is intended to be publishable as a standalone open-source project for building theoretical-physics knowledge bases with:

- stable typed ids;
- explicit source anchors;
- deterministic retrieval indexes;
- graph structure via explicit edges;
- a human-readable mirror that follows the same object boundaries.

## Relationship To AITP

This repository is the public knowledge backend, not the AITP runtime kernel.

In the current stack:

- `AITP-Research-Protocol` owns the research protocol, runtime state, gap recovery, validation flow, and promotion logic.
- `theoretical-physics-knowledge-network` owns the typed long-term knowledge surface that AITP can target as an `L2`-compatible backend.
- `Theoretical-Physics` is the active private workspace where mirror notes, staging logic, and developer handoff material can evolve before selected content is published here.

The intended lifecycle is:

`source work in AITP/workspace -> validation/promotion -> write into TPKN`

That separation is deliberate:

- the runtime should not be forced into the public backend repo;
- the public backend should not become a dumping ground for raw runtime notes;
- the private workspace can remain productive without corrupting the public backend history.

The current exemplar source is:

- Edward Witten, *Three Lectures On Topological Phases Of Matter*, arXiv:1510.07698v2
- current stage-two scope: Lecture One proof-grade exemplar plus promoted Lecture Two / Three flagship theorem families, topic-level regression assets, and explicit future-buffer routing

## Core Contracts

Read these first:

- `docs/PROTOCOLS.md`
- `docs/L2_RETRIEVAL_PROTOCOL.md`
- `docs/L2_BRIDGE_PROTOCOL.md`
- `docs/STANDALONE_REPO_INIT.md`

## Repository Layout

```text
theoretical-physics-knowledge-network/
├── docs/            # contracts and design notes
├── schema/          # JSON Schemas for canonical objects
├── sources/         # source manifests
├── units/           # canonical typed knowledge objects
├── edges/           # canonical graph relations
├── indexes/         # generated retrieval-facing indexes
├── portal/          # generated human-readable projections
├── human-mirror/    # hand-curated example mirror layer
├── queues/          # durable unresolved-work surfaces
├── regressions/     # topic-level regression suites and logs
├── examples/        # worked examples and source-specific notes
├── scripts/         # minimal protocol/build scripts
└── .github/         # CI for protocol/build checks
```

## Canonical vs Human Layers

Canonical backend:

- `sources/`
- `units/`
- `edges/`

Non-canonical surfaces:

- `indexes/`
- `portal/`
- `human-mirror/`

The human mirror is allowed to add explanation, intuition, examples, and navigation. It is not allowed to replace typed ids, source grounding, assumptions, regime statements, or dependency information when mirroring a typed object.

## Quick Start

```bash
python3 scripts/check_protocol.py
python3 scripts/build.py
```

`python3 scripts/build.py` runs the protocol check before rebuilding generated outputs.

## Windows Development Handoff

If you continue development on Windows, treat this repository as the clean
publish target, not the only place where active note-writing happens.

Recommended setup:

- clone this repo as a sibling of `AITP-Research-Protocol` and `Theoretical-Physics`;
- do runtime-heavy work under `WSL2 Ubuntu`;
- keep publication into this repo as an explicit, clean-repo step.

In other words:

- use `AITP-Research-Protocol` to run the protocol;
- use `Theoretical-Physics` for active workspace editing and mirror work;
- use `theoretical-physics-knowledge-network` when you are ready to publish typed backend state.

## What The Public Skeleton Includes

- protocol docs in `docs/`;
- schemas in `schema/`;
- one source manifest in `sources/`;
- a first object cluster around Weyl nodes, Berry geometry, Nielsen-Ninomiya, and Fermi arcs;
- promoted Lecture Two / Three theorem-family branches, proof states, proof obligations, and cited-source recovery tasks;
- deterministic retrieval indexes and portal projections;
- durable queues and regression assets for proof-grade topic maintenance;
- a small `human-mirror/` example showing how a `01 Theoretical Physics` style knowledge base can remain human-facing while staying structurally compatible with `L2`.

## Current Example Mirror

The curated example mirror lives under `human-mirror/` and includes:

- an entry note at `human-mirror/Index.md`;
- a root index and mirror contract;
- a `Quantum Matter / Topological Phases` branch;
- a small set of directly bound object mirrors such as `Weyl Node`, `Berry Connection`, `Berry Curvature`, `Nielsen-Ninomiya Theorem`, and `Fermi Arc`.

## Design Alignment

This repository is intentionally independent from:

- any private Obsidian vault as a source of truth;
- AITP runtime orchestration;
- Lean build tooling.

But it is intentionally compatible with:

- AITP `L2` style typed retrieval;
- metadata-rich object design lessons visible in LeanCat;
- physics-first topic organization familiar from physlib-style documentation;
- zettelkasten-like dense local linking on the human side, without making note blobs canonical.

If AITP `L2` later writes into this repository, it should do so through `docs/L2_BRIDGE_PROTOCOL.md`, not by exporting runtime notes directly.

## License

This skeleton is released under the MIT License. See `LICENSE`.

## Publishing

If you want to split this directory into a standalone public repository, see `docs/PUBLISHING.md`.
