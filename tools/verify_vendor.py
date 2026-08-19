#!/usr/bin/env python3
"""Compatibility wrapper for the vendored governance integrity verifier."""

from __future__ import annotations

import runpy
from pathlib import Path


if __name__ == "__main__":
    verifier = (
        Path(__file__).resolve().parents[1]
        / ".agents"
        / "tools"
        / "verify_governance.py"
    )
    runpy.run_path(str(verifier), run_name="__main__")
