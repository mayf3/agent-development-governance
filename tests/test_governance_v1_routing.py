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


def mandate(
    status: str = "NOT_APPLICABLE",
    *,
    general: bool = False,
    controlled: bool = False,
) -> dict[str, object]:
    if controlled:
        general = True
    return {
        "status": status,
        "attributable": general,
        "target_bound": general,
        "actor_bound": controlled,
        "environment_bound": controlled,
        "scope_bound": general,
        "allowed_effects_bound": general,
        "forbidden_effects_bound": general,
        "exact_operation_bound": controlled,
        "done_when_bound": general,
        "abort_conditions_bound": controlled,
        "secret_handling_bound": controlled,
        "receipt_bound": controlled,
        "attempt_bounds_bound": controlled,
        "self_issued": False,
    }


def record(
    *,
    action: str = "REUSE",
    route_stage: str | None = None,
    authority_accepted_in_base: str | None = None,
    owner_decision_required: bool = False,
    accepted_owner: bool | None = True,
    ownership_known: bool = True,
    accepted_meaning_changed: bool = False,
    strict_addition: bool = False,
    proposed: bool = False,
    scope_changed: bool = False,
    ownership_changed: bool = False,
    decision_changed: bool = False,
    implementation_authority: str = "contracts",
    atomic_spec_implementation_permitted: bool = False,
    complexity: str = "BOUNDED",
    plan: str = "BRIEF",
    consequence: str = "LOW",
    assurance: str = "ROUTINE",
    runbook: bool = False,
    mandate_value: dict[str, object] | None = None,
    mutation_planned: bool | None = None,
    isolated_write_surface: bool | None = None,
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
    emergency_state: str = "NONE",
    emergency_action: str = "NONE",
    emergency_owner_authorized: bool = False,
    incident_reference_present: bool = False,
    emergency_durable_new_behavior: bool = False,
    emergency_reconciliation_required: bool = False,
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
    scenario: dict[str, object] | None = None,
) -> dict[str, object]:
    if route_stage is None:
        route_stage = (
            "AUTHORITY_AUTHORING"
            if action in {
                "AMEND",
                "SUPERSEDE",
                "NEW",
                "AMEND_OR_NEW_PENDING_OWNERSHIP",
            }
            else "IMPLEMENTATION"
        )
    if authority_accepted_in_base is None:
        authority_accepted_in_base = "YES" if action == "REUSE" else "NO"

    mutation_allowed = (
        implementation_allowed == "YES" or operation_allowed == "YES"
    )
    if mandate_value is None:
        if mutation_allowed:
            mandate_value = mandate(
                "VALID",
                general=True,
                controlled=assurance == "CONTROLLED",
            )
        else:
            mandate_value = mandate()
    if mutation_planned is None:
        mutation_planned = mutation_allowed
    if isolated_write_surface is None:
        isolated_write_surface = mutation_allowed

    value: dict[str, object] = {
        "schema_version": 1,
        "task_id": "case",
        "goal": "close the real gap",
        "current_gap": "declared behavior is not yet complete",
        "done_when": "declared bounded result is observed",
        "route_stage": route_stage,
        "authority_accepted_in_base": authority_accepted_in_base,
        "owner_decision_required": owner_decision_required,
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
            "atomic_spec_implementation_permitted": atomic_spec_implementation_permitted,
        },
        "plan": {"complexity": complexity, "level": plan},
        "assurance": {
            "failure_consequence": consequence,
            "level": assurance,
            "controlled_runbook_present": runbook,
        },
        "execution_mandate": mandate_value,
        "write_surface": {
            "mutation_planned": mutation_planned,
            "isolated": isolated_write_surface,
        },
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
        "emergency": {
            "state": emergency_state,
            "action_kind": emergency_action,
            "owner_authorized": emergency_owner_authorized,
            "incident_reference_present": incident_reference_present,
            "durable_new_behavior": emergency_durable_new_behavior,
            "normal_authority_reconciliation_required": emergency_reconciliation_required,
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
    if scenario is not None:
        value["scenario"] = scenario
    return value


def blocker(
    blocker_class: str,
    source_type: str,
    source: str,
    counterexample: str,
    impact: str,
    minimal_closure: str,
) -> dict[str, object]:
    return {
        "kind": "BLOCKER",
        "blocker_class": blocker_class,
        "source_type": source_type,
        "source": source,
        "counterexample": counterexample,
        "impact": impact,
        "minimal_closure": minimal_closure,
    }


class GovernanceV1RoutingTest(unittest.TestCase):
    def assert_valid(self, value: dict[str, object]) -> None:
        self.assertEqual([], validator.validate_route(value))

    def assert_invalid(self, value: dict[str, object], fragment: str) -> None:
        errors = validator.validate_route(value)
        self.assertTrue(any(fragment in error for error in errors), errors)

    # Three rollout canaries.
    def test_canary_forum_state_storage(self) -> None:
        value = record(
            action="REUSE",
            route_stage="IMPLEMENTATION",
            authority_accepted_in_base="YES",
            complexity="COMPLEX",
            plan="EXEC_PLAN",
            consequence="DURABLE_STATE",
            assurance="DURABLE",
            operation_allowed="NOT_APPLICABLE",
        )
        self.assert_valid(value)
        self.assertEqual("REUSE", value["authority"]["declared_action"])
        self.assertEqual("EXEC_PLAN", value["plan"]["level"])
        self.assertEqual("DURABLE", value["assurance"]["level"])
        self.assertEqual("VALID", value["execution_mandate"]["status"])
        self.assertTrue(value["write_surface"]["isolated"])

    def test_canary_disabled_workflow_admin_identity(self) -> None:
        value = record(
            action="REUSE",
            route_stage="OPERATION",
            authority_accepted_in_base="YES",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            mandate_value=mandate("VALID", controlled=True),
            implementation_allowed="NO",
            merge_ready="NOT_APPLICABLE",
            operation_allowed="YES",
        )
        self.assert_valid(value)
        self.assertEqual("BRIEF", value["plan"]["level"])
        self.assertEqual("CONTROLLED", value["assurance"]["level"])
        self.assertTrue(value["execution_mandate"]["target_bound"])
        self.assertTrue(value["execution_mandate"]["exact_operation_bound"])

    def test_canary_auth_service_permission_gap(self) -> None:
        value = record(
            action="NEW",
            route_stage="AUTHORITY_AUTHORING",
            authority_accepted_in_base="NO",
            owner_decision_required=True,
            accepted_owner=False,
            implementation_authority="unknown",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            spec_gap="LOAD_BEARING",
            live_gap=True,
            expansion_frozen=True,
            owner_disposition=False,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="RE_PREFLIGHT",
        )
        self.assert_valid(value)
        self.assertEqual("NEW", value["authority"]["declared_action"])
        self.assertEqual("BRIEF", value["plan"]["level"])
        self.assertEqual("CONTROLLED", value["assurance"]["level"])
        self.assertEqual("RE_PREFLIGHT", value["stop"]["next_action"])

    # Blocker 01: docs-first stage barrier.
    def test_new_controlled_cannot_execute_before_authority_acceptance(self) -> None:
        value = record(
            action="NEW",
            route_stage="OPERATION",
            authority_accepted_in_base="NO",
            accepted_owner=False,
            implementation_authority="unknown",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            mandate_value=mandate("VALID", controlled=True),
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="YES",
        )
        self.assert_invalid(value, "docs-first")

    def test_amend_controlled_cannot_execute_before_authority_acceptance(self) -> None:
        value = record(
            action="AMEND",
            route_stage="OPERATION",
            authority_accepted_in_base="NO",
            proposed=True,
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            mandate_value=mandate("VALID", controlled=True),
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="YES",
        )
        self.assert_invalid(value, "docs-first")

    def test_supersede_cannot_share_implementation_stage(self) -> None:
        value = record(
            action="SUPERSEDE",
            route_stage="IMPLEMENTATION",
            authority_accepted_in_base="NO",
            accepted_meaning_changed=True,
            implementation_allowed="YES",
            merge_ready="NO",
            operation_allowed="NO",
        )
        self.assert_invalid(value, "SUPERSEDE is docs-first")

    def test_amend_durable_atomic_route_requires_explicit_local_permission(self) -> None:
        value = record(
            action="AMEND",
            route_stage="IMPLEMENTATION",
            authority_accepted_in_base="NO",
            proposed=True,
            implementation_authority="unknown",
            atomic_spec_implementation_permitted=True,
            consequence="DURABLE_STATE",
            assurance="DURABLE",
            implementation_allowed="YES",
            merge_ready="YES",
            operation_allowed="NOT_APPLICABLE",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["authority"]["atomic_spec_implementation_permitted"] = False
        self.assert_invalid(
            bad,
            "requires explicit local atomic Spec-and-implementation permission",
        )

    # Blocker 02: mandate and write surface.
    def test_routine_mutation_requires_general_execution_mandate(self) -> None:
        value = record(
            mandate_value=mandate(),
            implementation_allowed="YES",
            operation_allowed="NOT_APPLICABLE",
        )
        self.assert_invalid(value, "mutation requires a valid attributable")

    def test_authoring_write_requires_general_execution_mandate(self) -> None:
        value = record(
            action="NEW",
            route_stage="AUTHORITY_AUTHORING",
            authority_accepted_in_base="NO",
            accepted_owner=False,
            implementation_authority="unknown",
            mandate_value=mandate(),
            mutation_planned=True,
            isolated_write_surface=True,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
        )
        self.assert_invalid(value, "mutation requires a valid attributable")

    def test_general_mandate_requires_target(self) -> None:
        value = record()
        value["execution_mandate"]["target_bound"] = False
        self.assert_invalid(value, "bound to target")

    def test_controlled_mandate_requires_exact_operation(self) -> None:
        value = record(
            route_stage="OPERATION",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            implementation_allowed="NO",
            merge_ready="NOT_APPLICABLE",
            operation_allowed="YES",
        )
        value["execution_mandate"]["exact_operation_bound"] = False
        self.assert_invalid(value, "exact operation")

    def test_write_work_requires_isolated_surface(self) -> None:
        value = record(isolated_write_surface=False)
        self.assert_invalid(value, "isolated worktree")

    def test_consumer_template_carries_mandatory_write_isolation(self) -> None:
        text = (
            ROOT / ".agents/templates/consumer/LOCAL_README.md"
        ).read_text(encoding="utf-8")
        self.assertIn("## Mandatory write isolation", text)
        self.assertIn("MUST use an isolated worktree", text)
        local_extensions = text.split("## Local extensions", 1)[1]
        self.assertNotIn("isolated write surfaces", local_extensions)

    # Blocker 03: load-bearing SPEC_GAP has one exact route.
    def test_load_bearing_gap_rejects_all_not_applicable_readiness(self) -> None:
        value = record(
            action="NEW",
            accepted_owner=False,
            implementation_authority="unknown",
            spec_gap="LOAD_BEARING",
            implementation_allowed="NOT_APPLICABLE",
            merge_ready="NOT_APPLICABLE",
            operation_allowed="NOT_APPLICABLE",
            next_action="RE_PREFLIGHT",
        )
        self.assert_invalid(value, "at least one applicable readiness")

    def test_load_bearing_gap_requires_re_preflight_not_owner_decision(self) -> None:
        value = record(
            action="NEW",
            accepted_owner=False,
            implementation_authority="unknown",
            spec_gap="LOAD_BEARING",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="OWNER_DECISION",
        )
        self.assert_invalid(value, "requires next_action=RE_PREFLIGHT")

    def test_load_bearing_gap_cannot_remain_reuse(self) -> None:
        value = record(
            action="REUSE",
            spec_gap="LOAD_BEARING",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="RE_PREFLIGHT",
        )
        self.assert_invalid(value, "AUTHORITY_ACTION=AMEND, SUPERSEDE, or NEW")

    def test_load_bearing_gap_must_resolve_pending_ownership(self) -> None:
        value = record(
            action="AMEND_OR_NEW_PENDING_OWNERSHIP",
            ownership_known=False,
            accepted_owner=None,
            implementation_authority="unknown",
            spec_gap="LOAD_BEARING",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="RE_PREFLIGHT",
        )
        self.assert_invalid(value, "AUTHORITY_ACTION=AMEND, SUPERSEDE, or NEW")

    # Blocker 04: emergency containment.
    def test_emergency_containment_with_owner_and_incident_is_valid(self) -> None:
        value = record(
            action="REUSE",
            route_stage="OPERATION",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="YES",
            emergency_state="ACTIVE",
            emergency_action="REVOCATION",
            emergency_owner_authorized=True,
            incident_reference_present=True,
            emergency_durable_new_behavior=False,
            emergency_reconciliation_required=True,
        )
        self.assert_valid(value)

    def test_emergency_containment_without_incident_fails(self) -> None:
        value = record(
            action="REUSE",
            route_stage="OPERATION",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="YES",
            emergency_state="ACTIVE",
            emergency_action="ISOLATION",
            emergency_owner_authorized=True,
            incident_reference_present=False,
            emergency_reconciliation_required=True,
        )
        self.assert_invalid(value, "incident reference")

    def test_emergency_containment_cannot_add_durable_behavior(self) -> None:
        value = record(
            action="REUSE",
            route_stage="OPERATION",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="YES",
            emergency_state="ACTIVE",
            emergency_action="CONTAINMENT",
            emergency_owner_authorized=True,
            incident_reference_present=True,
            emergency_durable_new_behavior=True,
            emergency_reconciliation_required=True,
        )
        self.assert_invalid(value, "must not introduce durable new behavior")

    # Blocker 05: full targeted failure scenarios.
    def test_scenario_a_investigation_base_movement_and_real_gap(self) -> None:
        scenario = {
            "unrelated_main_advanced": True,
            "investigation_nullable_pointer_is_exact": True,
            "investigation_promoted_to_product_authority": False,
            "public_reopen_semantic_gap": True,
            "expected_full_rereview": False,
            "expected_next_action": "RE_PREFLIGHT",
            "fixed_agent_formation_required": False,
            "unauthorized_platform_dependency": False,
        }
        value = record(
            action="NEW",
            accepted_owner=False,
            implementation_authority="unknown",
            complexity="COMPLEX",
            plan="EXEC_PLAN",
            consequence="DURABLE_STATE",
            assurance="DURABLE",
            spec_gap="LOAD_BEARING",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NOT_APPLICABLE",
            next_action="RE_PREFLIGHT",
            scenario=scenario,
        )
        self.assert_valid(value)
        self.assertFalse(value["review"]["full_rereview_required"])
        self.assertFalse(
            value["scenario"]["investigation_promoted_to_product_authority"]
        )
        self.assertEqual("RE_PREFLIGHT", value["stop"]["next_action"])

        bad_source = blocker(
            "REPOSITORY_INVARIANT_VIOLATION",
            "INVESTIGATION",
            "INV nullable pointer",
            "Investigation detail is treated as binding Product Authority",
            "implementation choice becomes product law",
            "remove the invented obligation",
        )
        self.assert_invalid(
            record(findings=[bad_source]),
            "legal blocker source",
        )

    def test_scenario_b_uid_invalid_mandate_no_platform_and_grant_escalation(self) -> None:
        scenario = {
            "actor_uid_can_access_private_store": False,
            "owner_approval_attributable": False,
            "platforms_proposed": [
                "UDS_OPERATOR",
                "GITHUB_APP",
                "WEBAUTHN",
                "MERGE_BROKER",
                "WORM",
            ],
            "platform_build_authorized": False,
            "extra_grant_attempted": True,
            "extra_grant_allowed": False,
            "fixed_agent_formation_required": False,
            "unauthorized_platform_dependency": False,
        }
        escalation = blocker(
            "SCOPE_ESCALATION",
            "ACCEPTED_PRODUCT_AUTHORITY",
            "workflow-admin bootstrap scope",
            "identity bootstrap attempts an extra Grant",
            "permission scope expands without a new authority decision",
            "remove the extra Grant and re-PREFLIGHT separately if needed",
        )
        value = record(
            action="REUSE",
            route_stage="OPERATION",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            mandate_value=mandate("INVALID"),
            implementation_allowed="NO",
            merge_ready="NOT_APPLICABLE",
            operation_allowed="NO",
            next_action="OWNER_DECISION",
            findings=[escalation],
            scenario=scenario,
        )
        self.assert_valid(value)
        self.assertFalse(value["scenario"]["platform_build_authorized"])
        self.assertFalse(value["scenario"]["extra_grant_allowed"])
        bad = copy.deepcopy(value)
        bad["readiness"]["operation_allowed"] = "YES"
        bad["write_surface"] = {"mutation_planned": True, "isolated": True}
        self.assert_invalid(bad, "invalid Execution Mandate")

    def test_scenario_c_hidden_evidence_live_gap_and_principal_expansion(self) -> None:
        scenario = {
            "hidden_chat_is_reviewable_evidence": False,
            "auto_delete_requested": True,
            "permanent_grandfather_requested": True,
            "third_principal_expansion_requested": True,
            "third_principal_allowed": False,
            "fixed_agent_formation_required": False,
            "unauthorized_platform_dependency": False,
        }
        expansion = blocker(
            "SCOPE_ESCALATION",
            "ACCEPTED_PRODUCT_AUTHORITY",
            "bounded two-principal permission scope",
            "a third principal is added while the live authority gap is open",
            "unaccepted permission scope expands",
            "freeze expansion and resolve authority ownership",
        )
        value = record(
            action="NEW",
            owner_decision_required=True,
            accepted_owner=False,
            implementation_authority="unknown",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            spec_gap="LOAD_BEARING",
            evidence_required=True,
            evidence_reviewability="FAIL",
            evidence_failure="REQUIRED_GATE_FAILURE",
            live_gap=True,
            expansion_frozen=True,
            auto_delete=False,
            permanent_grandfather=False,
            owner_disposition=False,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="RE_PREFLIGHT",
            findings=[expansion],
            scenario=scenario,
        )
        self.assert_valid(value)
        self.assertFalse(value["live_authority_gap"]["auto_delete"])
        self.assertFalse(value["live_authority_gap"]["permanent_grandfather"])
        self.assertFalse(value["scenario"]["third_principal_allowed"])

        bad = copy.deepcopy(value)
        bad["live_authority_gap"]["permanent_grandfather"] = True
        self.assert_invalid(bad, "must not permanently grandfather")

    def test_scenario_d_public_interface_mislabel_and_hard_split_boundaries(self) -> None:
        scenario = {
            "public_export_or_consumer_dependency": True,
            "author_labels_implementation_detail": True,
            "reviewer_authors_product_contract": False,
            "investigation_recommends_hard_split": True,
            "mandate_forbids_hard_split": True,
            "hard_split_allowed": False,
            "fixed_agent_formation_required": False,
            "unauthorized_platform_dependency": False,
        }
        hard_split = blocker(
            "SCOPE_ESCALATION",
            "EXECUTION_MANDATE",
            "current no-hard-split operation mandate",
            "implementation creates repositories or migrates consumers",
            "the change exceeds the authorized public-interface scope",
            "remove hard split and return to the bounded interface route",
        )
        value = record(
            action="NEW",
            accepted_owner=False,
            implementation_authority="unknown",
            complexity="COMPLEX",
            plan="EXEC_PLAN",
            consequence="DURABLE_STATE",
            assurance="DURABLE",
            mandate_value=mandate("VALID", general=True),
            spec_gap="LOAD_BEARING",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NOT_APPLICABLE",
            next_action="RE_PREFLIGHT",
            findings=[hard_split],
            scenario=scenario,
        )
        self.assert_valid(value)
        self.assertFalse(value["scenario"]["reviewer_authors_product_contract"])
        self.assertFalse(value["scenario"]["hard_split_allowed"])
        bad = copy.deepcopy(value)
        bad["authority"]["declared_action"] = "REUSE"
        self.assert_invalid(bad, "must be NEW")

    def test_failure_scenarios_require_no_fixed_agents_or_platform(self) -> None:
        scenarios = [
            {
                "fixed_agent_formation_required": False,
                "unauthorized_platform_dependency": False,
            }
            for _ in range(4)
        ]
        for scenario in scenarios:
            self.assertFalse(scenario["fixed_agent_formation_required"])
            self.assertFalse(scenario["unauthorized_platform_dependency"])

    # Existing boundary regressions retained.
    def test_unrelated_base_movement_is_bounded_while_real_gap_blocks(self) -> None:
        self.assert_valid(
            record(
                action="NEW",
                accepted_owner=False,
                implementation_authority="unknown",
                complexity="COMPLEX",
                plan="EXEC_PLAN",
                consequence="DURABLE_STATE",
                assurance="DURABLE",
                spec_gap="LOAD_BEARING",
                implementation_allowed="NO",
                merge_ready="NO",
                operation_allowed="NO",
                full_rereview=False,
                next_action="RE_PREFLIGHT",
            )
        )
        bad = record(full_rereview=True)
        self.assert_invalid(bad, "full_rereview_required")

    def test_invalid_owner_mandate_blocks_operation_without_new_platform(self) -> None:
        value = record(
            action="REUSE",
            route_stage="OPERATION",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            runbook=True,
            mandate_value=mandate("INVALID"),
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="OWNER_DECISION",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["readiness"]["operation_allowed"] = "YES"
        bad["write_surface"] = {"mutation_planned": True, "isolated": True}
        self.assert_invalid(bad, "invalid Execution Mandate")

    def test_hidden_evidence_and_live_gap_are_contained(self) -> None:
        value = record(
            action="NEW",
            owner_decision_required=True,
            accepted_owner=False,
            implementation_authority="unknown",
            consequence="HIGH_RISK",
            assurance="CONTROLLED",
            spec_gap="LOAD_BEARING",
            evidence_required=True,
            evidence_reviewability="FAIL",
            evidence_failure="REQUIRED_GATE_FAILURE",
            live_gap=True,
            expansion_frozen=True,
            owner_disposition=False,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="RE_PREFLIGHT",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["live_authority_gap"]["auto_delete"] = True
        self.assert_invalid(bad, "must not auto-delete")

    def test_public_interface_cannot_be_demoted_to_reuse(self) -> None:
        value = record(
            action="NEW",
            accepted_owner=False,
            implementation_authority="unknown",
            complexity="COMPLEX",
            plan="EXEC_PLAN",
            consequence="DURABLE_STATE",
            assurance="DURABLE",
            spec_gap="LOAD_BEARING",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
            next_action="RE_PREFLIGHT",
        )
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["authority"]["declared_action"] = "REUSE"
        self.assert_invalid(bad, "must be NEW")

    def test_named_proposal_decision_identity_change_is_new(self) -> None:
        good = record(
            action="NEW",
            accepted_owner=False,
            proposed=True,
            decision_changed=True,
            implementation_authority="unknown",
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
        )
        self.assert_valid(good)
        bad = copy.deepcopy(good)
        bad["authority"]["declared_action"] = "AMEND"
        self.assert_invalid(bad, "must be NEW")

    def test_false_evidence_requires_fabrication(self) -> None:
        value = record(
            evidence_required=True,
            evidence_reviewability="FAIL",
            evidence_failure="FALSE_EVIDENCE",
            fabrication=False,
            implementation_allowed="NO",
            merge_ready="NO",
            operation_allowed="NO",
        )
        self.assert_invalid(value, "FALSE_EVIDENCE requires")

    def test_done_when_requires_stop(self) -> None:
        value = record(done=True, next_action="STOP")
        self.assert_valid(value)
        bad = copy.deepcopy(value)
        bad["stop"]["next_action"] = "CONTINUE"
        self.assert_invalid(bad, "requires next_action=STOP")

    def test_blocker_requires_legal_source_and_counterexample(self) -> None:
        legal = blocker(
            "CONTRACT_VIOLATION",
            "ACCEPTED_PRODUCT_AUTHORITY",
            "SPEC#CTR-1",
            "wrong behavior is reproducible",
            "accepted obligation is violated",
            "repair the bounded path",
        )
        self.assert_valid(record(findings=[legal]))
        illegal = copy.deepcopy(legal)
        illegal["source_type"] = "INVESTIGATION"
        self.assert_invalid(
            record(findings=[illegal]),
            "legal blocker source",
        )


if __name__ == "__main__":
    unittest.main()
