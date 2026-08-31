# Spec Governance Protocol V1

```text
PROTOCOL_VERSION = 0.2.0-draft.1
GOVERNING_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_V1
STATUS = accepted
ENFORCEMENT_LEVEL = manual_semantic_policy_plus_deterministic_integrity
```

This protocol turns Development Grammar V1 into a repository workflow. The executable router is `.agents/skills/spec-governance/SKILL.md`; formal governing-Spec syntax remains `.agents/protocol/SPEC_FORMAT_V0.md`.

## Scope

This protocol governs authority discovery/mutation, one-operation mandates, three-axis routing, compact execution artifacts, governing-Spec lifecycle, load-bearing gaps, Evidence reviewability, live-authority gaps, exact-Head review, proportional conformance, and exact-revision consumer adoption.

It does not prescribe a central registry, project manager, GitHub App, merge broker, WORM store, fixed Agent count, or semantic CI oracle.

## Required consumer surfaces

```text
AGENTS.md
.agents/README.md
.agents/local/README.md
.agents/governance.lock.json
.agents/protocol/SPEC_GOVERNANCE_V1.md
.agents/protocol/SPEC_FORMAT_V0.md
.agents/skills/spec-governance/SKILL.md
.agents/skills/spec-governance/modes/<MODE>.md
.agents/tools/verify_governance.py
.agents/tools/validate_governance_route.py
docs/specs/README.md
```

## PREFLIGHT

Before non-trivial implementation, configuration, schema, behavior-defining tests, or operation:

1. bind target repository, candidate Head, Base snapshot, and current Base tip;
2. state Goal/target and Current Gap;
3. read local precedence and exact relevant authorities;
4. separate Observations from Working Guesses when interpretation changes routing;
5. classify exactly one Authority action;
6. classify Plan from execution complexity;
7. classify Assurance from failure consequence;
8. check implementation authority, mandate, load-bearing gap, Evidence reviewability, live authority gap, and stop controls;
9. select the shortest authorized route.

### Authority action

```text
REUSE | AMEND | SUPERSEDE | NEW
```

Named proposed target:

```text
same scope + same ownership + same bounded Decision identity -> AMEND
changed scope or ownership or bounded Decision identity      -> NEW
```

Accepted authority:

```text
same decided behavior, no meaning change -> REUSE
strictly additive new IDs under unchanged accepted Decisions -> AMEND
changed accepted meaning -> SUPERSEDE
no accepted owner for independent decision -> NEW
```

`AMEND_OR_NEW_PENDING_OWNERSHIP` is investigation-only and cannot cross a readiness boundary.

### Plan and Assurance

```text
PLAN_LEVEL = NONE | BRIEF | EXEC_PLAN
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
```

A Controlled Runbook is required for a controlled operation but does not force `EXEC_PLAN`.

### Required PREFLIGHT output

```text
SPEC_GOVERNANCE_MODE = PREFLIGHT
TARGET_REPOSITORY = <owner/repository>
REVIEW_TARGET_HEAD = <sha | NOT_APPLICABLE>
BASE_HEAD = <sha | NOT_APPLICABLE>
CURRENT_BASE_HEAD = <sha | NOT_APPLICABLE>
GOAL_OR_TARGET = <outcome>
CURRENT_GAP = <gap>
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
IMPLEMENTATION_ALLOWED = YES | NO | NOT_APPLICABLE
MERGE_READY = YES | NO | NOT_APPLICABLE
OPERATION_ALLOWED = YES | NO | NOT_APPLICABLE
EVIDENCE_NEEDED = <items>
DONE_WHEN = <condition>
EXPANSION_TRIGGER = <condition | NOT_APPLICABLE>
NEXT_ACTION = CONTINUE | STOP | RE_PREFLIGHT | OWNER_DECISION
```

## Artifact selection

- **Change Brief** — bounded reason, route, scope, Evidence, and stop boundary.
- **ExecPlan** — phases, dependencies, checkpoints, migration/rollback, re-PREFLIGHT triggers.
- **Execution Mandate** — attributable authorization and limits for one mutation.
- **Controlled Runbook** — exact dangerous-operation steps, aborts, receipts, and post-state verification.
- **Standing Spec / Spec delta** — only for new or changed long-lived obligations.
- **Receipt / Conformance Record** — what occurred and what it verifies.
- **Investigation** — non-authoritative durable findings.

Default authoring route:

```text
REUSE -> no new Spec
AMEND/NEW + ROUTINE/DURABLE -> Spec delta and code may share one atomic PR if local authority permits
AMEND/NEW + CONTROLLED -> docs-first
SUPERSEDE -> docs-first whole-authority successor
```

## Governing-Spec authoring

The Author resolves ownership and load-bearing normative decisions before implementation depends on them. Formal Specs follow `SPEC_FORMAT_V0.md` and preserve Goal, scope/non-goals, authority, qualified knowledge where load-bearing, Decisions, Contracts, Acceptance with Required Evidence and negative controls, alternatives, migration/compatibility/rollback, and open owner decisions.

A named proposal can be `AMEND` only inside its declared scope, ownership, and bounded Decision identity. Accepted meaning is immutable under the same stable IDs.

## Load-bearing gaps

Reviewer may identify a missing long-lived decision but cannot author it in Review. If implementation, merge, or operation depends on it:

```text
SPEC_GAP_DEPENDENCY = LOAD_BEARING
READINESS = NOT_READY
NEXT_ACTION = RE_PREFLIGHT
```

The owning Author/Owner resolves `AMEND`, `SUPERSEDE`, or `NEW`, or removes the dependency.

## Evidence reviewability

Evidence for acceptance/conformance is accessible to the independent Reviewer, reproducible in an authorized environment, or represented by a sanitized coordinate-bound receipt from a legally independent actor.

- inaccessible/unverifiable/unknown provenance required material -> `REQUIRED_GATE_FAILURE`;
- fabrication/material distortion/false execution claim -> `FALSE_EVIDENCE`.

Do not expose Secrets.

## Live authority gap

When live state exists without accepted Product Authority:

1. record exact Observation;
2. freeze expansion;
3. neither auto-delete nor permanently grandfather;
4. obtain attributable scope-bound Owner containment with expiry/closure condition;
5. close long-lived meaning docs-first;
6. perform minimum reconcile after acceptance;
7. independently verify conformance;
8. end containment and stop.

## Implementation

Implementation records primary/related authorities, Base, implementation commit, Authority action, Plan, Assurance, and mandate where applicable. Work stays inside accepted Contracts and mandate scope.

If a load-bearing gap appears, stop only dependent semantic work and re-PREFLIGHT. Do not rewrite accepted authority to excuse code or expand into optional infrastructure without an observed Expansion Trigger.

## Review

Review binds exact candidate/Base coordinates and is independent where Durable/Controlled assurance, authority acceptance, or local policy requires it.

A Blocker uses one closed class:

```text
CONTRACT_VIOLATION
REPOSITORY_INVARIANT_VIOLATION
CONCRETE_REGRESSION
SECURITY_OR_DATA_LOSS
FALSE_EVIDENCE
SCOPE_ESCALATION
REQUIRED_GATE_FAILURE
```

Every Blocker records `SOURCE`, `COUNTEREXAMPLE`, `IMPACT`, and `MINIMAL_CLOSURE`. Legal sources are accepted Product Authority, accepted local governance/invariant authority, a pre-existing active machine gate, or a valid Execution Mandate. Investigation preference, proposed tests, task product prose, Reviewer preference, and Review comments are not Product-Contract sources.

`SPEC_GAP`, `FOLLOW_UP`, and `TOOLING_DEBT` are non-Blocker finding kinds, though a load-bearing gap still makes readiness false.

## Candidate, Base, and acceptance

```text
REVIEW_TARGET_HEAD = exact candidate under review
BASE_HEAD = integration snapshot
CURRENT_BASE_HEAD = current branch tip at impact recheck
```

Unrelated Base movement gets a bounded conflict/authority/behavior/Evidence check, not automatic full review. Candidate semantic change, relevant authority change, affected behavior/Evidence change, or real conflict invalidates affected review.

Acceptance additionally binds:

```text
FINAL_ACCEPTED_HEAD
ACCEPTANCE_ACTOR
ACCEPTED_AT
SEMANTIC_DELTA_AFTER_REVIEW
```

Any semantic delta invalidates the recommendation. Lifecycle-only acceptance still receives independent final-Head recheck.

## Conformance

Standard review covers affected Contracts and directly dependent invariants. Use a full matrix for controlled operations, releases, explicit full audits, or unbounded surfaces.

A Conformance Record binds exact authority revision, implementation revision, environment, evaluated time, implementation state, verification state, `conformance_result`, executed Observations, and Evidence.

```text
conformance_result = UNKNOWN | VERIFIED | DRIFTED
```

Changed coordinates do not inherit old `VERIFIED`.

## Stop and adoption

```text
DONE_WHEN met + EXPANSION_TRIGGER not fired = STOP
```

Optional platform work, extra fault research, Agent availability, sunk cost, and unrequested cleanup are not progress.

A consumer adopts exact bytes and source commit through its own local acceptance. Preparing vendored files is not acceptance. No bulk historical rewrite is required.

## Deterministic versus semantic enforcement

Tools may check file integrity, pins, enums, structured contradictions, lifecycle closure, required coordinates, blocker shape, and declared readiness consistency. They cannot decide true authority ownership, Claim justification, Contract completeness, or real Evidence sufficiency.
