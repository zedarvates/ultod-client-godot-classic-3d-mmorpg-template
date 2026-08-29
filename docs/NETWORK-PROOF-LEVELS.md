# Network proof levels

This public Godot Classic starter must distinguish design intent, synthetic fixtures and real compatibility with the private canonical Ultimate Odycer Zig server.

## Levels

| Level | Meaning | May claim Zig compatibility? |
|---|---|---|
| `DOCUMENTED` | Intent/authority rules are documented only. | No |
| `SYNTHETIC_FIXTURE_ONLY` | Isolated public fixture exercises client semantics without the private server. | No |
| `PINNED_SERVER_AVAILABLE` | Exact private Zig repository revision, toolchain, build mode and protocol revision are recorded. | No, not until exercised |
| `REAL_SERVER_E2E` | Exact Godot and Zig revisions pass the canonical interoperability scenario. | Yes, only for the tested scope |
| `ADVERSARIAL_E2E` | Negative/replay/malformed/authority-abuse fixtures also pass against the pinned server. | Yes, with tested security scope named |
| `RELEASE_PROVEN` | Exact release revisions repeat the required engine, network and release gates. | Yes, for those exact revisions |

## Fake-green rule

A result is `FAKE-GREEN` when it is presented as proof of a system it did not exercise. Examples include a JSON fixture presented as a live server test, a Godot scene loading in isolation presented as Zig interoperability, a mock credential presented as JWT validation, or a metadata-only engine version edit presented as a 4.7.2 migration.

## Current Classic 3D status

- Network authority contract: `DOCUMENTED`.
- Live Zig compatibility: `NOT_PROVEN`.
- Live socket implementation: intentionally absent until the private server baseline is pinned.
- Engine declaration: currently Godot 4.3 in `project.godot`; target project baseline is Godot 4.7.2, but the migration is not proven until the project is loaded/executed with that engine.

## Licensing boundary

This public starter remains governed by its explicit repository license. The private canonical Zig server, proprietary gameplay implementation, production configuration, private assets/lore and other commercial components remain outside this repository and are proprietary/commercial, all rights reserved unless their own explicit license states otherwise. Public fixtures must never copy private implementation code merely to make a test pass.
