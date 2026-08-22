# Original Shell Layout

Status: planned layout for the original Classic 3D starter. These files are
isolated and original to this template repository.

```text
ultod-client-godot-classic-3d-mmorpg-template/
  project.godot                      # original metadata
  scenes/
    bootstrap.tscn                   # platform and window initialization
    player_3d_presentation.tscn      # third-person local presentation
    npc_3d_presentation.tscn         # talk/interact prompt presentation
    zone_stub.tscn                   # synthetic 3D geometry
    ui_stub.tscn                     # desktop HUD panels
  input/
    third_person_camera.gd           # orbit / spring arm follow
    desktop_movement_stub.gd         # keyboard/mouse presentation locomotion
  net/
    intent_contract.md               # documentation map to network-intent-v1
  content/
    pinned_templates.md              # version + SHA-256 only
  tests/
    synthetic_fixtures/              # player_demo_* / npc_demo_*
```

Local physics and camera poses provide visual responsiveness. They must not
award loot, apply damage, change inventory, or accept a speed hack.

No `net/*.gd` socket implementation is allowed while server compatibility is
not validated. See [SERVER-COMPATIBILITY.md](SERVER-COMPATIBILITY.md) and the public
[network-intent-v1](https://github.com/zedarvates/ultimate-odycer-docs/blob/main/schemas/network-intent-v1.schema.json)
fixture.
