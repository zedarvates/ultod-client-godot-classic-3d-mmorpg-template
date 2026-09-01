# Synthetic transport fixture

Status: **prepared, runtime proof pending**.

The public Godot starter contains a deterministic, socket-free transport fixture for exercising the client intent/state-machine boundary before the canonical Zig server is available.

## Proof level

The maximum proof level produced by this fixture is:

`SYNTHETIC_FIXTURE_ONLY`

It does **not** prove:

- canonical Zig compatibility;
- any TCP/WebSocket/ENet framing;
- login or game endpoints;
- production authentication or TLS;
- server persistence, economy, combat, permissions, or anti-cheat behavior.

## Components

- `net/intent_contract.gd` — bounded client intent validation;
- `net/transport_adapter.gd` — abstract transport lifecycle;
- `net/synthetic_transport.gd` — deterministic local test authority with no socket;
- `tests/synthetic_transport_fixture.gd` — offline/auth/movement/forbidden-authority/drop/resume assertions;
- `tools/validate_synthetic_transport.py` — Godot 4.7.2 runner and JSON evidence writer.

## Executable proof

With an exact Godot 4.7.2-stable binary:

```bash
python tools/validate_synthetic_transport.py --godot /path/to/godot
```

The receipt is written under `.evidence/` and is intentionally ignored by Git.

A successful run demonstrates only that the public Godot client boundary executes the named deterministic fixture under the named engine version. Promotion to `REAL_SERVER_E2E` still requires the pinned private canonical Zig baseline and a real server scenario.

## Security behavior exercised

The fixture is expected to prove that:

- intents fail closed while offline;
- authentication is a separate state gate;
- nested client-authority fields are rejected;
- malformed movement is rejected;
- movement components are sanitized before the synthetic authority applies them;
- a dropped fixture session becomes unavailable rather than silently staying online;
- synthetic resume preserves fixture-owned state;
- closing returns to a disconnected state.

## Licensing boundary

This synthetic fixture is original public starter code under MIT. It contains no private Zig implementation, private protocol dump, production endpoint, asset/lore, or commercial configuration. The private Ultimate Odycer server/game implementation remains proprietary/commercial, all rights reserved unless explicitly licensed otherwise.
