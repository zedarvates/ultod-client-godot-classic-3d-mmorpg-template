#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Local executable proof for the Godot Classic 4.7.2 baseline.

This script does not edit project.godot and does not prove Zig compatibility.
It verifies an exact Godot 4.7.2 stable editor binary, imports the project in
headless mode, then boots the configured main scene for a few iterations.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TARGET_PREFIX = "4.7.2.stable"


def run_step(name: str, command: list[str], cwd: Path, timeout: int) -> dict[str, Any]:
    started = datetime.now(timezone.utc)
    try:
        process = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
        result = {
            "name": name,
            "command": command,
            "returncode": process.returncode,
            "stdout": process.stdout[-12000:],
            "stderr": process.stderr[-12000:],
            "started_at": started.isoformat(),
            "finished_at": datetime.now(timezone.utc).isoformat(),
        }
    except subprocess.TimeoutExpired as exc:
        result = {
            "name": name,
            "command": command,
            "returncode": None,
            "timed_out": True,
            "stdout": (exc.stdout or "")[-12000:] if isinstance(exc.stdout, str) else "",
            "stderr": (exc.stderr or "")[-12000:] if isinstance(exc.stderr, str) else "",
            "started_at": started.isoformat(),
            "finished_at": datetime.now(timezone.utc).isoformat(),
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--godot",
        default=os.environ.get("GODOT_BIN", "godot"),
        help="Godot editor binary path (default: GODOT_BIN or godot on PATH)",
    )
    parser.add_argument(
        "--project",
        default=str(Path(__file__).resolve().parents[1]),
        help="Project directory containing project.godot",
    )
    parser.add_argument("--timeout", type=int, default=120, help="Timeout per Godot step in seconds")
    parser.add_argument("--evidence", help="Optional JSON evidence output path")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not (project / "project.godot").is_file():
        print(f"ERROR: project.godot not found under {project}", file=sys.stderr)
        return 2
    if args.timeout < 5 or args.timeout > 900:
        print("ERROR: --timeout must be between 5 and 900 seconds", file=sys.stderr)
        return 2

    report: dict[str, Any] = {
        "schema": "uo.godot-engine-proof/v1",
        "proof_scope": "ENGINE_LOAD_AND_HEADLESS_BOOT_ONLY",
        "target": "4.7.2-stable",
        "project": str(project),
        "platform": platform.platform(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "network_compatibility_proven": False,
        "steps": [],
    }

    version = run_step("version", [args.godot, "--version"], project, args.timeout)
    report["steps"].append(version)
    version_text = (version.get("stdout", "") + version.get("stderr", "")).strip()
    report["detected_version"] = version_text
    if version.get("returncode") != 0 or not version_text.startswith(TARGET_PREFIX):
        report["passed"] = False
        report["failure"] = f"Expected Godot {TARGET_PREFIX}*, got {version_text!r}"
        return finish(report, args.evidence, 1)

    import_step = run_step(
        "headless_import",
        [args.godot, "--headless", "--path", str(project), "--import"],
        project,
        args.timeout,
    )
    report["steps"].append(import_step)
    if import_step.get("returncode") != 0:
        report["passed"] = False
        report["failure"] = "Headless project import failed"
        return finish(report, args.evidence, 1)

    boot_step = run_step(
        "headless_boot",
        [args.godot, "--headless", "--path", str(project), "--quit-after", "3"],
        project,
        args.timeout,
    )
    report["steps"].append(boot_step)
    report["passed"] = boot_step.get("returncode") == 0
    if not report["passed"]:
        report["failure"] = "Headless bootstrap failed"

    return finish(report, args.evidence, 0 if report["passed"] else 1)


def finish(report: dict[str, Any], evidence_path: str | None, code: int) -> int:
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if evidence_path:
        target = Path(evidence_path).resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered + "\n", encoding="utf-8")
        print(f"Evidence written to {target}", file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
