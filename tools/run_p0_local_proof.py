#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run the local Classic P0 proof chain with one exact Godot 4.7.2 binary.

This script never downloads Godot, never enables networking, never edits proof
metadata, and stops at the first failed evidence gate.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / ".evidence"


def run(command: list[str]) -> int:
    print("+", " ".join(command))
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--godot", default=os.environ.get("GODOT_BIN"), help="Exact Godot 4.7.2-stable executable")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    if not args.godot:
        print("ERROR: provide --godot or GODOT_BIN; automatic downloads/discovery are intentionally disabled", file=sys.stderr)
        return 2

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    engine_receipt = EVIDENCE / "godot-4.7.2-engine.json"
    synthetic_receipt = EVIDENCE / "synthetic-transport.json"

    engine = [
        sys.executable,
        str(ROOT / "tools" / "validate_godot_4_7_2.py"),
        "--godot", args.godot,
        "--timeout", str(args.timeout),
        "--evidence", str(engine_receipt),
    ]
    if run(engine) != 0:
        print("P0 local proof stopped: engine/import/bootstrap evidence failed", file=sys.stderr)
        return 1

    synthetic = [
        sys.executable,
        str(ROOT / "tools" / "validate_synthetic_transport.py"),
        "--godot", args.godot,
        "--timeout", str(args.timeout),
        "--receipt", str(synthetic_receipt),
    ]
    if run(synthetic) != 0:
        print("P0 local proof stopped: synthetic transport evidence failed", file=sys.stderr)
        return 1

    print("Classic P0 local proof passed.")
    print(f"Engine receipt: {engine_receipt}")
    print(f"Synthetic receipt: {synthetic_receipt}")
    print("Scope remains bounded: synthetic transport != canonical Zig interoperability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
