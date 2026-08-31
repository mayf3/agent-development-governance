# PREFLIGHT mode

## Goal

Select the shortest authorized route by classifying Product Authority, execution complexity, failure consequence, and readiness independently.

## Procedure

1. Bind target repository, `REVIEW_TARGET_HEAD`, `BASE_HEAD`, `CURRENT_BASE_HEAD`, Goal/target, and Current Gap.
2. Read local precedence, exact adoption lock, Product Direction, Architecture/invariants, overlapping accepted Specs, named proposed target, and exact external authorities.
3. Record qualified Observations; separate a Working Guess when interpretation changes routing.
4. Choose one Authority action:

```text
REUSE | AMEND | SUPERSEDE | NEW
```

Named proposal:

```text
scope/ownership/bounded Decision identity unchanged -> AMEND
any changed -> NEW
```

Accepted authority:

```text
already decides behavior, no meaning change -> REUSE
strictly additive new IDs under unchanged accepted Decisions -> AMEND
accepted meaning changes -> SUPERSEDE
no owner for independent decision -> NEW
```

5. Choose Plan from complexity: `NONE | BRIEF | EXEC_PLAN`.
6. Choose Assurance from consequence: `ROUTINE | DURABLE | CONTROLLED`.
7. Check accepted implementation authority, attributable mandate, Controlled Runbook, load-bearing gap, Evidence reviewability, live authority gap, Base impact, Done When, and Expansion Trigger.
8. Use the route table in `.agents/README.md`.

## Output

```text
SPEC_GOVERNANCE_MODE = PREFLIGHT
TARGET_REPOSITORY = <owner/repository>
REVIEW_TARGET_HEAD = <sha | NOT_APPLICABLE>
BASE_HEAD = <sha | NOT_APPLICABLE>
CURRENT_BASE_HEAD = <sha | NOT_APPLICABLE>
GOAL_OR_TARGET = <outcome>
CURRENT_GAP = <gap>
OBSERVATIONS = <qualified items>
WORKING_GUESS = <item | NOT_APPLICABLE>
AUTHORITY_ACTION = REUSE | AMEND | SUPERSEDE | NEW |
                   AMEND_OR_NEW_PENDING_OWNERSHIP
PRIMARY_AUTHORITY = <ID@revision | NONE>
RELATED_AUTHORITIES = <IDs@revisions | NONE>
IMPLEMENTATION_AUTHORITY = contracts | none | unknown | not_applicable
PLAN_LEVEL = NONE | BRIEF | EXEC_PLAN
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
EXECUTION_MANDATE = VALID | INVALID | NOT_APPLICABLE
CONTROLLED_RUNBOOK_REQUIRED = YES | NO
SPEC_GAP_DEPENDENCY = NONE | NON_LOAD_BEARING | LOAD_BEARING
EVIDENCE_REVIEWABILITY = PASS | FAIL | NOT_APPLICABLE
LIVE_AUTHORITY_GAP = NONE | DETECTED
BASE_IMPACT = NONE | BOUNDED | RELEVANT
IMPLEMENTATION_ALLOWED = YES | NO | NOT_APPLICABLE
MERGE_READY = YES | NO | NOT_APPLICABLE
OPERATION_ALLOWED = YES | NO | NOT_APPLICABLE
EVIDENCE_NEEDED = <items>
DONE_WHEN = <observable result>
EXPANSION_TRIGGER = <condition | NOT_APPLICABLE>
NEXT_REAL_ACTION = <product-facing action | NOT_APPLICABLE>
NEXT_ACTION = CONTINUE | STOP | RE_PREFLIGHT | OWNER_DECISION
```

Do not start semantic implementation or mutation when the relevant readiness flag is `NO`.
