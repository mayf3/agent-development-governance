from __future__ import annotations

import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build_manifest = load_module("build_manifest", ROOT / "tools/build_manifest.py")
vendor = load_module("vendor", ROOT / "tools/vendor.py")
verify_governance = load_module(
    "verify_governance", ROOT / ".agents/tools/verify_governance.py"
)


class DistributionToolsTest(unittest.TestCase):
    def plan(
        self,
        target: Path,
        source_commit: str = "a" * 40,
        adoption_status: str = "proposed",
    ):
        accepted = adoption_status == "accepted"
        return vendor.plan_vendor(
            ROOT,
            target,
            source_commit,
            "test-author",
            "2026-08-18T00:00:00Z",
            adoption_status,
            "test-maintainer" if accepted else None,
            "2026-08-18T00:01:00Z" if accepted else None,
            verify_source_revision=False,
        )

    def test_manifest_matches_distributed_files(self) -> None:
        expected = build_manifest.build_manifest(ROOT)
        actual = json.loads(
            (ROOT / "distribution/manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(expected, actual)

    def test_manifest_includes_mode_router_and_local_verifier(self) -> None:
        manifest = build_manifest.build_manifest(ROOT)
        paths = {entry["path"] for entry in manifest["files"]}
        self.assertIn(".agents/skills/spec-governance/SKILL.md", paths)
        for mode in ("PREFLIGHT", "AUTHOR", "REVIEW", "COMPLIANCE"):
            self.assertIn(
                f".agents/skills/spec-governance/modes/{mode}.md", paths
            )
        self.assertIn(".agents/tools/verify_governance.py", paths)
        self.assertTrue(all(path.startswith(".agents/") for path in paths))

    def test_vendor_proposed_adoption_and_tamper_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            operations, lock = self.plan(target)
            vendor.apply_operations(target, operations)

            self.assertEqual([], verify_governance.verify(target))
            self.assertTrue(
                any("adoption is not accepted" in error for error in verify_governance.verify(target, require_accepted=True))
            )
            self.assertEqual("a" * 40, lock["source_commit"])
            self.assertEqual("proposed", lock["adoption"]["status"])
            self.assertIsNone(lock["adoption"]["accepted_by"])
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / ".agents/local/README.md").is_file())
            self.assertTrue((target / "docs/specs/README.md").is_file())

            tampered = target / ".agents/README.md"
            tampered.write_text(
                tampered.read_text(encoding="utf-8") + "\nTAMPERED\n",
                encoding="utf-8",
            )
            errors = verify_governance.verify(target)
            self.assertTrue(any("mismatch" in error for error in errors))

    def test_vendor_can_finalize_accepted_adoption(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            operations, lock = self.plan(target, adoption_status="accepted")
            vendor.apply_operations(target, operations)

            self.assertEqual(
                [], verify_governance.verify(target, require_accepted=True)
            )
            self.assertEqual("accepted", lock["adoption"]["status"])
            self.assertEqual("test-maintainer", lock["adoption"]["accepted_by"])

    def test_vendor_refuses_to_overwrite_dirty_vendored_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            operations, _lock = self.plan(target)
            vendor.apply_operations(target, operations)
            shared = target / ".agents/README.md"
            shared.write_text("LOCAL MUTATION\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
                self.plan(target, source_commit="b" * 40)

            operations, _lock = vendor.plan_vendor(
                ROOT,
                target,
                "b" * 40,
                "test-author",
                "2026-08-18T00:02:00Z",
                verify_source_revision=False,
                allow_dirty_vendored=True,
            )
            vendor.apply_operations(target, operations)
            self.assertEqual([], verify_governance.verify(target))

    def test_vendor_does_not_overwrite_local_extensions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            local = target / ".agents/local/README.md"
            local.parent.mkdir(parents=True)
            local.write_text("LOCAL RULES\n", encoding="utf-8")
            agents = target / "AGENTS.md"
            agents.write_text("LOCAL ENTRY\n", encoding="utf-8")

            operations, _lock = self.plan(target, source_commit="b" * 40)
            vendor.apply_operations(target, operations)

            self.assertEqual("LOCAL RULES\n", local.read_text(encoding="utf-8"))
            self.assertEqual("LOCAL ENTRY\n", agents.read_text(encoding="utf-8"))

    def test_adoption_metadata_rejects_false_acceptance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            with self.assertRaisesRegex(ValueError, "must not claim"):
                vendor.plan_vendor(
                    ROOT,
                    target,
                    "c" * 40,
                    "test-author",
                    "2026-08-18T00:00:00Z",
                    "proposed",
                    "test-maintainer",
                    "2026-08-18T00:01:00Z",
                    verify_source_revision=False,
                )

    def test_local_markdown_links_resolve(self) -> None:
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        errors: list[str] = []
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path).resolve()
                if not resolved.exists():
                    errors.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual([], errors)

    def test_json_files_parse(self) -> None:
        for path in ROOT.rglob("*.json"):
            if ".git" in path.parts:
                continue
            json.loads(path.read_text(encoding="utf-8"))

    def test_bootstrap_contract_coverage_is_bidirectional(self) -> None:
        path = ROOT / "docs/specs/AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0.md"
        text = path.read_text(encoding="utf-8")
        contracts = set(re.findall(r"^### (CTR-[A-Z0-9-]+) —", text, re.MULTILINE))
        acceptance_refs: set[str] = set()
        for line in re.findall(r"^- Contracts: (.+)$", text, re.MULTILINE):
            acceptance_refs.update(re.findall(r"`(CTR-[A-Z0-9-]+)`", line))
        coverage_rows = set(
            re.findall(r"^\| `(CTR-[A-Z0-9-]+)` \|", text, re.MULTILINE)
        )
        self.assertTrue(contracts)
        self.assertEqual(contracts, acceptance_refs)
        self.assertEqual(contracts, coverage_rows)

    def test_adoption_template_has_required_sections_in_order(self) -> None:
        path = ROOT / ".agents/templates/GOVERNANCE_ADOPTION_SPEC_TEMPLATE.md"
        text = path.read_text(encoding="utf-8")
        required = [
            "## 1. Goal",
            "## 2. Scope and non-goals",
            "## 3. Authority and dependencies",
            "## 4. Current State",
            "## 5. Observations",
            "## 6. Claims and assumptions",
            "## 7. Evidence relations",
            "## 8. Decisions",
            "## 9. Contracts",
            "## 10. Acceptance",
            "## 11. Alternatives and disposition",
            "## 12. Migration, compatibility, and rollback",
            "## 13. Open questions",
        ]
        positions = [text.index(section) for section in required]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("### EVD-ADOPT-001", text)
        self.assertIn("### EVD-ADOPT-002", text)

    def test_adoption_template_contract_coverage_and_acceptance_fields(self) -> None:
        path = ROOT / ".agents/templates/GOVERNANCE_ADOPTION_SPEC_TEMPLATE.md"
        text = path.read_text(encoding="utf-8")
        contracts = set(re.findall(r"^### (CTR-ADOPT-[A-Z0-9-]+) —", text, re.MULTILINE))
        acceptance_refs: set[str] = set()
        items = re.split(r"(?=^### ACC-ADOPT-[A-Z0-9-]+ —)", text, flags=re.MULTILINE)
        acceptance_items = [item for item in items if item.startswith("### ACC-ADOPT-")]
        self.assertTrue(acceptance_items)
        for item in acceptance_items:
            for field in (
                "- Contracts:",
                "- Method:",
                "- Environment:",
                "- Required evidence:",
                "- Expected result:",
                "- Failure condition:",
            ):
                self.assertIn(field, item)
            acceptance_refs.update(re.findall(r"`(CTR-ADOPT-[A-Z0-9-]+)`", item.split("### Contract coverage", 1)[0]))
        coverage_rows = set(re.findall(r"^\| `(CTR-ADOPT-[A-Z0-9-]+)` \|", text, re.MULTILINE))
        self.assertEqual(contracts, acceptance_refs)
        self.assertEqual(contracts, coverage_rows)

    def test_bootstrap_decisions_and_acceptance_have_required_fields(self) -> None:
        path = ROOT / "docs/specs/AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0.md"
        text = path.read_text(encoding="utf-8")
        decision_items = [
            item for item in re.split(r"(?=^### DEC-[A-Z0-9-]+ —)", text, flags=re.MULTILINE)
            if item.startswith("### DEC-")
        ]
        self.assertTrue(decision_items)
        for item in decision_items:
            for field in (
                "- Decision owner:",
                "- Decision:",
                "- Rejected alternative",
                "- Reason:",
                "- Owner input remaining:",
            ):
                self.assertIn(field, item)
        acceptance_items = [
            item for item in re.split(r"(?=^### ACC-GOV-[A-Z0-9-]+ —)", text, flags=re.MULTILINE)
            if item.startswith("### ACC-GOV-")
        ]
        self.assertTrue(acceptance_items)
        for item in acceptance_items:
            for field in (
                "- Contracts:",
                "- Method:",
                "- Environment:",
                "- Required evidence:",
                "- Expected result:",
                "- Failure condition:",
            ):
                self.assertIn(field, item)


    def test_distribution_version_is_coherent(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        manifest = json.loads(
            (ROOT / "distribution/manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(version, manifest["version"])
        for relative in (
            ".agents/README.md",
            ".agents/protocol/SPEC_GOVERNANCE_V0.md",
            ".agents/protocol/SPEC_FORMAT_V0.md",
            "README.md",
        ):
            self.assertIn(version, (ROOT / relative).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
