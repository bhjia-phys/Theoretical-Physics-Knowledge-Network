## Change Type

- [ ] `source-onboarding`
- [ ] `unit-promotion`
- [ ] `graph-refinement`
- [ ] `mirror-sync`
- [ ] `docs`

## Source IDs

List public source ids touched by this PR.

## Canonical Objects

List typed ids created or updated under `units/`.

## Edge Changes

List edge ids created or updated in `edges/edges.jsonl`.

## Human Mirror Changes

List notes added or updated under `human-mirror/`.

## Protocol Checks

- [ ] I read `docs/PROTOCOLS.md`.
- [ ] I read `docs/L2_RETRIEVAL_PROTOCOL.md`.
- [ ] I read `docs/L2_BRIDGE_PROTOCOL.md` if this PR came from an AITP `L2` workflow.
- [ ] I queried existing indexes before creating new typed objects.
- [ ] Every new or updated unit has valid source anchors.
- [ ] Every object-like mirror note includes `kb_unit_id` or `kb_source_map_id`.
- [ ] I ran `python3 scripts/kb.py check`.
- [ ] I ran `python3 scripts/kb.py build`.
- [ ] Generated `indexes/` and `portal/` outputs are included.

## Unresolved Items

List anything intentionally left upstream instead of committing it into this repo.
