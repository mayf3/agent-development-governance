#!/usr/bin/env python3
"""Vendor an exact governance distribution into a consumer repository.

Dry-run is the default. The command refuses to claim a source commit that does
not match the current clean checkout, and it refuses to overwrite tampered
vendored files unless the caller supplies an explicit override.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

SOURCE_REPOSITORY = "mayf3/agent-development-governance"
DISTRIBUTION = "development-governance-v0"
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ADOPTION_STATUSES = {"proposed", "accepted"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_root() -> Path:
    return Path(__file__).resolve().parents[1]


def utc_now() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def parse_timestamp(value: str, field: str) -> dt.datetime:
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field} must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{field} must include a timezone")
    return parsed.astimezone(dt.timezone.utc)


def safe_relative_path(relative: str, field: str = "path") -> Path:
    rel = Path(relative)
    if not relative or rel.is_absolute() or ".." in rel.parts:
        raise ValueError(f"unsafe {field}: {relative}")
    return rel


def safe_destination(target: Path, relative: str) -> Path:
    rel = safe_relative_path(relative, "distribution path")
    destination = (target / rel).resolve()
    target_resolved = target.resolve()
    if target_resolved != destination and target_resolved not in destination.parents:
        raise ValueError(f"distribution path escapes target: {relative}")
    return destination


def load_manifest(root: Path) -> tuple[dict[str, Any], bytes]:
    path = root / "distribution" / "manifest.json"
    raw = path.read_bytes()
    manifest = json.loads(raw)
    if manifest.get("$schema") != "urn:mayf3:agent-development-governance:distribution-manifest:v0":
        raise ValueError("unexpected distribution manifest $schema")
    if manifest.get("schema_version") != 1:
        raise ValueError("unsupported distribution manifest schema")
    if manifest.get("distribution") != DISTRIBUTION:
        raise ValueError("unexpected distribution name")
    if not isinstance(manifest.get("version"), str) or not manifest["version"]:
        raise ValueError("distribution manifest has no version")

    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("distribution manifest has no files")

    seen: set[str] = set()
    for entry in files:
        if not isinstance(entry, dict):
            raise ValueError("invalid manifest file entry")
        relative = entry.get("path")
        expected_size = entry.get("size")
        expected_sha = entry.get("sha256")
        if not isinstance(relative, str):
            raise ValueError("manifest path is missing")
        safe_relative_path(relative, "manifest path")
        if relative in seen:
            raise ValueError(f"duplicate manifest path: {relative}")
        seen.add(relative)
        if not isinstance(expected_size, int) or expected_size < 0:
            raise ValueError(f"invalid manifest size: {relative}")
        if not isinstance(expected_sha, str) or not SHA_RE.fullmatch(expected_sha):
            raise ValueError(f"invalid manifest digest: {relative}")

        source = root / relative
        if not source.is_file():
            raise ValueError(f"source file missing: {relative}")
        data = source.read_bytes()
        if len(data) != expected_size or sha256_bytes(data) != expected_sha:
            raise ValueError(f"manifest mismatch for source file: {relative}")
    return manifest, raw


def git_output(root: Path, *args: str) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise ValueError("git is required to verify the source revision") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "git command failed").strip()
        raise ValueError(detail) from exc
    return completed.stdout.strip()


def validate_source_checkout(
    root: Path, source_commit: str, manifest: dict[str, Any]
) -> None:
    """Bind the declared source commit to the exact clean source checkout."""

    top = Path(git_output(root, "rev-parse", "--show-toplevel")).resolve()
    if top != root.resolve():
        raise ValueError(f"source root is not the Git worktree root: {root}")

    head = git_output(root, "rev-parse", "HEAD")
    if head != source_commit:
        raise ValueError(
            f"--source-commit does not match checkout HEAD: declared {source_commit}, "
            f"actual {head}"
        )

    paths = [
        "VERSION",
        "distribution/manifest.json",
        "tools/vendor.py",
        ".agents/templates/consumer/AGENTS.md",
        ".agents/templates/consumer/LOCAL_README.md",
        ".agents/templates/consumer/SPECS_README.md",
    ]
    paths.extend(str(entry["path"]) for entry in manifest["files"])
    status = git_output(
        root,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
        "--",
        *paths,
    )
    if status:
        raise ValueError(
            "distributed source files are dirty or untracked; commit the exact "
            f"distribution before vendoring:\n{status}"
        )


def existing_vendor_errors(target: Path) -> list[str]:
    """Return integrity errors for an existing lock, or [] when no lock exists."""

    lock_path = target / ".agents" / "governance.lock.json"
    if not lock_path.exists():
        return []
    if not lock_path.is_file():
        return ["existing governance lock is not a regular file"]

    try:
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read existing governance lock: {exc}"]

    files = lock.get("files")
    if not isinstance(files, list) or not files:
        return ["existing governance lock contains no files"]

    errors: list[str] = []
    for entry in files:
        if not isinstance(entry, dict):
            errors.append("existing lock has an invalid file entry")
            continue
        relative = entry.get("path")
        expected_sha = entry.get("sha256")
        expected_size = entry.get("size")
        if not isinstance(relative, str):
            errors.append("existing lock file entry has no path")
            continue
        try:
            path = safe_destination(target, relative)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not path.is_file():
            errors.append(f"missing previously vendored file: {relative}")
            continue
        data = path.read_bytes()
        if len(data) != expected_size or sha256_bytes(data) != expected_sha:
            errors.append(f"previously vendored file was modified: {relative}")
    return errors


def bootstrap_files(root: Path) -> tuple[tuple[str, Path], ...]:
    return (
        ("AGENTS.md", root / ".agents/templates/consumer/AGENTS.md"),
        (".agents/local/README.md", root / ".agents/templates/consumer/LOCAL_README.md"),
        ("docs/specs/README.md", root / ".agents/templates/consumer/SPECS_README.md"),
    )


def validate_adoption_fields(
    adoption_status: str,
    prepared_by: str,
    prepared_at: str,
    accepted_by: str | None,
    accepted_at: str | None,
) -> None:
    if adoption_status not in ADOPTION_STATUSES:
        raise ValueError("adoption_status must be proposed or accepted")
    if not prepared_by.strip():
        raise ValueError("prepared_by must not be empty")
    prepared_time = parse_timestamp(prepared_at, "prepared_at")

    if adoption_status == "proposed":
        if accepted_by is not None or accepted_at is not None:
            raise ValueError(
                "proposed adoption must not claim accepted_by or accepted_at"
            )
        return

    if accepted_by is None or not accepted_by.strip():
        raise ValueError("accepted adoption requires accepted_by")
    if accepted_at is None:
        raise ValueError("accepted adoption requires accepted_at")
    accepted_time = parse_timestamp(accepted_at, "accepted_at")
    if accepted_time < prepared_time:
        raise ValueError("accepted_at must not precede prepared_at")


def plan_vendor(
    root: Path,
    target: Path,
    source_commit: str,
    prepared_by: str,
    prepared_at: str,
    adoption_status: str = "proposed",
    accepted_by: str | None = None,
    accepted_at: str | None = None,
    *,
    verify_source_revision: bool = True,
    allow_dirty_vendored: bool = False,
) -> tuple[list[tuple[str, bytes, str]], dict[str, Any]]:
    if not COMMIT_RE.fullmatch(source_commit):
        raise ValueError("source_commit must be a lowercase 40-hex commit")
    if not target.exists() or not target.is_dir():
        raise ValueError("target must be an existing directory")
    validate_adoption_fields(
        adoption_status, prepared_by, prepared_at, accepted_by, accepted_at
    )

    manifest, manifest_raw = load_manifest(root)
    if verify_source_revision:
        validate_source_checkout(root, source_commit, manifest)

    existing_errors = existing_vendor_errors(target)
    if existing_errors and not allow_dirty_vendored:
        detail = "\n".join(f"  - {error}" for error in existing_errors)
        raise ValueError(
            "existing vendored governance does not match its lock; refusing to "
            "overwrite local changes. Reconcile or pass --allow-dirty-vendored "
            f"explicitly:\n{detail}"
        )

    operations: list[tuple[str, bytes, str]] = []
    locked_files: list[dict[str, Any]] = []

    for entry in manifest["files"]:
        relative = str(entry["path"])
        data = (root / relative).read_bytes()
        destination = safe_destination(target, relative)
        action = "replace" if destination.exists() else "create"
        operations.append((relative, data, action))
        locked_files.append(
            {
                "path": relative,
                "sha256": sha256_bytes(data),
                "size": len(data),
            }
        )

    for relative, template in bootstrap_files(root):
        destination = safe_destination(target, relative)
        if not destination.exists():
            operations.append((relative, template.read_bytes(), "create-local-template"))

    lock: dict[str, Any] = {
        "schema_version": 1,
        "distribution": manifest["distribution"],
        "version": manifest["version"],
        "source_repository": SOURCE_REPOSITORY,
        "source_commit": source_commit,
        "distribution_manifest_sha256": sha256_bytes(manifest_raw),
        "adoption": {
            "mode": "vendored",
            "status": adoption_status,
            "prepared_by": prepared_by,
            "prepared_at": prepared_at,
            "accepted_by": accepted_by,
            "accepted_at": accepted_at,
        },
        "files": locked_files,
    }
    lock_data = (json.dumps(lock, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    lock_relative = ".agents/governance.lock.json"
    lock_destination = safe_destination(target, lock_relative)
    operations.append(
        (lock_relative, lock_data, "replace" if lock_destination.exists() else "create")
    )
    return operations, lock


def atomic_write(destination: Path, data: bytes) -> None:
    if destination.is_symlink():
        raise OSError(f"refusing to replace symlink: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def apply_operations(target: Path, operations: list[tuple[str, bytes, str]]) -> None:
    for relative, data, _action in operations:
        atomic_write(safe_destination(target, relative), data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--prepared-by", required=True)
    parser.add_argument(
        "--prepared-at",
        default=None,
        help="ISO-8601 timestamp; defaults to current UTC time",
    )
    parser.add_argument(
        "--adoption-status",
        choices=sorted(ADOPTION_STATUSES),
        default="proposed",
    )
    parser.add_argument("--accepted-by", default=None)
    parser.add_argument(
        "--accepted-at",
        default=None,
        help="required for accepted adoption; defaults to current UTC time",
    )
    parser.add_argument(
        "--allow-dirty-vendored",
        action="store_true",
        help="explicitly replace files that no longer match the existing lock",
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    prepared_at = args.prepared_at or utc_now()
    accepted_at = args.accepted_at
    if args.adoption_status == "accepted" and accepted_at is None:
        accepted_at = utc_now()

    try:
        operations, _lock = plan_vendor(
            source_root(),
            args.target,
            args.source_commit,
            args.prepared_by,
            prepared_at,
            args.adoption_status,
            args.accepted_by,
            accepted_at,
            allow_dirty_vendored=args.allow_dirty_vendored,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"vendor plan failed: {exc}", file=sys.stderr)
        return 2

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"{mode}: {len(operations)} file operations")
    for relative, _data, action in operations:
        print(f"  {action:21s} {relative}")

    if not args.apply:
        print("No files written. Re-run with --apply after reviewing the plan.")
        return 0

    try:
        apply_operations(args.target, operations)
    except OSError as exc:
        print(f"vendor apply failed: {exc}", file=sys.stderr)
        return 2

    print("Governance files and lock written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
