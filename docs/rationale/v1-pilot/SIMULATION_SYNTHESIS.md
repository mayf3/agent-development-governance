# Agent Development Governance V1 pilot synthesis

## Status and source identity

```text
DOCUMENT_CLASS = NON_AUTHORITATIVE_RATIONALE
INITIAL_SIMULATION_ROUNDS = 8
TARGETED_RESIMULATION_TESTS = 4
REPOSITORY_WRITE = NO
GITHUB_WRITE = NO
RUNTIME_WRITE = NO
PRODUCTION_OPERATION = NO
```

Source artifacts supplied to formal authoring:

| Artifact | SHA-256 |
|---|---|
| `AGENT_DEVELOPMENT_GOVERNANCE_V1_SIMULATION_CANDIDATE_R2.md` | `29f006832cf40dec4514111fbbf21a7bd07f296d69c784f84fe80c94f0f87bc0` |
| `AGENT_GOVERNANCE_V1_MULTI_AGENT_SIMULATION_REPORT.md` | `28bebbd36fcd2e79da099c4739b38a4f27b5eebde636620bd9c798c76821c9cb` |
| `AGENT_GOVERNANCE_V1_R2_TARGETED_RESIMULATION_REPORT.md` | `bc243eee0e27c7db3b806028b09cf51602ad35861ef5bd7448f2be25f1314e0b` |

The source artifacts are evidence inputs, not active authority.

## Initial eight-round result

Four real scenarios were each simulated once normally and once with adversarial failure injection:

1. Agent Forum state storage;
2. disabled workflow-admin identity bootstrap;
3. auth-service `workflow.execute` permission;
4. dsh-agent-core split into public interface, test isolation, and Scheduler package work.

The initial result retained the core direction:

```text
long-lived normative change -> Authority
execution complexity        -> Plan
failure consequence         -> Assurance
```

It also found six critical ambiguities:

1. Product Authority and one-operation Execution Mandate were not explicitly separated.
2. `SPEC_GAP` was classified separately from a Contract violation but its blocking routing effect was unclear.
3. Reviewer-inaccessible Evidence had no precise failure class.
4. Controlled Runbook and Plan level could be confused.
5. Live state ahead of authority had no ordered containment path.
6. Candidate-Head drift and unrelated base movement could be confused.

The result was:

```text
VERDICT = REVISE_BEFORE_AUTHORING
CRITICAL_BLOCKERS = 6
DIRECTION_REJECTED = NO
NEW_GOVERNANCE_PLATFORM_REQUIRED = NO
```

## Minimum revisions incorporated into R2

### Product Authority versus Execution Mandate

Product Authority creates long-lived obligations. A valid Execution Mandate only authorizes and constrains one task or operation, including actor, target, environment, allowed effects, forbidden effects, scope, and stop condition. It cannot change Product Contracts, and an Agent cannot self-issue controlled authority.

### Load-bearing `SPEC_GAP`

Reviewer may identify a gap but cannot write the product answer. When current implementation, merge, or operation depends on the unresolved meaning, readiness is `NOT_READY` and the route returns to PREFLIGHT until the owning authority action is resolved.

### Evidence reviewability

Load-bearing Evidence that the designated independent Reviewer cannot access, attribute, reproduce, or have independently examined is `REQUIRED_GATE_FAILURE`. `FALSE_EVIDENCE` is reserved for fabrication, material distortion, or false claims of execution.

### Controlled Runbook versus Plan

A Controlled Runbook is an Assurance artifact. A simple one-shot controlled operation can remain `PLAN_LEVEL = BRIEF` with an embedded exact runbook. Risk alone does not create an ExecPlan or platform.

### Live authority gap

Live state is an Observation, not authority. Expansion freezes. The system neither deletes automatically nor permanently grandfathers. An authorized Owner gives a bounded temporary risk disposition, the authority gap closes docs-first, runtime is minimally reconciled, conformance is independently checked, and containment ends.

### Candidate Head versus base movement

`REVIEW_TARGET_HEAD` is the exact candidate. `BASE_HEAD` is the integration snapshot. `CURRENT_BASE_HEAD` may move. Unrelated base movement triggers bounded conflict, authority-overlap, affected-behavior, and evidence-impact checks rather than automatic full review.

## Research and life primitives retained

The simulations found the following compact decision aids load-bearing:

```text
GOAL / CURRENT_GAP
OBSERVATION / WORKING_GUESS
EVIDENCE_NEEDED
DONE_WHEN
EXPANSION_TRIGGER
NEXT_REAL_ACTION
```

Their value is semantic rather than ceremonial:

- “current uid cannot read the private store” is an Observation; “therefore build an Operator platform” is a Guess;
- “runtime has a Grant” is an Observation; “therefore it should permanently remain” is a Claim;
- Investigation precision does not make an implementation choice a Contract;
- Activity is not Progress unless it changes State, a decision, conformance, or a required risk control;
- `DONE_WHEN` satisfied with no `EXPANSION_TRIGGER` yields `STOP`.

Recorder and Goal/Stop Auditor are cognitive views, not required Agent roles. One Agent may record, PREFLIGHT, and plan; independence is required only at the review, acceptance, or controlled-verification boundaries that need it.

## Targeted resimulation disposition

R2 was tested against:

- unrelated main/base movement plus a real public semantic gap;
- uid isolation plus an invalid “Owner approved” mandate and pressure to build a platform;
- hidden Evidence plus a live permission ahead of authority;
- a public interface mislabeled as an implementation detail plus an unauthorized hard split.

The full report records:

```text
TARGETED_RESIMULATION = PASS
VERDICT = READY_FOR_FORMAL_AUTHORING
CRITICAL_BOUNDARIES_CLOSED = 6 / 6
FAILED_TESTS = NONE
CRITICAL_BLOCKERS = 0
MINIMAL_REQUIRED_REVISIONS = NONE
NEW_GOVERNANCE_PLATFORM_REQUIRED = NO
FULL_NORMAL_ROUND_RERUN_REQUIRED = NO
```

This authorizes formal authoring only. It does not make R2 active authority, accept a Spec, implement the distribution, change a consumer, or authorize a runtime operation.
