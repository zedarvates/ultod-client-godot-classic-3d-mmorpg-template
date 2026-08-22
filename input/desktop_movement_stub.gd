# SPDX-License-Identifier: MIT
# Desktop keyboard and mouse presentation locomotion calculator.
# Note: Client-side movement is presentation-only and subject to authoritative server reconciliation.
extends Node
class_name DesktopMovementStub

@export var max_presentation_speed_m_s: float = 5.0
@export var jump_velocity: float = 4.5

signal presentation_movement_requested(delta_position: Vector3, new_yaw: float)

func compute_movement_vector(input_dir: Vector2, camera_basis: Basis, delta: float) -> Vector3:
	if input_dir.length_squared() < 0.01:
		return Vector3.ZERO
	var forward = -camera_basis.z
	var right = camera_basis.x
	forward.y = 0.0
	right.y = 0.0
	forward = forward.normalized()
	right = right.normalized()
	
	var wish_dir = (forward * input_dir.y + right * input_dir.x).normalized()
	return wish_dir * max_presentation_speed_m_s * delta
