#!/usr/bin/env python3
"""Build or verify the deterministic governance distribution manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

DISTRIBUTION = "development-governance-v0"
DISTRIBUTED_PATHS = (
    ".agents/README.md",
    ".agents/protocol/SPEC_GOVERNANCE_V0.md",
    ".agents/protocol/SPEC_FORMAT_V0.md",
    ".agents/skills/spec-governance/SKILL.md",
    ".agents/skills/spec-governance/modes/PREFLIGHT.md",
    ".agents/skills/spec-governance/modes/AUTHOR.md",
    ".agents/skills/spec-governance/modes/REVIEW.md",
    ".agents/skills/spec-governance/modes/COMPLIANCE.md",
    ".agents/tools/verify_governance.py",
    ".agents/schemas/distribution-manifest.schema.json",
    ".agents/schemas/spec-frontmatter.schema.json",
    ".agents/schemas/governance-lock.schema.json",
    ".agents/templates/SPEC_TEMPLATE.md",
    ".agents/templates/GOVERNANCE_ADOPTION_SPEC_TEMPLATE.md",
    ".agents/templates/REVIEW_RECORD_TEMPLATE.md",
    ".agents/templates/CONFORMANCE_RECORD_TEMPLATE.md",
    ".agents/templates/INVESTIGATION_RECORD_TEMPLATE.md",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_manifest(root: Path) -> dict[str, object]:
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    files: list[dict[str, object]] = []

    for relative in DISTRIBUTED_PATHS:
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(f"required distribution file is missing: {relative}")
        data = path.read_bytes()
        files.append(
            {
                "path": relative,
                "sha256": sha256_bytes(data),
                "size": len(data),
            }
        )

    return {
        "$schema": "urn:mayf3:agent-development-governance:distribution-manifest:v0",
        "schema_version": 1,
        "distribution": DISTRIBUTION,
        "version": version,
        "files": files,
    }


def serialize(manifest: dict[str, object]) -> bytes:
    return (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when distribution/manifest.json differs from generated content",
    )
    args = parser.parse_args(argv)

    root = repo_root()
    output = root / "distribution" / "manifest.json"

    try:
        expected = serialize(build_manifest(root))
    except (OSError, ValueError) as exc:
        print(f"manifest build failed: {exc}", file=sys.stderr)
        return 2

    if args.check:
        if not output.is_file():
            print("distribution/manifest.json is missing", file=sys.stderr)
            return 1
        actual = output.read_bytes()
        if actual != expected:
            print(
                "distribution/manifest.json is stale; run tools/build_manifest.py",
                file=sys.stderr,
            )
            return 1
        print("distribution manifest is current")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(expected)
    print(f"wrote {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
