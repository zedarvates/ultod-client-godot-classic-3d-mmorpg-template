# Public Extraction Design

Status: `decision` for the extraction method. Future starter files MUST be
original, isolated, and created inside this repository. Existing Ultimate
Odycer client or server files MUST NOT be copied, renamed, or vendored.

The extraction unit is one file. A directory, scene tree, or Git history is
not an allowlist.

## Source boundary

| Source | Allowed use | Forbidden use |
|---|---|---|
| This repository's documentation | continue and refine | treat docs as a playable client |
| [ultimate-odycer-docs](https://github.com/zedarvates/ultimate-odycer-docs) public contracts | consume published authority rules and `network-intent-v1` as documentation | invent opcodes or live endpoints |
| [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry) | pin reviewed snapshots by version and SHA-256 | auto-download at runtime or treat templates as grants |
| Existing Ultimate Odycer Godot client | none | copy, rewrite-in-place, or "clean up" proprietary scenes |
| Zig server, WebAdmin, production configs | none | protocol dumps, binaries, credentials, billing |
| Third-party Godot samples | only permissively licensed, file-audited, attributed originals | unaudited assets, brands, or unknown licenses |

## File-level allowlist for the Classic 3D original shell

| Planned path | Purpose | License | Authority |
|---|---|---|---|
| `project.godot` | original Godot 3D project metadata | MIT, this repository | none |
| `scenes/bootstrap.tscn` | engine, window, and quality checks | MIT, original | none |
| `scenes/player_3d_presentation.tscn` | local third-person presentation of a server entity | MIT, original | presentation only |
| `scenes/npc_3d_presentation.tscn` | interaction prompt presentation | MIT, original | presentation only |
| `scenes/zone_stub.tscn` | synthetic local geometry, no production map | MIT, original | no world grants |
| `scenes/ui_stub.tscn` | HUD / desktop panel stub | MIT, original | no economy or inventory truth |
| `input/third_person_camera.gd` | third-person spring arm and orbit camera | MIT, original | local view only |
| `input/desktop_movement_stub.gd` | desktop keyboard/mouse movement calculator | MIT, original | discarded if a future server rejects it |
| `net/intent_contract.md` | maps public `network-intent-v1` families to client methods | MIT, documentation | no live socket |
| `content/pinned_templates.md` | records pinned registry versions and SHA-256 | MIT, documentation | templates never grant gold, items, or speed |
| `tests/synthetic_fixtures/` | names like `player_demo_01`, never live ids | MIT, original | synthetic only |

Anything not listed is denied until a new audited row is added.

## Denied classes

- any path from an existing Ultimate Odycer client checkout;
- `.pck`, exported binaries, or prebuilt Godot templates from the private game;
- protocol captures, TLS materials, realm URLs, or player identifiers;
- WebAdmin, billing, moderation, or commercial configuration;
- unaudited GLB/PNG/audio, brand marks, or third-party packs;
- a network client before [SERVER-COMPATIBILITY.md](SERVER-COMPATIBILITY.md) is resolved.

## License audit

- Future original starter files: MIT, as declared in [LICENSE](../LICENSE).
- Documentation already in this repository: remains documentation, not a game asset grant.
- JSON registry snapshots: Apache-2.0 in their own repository; pin and attribute, do not relicense.
- Godot runtime: stays outside this repository; document exact versions when a shell is published.
- Ultimate Odycer name, proprietary server, hosted services, and commercial components: no license is granted here.

## Non-claims

This document does not prove that a playable game exists, that performance is certified, or that a server will accept a client. Missing evidence stays unsupported.
