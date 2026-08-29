# Roadmap

| Gate | State | Exit condition |
|---|---|---|
| Documentation foundation | complete | Scope, security and publication boundaries are public |
| Client architecture decision | complete | Minimal public feature boundary documented in [docs/PUBLIC-EXTRACTION-DESIGN.md](docs/PUBLIC-EXTRACTION-DESIGN.md) |
| Server contract review | complete | Public network authority mapped via [net/intent_contract.md](net/intent_contract.md) |
| Public extraction design | complete | File-level allowlist and license audit are documented in [docs/PUBLIC-EXTRACTION-DESIGN.md](docs/PUBLIC-EXTRACTION-DESIGN.md) |
| Minimal Godot 3D shell | complete | Original isolated presentation shell created from allowlist (project.godot, scenes, input) |
| Canonical Zig baseline | blocked / tracked | `ultimate-odycer-feedback#5` must pin the exact private server revision before live compatibility is claimed |
| Local connectivity fixture | waiting / tracked | `ultimate-odycer-feedback#7` ports the same authoritative fixture proven first by Three.js |
| Paranoid protocol security | waiting / tracked | `ultimate-odycer-feedback#8` supplies negative fixtures, fuzzing, anti-replay and anti-duplication gates |
| Crash-safe persistence evidence | server-side / tracked | `ultimate-odycer-feedback#9` proves persistence and restore invariants before production compatibility |
| Template release | waiting | Fresh clone, license, secrets and documentation gates pass |

## P0 interoperability program

Godot Classic must not invent a separate gameplay protocol. It consumes the same public intent semantics and exact pinned Zig baseline used by Three.js:

1. `ultimate-odycer-feedback#5` — freeze server revision/version negotiation.
2. `ultimate-odycer-feedback#6` — establish the canonical Zig ↔ Three.js proof fixture.
3. `ultimate-odycer-feedback#7` — implement the Godot transport adapter and pass that same fixture and its negative cases.
4. `ultimate-odycer-feedback#8` — fuzz and abuse gates.
5. `ultimate-odycer-feedback#9` — critical-state recovery proof remains server-owned.

## License boundary

This public starter remains under its explicit public license and contains independently written client material plus compatible third-party dependencies. Private Ultimate Odycer server/gameplay code, production configuration, private assets/lore and commercial components remain proprietary/commercial, all rights reserved unless explicitly licensed otherwise. Private-repository access grants no right to redistribute or copy implementation into this repository. Public adapters should be written against approved contracts/fixtures, with file-level provenance review for any proposed extraction.

No waiting gate implies implementation or compatibility.
