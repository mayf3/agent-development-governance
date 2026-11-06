from __future__ import annotations

import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path

from test_spec_transition import transition


class MalformedListFormatCorrectionTest(unittest.TestCase):
    SPEC_ID = "CODE_STRUCTURE_GUARDRAILS_V3_TRANSITION_EXCEPTION_V1"

    def record(self, supersedes):
        return {
            "spec_id": self.SPEC_ID,
            "status": "accepted",
            "spec_kind": "implementation",
            "authority_level": "governing_spec",
            "implementation_authority": "contracts",
            "scope": ["fixture"],
            "governed_by": [],
            "external_authorities": [],
            "supersedes": supersedes,
            "superseded_by": None,
            "owners": ["fixture-owner"],
        }

    def validate(self, old, new, registered=True, **kwargs):
        return transition.validate_transition(
            [self.record(old)],
            [self.record(new)],
            format_correction_specs=frozenset({self.SPEC_ID} if registered else ()),
            **kwargs,
        )

    def assert_mutation(self, errors):
        self.assertTrue(any("mutates accepted supersedes metadata" in e for e in errors), errors)

    def test_registered_list_of_objects_to_empty_passes(self):
        self.assertEqual([], self.validate([{"authority": "OLD_V1"}], []))

    def test_other_illegal_elements_to_empty_pass(self):
        for value in (None, 1, True, [], "OLD_V1#CTR-001", "arbitrary", ""):
            with self.subTest(value=value):
                self.assertEqual([], self.validate([value], []))

    def test_mixed_list_to_empty_passes_when_no_real_binding_is_removed(self):
        self.assertEqual([], self.validate(["UNBOUND_V1", {"invalid": True}], []))

    def test_unregistered_or_wrong_id_list_correction_fails(self):
        old = [{"authority": "OLD_V1"}]
        self.assert_mutation(self.validate(old, [], registered=False))
        errors = transition.validate_transition(
            [self.record(old)], [self.record([])],
            format_correction_specs=frozenset({"OTHER_V1"}),
        )
        self.assert_mutation(errors)

    def test_list_of_objects_to_nonempty_or_other_forms_fails(self):
        for new in (["OTHER_V1"], [{"other": True}], {}, None, "", 0, False):
            with self.subTest(new=new):
                self.assert_mutation(self.validate([{"old": True}], new))

    def test_record_marker_is_collected_separately_from_hard_errors(self):
        for value in ({"old": True}, [{"old": True}], ["OLD_V1", None]):
            with self.subTest(value=value):
                markers = []
                errors = transition.validate_metadata(
                    self.record(value), format_correction_candidates=markers,
                )
                self.assertEqual([], errors)
                self.assertEqual(1, len(markers))
                self.assertIn("FORMAT_CORRECTION_CANDIDATE", markers[0])

    def test_unresolved_or_new_malformed_candidate_fails_even_when_registered(self):
        record = self.record([{"old": True}])
        for base in ([copy.deepcopy(record)], []):
            with self.subTest(base=base):
                errors = transition.validate_transition(
                    base, [record], format_correction_specs=frozenset({self.SPEC_ID}),
                )
                self.assertTrue(errors)
                self.assertTrue(any("FORMAT_CORRECTION_CANDIDATE" in e for e in errors))

    def test_valid_strict_legacy_and_duplicate_id_lists_cannot_be_cleared(self):
        for old in (["OLD_V1"], ["OLD_V1_HISTORY_AMENDMENT"], ["OLD_V1", "OLD_V1"]):
            with self.subTest(old=old):
                self.assert_mutation(self.validate(old, []))
                markers = []
                transition.validate_metadata(self.record(old), format_correction_candidates=markers)
                self.assertEqual([], markers)

    def test_nonlist_scalars_remain_hard_errors_and_ineligible(self):
        for old in (None, "OLD_V1", 1, False):
            with self.subTest(old=old):
                markers = []
                self.assertTrue(transition.validate_metadata(
                    self.record(old), format_correction_candidates=markers,
                ))
                self.assertEqual([], markers)
                self.assert_mutation(self.validate(old, []))

    def test_correction_does_not_allow_other_immutable_field_changes(self):
        base = self.record([{"old": True}])
        candidate = self.record([])
        candidate["scope"] = ["changed"]
        errors = transition.validate_transition(
            [base], [candidate], format_correction_specs=frozenset({self.SPEC_ID}),
        )
        self.assertTrue(any("mutates accepted authority field: scope" in e for e in errors))

    def test_correction_cannot_remove_an_existing_backlink(self):
        predecessor = self.record([])
        predecessor.update(spec_id="OLD_V1", status="superseded", superseded_by=self.SPEC_ID)
        base = [predecessor, self.record(["OLD_V1", {"invalid": True}])]
        candidate = [copy.deepcopy(predecessor), self.record([])]
        errors = transition.validate_transition(
            base, candidate, format_correction_specs=frozenset({self.SPEC_ID}),
        )
        self.assertTrue(any("does not backlink superseded authority: OLD_V1" in e for e in errors))

    def test_superseded_record_correction_keeps_successor_binding(self):
        base = self.record([{"old": True}])
        base.update(status="superseded", superseded_by="SUCCESSOR_V1")
        successor = self.record([self.SPEC_ID])
        successor["spec_id"] = "SUCCESSOR_V1"
        candidate = copy.deepcopy(base)
        candidate["supersedes"] = []
        self.assertEqual([], transition.validate_transition(
            [base, successor], [candidate, copy.deepcopy(successor)],
            format_correction_specs=frozenset({self.SPEC_ID}),
        ))
        candidate["superseded_by"] = "DIFFERENT_V1"
        errors = transition.validate_transition(
            [base, successor], [candidate, successor],
            format_correction_specs=frozenset({self.SPEC_ID}),
        )
        self.assertTrue(any("mutates historical successor backlink" in e for e in errors))

    def test_cli_registration_and_visible_classification(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / "base.json"
            candidate = Path(tmp) / "candidate.json"
            base.write_text(json.dumps([self.record([{"old": True}])]), encoding="utf-8")
            candidate.write_text(json.dumps([self.record([])]), encoding="utf-8")
            args = ["--base", str(base), "--candidate", str(candidate)]
            for registered, expected in ((False, 1), (True, 0)):
                with self.subTest(registered=registered):
                    out, err = io.StringIO(), io.StringIO()
                    invocation = args + (["--format-correction-spec", self.SPEC_ID] if registered else [])
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        rc = transition.main(invocation)
                    self.assertEqual(expected, rc)
                    if registered:
                        self.assertIn("FORMAT_CORRECTION", out.getvalue())
                        self.assertIn(self.SPEC_ID, out.getvalue())
                    else:
                        self.assertIn("mutates accepted supersedes metadata", err.getvalue())


if __name__ == "__main__":
    unittest.main()
