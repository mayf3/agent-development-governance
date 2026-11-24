# Change Brief

Current structured decisions use route schema v2; legacy inspection is not a readiness result.

```text
TASK_ID =
TARGET_REPOSITORY =
BASE_HEAD =
REVIEW_TARGET_HEAD = <sha | PENDING>
ROUTE_STAGE = AUTHORITY_AUTHORING | IMPLEMENTATION | OPERATION
AUTHORITY_ACCEPTED_IN_BASE = YES | NO | NOT_APPLICABLE
GOAL_OR_TARGET =
CURRENT_GAP =
AUTHORITY_ACTION = REUSE | AMEND | SUPERSEDE | NEW |
                   AMEND_OR_NEW_PENDING_OWNERSHIP
PRIMARY_AUTHORITY = <ID@revision | NONE>
RELATED_AUTHORITIES = <IDs@revisions | NONE>
ATOMIC_SPEC_IMPLEMENTATION_PERMITTED = YES | NO
PLAN_LEVEL = NONE | BRIEF | EXEC_PLAN
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
```

## Scope

```text
IN_SCOPE =
OUT_OF_SCOPE =
ALLOWED_EFFECTS =
FORBIDDEN_EFFECTS =
```

## Delivery continuity (only for release/recovery or expanding work)

Reuse this Brief, task, PR, or existing release record; do not create a second authority tree.

```text
DELIVERY_ID = <original business outcome; retain across candidate/packet renames>
FROZEN_ACCEPTANCE = <accepted scope and Done-When references, not new product law>
APPLICABLE_GATES = <finite operation/release gate references and status>
VALID_BLOCKERS = <all current valid blockers; do not hide secondary ones>
PRIMARY_BLOCKER = <current execution priority, or NONE>
REVIEW_REPAIR_ROUNDS = <cumulative unsuccessful rounds for this delivery>
LAST_REAL_ACTION = <executed action and result, or explicit waiting state>
```

Use the cumulative history to spot repeated work without new evidence and consider a smaller scope or simpler authorized path. This template sets no numeric cutoff or new gate; task-specific budgets need applicable authorization. Gates satisfied plus valid authorization means perform the next real action. Fresh production preconditions, genuine risks, and required evidence still apply; the record itself grants no permission.

## Relevant knowledge

```text
OBSERVATIONS =
WORKING_GUESS = <only when interpretation affects routing>
EVIDENCE_NEEDED =
```

Each Evidence item states which decision or acceptance result it can change.

## Modeling and verification (affected behavior only)

Assess each behavior change under the grammar's Model-guided development rule.
Use one sentence or references when sufficient; use only the applicable fields
below. Unchanged behavior checks its existing assumptions/mapping. Editorial or
cosmetic work skips this section rather than filling an empty form.

```text
AFFECTED_BEHAVIOR_AND_PROPERTY = <original outcome and properties at risk>
MODEL_CHOICE = <exact existing model/property revision | minimum new/repaired model | no critical mechanism, with reason>
MODEL_BOUNDARY = <entities/state/transitions/assumptions/reachable examples and counterexamples, or reference>
VERIFICATION_CHOICE = <reuse proof | formalize now | defer with reason, gap, controls, owner and trigger | not applicable with reason>
IMPLEMENTATION_MAPPING = <code/input revision, concrete-to-model mapping and supported premises>
EVIDENCE_LAYERS = <model result / implementation evidence / original acceptance; retain unknown or unexecuted parts>
SHARED_FOLLOW_UP = <reusable correction with owner and link, or NONE>
```

Critical mechanisms need a reviewable model before dependent implementation.
Proof deferral cannot waive an existing proof gate. Upstream model work and
unrelated formalization do not automatically block a bounded authorized repair.

## Model convergence (conditional)

```text
MODEL_CONVERGENCE_APPLICABLE = YES | NO

# Remaining fields are required only when MODEL_CONVERGENCE_APPLICABLE = YES;
# when NO, skip them and keep the normal route.
RETAIN = <distinct or still-supported entities kept without merge>
RETIRE = <obsolete executable paths that exit execution>
MIGRATE = <consumers moved to the current model>
TEMPORARY_BRIDGE = <bounded compatibility, or NONE>
REAL_CONSUMERS = <actual consumers of any retained bridge or legacy path>
BRIDGE_EXIT_CONDITION = <exit date or objectively verifiable condition, or NONE>
```

## Execution controls

```text
EXECUTION_MANDATE = <reference | inline authorization | NOT_APPLICABLE>
MUTATION_AUTHORIZATION = VALID | INVALID | NOT_APPLICABLE
ISOLATED_WRITE_SURFACE = <worktree/ref/tree coordinates | NOT_APPLICABLE>
CONTROLLED_RUNBOOK = <embedded/reference | NOT_APPLICABLE>
SPEC_GAP_DEPENDENCY = NONE | NON_LOAD_BEARING | LOAD_BEARING
LIVE_AUTHORITY_GAP = NONE | DETECTED
OWNER_DECISION_REQUIRED = YES | NO
EMERGENCY_STATE = NONE | ACTIVE
INCIDENT_REFERENCE = <reference | NOT_APPLICABLE>
```

## Stop

```text
DONE_WHEN =
EXPANSION_TRIGGER = <condition | NOT_APPLICABLE>
NEXT_REAL_ACTION = <product-facing action | NOT_APPLICABLE>
NEXT_ACTION = CONTINUE | STOP | RE_PREFLIGHT | OWNER_DECISION
```
