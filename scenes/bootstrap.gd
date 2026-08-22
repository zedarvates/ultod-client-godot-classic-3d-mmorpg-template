# SPDX-License-Identifier: MIT
# Bootstrap controller for isolated Classic 3D presentation shell.
extends Node3D

@onready var status_label: Label3D = $StatusLabel

func _ready() -> void:
	var msg = "UltOd Classic 3D Client Shell (v0.1.0)
Presentation Mode - Server Authority Retained"
	print(msg)
	if status_label:
		status_label.text = msg
