# Godot engine baseline

## Current state

`project.godot` currently declares a Godot `4.3` feature baseline. That is historical metadata, not evidence that the project has been validated on the current Ultimate Odycer target engine.

## Target

Target validation baseline: **Godot 4.7.2-stable**.

Do not change `config/features` merely to make the repository look current. The version metadata is promoted only after an executable validation run loads the project with Godot 4.7.2 and records the result.

## Required validation sequence

1. Record exact Godot binary/version output.
2. Run a headless project import/load on the unmodified 4.3-declared project.
3. Capture parser, scene, resource and compatibility warnings/errors.
4. Correct only issues demonstrated by that run.
5. Re-run project load until clean enough for the agreed gate.
6. Run the bootstrap scene headlessly where supported and record exit behavior.
7. Only then update project metadata to the proven baseline.
8. Repeat the validation after the metadata change.

Use the repository validator and keep the receipt local:

```bash
python tools/validate_godot_4_7_2.py \
  --godot /path/to/godot-4.7.2 \
  --evidence .evidence/godot-4.7.2-classic.json
```

`.evidence/` is intentionally gitignored. A receipt may be retained as controlled test evidence, but it must not be published automatically or confused with Zig/network proof.

## Evidence states

- `DECLARED_4_3`: current repository metadata.
- `TARGET_4_7_2`: desired baseline, not proof.
- `LOAD_PROVEN_4_7_2`: headless project load succeeded with named binary/revision.
- `BOOT_PROVEN_4_7_2`: bootstrap scene executed with named binary/revision.
- `RELEASE_PROVEN_4_7_2`: exact release commit repeated the required validation gate.

## CI / cost rule

Prefer an existing authorized self-hosted Ultimate Odycer runner for repeated Godot validation when available. Hosted CI may be used for small proof runs when appropriate, but the repository must not silently burn hosted CI budget merely to download the engine on every documentation change.

## Network independence

A successful Godot engine migration does not prove Zig server compatibility. Engine and network proof levels are independent gates.

## Licensing boundary

This public starter remains under its explicit open-source license. Private Ultimate Odycer server/game implementation and commercial content remain proprietary/commercial, all rights reserved unless explicitly licensed otherwise.
