from __future__ import annotations

import unittest

from test_governance_v1_routing import blocker, record, validator


def review_record(*, moved=False, base_impact=False, scope="DELTA", basis=None):
    value = record(target_changed=moved, relevant_base_impact=base_impact,
                   full_rereview=scope == "FULL")
    value["review"].update(
        scope=scope,
        scope_reason="Only the receipt or the bounded repair and its dependencies changed",
        impact_evidence="Fixture diff and affected-Contract map at the recorded heads",
    )
    if basis is not None:
        value["review"]["full_review_basis"] = basis
    return value


def gap_record():
    return record(action="NEW", accepted_owner=False,
                  implementation_authority="unknown", spec_gap="LOAD_BEARING",
                  implementation_allowed="NO", merge_ready="NO", operation_allowed="NO",
                  next_action="RE_PREFLIGHT")


class BoundedDeliveryReviewTest(unittest.TestCase):
    def assert_valid(self, value):
        self.assertEqual([], validator.validate_route(value))

    def assert_invalid(self, value, fragment):
        errors = validator.validate_route(value)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_receipt_only_head_change_uses_delta_recheck(self):
        self.assert_valid(review_record(moved=True))

    def test_bounded_semantic_repair_uses_delta_review(self):
        value = review_record(moved=True)
        value["review"]["scope_reason"] = "One blocker fix and its dependent invariants"
        self.assert_valid(value)

    def test_relevant_base_change_need_not_force_full_review(self):
        self.assert_valid(review_record(base_impact=True))

    def test_movement_without_scope_is_not_silently_accepted(self):
        value = record(target_changed=True, full_rereview=True)
        self.assert_invalid(value, "review.scope")

    def test_movement_cannot_skip_final_head_recheck(self):
        self.assert_invalid(review_record(moved=True, scope="NONE"), "DELTA or FULL")

    def test_delta_review_requires_impact_evidence(self):
        value = review_record(moved=True)
        value["review"].pop("impact_evidence")
        self.assert_invalid(value, "impact_evidence")

    def test_delta_review_requires_scope_reason(self):
        value = review_record(moved=True)
        value["review"]["scope_reason"] = "  "
        self.assert_invalid(value, "scope_reason")

    def test_full_review_requires_an_explicit_basis(self):
        self.assert_invalid(review_record(moved=True, scope="FULL"), "full_review_basis")

    def test_unbounded_impact_allows_full_review(self):
        self.assert_valid(review_record(moved=True, scope="FULL", basis="UNBOUNDED_IMPACT"))

    def test_initial_full_review_does_not_require_head_movement(self):
        self.assert_valid(review_record(scope="FULL", basis="INITIAL_REVIEW"))

    def test_accepted_full_gate_can_be_rechecked_without_head_movement(self):
        value = review_record(scope="FULL", basis="ACCEPTED_FULL_GATE")
        value["review"]["scope_reason"] = "Fixture accepted operation gate G3, runtime pre-state changed"
        self.assert_valid(value)

    def test_head_change_is_not_itself_a_full_review_basis(self):
        self.assert_invalid(review_record(moved=True, scope="FULL", basis="HEAD_CHANGED"),
                            "full_review_basis")

    def test_delta_scope_cannot_claim_full_review(self):
        value = review_record(moved=True)
        value["review"]["full_rereview_required"] = True
        self.assert_invalid(value, "full_rereview_required")

    def test_explicit_invalid_review_scope_is_rejected(self):
        self.assert_invalid(review_record(scope="MAYBE"), "review.scope")

    def test_malformed_scope_is_a_validation_error_not_a_crash(self):
        for invalid in (None, [], {}, True, 3):
            with self.subTest(invalid=invalid):
                value = review_record(scope="NONE")
                value["review"]["scope"] = invalid
                self.assert_invalid(value, "review.scope")

    def test_malformed_full_review_basis_is_a_validation_error(self):
        for invalid in ([], {}, False, "", "  "):
            with self.subTest(invalid=invalid):
                self.assert_invalid(review_record(scope="FULL", basis=invalid), "full_review_basis")

    def test_unchanged_legacy_route_remains_valid(self):
        self.assert_valid(record())

    def test_boolean_movement_flags_are_still_required(self):
        value = review_record(moved=True)
        value["review"]["target_head_changed"] = "yes"
        self.assert_invalid(value, "booleans")

    def test_load_bearing_label_without_diagnosis_is_rejected(self):
        value = gap_record()
        value.pop("spec_gap_detail")
        self.assert_invalid(value, "spec_gap_detail")

    def test_each_missing_decision_diagnosis_field_is_required(self):
        for field in gap_record()["spec_gap_detail"]:
            with self.subTest(field=field):
                value = gap_record()
                value["spec_gap_detail"].pop(field)
                self.assert_invalid(value, field)

    def test_diagnosis_fields_reject_blank_and_non_text(self):
        for invalid in ("", "  ", None, False, [], {}):
            with self.subTest(invalid=invalid):
                value = gap_record()
                value["spec_gap_detail"]["counterexample"] = invalid
                self.assert_invalid(value, "counterexample")

    def test_concrete_missing_permission_remains_stopped(self):
        self.assert_valid(gap_record())
        value = gap_record()
        value["readiness"]["operation_allowed"] = "YES"
        self.assert_invalid(value, "load-bearing SPEC_GAP")

    def test_optional_hardening_needs_no_gap_diagnosis(self):
        value = record(findings=[{"kind": "FOLLOW_UP", "description": "Generalized replay framework"}])
        self.assert_valid(value)

    def test_spec_gap_finding_cannot_bypass_dependency_routing(self):
        value = record(findings=[{"kind": "SPEC_GAP", "load_bearing": True}])
        self.assert_invalid(value, "LOAD_BEARING")

    def test_non_load_bearing_gap_stays_advisory(self):
        self.assert_valid(record(spec_gap="NON_LOAD_BEARING",
                                 findings=[{"kind": "SPEC_GAP", "load_bearing": False}]))

    def test_real_blocker_cannot_coexist_with_ready_yes(self):
        finding = blocker("SECURITY_OR_DATA_LOSS", "ACCEPTED_PRODUCT_AUTHORITY",
                          "Fixture permission invariant", "Unauthorized principal gets access",
                          "Privilege escalation", "Reject the unauthorized principal")
        finding["affected_readiness"] = ["implementation_allowed", "merge_ready"]
        self.assert_invalid(record(findings=[finding]), "open Blocker")

    def test_real_blocker_remains_valid_when_dependent_work_is_stopped(self):
        finding = blocker("SECURITY_OR_DATA_LOSS", "ACCEPTED_PRODUCT_AUTHORITY",
                          "Fixture permission invariant", "Unauthorized principal gets access",
                          "Privilege escalation", "Reject the unauthorized principal")
        self.assert_valid(record(findings=[finding], implementation_allowed="NO", merge_ready="NO",
                                 operation_allowed="NO", next_action="RE_PREFLIGHT"))

    def test_blocker_may_scope_its_stop_to_the_dependent_boundary(self):
        finding = blocker("REQUIRED_GATE_FAILURE", "EXECUTION_MANDATE",
                          "Fixture production mandate", "Production approval expired",
                          "Operation not authorized", "Renew operation approval")
        finding["affected_readiness"] = ["operation_allowed"]
        self.assert_valid(record(findings=[finding], operation_allowed="NO"))

    def test_blocker_cannot_escape_by_naming_no_affected_boundary(self):
        finding = blocker("REQUIRED_GATE_FAILURE", "EXECUTION_MANDATE", "Fixture G1",
                          "Missing approval", "Unauthorized operation", "Get approval")
        finding["affected_readiness"] = []
        self.assert_invalid(record(findings=[finding]), "affected_readiness")

    def test_blocker_cannot_hide_in_not_applicable_boundary(self):
        finding = blocker("REQUIRED_GATE_FAILURE", "EXECUTION_MANDATE", "Fixture G1",
                          "Missing approval", "Unauthorized operation", "Get approval")
        finding["affected_readiness"] = ["operation_allowed"]
        self.assert_invalid(record(findings=[finding]), "explicitly NO")


if __name__ == "__main__":
    unittest.main()
