from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_governance_v1_routing import blocker, mandate, record, validator

ROOT = Path(__file__).resolve().parents[1]


def operation_finding():
    finding = blocker("REQUIRED_GATE_FAILURE", "EXECUTION_MANDATE",
                      "fixture operation mandate", "production approval unavailable",
                      "only the production operation is unauthorized", "obtain operation authority")
    finding.pop("affected_readiness")
    return finding


class Pr21ReviewRegressionTest(unittest.TestCase):
    def test_current_record_requires_v2_and_explicit_blocker_scope(self):
        finding = operation_finding()
        finding["affected_readiness"] = ["operation_allowed"]
        current = record(findings=[finding], operation_allowed="NO")
        current["schema_version"] = 2
        self.assertEqual([], validator.validate_route(current))
        del finding["affected_readiness"]
        errors = validator.validate_route(current)
        self.assertTrue(any("affected_readiness" in error for error in errors), errors)

    def test_default_validation_cannot_claim_legacy_omission_for_current_use(self):
        legacy = record(findings=[operation_finding()])
        legacy["schema_version"] = 1
        errors = validator.validate_route(legacy)
        self.assertTrue(any("schema_version" in error for error in errors), errors)

    def test_legacy_cli_is_explicit_and_not_current_readiness(self):
        legacy = record(findings=[operation_finding()], operation_allowed="NO")
        legacy["schema_version"] = 1
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "legacy.json"
            path.write_text(json.dumps(legacy))
            result = subprocess.run([sys.executable, str(ROOT / ".agents/tools/validate_governance_route.py"),
                                     "--legacy-inspection", str(path)],
                                    text=True, capture_output=True, timeout=10)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("not current readiness", result.stdout.lower())

    def test_record_field_cannot_select_legacy_inspection(self):
        current = record(findings=[operation_finding()], operation_allowed="NO")
        current["legacy_inspection"] = True
        errors = validator.validate_route(current)
        self.assertTrue(any("affected_readiness" in error for error in errors), errors)

    def test_legacy_inspection_rejects_current_record_version(self):
        errors = validator.validate_route(record(), legacy_inspection=True)
        self.assertTrue(any("schema_version" in error for error in errors), errors)

    def test_legacy_movement_keeps_original_flag_semantics(self):
        historical = record(target_changed=True, full_rereview=True)
        historical["schema_version"] = 1
        self.assertEqual([], validator.validate_route(historical, legacy_inspection=True))
        historical["review"]["full_rereview_required"] = False
        self.assertTrue(validator.validate_route(historical, legacy_inspection=True))

    def test_legacy_gap_does_not_require_new_diagnosis_fields(self):
        historical = record(action="NEW", accepted_owner=False,
                            implementation_authority="unknown", spec_gap="LOAD_BEARING",
                            implementation_allowed="NO", merge_ready="NO", operation_allowed="NO",
                            next_action="RE_PREFLIGHT")
        historical["schema_version"] = 1
        historical.pop("spec_gap_detail")
        self.assertEqual([], validator.validate_route(historical, legacy_inspection=True))

    def test_legacy_operation_only_blocker_preserves_unrelated_readiness(self):
        value = record(findings=[operation_finding()], operation_allowed="NO")
        value["schema_version"] = 1
        before = copy.deepcopy(value)
        self.assertEqual([], validator.validate_route(value, legacy_inspection=True))
        self.assertEqual(before, value, "validation cannot invent or rewrite blocker scope")

    def test_legacy_omission_retains_schema_v1_shape_validation(self):
        # Legacy validity is not a new readiness or authorization proof.
        value = record(findings=[operation_finding()])
        value["schema_version"] = 1
        self.assertEqual([], validator.validate_route(value, legacy_inspection=True))
        self.assertNotIn("affected_readiness", value["findings"][0])

    def test_explicit_operation_blocker_still_rejects_operation_yes(self):
        finding = operation_finding()
        finding["affected_readiness"] = ["operation_allowed"]
        value = record(findings=[finding], operation_allowed="YES")
        errors = validator.validate_route(value)
        self.assertTrue(any("open Blocker" in error for error in errors), errors)

    def test_explicit_scope_with_unrelated_ready_work_is_valid(self):
        finding = operation_finding()
        finding["affected_readiness"] = ["operation_allowed"]
        self.assertEqual([], validator.validate_route(record(findings=[finding], operation_allowed="NO")))

    def test_explicit_malformed_scope_is_not_treated_as_legacy_omission(self):
        for scope in (None, [], {}, False, "operation_allowed", ["unknown"], [[]]):
            with self.subTest(scope=scope):
                finding = operation_finding()
                finding["affected_readiness"] = scope
                errors = validator.validate_route(record(findings=[finding], operation_allowed="NO"))
                self.assertTrue(any("affected_readiness" in error for error in errors), errors)

    def test_legacy_scope_does_not_bypass_operation_mandate(self):
        value = record(findings=[operation_finding()], route_stage="OPERATION",
                       implementation_allowed="NO", merge_ready="NO", operation_allowed="YES",
                       mandate_value=mandate("INVALID"))
        value["schema_version"] = 1
        errors = validator.validate_route(value, legacy_inspection=True)
        self.assertTrue(any("invalid Execution Mandate" in error for error in errors), errors)

    def test_legacy_scope_does_not_bypass_legal_blocker_source(self):
        finding = operation_finding()
        finding["source_type"] = "REVIEWER_PREFERENCE"
        value = record(findings=[finding], operation_allowed="NO")
        value["schema_version"] = 1
        errors = validator.validate_route(value, legacy_inspection=True)
        self.assertTrue(any("legal blocker source" in error for error in errors), errors)

    def test_real_cli_accepts_legacy_operation_only_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "legacy-route.json"
            value = record(findings=[operation_finding()], operation_allowed="NO")
            value["schema_version"] = 1
            path.write_text(json.dumps(value))
            result = subprocess.run([sys.executable, str(ROOT / ".agents/tools/validate_governance_route.py"), "--legacy-inspection", str(path)],
                                    text=True, capture_output=True, check=False, timeout=10)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("not current readiness", result.stdout.lower())

    def test_grammar_has_no_unaccepted_numeric_cutoff(self):
        text = (ROOT / ".agents/README.md").read_text()
        self.assertNotIn("At three unsuccessful review/repair rounds", text)
        self.assertNotIn("do not silently start a fourth expansion", text)

    def test_brief_does_not_reintroduce_unaccepted_numeric_cutoff(self):
        text = (ROOT / ".agents/templates/CHANGE_BRIEF_TEMPLATE.md").read_text()
        self.assertNotIn("At three unsuccessful rounds", text)


if __name__ == "__main__":
    unittest.main()
