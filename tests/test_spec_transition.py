from __future__ import annotations

import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/legacy_authority_retirement"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


transition = load_module(
    "validate_spec_transition",
    ROOT / ".agents/tools/validate_spec_transition.py",
)


def load_fixture(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class LegacyAuthorityRetirementTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base = load_fixture("base.json")
        self.candidate = load_fixture("candidate.json")

    def errors(self, base=None, candidate=None):
        return transition.validate_transition(
            self.base if base is None else base,
            self.candidate if candidate is None else candidate,
        )

    def strict_record(self, spec_id="STRICT_AUTHORITY_V1", status="accepted"):
        record = copy.deepcopy(self.candidate[1])
        record["spec_id"] = spec_id
        record["status"] = status
        record["supersedes"] = []
        record["superseded_by"] = None
        return record

    def proposed_successor_records(self):
        predecessor = self.strict_record("EXAMPLE_AUTHORITY_V1")
        successor = self.strict_record("EXAMPLE_AUTHORITY_V2", "proposed")
        successor["supersedes"] = [predecessor["spec_id"]]
        return [predecessor], [copy.deepcopy(predecessor), successor]

    def test_proposed_successor_can_declare_intent_without_retiring_predecessor(self) -> None:
        base, candidate = self.proposed_successor_records()
        self.assertEqual([], transition.validate_transition(base, candidate))

    def test_proposed_successor_cannot_retire_predecessor_early(self) -> None:
        base, candidate = self.proposed_successor_records()
        candidate[0]["status"] = "superseded"
        candidate[0]["superseded_by"] = candidate[1]["spec_id"]
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("cannot retire" in error for error in errors))
        self.assertTrue(any("non-accepted successor" in error for error in errors))

    def test_proposed_successor_cannot_set_predecessor_backlink_early(self) -> None:
        base, candidate = self.proposed_successor_records()
        candidate[0]["superseded_by"] = candidate[1]["spec_id"]
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("must be null while active" in error for error in errors))
        self.assertTrue(any("cannot set predecessor backlink" in error for error in errors))

    def test_accepted_successor_still_requires_atomic_predecessor_transition(self) -> None:
        base, candidate = self.proposed_successor_records()
        candidate[1]["status"] = "accepted"
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("not superseded atomically" in error for error in errors))
        self.assertTrue(any("backlink does not name" in error for error in errors))

    def test_accepted_successor_with_atomic_backlinks_is_valid(self) -> None:
        base, candidate = self.proposed_successor_records()
        candidate[0]["status"] = "superseded"
        candidate[0]["superseded_by"] = candidate[1]["spec_id"]
        candidate[1]["status"] = "accepted"
        self.assertEqual([], transition.validate_transition(base, candidate))

    def test_proposed_successor_cannot_target_nonexistent_predecessor(self) -> None:
        successor = self.strict_record("EXAMPLE_AUTHORITY_V2", "proposed")
        successor["supersedes"] = ["MISSING_AUTHORITY_V1"]
        errors = transition.validate_transition([], [successor])
        self.assertTrue(any("nonexistent base authority" in error for error in errors))

    def test_schema_keeps_active_ids_strict_and_retirement_references_narrow(self) -> None:
        schema = json.loads(
            (ROOT / ".agents/schemas/spec-frontmatter.schema.json").read_text(
                encoding="utf-8"
            )
        )
        strict = schema["$defs"]["strictSpecId"]
        legacy = schema["$defs"]["legacyHistoricalSpecId"]
        self.assertEqual("^[A-Z][A-Z0-9_]*_V[0-9]+$", strict["pattern"])
        self.assertEqual(
            "^[A-Z][A-Z0-9_]*_V[0-9]+_[A-Z][A-Z0-9_]*$",
            legacy["pattern"],
        )
        self.assertEqual(strict["pattern"], legacy["not"]["pattern"])
        overlap_id = "AUTH_V1_COMPONENT_V2"
        self.assertRegex(overlap_id, re.compile(strict["pattern"]))
        self.assertFalse(transition.is_legacy_spec_id(overlap_id))
        self.assertEqual(
            {"$ref": "#/$defs/strictSpecId"},
            schema["properties"]["governed_by"]["items"],
        )
        self.assertEqual(
            [
                {"$ref": "#/$defs/strictSpecId"},
                {"$ref": "#/$defs/legacyHistoricalSpecId"},
            ],
            schema["properties"]["supersedes"]["items"]["oneOf"],
        )
        self.assertEqual(
            {"$ref": "#/$defs/strictSpecId"},
            schema["allOf"][0]["else"]["properties"]["spec_id"],
        )

    def test_arbitrary_uppercase_is_not_a_legacy_reference(self) -> None:
        self.assertFalse(transition.is_legacy_spec_id("UNVERSIONED_AMENDMENT"))
        record = copy.deepcopy(self.candidate[0])
        record["spec_id"] = "UNVERSIONED_AMENDMENT"
        self.assertTrue(transition.validate_metadata(record))

    def test_positive_fixture_closes_whole_legacy_lifecycle(self) -> None:
        self.assertEqual([], self.errors())
        for record in self.candidate:
            self.assertEqual(
                [], transition.validate_metadata(record, record["spec_id"])
            )

    def test_proposed_legacy_id_fails(self) -> None:
        candidate = [copy.deepcopy(self.base[0])]
        candidate[0]["status"] = "proposed"
        errors = self.errors(base=[], candidate=candidate)
        self.assertTrue(any("strict _V<number>" in error for error in errors))
        self.assertTrue(any("invents legacy authority" in error for error in errors))

    def test_accepted_new_legacy_id_fails(self) -> None:
        errors = self.errors(base=[], candidate=copy.deepcopy(self.base))
        self.assertTrue(any("strict _V<number>" in error for error in errors))
        self.assertTrue(any("creates active legacy authority" in error for error in errors))

    def test_legacy_id_cannot_be_new_governed_by_dependency(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[1]["governed_by"] = [candidate[0]["spec_id"]]
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("governed_by contains a non-strict ID" in error for error in errors))

    def test_legacy_successor_fails(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[1]["spec_id"] = "SOME_AUTHORITY_V3_REPLACEMENT"
        candidate[0]["superseded_by"] = "SOME_AUTHORITY_V3_REPLACEMENT"
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("strict _V<number>" in error for error in errors))
        self.assertTrue(any("superseded_by must name a strict successor" in error for error in errors))

    def test_partial_contract_reference_fails(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[1]["supersedes"] = [
            candidate[0]["spec_id"] + "#CTR-001"
        ]
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("invalid whole-authority ID" in error for error in errors))

    def test_missing_old_backlink_fails_atomic_transition(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[0]["superseded_by"] = None
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("backlink does not name" in error for error in errors))

    def test_missing_new_backlink_fails_atomic_transition(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[1]["supersedes"] = []
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("does not backlink superseded authority" in error for error in errors))

    def test_invented_legacy_reference_fails(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[1]["supersedes"] = ["INVENTED_AUTHORITY_V1_HISTORY_AMENDMENT"]
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("supersedes nonexistent base authority" in error for error in errors))

    def test_superseded_without_successor_fails(self) -> None:
        candidate = copy.deepcopy(self.base)
        candidate[0]["status"] = "superseded"
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("must name a strict successor" in error for error in errors))

    def test_retiring_authority_scope_mutation_fails(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate[0]["scope"] = ["changed accepted scope"]
        errors = self.errors(candidate=candidate)
        self.assertTrue(any("mutates accepted authority field: scope" in error for error in errors))

    def test_accepted_strict_authority_mutation_and_regression_fail(self) -> None:
        base = [self.strict_record()]
        candidate = copy.deepcopy(base)
        candidate[0]["scope"] = ["changed accepted scope"]
        candidate[0]["status"] = "proposed"
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("mutates accepted authority field: scope" in error for error in errors))
        self.assertTrue(any("forbidden lifecycle transition" in error for error in errors))

    def test_superseded_strict_authority_cannot_reactivate(self) -> None:
        old = self.strict_record("OLD_AUTHORITY_V2", "superseded")
        old["superseded_by"] = "SOME_AUTHORITY_V3"
        successor = self.strict_record("SOME_AUTHORITY_V3")
        successor["supersedes"] = ["OLD_AUTHORITY_V2"]
        base = [old, successor]
        candidate = copy.deepcopy(base)
        candidate[0]["status"] = "accepted"
        candidate[0]["superseded_by"] = None
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("forbidden lifecycle transition" in error for error in errors))

    def test_existing_accepted_authority_cannot_be_mutated_into_successor(self) -> None:
        existing_successor = self.strict_record("SOME_AUTHORITY_V3")
        base = copy.deepcopy(self.base) + [existing_successor]
        candidate = copy.deepcopy(base)
        candidate[0]["status"] = "superseded"
        candidate[0]["superseded_by"] = "SOME_AUTHORITY_V3"
        candidate[1]["supersedes"] = [candidate[0]["spec_id"]]
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("mutates accepted supersedes metadata" in error for error in errors))
        self.assertTrue(any("successor was already normative" in error for error in errors))

    def test_fabricated_superseded_authority_and_nonexistent_successor_fail(self) -> None:
        candidate = [self.strict_record("FABRICATED_AUTHORITY_V1", "superseded")]
        candidate[0]["superseded_by"] = "NEXT_AUTHORITY_V1"
        errors = transition.validate_transition([], candidate)
        self.assertTrue(any("creates already-superseded authority" in error for error in errors))
        self.assertTrue(any("backlinks nonexistent successor" in error for error in errors))

    def test_historical_successor_backlink_cannot_change(self) -> None:
        old = self.strict_record("OLD_AUTHORITY_V2", "superseded")
        old["superseded_by"] = "SOME_AUTHORITY_V3"
        successor = self.strict_record("SOME_AUTHORITY_V3")
        successor["supersedes"] = ["OLD_AUTHORITY_V2"]
        base = [old, successor]
        candidate = copy.deepcopy(base)
        candidate[0]["superseded_by"] = "DOES_NOT_EXIST_V9"
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("mutates historical successor backlink" in error for error in errors))
        self.assertTrue(any("backlinks nonexistent successor" in error for error in errors))

    def test_legacy_path_can_only_shrink_active_set(self) -> None:
        base = copy.deepcopy(self.base)
        second = copy.deepcopy(self.base[0])
        second["spec_id"] = "ANOTHER_AUTHORITY_V1_HISTORICAL_AMENDMENT"
        base.append(second)

        candidate = copy.deepcopy(self.candidate)
        retired_second = copy.deepcopy(second)
        retired_second["status"] = "superseded"
        retired_second["superseded_by"] = "ANOTHER_AUTHORITY_V3"
        successor = copy.deepcopy(self.candidate[1])
        successor["spec_id"] = "ANOTHER_AUTHORITY_V3"
        successor["supersedes"] = [second["spec_id"]]
        candidate.extend([retired_second, successor])
        self.assertEqual([], transition.validate_transition(base, candidate))

        invented = copy.deepcopy(second)
        invented["spec_id"] = "NEW_AUTHORITY_V1_ACTIVE_AMENDMENT"
        candidate.append(invented)
        errors = transition.validate_transition(base, candidate)
        self.assertTrue(any("active legacy authority" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
