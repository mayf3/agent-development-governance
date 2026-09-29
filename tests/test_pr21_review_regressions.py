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
    return blocker("REQUIRED_GATE_FAILURE", "EXECUTION_MANDATE",
                   "fixture operation mandate", "production approval unavailable",
                   "only the production operation is unauthorized", "obtain operation authority")


class Pr21ReviewRegressionTest(unittest.TestCase):
    def test_legacy_operation_only_blocker_preserves_unrelated_readiness(self):
        value = record(findings=[operation_finding()], operation_allowed="NO")
        before = copy.deepcopy(value)
        self.assertEqual([], validator.validate_route(value))
        self.assertEqual(before, value, "validation cannot invent or rewrite blocker scope")

    def test_legacy_omission_retains_schema_v1_shape_validation(self):
        # Legacy validity is not a new readiness or authorization proof.
        value = record(findings=[operation_finding()])
        self.assertEqual([], validator.validate_route(value))
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
        errors = validator.validate_route(value)
        self.assertTrue(any("invalid Execution Mandate" in error for error in errors), errors)

    def test_legacy_scope_does_not_bypass_legal_blocker_source(self):
        finding = operation_finding()
        finding["source_type"] = "REVIEWER_PREFERENCE"
        errors = validator.validate_route(record(findings=[finding], operation_allowed="NO"))
        self.assertTrue(any("legal blocker source" in error for error in errors), errors)

    def test_real_cli_accepts_legacy_operation_only_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "legacy-route.json"
            path.write_text(json.dumps(record(findings=[operation_finding()], operation_allowed="NO")))
            result = subprocess.run([sys.executable, str(ROOT / ".agents/tools/validate_governance_route.py"), str(path)],
                                    text=True, capture_output=True, check=False, timeout=10)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("internally consistent", result.stdout)

    def test_grammar_has_no_unaccepted_numeric_cutoff(self):
        text = (ROOT / ".agents/README.md").read_text()
        self.assertNotIn("At three unsuccessful review/repair rounds", text)
        self.assertNotIn("do not silently start a fourth expansion", text)

    def test_brief_does_not_reintroduce_unaccepted_numeric_cutoff(self):
        text = (ROOT / ".agents/templates/CHANGE_BRIEF_TEMPLATE.md").read_text()
        self.assertNotIn("At three unsuccessful rounds", text)


if __name__ == "__main__":
    unittest.main()
