# Agent Development Governance

A versioned development grammar, Spec-governance protocol, and reusable Agent Skill for repositories developed across many Agent sessions.

```text
what we observed
-> what we think it means
-> what we decided
-> what the system must guarantee
-> what was implemented or operated
-> what the Evidence actually verifies
```

It is not a central product authority. A consumer adopts an exact immutable source revision and remains owner of its Product Direction, Architecture, Specs, acceptance actors, code, runtime, and operations.

## Current status

```text
DISTRIBUTION_VERSION = 1.0.1
GOVERNANCE_V1_SPEC_STATUS = accepted
GOVERNANCE_V1_ACTIVE_ON_MAIN = yes
BOOTSTRAP_V0_STATUS = superseded
OPERATIONAL_LAYER_SPEC_STATUS = accepted
OPERATIONAL_LAYER_IMPLEMENTATION = not_started
ENFORCEMENT_LEVEL = manual_policy_plus_deterministic_integrity
SEMANTIC_SPEC_VERIFIER = not_implemented
SPEC_TRANSITION_VALIDATOR = implemented
ROUTE_CONSISTENCY_VALIDATOR = implemented
STABLE_RELEASE = v1.0.1
```

Governance V1 separates:

```text
new or changed long-lived obligation -> Authority action
execution complexity                 -> Plan level
failure consequence                  -> Assurance level
```

Complex work gets enough planning. Dangerous work gets stronger authorization, controls, Evidence, and receipts. Neither fact automatically creates a new Spec.

## Core rules

- only active accepted Product Authority creates long-lived Contracts;
- an Execution Mandate constrains one operation and cannot change Product Contracts;
- Investigation, Task, Brief, test, runtime, or Review comment cannot become Product Authority;
- `REUSE`, `AMEND`, `SUPERSEDE`, and `NEW` are mutually exclusive at readiness boundaries;
- a load-bearing `SPEC_GAP` stops dependent implementation, merge, or operation;
- inaccessible required Evidence is a gate failure, not automatically false evidence;
- a Controlled Runbook is an Assurance artifact, not an ExecPlan;
- live state without authority freezes expansion and requires Owner containment plus docs-first closure;
- exact candidate Head and Base movement are different facts;
- Blockers have closed classes, legal sources, counterexamples, impact, and minimal closure;
- affected-Contract review is default; full matrices are for controlled, release, explicit full, or unbounded surfaces;
- `DONE_WHEN` met without an `EXPANSION_TRIGGER` means `STOP`.

## Layout

```text
.agents/
├── README.md
├── protocol/
│   ├── SPEC_GOVERNANCE_V1.md
│   ├── SPEC_GOVERNANCE_V0.md        # historical compatibility
│   └── SPEC_FORMAT_V0.md
├── skills/spec-governance/
├── schemas/governance-route.schema.json
├── tools/validate_governance_route.py
└── templates/
    ├── CHANGE_BRIEF_TEMPLATE.md
    ├── EXEC_PLAN_TEMPLATE.md
    ├── EXECUTION_MANDATE_TEMPLATE.md
    ├── CONTROLLED_RUNBOOK_TEMPLATE.md
    ├── REVIEW_RECORD_TEMPLATE.md
    └── CONFORMANCE_RECORD_TEMPLATE.md

docs/changes/
distribution/manifest.json
tools/{build_manifest.py,vendor.py,verify_vendor.py}
```

## Deterministic tool boundary

`validate_governance_route.py` checks structured route consistency and known negative controls. It does not decide whether an authority truly owns a decision, whether a Claim is justified, whether a Contract is complete, or whether real Evidence is sufficient.

`verify_governance.py`, the manifest, and transition validator check bytes, adoption metadata, and lifecycle closure. None performs semantic acceptance.

## Consumer model

Consumers vendor an exact source commit and record preparation separately from local acceptance. Upstream movement cannot alter a consumer without a new consumer commit.

```json
{
  "source_repository": "mayf3/agent-development-governance",
  "source_commit": "<40-hex commit>",
  "distribution": "development-governance-v0",
  "version": "1.0.1",
  "adoption": {"status": "proposed | accepted"}
}
```

The distribution identifier remains stable for compatibility; exact source commit and version carry revision identity.

The current stable distribution is `v1.0.1`. Consumers should pin the exact `v1.0.1` commit and still complete their own local acceptance; an upstream release never changes a consumer automatically. `v1.0.0` remains immutable but its transition validator does not accept the legal state in which an accepted predecessor coexists with a proposed successor that declares future whole-authority replacement intent. `AGENT_OPERATIONAL_LAYER_V1` remains accepted but is not implemented by this release.
