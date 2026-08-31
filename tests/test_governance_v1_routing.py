from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    path = ROOT / ".agents/tools/validate_governance_route.py"
    spec = importlib.util.spec_from_file_location("validate_governance_route", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_validator()


def mandate(status: str = "NOT_APPLICABLE", valid: bool = False) -> dict[str, object]:
    return {
        "status": status,
        "attributable": valid,
        "actor_bound": valid,
        "environment_bound": valid,
        "scope_bound": valid,
        "allowed_effects_bound": valid,
        "forbidden_effects_bound": valid,
        "done_when_bound": valid,
        "abort_conditions_bound": valid,
        "secret_handling_bound": valid,
        "receipt_bound": valid,
        "attempt_bounds_bound": valid,
        "self_issued": False,
    }


def record(
    *,
    action: str = "REUSE",
    accepted_owner: bool | None = True,
    ownership_known: bool = True,
    accepted_meaning_changed: bool = False,
    strict_addition: bool = False,
    proposed: bool = False,
    scope_changed: bool = False,
    ownership_changed: bool = False,
    decision_changed: bool = False,
    implementation_authority: str = "contracts",
    complexity: str = "BOUNDED",
    plan: str = "BRIEF",
    consequence: str = "LOW",
    assurance: str = "ROUTINE",
    runbook: bool = False,
    mandate_value: dict[str, object] | None = None,
    spec_gap: str = "NONE",
    evidence_required: bool = False,
    evidence_reviewability: str = "NOT_APPLICABLE",
    evidence_failure: str = "NONE",
    fabrication: bool = False,
    live_gap: bool = False,
    expansion_frozen: bool = False,
    auto_delete: bool = False,
    permanent_grandfather: bool = False,
    owner_disposition: bool = False,
    target_changed: bool = False,
    relevant_base_impact: bool = False,
    full_rereview: bool = False,
    implementation_allowed: str = "YES",
    merge_ready: str = "YES",
    operation_allowed: str = "NOT_APPLICABLE",
    done: bool = False,
    triggered: bool = False,
    next_action: str = "CONTINUE",
    findings: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "task_id": "case",
        "goal": "close the real gap",
        "current_gap": "declared behavior is not yet complete",
        "done_when": "declared bounded result is observed",
        "authority": {
            "declared_action": action,
            "ownership_known": ownership_known,
            "accepted_owner_exists": accepted_owner,
            "accepted_meaning_changed": accepted_meaning_changed,
            "accepted_strict_addition": strict_addition,
            "proposed_target_named": proposed,
            "proposal_scope_changed": scope_changed,
            "proposal_ownership_changed": ownership_changed,
            "proposal_decision_identity_changed": decision_changed,
            "implementation_authority": implementation_authority,
        },
        "plan": {"complexity": complexity, "level": plan},
        "assurance": {
            "failure_consequence": consequence,
            "level": assurance,
            "controlled_runbook_present": runbook,
        },
        "execution_mandate": mandate_value or mandate(),
        "spec_gap_dependency": spec_gap,
        "evidence": {
            "load_bearing_required": evidence_required,
            "reviewability": evidence_reviewability,
            "fabrication_observed": fabrication,
            "failure_class": evidence_failure,
        },
        "live_authority_gap": {
            "state": "DETECTED" if live_gap else "NONE",
            "expansion_frozen": expansion_frozen,
            "auto_delete": auto_delete,
            "permanent_grandfather": permanent_grandfather,
            "owner_disposition_present": owner_disposition,
        },
        "review": {
            "review_target_head": "a" * 40,
            "base_head": "b" * 40,
            "current_base_head": "c" * 40,
            "target_head_changed": target_changed,
            "relevant_base_impact": relevant_base_impact,
            "full_rereview_required": full_rereview,
        },
        "readiness": {
            "implementation_allowed": implementation_allowed,
            "merge_ready": merge_ready,
            "operation_allowed": operation_allowed,
        },
        "stop": {
            "done_when_met": done,
            "expansion_triggered": triggered,
            "next_action": next_action,
        },
        "findings": findings or [],
    }


class GovernanceV1RoutingTest(unittest.TestCase):
    def assert_valid(self, value: dict[str, object]) -> None:
        self.assertEqual([], validator.validate_route(value))

    def assert_invalid(self, value: dict[str, object], fragment: str) -> None:
        errors = validator.validate_route(value)
        self.assertTrue(any(fragment in error for error in errors), errors)

    # Three rollout canaries.
    def test_canary_forum_state_storage(self) -> None:
        self.assert_valid(record(
            action="REUSE", complexity="COMPLEX", plan="EXEC_PLAN",
            consequence="DURABLE_STATE", assurance="DURABLE",
            operation_allowed="NOT_APPLICABLE",
        ))

    def test_canary_disabled_workflow_admin_identity(self) -> None:
        self.assert_valid(record(
            action="REUSE", consequence="HIGH_RISK", assurance="CONTROLLED",
            runbook=True, mandate_value=mandate("VALID", True),
            operation_allowed="YES",
        ))

    def test_canary_auth_service_permission_gap(self) -> None:
        self.assert_valid(record(
            action="NEW", accepted_owner=False, implementation_authority="unknown",
            consequence="HIGH_RISK", assurance="CONTROLLED",
            spec_gap="LOAD_BEARING", live_gap=True, expansion_frozen=True,
            owner_disposition=False, implementation_allowed="NO", merge_ready="NO",
            operation_allowed="NO", next_action="OWNER_DECISION",
        ))

    # Four targeted failure regressions.
    def test_unrelated_base_movement_is_bounded_while_real_gap_blocks(self) -> None:
        self.assert_valid(record(
            action="NEW", accepted_owner=False, implementation_authority="unknown",
            complexity="COMPLEX", plan="EXEC_PLAN",
            consequence="DURABLE_STATE", assurance="DURABLE",
            spec_gap="LOAD_BEARING", implementation_allowed="NO", merge_ready="NO",
            operation_allowed="NO", full_rereview=False, next_action="RE_PREFLIGHT",
        ))
        bad = record(full_rereview=True)
        self.assert_invalid(bad, "full_rereview_required")

    def test_invalid_owner_mandate_blocks_operation_without_new_platform(self) -> None:
        value = record(
            action="REUSE", consequence="HIGH_RISK", assurance="CONTROLLED",
            runbook=True, mandate_value=mandate("INVALID", False),
            implementation_allowed="NO", merge_ready="NO", operation_allowed="NO",
            next_action="OWNER_DECISION",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["readiness"]["operation_allowed"] = "YES"
        self.assert_invalid(bad, "invalid Execution Mandate")

    def test_hidden_evidence_and_live_gap_are_contained(self) -> None:
        value = record(
            action="NEW", accepted_owner=False, implementation_authority="unknown",
            consequence="HIGH_RISK", assurance="CONTROLLED",
            spec_gap="LOAD_BEARING", evidence_required=True,
            evidence_reviewability="FAIL", evidence_failure="REQUIRED_GATE_FAILURE",
            live_gap=True, expansion_frozen=True, owner_disposition=False,
            implementation_allowed="NO", merge_ready="NO", operation_allowed="NO",
            next_action="OWNER_DECISION",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["live_authority_gap"]["auto_delete"] = True
        self.assert_invalid(bad, "must not auto-delete")

    def test_public_interface_cannot_be_demoted_to_reuse(self) -> None:
        value = record(
            action="NEW", accepted_owner=False, implementation_authority="unknown",
            complexity="COMPLEX", plan="EXEC_PLAN",
            consequence="DURABLE_STATE", assurance="DURABLE",
            spec_gap="LOAD_BEARING", implementation_allowed="NO", merge_ready="NO",
            operation_allowed="NO", next_action="RE_PREFLIGHT",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["authority"]["declared_action"] = "REUSE"
        self.assert_invalid(bad, "must be NEW")

    def test_named_proposal_decision_identity_change_is_new(self) -> None:
        good = record(
            action="NEW", accepted_owner=False, proposed=True, decision_changed=True,
            implementation_authority="unknown", implementation_allowed="NO",
            merge_ready="NO", operation_allowed="NO",
        )
        self.assert_valid(good)
        bad = copy.deepcopy(good)
        bad["authority"]["declared_action"] = "AMEND"
        self.assert_invalid(bad, "must be NEW")

    def test_false_evidence_requires_fabrication(self) -> None:
        value = record(
            evidence_required=True, evidence_reviewability="FAIL",
            evidence_failure="FALSE_EVIDENCE", fabrication=False,
            implementation_allowed="NO", merge_ready="NO", operation_allowed="NO",
        )
        self.assert_invalid(value, "FALSE_EVIDENCE requires")

    def test_done_when_requires_stop(self) -> None:
        value = record(done=True, next_action="STOP")
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["stop"]["next_action"] = "CONTINUE"
        self.assert_invalid(bad, "requires next_action=STOP")

    def test_blocker_requires_legal_source_and_counterexample(self) -> None:
        legal = {
            "kind": "BLOCKER",
            "blocker_class": "CONTRACT_VIOLATION",
            "source_type": "ACCEPTED_PRODUCT_AUTHORITY",
            "source": "SPEC#CTR-1",
            "counterexample": "wrong behavior is reproducible",
            "impact": "accepted obligation is violated",
            "minimal_closure": "repair the bounded path",
        }
        self.assert_valid(record(findings=[legal]))
        illegal = copy.deepcopy(legal)
        illegal["source_type"] = "INVESTIGATION"
        self.assert_invalid(record(findings=[illegal]), "legal blocker source")


if __name__ == "__main__":
    unittest.main()
