# SPDX-License-Identifier: MIT
# Third-person spring arm camera controller for Classic 3D presentation.
extends SpringArm3D
class_name ThirdPersonCamera

@export var mouse_sensitivity: float = 0.003
@export var min_pitch_deg: float = -60.0
@export var max_pitch_deg: float = 20.0

func _ready() -> void:
	add_excluded_object(get_parent().get_rid())

func handle_mouse_motion(event: InputEventMouseMotion) -> void:
	rotation.y -= event.relative.x * mouse_sensitivity
	rotation.x -= event.relative.y * mouse_sensitivity
	rotation.x = clamp(rotation.x, deg_to_rad(min_pitch_deg), deg_to_rad(max_pitch_deg))
