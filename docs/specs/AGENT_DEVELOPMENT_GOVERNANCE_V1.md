---
spec_id: AGENT_DEVELOPMENT_GOVERNANCE_V1
status: proposed
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
governed_by: []
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# AGENT_DEVELOPMENT_GOVERNANCE_V1

## 1. Goal

Replace the single heavy route for all non-mechanical work with a goal-driven, risk-calibrated governance model.

```text
GOAL = let Agents take the shortest authorized path that closes the real product gap
SUCCESS_OUTCOME = preserve authority, evidence, review, and high-risk controls without turning implementation choices or execution friction into new product law
```

The governing distinction is:

```text
new or changed long-lived obligation -> Authority action
execution complexity                 -> Plan level
failure consequence                  -> Assurance level
```

Complex work needs enough planning. Dangerous work needs stronger authorization, controls, evidence, and receipts. Only a new or changed long-lived obligation requires a new or changed Product Authority.

## 2. Scope and non-goals

### In scope

- repository-local Product Authority and exact-revision consumer adoption;
- Product Authority versus one-operation Execution Mandate;
- three-axis PREFLIGHT: Authority, Plan, and Assurance;
- Standing Specs, Change Briefs, ExecPlans, Controlled Runbooks, Evidence, and Receipts;
- load-bearing `SPEC_GAP` routing;
- Evidence reviewability and precise `FALSE_EVIDENCE` semantics;
- live state ahead of accepted Product Authority;
- closed Reviewer blocker classes and legal source namespaces;
- exact candidate review binding and bounded base-impact checks;
- proportional Contract-focused conformance;
- compact Goal, Gap, Observation, Guess, Evidence, Decision, and Stop controls;
- later implementation of this governance distribution after this Spec is accepted.

### Out of scope

This Spec does not authorize or require:

- product rules for Forum, auth-service, Agent Core, Workflow, or another consumer;
- a GitHub App, WebAuthn ceremony, merge broker, WORM platform, central Spec database, or cross-repository settings controller;
- a fixed six-Agent workflow or required Agent count;
- automatic semantic acceptance or an unbypassable merge gate where none exists;
- consumer changes, historical rewrites, or bulk migration;
- implementation of `.agents/**`, `distribution/**`, tools, validators, templates, tests, or release metadata in this PR;
- product implementation, deployment, production writes, permissions, Grants, Credentials, Secrets, or other runtime operation;
- superseding, amending, implementing, or silently reparenting the accepted `AGENT_OPERATIONAL_LAYER_V1` in this PR;
- adoption of open PR #4 as active authority.

## 3. Authority and dependencies

```text
CURRENT_GENERAL_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
CURRENT_GENERAL_AUTHORITY_REVISION = 45d4835723874ac1632434baded7ae5672225389
CURRENT_ACCEPTED_RELATED_AUTHORITY = AGENT_OPERATIONAL_LAYER_V1
CURRENT_ACCEPTED_RELATED_AUTHORITY_REVISION = 45d4835723874ac1632434baded7ae5672225389
AUTHORITY_ACTION = SUPERSEDE
SUPERSESSION_TARGET = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
PRESERVED_ACCEPTED_AUTHORITY = AGENT_OPERATIONAL_LAYER_V1
PROPOSED_SUCCESSOR = AGENT_DEVELOPMENT_GOVERNANCE_V1
ACCEPTANCE_ACTOR = mayf3 or another explicitly authorized maintainer
EXTERNAL_AUTHORITIES = NONE
```

This proposed Spec is not normative and does not yet supersede V0. Therefore its frontmatter remains:

```text
status = proposed
supersedes = []
superseded_by = null
```

After independent review, an authorized acceptance transaction must atomically prepare:

```text
V1.status = accepted
V1.supersedes = [AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0]
V0.status = superseded
V0.superseded_by = AGENT_DEVELOPMENT_GOVERNANCE_V1
```

That transaction becomes active only after merge into the designated authority branch. Updating the distributed `.agents` implementation is a later change based on accepted V1.

`AGENT_OPERATIONAL_LAYER_V1` is already accepted and active on the reconciled authoring base. This Spec supersedes V0 only; it does not supersede, amend, implement, or silently reparent the Operational Layer. The Operational Layer's exact accepted frontmatter, Decisions, and Contracts remain unchanged. Its `governed_by: AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` field is retained as immutable acceptance-time lineage, while this V1 successor explicitly carries the Operational Layer forward as a compatible specialized authority constrained by the current general governance from V1 activation onward.

Before any Operational Layer implementation begins after V1 activation, PREFLIGHT MUST evaluate the exact active V1 revision and the exact accepted Operational Layer revision together. A conflict or uncovered semantic dependency is `NOT_READY` and returns to PREFLIGHT. Any future change to Operational Layer meaning or to its parent relationship requires a separate authority action and, when accepted meaning changes, a whole-authority successor; it MUST NOT be performed as an in-place edit in this PR.

Current PR dispositions are:

```text
PR #3 = MERGED / AGENT_OPERATIONAL_LAYER_V1 ACTIVE
PR #4 = HOLD / OUT_OF_SCOPE_FOR_V1
```

## 4. Current State

### STATE-GOV1-001 — V0 and the Operational Layer are active on the reconciled base

- Subject: `mayf3/agent-development-governance`
- As of commit: `45d4835723874ac1632434baded7ae5672225389`
- Environment: repository `main`
- Projection: V0 is the accepted active general governance authority; `AGENT_OPERATIONAL_LAYER_V1` is an accepted active specialized authority that refines V0; no V1 distribution or consumer adoption exists.
- Basis: `OBS-GOV1-001`

### STATE-GOV1-002 — Cross-repository pilots exposed one repeated routing failure

- Subject: V0 use across four development lines
- As of artifact: `docs/rationale/v1-pilot/SIMULATION_SYNTHESIS.md`
- Environment: read-only simulation and targeted failure injection
- Projection: procedural gates generally held, but Investigation, Task text, test tooling, Reviewer suggestions, execution friction, and base movement could still be promoted into authority or unnecessary blockers.
- Basis: `OBS-GOV1-002`, `OBS-GOV1-003`, `EVD-GOV1-001`

### STATE-GOV1-003 — Six critical boundaries passed targeted resimulation

- Subject: V1 R2 behavior
- As of artifact: `docs/rationale/v1-pilot/AGENT_GOVERNANCE_V1_R2_TARGETED_RESIMULATION_REPORT.md`
- Environment: four read-only adversarial tests
- Projection: all six critical boundaries closed, no test failed, and no new governance platform was required; the result authorizes formal authoring only.
- Basis: `OBS-GOV1-004`, `EVD-GOV1-002`

## 5. Observations

### OBS-GOV1-001 — The reconciled base has two accepted authorities

- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `45d4835723874ac1632434baded7ae5672225389`
- Environment: `main`
- Observed at: 2026-08-31
- Method: inspect the Spec index, V0 and Operational Layer frontmatter, repository-local authority state, and repository version
- Result: V0 is accepted with `implementation_authority: contracts`; `AGENT_OPERATIONAL_LAYER_V1` is accepted with `implementation_authority: contracts` and `governed_by: [AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0]`; the distribution version remains `0.2.0-draft.1` and Operational Layer implementation has not started.
- Provenance: `docs/specs/README.md`, `docs/specs/AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0.md`, `docs/specs/AGENT_OPERATIONAL_LAYER_V1.md`, `.agents/local/README.md`, `VERSION`

### OBS-GOV1-002 — Eight initial simulations retained the three-axis direction

- Repository/source: V1 pilot corpus
- Commit/artifact: source digest recorded in `docs/rationale/v1-pilot/SIMULATION_SYNTHESIS.md`
- Environment: four scenarios, normal and failure-injection rounds
- Observed at: 2026-08-30
- Method: simulate Recorder, PREFLIGHT, Planner, Implementation, Reviewer, and Goal/Stop views without repository writes
- Result: the direction was retained, but six load-bearing ambiguities required revision.
- Provenance: `docs/rationale/v1-pilot/SIMULATION_SYNTHESIS.md`

### OBS-GOV1-003 — The six ambiguities were bounded rather than platform gaps

- Repository/source: initial simulation report
- Commit/artifact: source digest recorded in the synthesis
- Environment: read-only simulation
- Observed at: 2026-08-30
- Method: classify each failure by its minimum routing correction
- Result: the required fixes were Product Authority versus Execution Mandate, routing effect of load-bearing `SPEC_GAP`, Evidence reviewability, Controlled Runbook versus Plan, live authority gaps, and review target versus base movement. No platform or fixed Agent formation was required.
- Provenance: `docs/rationale/v1-pilot/SIMULATION_SYNTHESIS.md`

### OBS-GOV1-004 — Targeted adversarial resimulation passed

- Repository/source: V1 pilot corpus
- Commit/artifact: `docs/rationale/v1-pilot/AGENT_GOVERNANCE_V1_R2_TARGETED_RESIMULATION_REPORT.md`
- Environment: read-only failure injection
- Observed at: 2026-08-30
- Method: test unrelated base movement, invalid Owner mandate with uid isolation, hidden Evidence plus live authority gap, and a public interface mislabeled as an implementation detail
- Result: `TARGETED_RESIMULATION = PASS`, `CRITICAL_BOUNDARIES_CLOSED = 6 / 6`, `CRITICAL_BLOCKERS = 0`, `VERDICT = READY_FOR_FORMAL_AUTHORING`.
- Provenance: the named report

## 6. Claims and assumptions

### CLM-GOV1-001 — One mechanical/non-mechanical switch conflates three independent decisions

- Support state: SUPPORTED
- Supported by evidence: `EVD-GOV1-001`
- Contradicted by evidence: none known
- Uncertainty: consumers may adopt stricter local rules, but the shared default must not impose them on all work.

### CLM-GOV1-002 — Three-axis routing closes both over-governance and under-governance paths

- Support state: SUPPORTED
- Supported by evidence: `EVD-GOV1-002`
- Contradicted by evidence: none known
- Uncertainty: later distribution implementation and real canaries still require verification.

### CLM-GOV1-003 — Compact research primitives improve routing when they change decisions rather than fill forms

- Support state: SUPPORTED
- Supported by evidence: `EVD-GOV1-003`
- Contradicted by evidence: none known
- Uncertainty: mechanical tasks may omit optional fields.

## 7. Evidence relations

### EVD-GOV1-001 — Pilot failures support separating Authority, Plan, and Assurance

- Source observations: `OBS-GOV1-002`, `OBS-GOV1-003`
- Target: `CLM-GOV1-001`
- Relation: SUPPORTS
- Bound coordinates: eight read-only simulations as recorded in the synthesis
- Strength/sufficiency: sufficient to demonstrate repeated routing failure across four different repositories and change types
- Limitations: simulation does not prove later implementation quality
- Provenance: `docs/rationale/v1-pilot/SIMULATION_SYNTHESIS.md`

### EVD-GOV1-002 — Targeted tests support the revised routing model

- Source observations: `OBS-GOV1-004`
- Target: `CLM-GOV1-002`
- Relation: SUPPORTS
- Bound coordinates: four targeted failure injections on 2026-08-30
- Strength/sufficiency: strong for formal authoring because every previously critical ambiguity was re-injected and closed
- Limitations: formal Spec review and later implementation remain required
- Provenance: `docs/rationale/v1-pilot/AGENT_GOVERNANCE_V1_R2_TARGETED_RESIMULATION_REPORT.md`

### EVD-GOV1-003 — Scenario decisions support compact Goal and stop primitives

- Source observations: `OBS-GOV1-002`, `OBS-GOV1-004`
- Target: `CLM-GOV1-003`
- Relation: SUPPORTS
- Bound coordinates: initial and targeted simulations
- Strength/sufficiency: sufficient to retain Goal/Gap, Observation/Guess, Evidence Needed, Done When, Expansion Trigger, and Next Real Action as decision aids
- Limitations: does not justify a full mandatory form or fixed Agent roles
- Provenance: the synthesis and targeted report

## 8. Decisions

### DEC-GOV1-001 — Consumer authority remains local

- Decision owner: repository owner
- Decision: this repository distributes governance methods; each consumer owns its Product Direction, Architecture, Specs, acceptance actors, code, runtime decisions, and local adoption.
- Rejected alternatives: central product authority; floating governance branch; implicit update.
- Reason: shared methods must not silently change another repository's obligations.
- Owner decision remaining: NONE

### DEC-GOV1-002 — Preserve semantic primitives but separate Activity from knowledge and progress

- Decision owner: repository owner
- Decision: preserve Goal, State, Observation, Claim, Decision, Contract, and Evidence; explicitly state `Activity != Knowledge` and `Activity != Progress`; require Observation versus Working Guess only when interpretation affects a decision.
- Rejected alternatives: every activity is evidence; remove the primitives; require a complete formal graph for every task.
- Reason: the primitives are useful when they change a decision, not when they only expand paperwork.
- Owner decision remaining: NONE

### DEC-GOV1-003 — Separate Product Authority from Execution Mandate

- Decision owner: repository owner
- Decision: Product Authority creates long-lived obligations; a valid Execution Mandate authorizes and constrains one task or operation without changing Product Contracts.
- Rejected alternatives: Task prompt as temporary Product Spec; Task and Brief having no effect on execution scope; self-issued Agent authorization.
- Reason: durable law and bounded work orders have different issuers, effects, and lifetimes.
- Owner decision remaining: NONE

### DEC-GOV1-004 — Use three independent PREFLIGHT axes

- Decision owner: repository owner
- Decision: classify `AUTHORITY_ACTION`, `PLAN_LEVEL`, and `ASSURANCE_LEVEL` independently.
- Rejected alternative: non-mechanical work automatically enters one complete Spec cycle.
- Reason: normative change, complexity, and failure consequence answer different questions.
- Owner decision remaining: NONE

### DEC-GOV1-005 — Give each artifact one legal effect

- Decision owner: repository owner
- Decision: Standing Specs carry Product Contracts; Briefs explain bounded changes; ExecPlans manage complex work; Controlled Runbooks constrain dangerous operations; Evidence and Receipts record what occurred. Investigation, Task, tests, and Review comments do not create Product Authority.
- Rejected alternatives: one full Spec-shaped document for every task; risk automatically creating an ExecPlan.
- Reason: one legal effect per artifact prevents authority drift.
- Owner decision remaining: NONE

### DEC-GOV1-006 — Permit proportional routes while keeping controlled and superseding changes docs-first

- Decision owner: repository owner
- Decision: `REUSE` may implement against accepted authority; `AMEND/NEW + ROUTINE/DURABLE` may use an atomic Spec-delta-and-code PR; `AMEND/NEW + CONTROLLED` and all `SUPERSEDE` routes are docs-first.
- Rejected alternatives: every change has a separate Spec PR; high-risk work self-authorizes in a combined PR.
- Reason: ordinary work should be short while new high-risk obligations remain independently authorized before execution.
- Owner decision remaining: NONE

### DEC-GOV1-007 — A load-bearing gap stops dependent work without giving Reviewer decision authority

- Decision owner: repository owner
- Decision: when implementation, merge, or operation depends on an unresolved long-lived semantic gap, readiness is `NOT_READY` and the route returns to PREFLIGHT. Reviewer identifies the gap but cannot write the answer.
- Rejected alternatives: `SPEC_GAP` as advisory only; Reviewer creates a Contract in review comments.
- Reason: under-governance must stop without transferring product authority to the Reviewer.
- Owner decision remaining: NONE

### DEC-GOV1-008 — Required Evidence must be reviewable

- Decision owner: repository owner
- Decision: inaccessible or unverifiable load-bearing Evidence is `REQUIRED_GATE_FAILURE`, not automatically `FALSE_EVIDENCE`; false evidence is reserved for fabrication, material distortion, or a false execution claim.
- Rejected alternatives: trust hidden author self-evidence; expose Secrets; call every inaccessible source fabricated.
- Reason: independent review requires inspectable support without unsupported accusations.
- Owner decision remaining: NONE

### DEC-GOV1-009 — Contain live authority gaps without runtime legislation or mechanical deletion

- Decision owner: repository owner
- Decision: live state without accepted authority is an Observation; freeze expansion, obtain an Owner-scoped temporary risk disposition, close the long-lived gap docs-first, minimally reconcile runtime, independently verify conformance, and end containment.
- Rejected alternatives: permanent grandfathering; automatic deletion; Reviewer decides the permanent result.
- Reason: runtime cannot create law, but a documentation gap alone does not justify a known regression.
- Owner decision remaining: NONE

### DEC-GOV1-010 — Close Reviewer power by source and counterexample

- Decision owner: repository owner
- Decision: only named blocker classes with a legal source and concrete counterexample may block. `SPEC_GAP`, `FOLLOW_UP`, and `TOOLING_DEBT` are distinct outputs.
- Rejected alternatives: open-ended reliability research as merge review; Investigation or preference relabeled as invariant.
- Reason: Agents can generate unlimited hypothetical concerns.
- Owner decision remaining: NONE

### DEC-GOV1-011 — Separate candidate identity from base movement

- Decision owner: repository owner
- Decision: bind review to `REVIEW_TARGET_HEAD`; treat `BASE_HEAD` as the integration snapshot and `CURRENT_BASE_HEAD` as a moving branch tip; unrelated base movement triggers bounded impact checks, not automatic rebase or full review.
- Rejected alternatives: every main commit invalidates review; old review survives candidate semantic change.
- Reason: candidate identity and integration impact are different facts.
- Owner decision remaining: NONE

### DEC-GOV1-012 — Make Done When and Expansion Trigger stop controls

- Decision owner: repository owner
- Decision: every non-trivial task states observable `DONE_WHEN`; durable, controlled, or drift-prone tasks state `EXPANSION_TRIGGER`; when Done When is met and no trigger occurred, the result is `STOP`.
- Rejected alternatives: Agent availability, sunk effort, tool imperfection, or possible platform work as expansion reasons.
- Reason: governance closes product gaps; it does not keep Agents busy.
- Owner decision remaining: NONE

### DEC-GOV1-013 — Scale conformance to the affected surface

- Decision owner: repository owner
- Decision: ordinary review evaluates affected Contracts and direct dependent invariants; controlled, release, or explicitly full audits use complete matrices. Evidence remains revision-, environment-, and time-qualified.
- Rejected alternatives: PR-by-impression; full active-Contract review for every local change.
- Reason: proportional scope avoids repeated work without weakening evidence semantics.
- Owner decision remaining: NONE

### DEC-GOV1-014 — Roll out only after exact-Head acceptance and behavioral canaries

- Decision owner: repository owner
- Decision: this PR only authors V1. A later change updates the distribution and reruns the failure evaluations. Consumers adopt an exact immutable revision locally, beginning with route-distinct canaries.
- Rejected alternatives: reuse the bootstrap exception; update consumers in this PR; require a new platform first.
- Reason: V0 remains active during authoring and rollout must test both over- and under-governance.
- Owner decision remaining: NONE

### DEC-GOV1-015 — Continue the accepted Operational Layer without in-place reparenting

- Decision owner: repository owner
- Decision: V1 supersedes V0 only. `AGENT_OPERATIONAL_LAYER_V1` remains accepted and active with its exact accepted frontmatter, Decisions, Contracts, lifecycle, and implementation authority unchanged. Its `governed_by: AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` field remains immutable acceptance-time lineage; V1 explicitly carries its compatible specialized obligations forward and becomes the current general constraint after V1 activation. Future Operational Layer implementation must re-run PREFLIGHT against both exact authorities. Any conflict, missing dependency, semantic change, or desired parent rebinding requires a separate authority action and, when accepted meaning changes, a whole-authority successor.
- Rejected alternatives: delete the accepted Operational Layer from the index; silently edit its accepted `governed_by` field; imply that V1 supersedes it; absorb or rewrite its specialized Contracts in this PR.
- Reason: current main already contains this accepted authority, while accepted identity and parent metadata cannot be silently rewritten merely to resolve a branch conflict.
- Owner decision remaining: NONE

### V0 Contract carry-forward matrix

| V0 Contract | V1 disposition | V1 owner |
|---|---|---|
| `CTR-GOV-001` | RETAINED | `CTR-GOV1-001` |
| `CTR-GOV-002` | RETAINED | `CTR-GOV1-002` |
| `CTR-GOV-003` | REPLACED_WITH_EQUIVALENT | `CTR-GOV1-003` |
| `CTR-GOV-004` | RETAINED | `CTR-GOV1-004` |
| `CTR-GOV-005` | REPLACED_WITH_EQUIVALENT | `CTR-GOV1-014` |
| `CTR-GOV-006` | REPLACED_WITH_EQUIVALENT | `CTR-GOV1-015` |
| `CTR-GOV-007` | REPLACED_WITH_EQUIVALENT | `CTR-GOV1-007`, `CTR-GOV1-009`, `CTR-GOV1-020` |
| `CTR-GOV-008` | RETAINED | `CTR-GOV1-016` |
| `CTR-GOV-009` | RETAINED | `CTR-GOV1-017` |
| `CTR-GOV-010` | RETAINED | `CTR-GOV1-018` |
| `CTR-GOV-011` | REPLACED_WITH_EQUIVALENT | `CTR-GOV1-020` |

No V0 protection is retired without replacement.

## 9. Contracts

### CTR-GOV1-001 — Consumer Product Authority remains local

This repository MUST NOT claim automatic Product Authority over a consumer. A consumer MUST own its Product Direction, Architecture, governing Specs, acceptance actors, code, runtime decisions, and Execution Mandates. Shared governance becomes locally applicable only through exact-revision local adoption.

### CTR-GOV1-002 — Governance adoption is exact, immutable, and locally accepted

Consumer adoption MUST bind an exact source commit and distributed-file digests. Preparation MUST remain distinct from acceptance. A mutable branch, unqualified `latest`, runtime fetch, or later upstream change MUST NOT alter consumer governance without a consumer commit and authorized local acceptance.

### CTR-GOV1-003 — Semantic primitives and Activity boundaries remain explicit

The distribution MUST preserve Goal, State, Observation, Claim, Decision, Contract, and Evidence boundaries. State MUST be coordinate-bound. A Claim that carries a load-bearing interpretation MUST use one support state: `SUPPORTED`, `INFERRED`, or `OPEN_ASSUMPTION`; `VERIFIED CLAIM` MUST NOT be a primitive category. A raw artifact or test definition MUST NOT be Evidence; an executed result is an Observation.

Evidence MUST be a first-class, auditable relation from qualified Observation(s) to a named Claim, State assertion, or Contract at pinned coordinates. Every load-bearing Evidence relation in a governing Spec or Conformance Record MUST have a stable `EVD-*` identity and MUST record its source Observation(s), target type and stable target ID, relation or polarity, bound repository/Spec/implementation/environment/time coordinates, strength or sufficiency, limitations, and provenance. Claim or State relations use `SUPPORTS` or `CONTRADICTS`; Contract relations use `SATISFIES`, `VIOLATES`, or `INCONCLUSIVE`.

The distribution MUST state `Activity != Knowledge` and `Activity != Progress`. It MUST NOT require a complete formal graph for a Routine Change Brief or another compact record when no load-bearing Claim or Evidence relation needs it.

### CTR-GOV1-004 — Accepted meaning and lineage remain immutable

Accepted Decision and Contract IDs MUST NOT be renumbered, reused, repurposed, or silently assigned new meaning. Meaning replacement, deletion, narrowing, expansion, or reversal MUST use the active authority-replacement protocol. Historical authority MUST retain exact revision identity and backlinks.

This Spec MUST supersede only `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0`. It MUST NOT silently supersede, delete, amend, implement, or reparent the accepted `AGENT_OPERATIONAL_LAYER_V1`. The Operational Layer remains accepted and active with its exact accepted bytes; its existing `governed_by` value is immutable acceptance-time lineage. From V1 activation forward, its specialized obligations remain applicable only when compatible with the exact active V1 revision. Any Operational Layer implementation MUST pass PREFLIGHT against both exact authorities. A conflict, uncovered dependency, semantic change, or parent-rebinding requirement MUST be `NOT_READY` and handled by a separate authority action; accepted Operational Layer meaning MUST NOT be repaired in place.

### CTR-GOV1-005 — Product Authority and Execution Mandate have different effects

Only active accepted Product Authority in the owning repository MAY create or change long-lived Product Contracts. Investigation, Task, Brief, ExecPlan, Runbook, tests, runtime state, and Review comments MUST NOT create Product Authority. A valid Execution Mandate MAY constrain one task or operation and MAY be the source for `SCOPE_ESCALATION`; it MUST NOT alter Product Contracts.

### CTR-GOV1-006 — Execution Mandates and controlled operations are attributable and bounded

Before mutation, the acting Agent MUST have attributable authorization binding target, scope, allowed and forbidden effects, and Done When. A controlled operation MUST additionally bind actor or allowed role, environment, exact operation or operation class, abort conditions, Secret handling, receipt requirements, and validity or attempt bounds before state change. “Owner approved” without persistent, reviewable coordinates is invalid. An Agent-authored Brief MUST NOT self-authorize. Write work MUST use an isolated worktree or equivalent isolated write surface and MUST NOT disturb another active checkout. An equivalent isolated write surface MUST bind an exact parent, write only to an isolated ref and the single intended tree, avoid mutating any existing checkout, and abort rather than silently adopt target-Head movement. Post-hoc text MUST NOT fabricate prior authorization.

### CTR-GOV1-007 — PREFLIGHT classifies three independent axes and one Authority action

Every non-trivial request MUST independently classify:

```text
AUTHORITY_ACTION = REUSE | AMEND | SUPERSEDE | NEW
PLAN_LEVEL = NONE | BRIEF | EXEC_PLAN
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
```

Authority is determined by whether long-lived required behavior changes. Plan is determined by execution complexity. Assurance is determined by failure consequence. No axis MAY silently determine another.

The Authority actions are mutually exclusive at every readiness boundary:

- `REUSE`: active accepted Product Authority already decides the requested long-lived behavior, and the request changes no Contract meaning.
- `AMEND`: the task explicitly targets one named existing proposed authority and revises that proposal; or an accepted authority receives a strictly additive obligation under unchanged Goal, scope, authority ownership, and accepted Decisions, using new stable IDs while preserving every existing Decision and Contract meaning. When the exact task target is an existing proposed authority, this proposal-target rule takes precedence over `NEW`.
- `SUPERSEDE`: existing accepted meaning is changed, deleted, narrowed, expanded, reversed, or assigned different failure semantics. The replacement MUST use a whole-authority successor with atomic backlinks; prose-only or inferred partial supersession is forbidden unless a later accepted protocol explicitly implements it.
- `NEW`: no active accepted Product Authority owns the bounded independent long-lived decision, and the task is not revising a named existing proposed authority. `NEW` creates a separate authority for a new Decision, expanded scope, changed authority ownership, or another independent obligation.

Expanding an authority's scope or ownership is `NEW`, not `AMEND`. Changing existing accepted Contract meaning or failure semantics is `SUPERSEDE`, not `AMEND` or `NEW`. The mere existence of an unrelated or abandoned proposal does not trigger `AMEND`; the task must name that proposal as its exact authoring target.

`AMEND_OR_NEW_PENDING_OWNERSHIP` MAY be used only while authority ownership and proposal-target identity are being investigated. Before `AUTHORING_READY_FOR_REVIEW = YES`, `IMPLEMENTATION_ALLOWED = YES`, `MERGE_READY = YES`, or `OPERATION_ALLOWED = YES`, it MUST resolve to exactly one Authority action.

An accepted Spec authorizes implementation only when it explicitly declares `implementation_authority: contracts` and the request remains within its active Contracts. An accepted Program Spec or any authority with `implementation_authority: none` MUST NOT authorize child implementation merely because it is accepted.

### CTR-GOV1-008 — Implementation choices do not become Product Contracts by precision or repetition

Table names, function names, index counts, DDL order, file layout, internal coordinators, and test-tool design are implementation choices by default. They become Product Contracts only when active Product Authority deliberately makes their exact form a compatibility, safety, durable-data, operational, or public obligation. Investigation detail, PR prose, test expectations, and Reviewer repetition MUST NOT promote them.

### CTR-GOV1-009 — Routes are proportional and high-risk authority remains docs-first

Default routing MUST be:

| Authority | Assurance | Route |
|---|---|---|
| `REUSE` | `ROUTINE` | Brief as needed + implementation + focused evidence |
| `REUSE` | `DURABLE` | Brief/ExecPlan + implementation + independent affected-Contract review |
| `REUSE` | `CONTROLLED` | valid Execution Mandate + exact Controlled Runbook + receipt + independent post-state verification; no new Spec solely for risk |
| `AMEND/NEW` | `ROUTINE/DURABLE` | atomic Spec delta + implementation MAY be used if local authority permits |
| `AMEND/NEW` | `CONTROLLED` | docs-first Product Authority, then controlled execution |
| `SUPERSEDE` | any | docs-first whole-authority successor |

Identity, authentication, authorization, Secret, Grant, destructive migration, backfill, deletion, cross-repository public protocol, production activation, and irreversible operations MUST use the controlled or superseding docs-first path when they create or change long-lived obligations.

### CTR-GOV1-010 — Controlled Runbook is an Assurance artifact, not a Plan level

Every controlled operation MUST have an exact Controlled Runbook. A simple one-shot operation MAY use `PLAN_LEVEL = BRIEF` with the Runbook embedded. Only execution complexity justifies `EXEC_PLAN`. Controlled risk alone MUST NOT create a project plan or governance platform.

### CTR-GOV1-011 — Load-bearing `SPEC_GAP` blocks dependent readiness

`SPEC_GAP` does not grant Reviewer authority to write a Product Contract. However, when current implementation, merge, or operation depends on an unresolved long-lived semantic decision, the dependent state MUST be `NOT_READY`, `IMPLEMENTATION_ALLOWED = NO`, `MERGE_READY = NO`, or `OPERATION_ALLOWED = NO` as applicable, and `NEXT_ACTION = RE-PREFLIGHT`. The owning authority action MUST resolve to one of `AMEND`, `SUPERSEDE`, or `NEW` before authoring-ready, implementation-ready, merge-ready, or operation-ready status.

### CTR-GOV1-012 — Load-bearing Evidence is reviewable without forcing Secret exposure

Evidence required for acceptance or conformance MUST be accessible and attributable to the designated independent Reviewer, reproducible in an authorized environment, or examined by a legally independent actor who emits a coordinate-bound receipt with sufficient sanitized content. Inaccessible, unverifiable, or provenance-unknown load-bearing Evidence MUST be `REQUIRED_GATE_FAILURE`. `FALSE_EVIDENCE` MUST be reserved for fabrication, material distortion, or a false claim that an execution occurred. Secret material MUST NOT be exposed merely to satisfy reviewability.

### CTR-GOV1-013 — Live authority gaps freeze expansion and require Owner containment

When live behavior, data, permission, or runtime state exists without accepted Product Authority:

```text
LIVE_STATE = Observation, not authority
EXPANSION = FROZEN
AUTO_DELETE = NO
PERMANENT_GRANDFATHER = NO
```

The Owner or authorized risk actor MUST issue an attributable, scope-bound, reviewable temporary containment or risk disposition with expiry or closure condition. The long-lived gap MUST close docs-first. After acceptance, runtime MUST be minimally reconciled, independently checked for conformance, and the temporary disposition ended. Reviewer MUST NOT choose permanent deletion or retention unless already authorized.

### CTR-GOV1-014 — Review target, acceptance tuple, and base movement are distinct

Every review MUST identify:

```text
REVIEW_TARGET_HEAD = exact candidate Head under review
BASE_HEAD = integration snapshot used for the review
CURRENT_BASE_HEAD = current branch tip when impact is rechecked
REVIEWED_BASE_COMMIT = BASE_HEAD
REVIEWED_SPEC_COMMIT = REVIEW_TARGET_HEAD
REVIEWER_ID = attributable independent reviewer
```

Every acceptance record MUST additionally bind:

```text
FINAL_ACCEPTED_HEAD
ACCEPTANCE_ACTOR
ACCEPTED_AT
SEMANTIC_DELTA_AFTER_REVIEW
```

Any semantic delta after `REVIEWED_SPEC_COMMIT` invalidates the prior acceptance recommendation and requires a new independent review. The final accepted Head MUST receive an independent delta recheck even when the intended change is lifecycle- or metadata-only, including `status`, `supersedes`, or `superseded_by`. That recheck MUST verify that only authorized acceptance fields changed and that the whole-authority transition and mutual backlinks are atomic.

Unrelated base movement MUST NOT be called target-Head drift and MUST NOT automatically require rebase or full re-review. A bounded impact check MUST examine merge conflict, relevant authority overlap, affected behavior, and invalidated evidence. Candidate semantic change, relevant authority change, affected-behavior change, or real conflict MUST trigger the required re-review or revalidation.

### CTR-GOV1-015 — Conformance remains qualified and proportional

A Conformance Record MUST bind Product Authority revision, implementation revision, environment, evaluated time, implementation state, verification state, `conformance_result`, executed Observations, and Evidence relations. Aggregate `conformance_result` MUST be `UNKNOWN`, `VERIFIED`, or `DRIFTED`; a Contract-level `NOT_APPLICABLE` result requires a reason derived from that Contract. `VERIFIED` is valid only for the exact bound Product Authority/implementation/environment/time tuple and MUST NOT be represented as an unqualified permanent property of a Spec. A changed bound coordinate does not automatically inherit the prior result.

Standard review SHOULD evaluate affected Contracts and directly dependent accepted invariants. Controlled operations, releases, explicit full audits, and changes whose affected scope cannot be bounded MUST use the complete applicable matrix. A prior passing mechanism MUST NOT be rerun unless the new change invalidates its result.

### CTR-GOV1-016 — Non-authoritative knowledge persists without becoming law

Important rejected, no-change, reuse, deferred, investigation, and simulation outcomes MUST persist in a repository file, issue, or PR record with stable provenance when future decisions depend on them. Their persistence MUST NOT convert them into accepted Product Authority.

### CTR-GOV1-017 — Enforcement maturity is represented honestly

The distribution MUST distinguish prose policy, deterministic syntax or integrity tooling, independent semantic review, repository protection, and runtime enforcement. It MUST NOT claim an unbypassable gate, semantic verifier, branch protection, or required check unless implemented and active at the stated coordinates.

### CTR-GOV1-018 — Emergency action remains containment-only

Pre-Spec emergency action MUST be limited to rollback, disablement, shutdown, revocation, isolation, or equivalent containment; MUST bind Owner authorization and an incident reference; and MUST NOT introduce durable new behavior. Permanent repair MUST return through normal authority routing.

### CTR-GOV1-019 — Review blockers have closed classes and legal sources

A blocking finding MUST use one of:

```text
CONTRACT_VIOLATION
REPOSITORY_INVARIANT_VIOLATION
CONCRETE_REGRESSION
SECURITY_OR_DATA_LOSS
FALSE_EVIDENCE
SCOPE_ESCALATION
REQUIRED_GATE_FAILURE
```

It MUST state `SOURCE`, `COUNTEREXAMPLE`, `IMPACT`, and `MINIMAL_CLOSURE`. Legal sources are limited to active accepted Product Authority; accepted local governance or invariant authority; a pre-existing active machine-enforced repository gate; or a valid Execution Mandate for this task or operation. Investigation, proposed tests, task product semantics, Reviewer preference, and review comments are not legal Product-Contract sources. Findings without legal source or concrete counterexample MUST be `SPEC_GAP`, `FOLLOW_UP`, or `TOOLING_DEBT`, not a Blocker. Advanced tooling debt blocks a product only when it causes false pass, harms non-test data, hides a concrete security/data-loss failure, or is itself an explicit accepted deliverable.

### CTR-GOV1-020 — Goal, stop, implementation, and rollout boundaries are explicit

Every non-trivial route MUST record a compact Goal or target, Current Gap, Authority action, primary authority, Plan level, Assurance level, Evidence needed, and observable `DONE_WHEN`. Tasks prone to expansion, and every durable or controlled task, MUST record `EXPANSION_TRIGGER`; `NEXT_REAL_ACTION` is required when governance or infrastructure drift is plausible. Observation and Working Guess MUST be separated when an interpretation changes routing. When Done When is met and no trigger occurred, the only valid result is `STOP`.

This authoring PR MUST NOT modify the distribution or consumers. The exhausted bootstrap exception MUST NOT authorize V1 implementation. A later implementation PR MUST be based on active accepted V1, implement the six critical boundaries, rerun the four targeted failures, and validate at least these three canaries:

```text
Forum state storage = REUSE + EXEC_PLAN + DURABLE
workflow-admin disabled identity = REUSE + BRIEF + CONTROLLED
auth-service workflow.execute = AMEND or NEW + BRIEF + CONTROLLED
```

## 10. Acceptance

### ACC-GOV1-001 — Authority and mandate separation

- Contracts: `CTR-GOV1-001`, `CTR-GOV1-005`, `CTR-GOV1-006`
- Method: independently classify a persistent product rule, an unattributed “Owner approved” task, and a valid one-shot controlled mandate
- Environment: exact candidate Head
- Required evidence: exact candidate Head; cited Product Authority revision; the unattributed task text; the valid mandate with attributable issuer, actor/role, environment, scope, allowed/forbidden effects, Done When, abort/Secret/receipt bounds; and the resulting classification record
- Expected result: only accepted Product Authority creates long-lived obligations; the unattributed mandate blocks operation; the valid mandate constrains one operation without becoming Product Authority
- Failure condition: Task text creates Product Contracts, self-authorizes an Agent, or has no execution-scope effect

### ACC-GOV1-002 — Three-axis routing and Authority-action separation

- Contracts: `CTR-GOV1-007`, `CTR-GOV1-008`, `CTR-GOV1-009`, `CTR-GOV1-010`
- Method: route a complex internal refactor under an implementation-authorizing Contract, a simple controlled one-shot operation, a revision whose exact target is a named existing proposed authority, the same independent decision when no proposed authority is the task target, a strictly additive same-scope obligation on accepted authority, an independent new permission obligation, a change to existing accepted meaning, and an accepted Program with `implementation_authority: none`
- Environment: exact candidate Head
- Required evidence: exact accepted/proposed authority inventory and revisions; the declared authoring target or explicit absence of one; one classification matrix showing a unique Authority action, Plan level, Assurance level, primary authority, proposal-target identity, and implementation-authority result for every case; plus a negative-control result for each incorrect route
- Expected result: complexity changes Plan only; risk changes Assurance only; revision of the named existing proposal is `AMEND`; the same decision without an existing proposed target is `NEW`; the additive accepted-authority case is `AMEND`; the independent obligation is `NEW`; changed existing meaning is `SUPERSEDE`; `REUSE` changes no Contract meaning; the one-shot remains Brief plus Controlled Runbook; and the accepted non-authorizing Program does not permit child implementation
- Failure condition: any one axis automatically forces another, a complete input with a named proposed target legally yields `NEW`, a complete input without such a target legally yields `AMEND` merely because another proposal exists, the same complete input legally yields both `AMEND` and `NEW`, Investigation detail becomes a Contract, risk alone creates an ExecPlan/platform, partial supersession is inferred from prose, or `implementation_authority: none` authorizes implementation

### ACC-GOV1-003 — Load-bearing gap stop

- Contracts: `CTR-GOV1-011`
- Method: inject an unresolved public-interface or permission semantic required by the candidate
- Environment: exact candidate Head
- Required evidence: exact authority inventory; the injected semantic dependency; classification output showing `SPEC_GAP_DEPENDENCY = LOAD_BEARING`, all applicable readiness flags set to no, and `NEXT_ACTION = RE-PREFLIGHT`; and a record showing no Reviewer-authored Contract
- Expected result: dependent implementation/merge/operation is not ready and returns to PREFLIGHT; Reviewer does not write the answer
- Failure condition: the work proceeds because `SPEC_GAP` is treated as advisory, or Reviewer invents the Product Contract

### ACC-GOV1-004 — Evidence reviewability and primitive fidelity

- Contracts: `CTR-GOV1-003`, `CTR-GOV1-012`
- Method: compare accessible Evidence, hidden author-only material, a sanitized independent receipt, and fabricated execution evidence; then inspect one load-bearing Claim and one Contract-targeted Evidence relation
- Environment: exact candidate Head
- Required evidence: source artifact and Observation identities; stable `EVD-*` records with target, polarity/relation, bound coordinates, sufficiency, limitations, and provenance; Claim support-state output; access/reproducibility disposition; sanitized receipt; fabricated-evidence negative control; and proof that no Secret value is disclosed
- Expected result: hidden evidence is a gate failure, sanitized independent receipt can qualify, fabrication is `FALSE_EVIDENCE`, Claim support uses the closed support states, load-bearing Evidence remains a first-class relation, and Secrets remain undisclosed
- Failure condition: Reviewer must trust hidden evidence, a filename/log is accepted as Evidence without a qualified relation, `VERIFIED CLAIM` is used, inaccessible evidence is automatically called fabricated, or Secret disclosure is required

### ACC-GOV1-005 — Live authority gap

- Contracts: `CTR-GOV1-013`, `CTR-GOV1-018`
- Method: simulate a live permission with no accepted authority and known current dependency
- Environment: exact candidate Head
- Required evidence: exact live-state Observation; authority-gap classification; frozen expansion scope; attributable Owner containment/risk disposition with expiry or closure condition; docs-first closure reference; minimal runtime-reconcile record; independent Conformance Record; and containment-termination record
- Expected result: expansion freezes; neither automatic deletion nor permanent grandfathering occurs; Owner containment precedes docs-first closure and minimal reconcile
- Failure condition: runtime creates authority, documentation gap causes automatic destructive change, or Reviewer chooses the permanent result

### ACC-GOV1-006 — Review, acceptance, base movement, and Conformance binding

- Contracts: `CTR-GOV1-004`, `CTR-GOV1-014`, `CTR-GOV1-015`
- Method: keep candidate Head fixed while adding an unrelated base commit; separately change candidate semantics and a relevant parent authority; prepare a lifecycle-only final accepted Head; then create one valid Conformance Record and three invalid variants that omit `conformance_result`, claim unqualified permanent Spec-level `VERIFIED`, and reuse an old `VERIFIED` result after changing one bound coordinate
- Environment: exact review candidate, exact acceptance candidate, and temporary Conformance fixtures
- Required evidence: complete review tuple (`REVIEWED_BASE_COMMIT`, `REVIEWED_SPEC_COMMIT`, `REVIEWER_ID`); exact `REVIEW_TARGET_HEAD`, `BASE_HEAD`, and `CURRENT_BASE_HEAD`; bounded conflict/authority/behavior/evidence impact result; complete acceptance tuple (`FINAL_ACCEPTED_HEAD`, `ACCEPTANCE_ACTOR`, `ACCEPTED_AT`, `SEMANTIC_DELTA_AFTER_REVIEW`); an independent final-head delta recheck of the lifecycle transition and atomic backlinks; one valid Conformance Record containing implementation state, verification state, `conformance_result`, exact authority/implementation/environment/time coordinates, Observations, and Evidence; and executed rejection results for all three invalid variants
- Expected result: unrelated base movement receives bounded impact check only; candidate or relevant authority change invalidates affected review evidence; semantic delta requires new review; even lifecycle-only acceptance receives the independent final-head recheck; the valid Conformance Record passes; missing `conformance_result`, permanent Spec-level `VERIFIED`, and coordinate-changed result inheritance all fail
- Failure condition: every main commit triggers full review, semantic target drift reuses old review, an acceptance tuple omits the final Head or actor/time/delta, lifecycle-only metadata bypasses final-head recheck, an invalid Conformance Record passes, a Spec is permanently marked `VERIFIED`, or a changed bound coordinate inherits the old result

### ACC-GOV1-007 — Reviewer source closure

- Contracts: `CTR-GOV1-019`
- Method: ask a Reviewer to block on an accepted Contract violation, an Investigation preference, missing extra fault injection, and a verifier false pass
- Environment: exact candidate Head
- Required evidence: a finding matrix containing class, legal source identity, counterexample/reproduction, impact, minimal closure, and final blocker/non-blocker disposition for every injected case
- Expected result: accepted violation and false pass may block with all four fields; preference and non-load-bearing tooling ideas cannot
- Failure condition: labels alone create authority, or a concrete false pass cannot block

### ACC-GOV1-008 — Goal and stop controls

- Contracts: `CTR-GOV1-020`
- Method: complete the declared disabled-identity target while leaving optional Operator/App/Broker work available
- Environment: exact candidate Head
- Required evidence: recorded Goal/current gap, observable `DONE_WHEN`, applicable `EXPANSION_TRIGGER`, post-state Observation(s), Evidence that Done When is satisfied, the `STOP` decision, and the rejected expansion reasons
- Expected result: Done When satisfied plus no Expansion Trigger yields `STOP`; optional infrastructure is not progress
- Failure condition: Agent availability, sunk cost, tool imperfection, or optional platform work extends the task

### ACC-GOV1-009 — V0 carry-forward and current-authority compatibility

- Contracts: `CTR-GOV1-001`, `CTR-GOV1-002`, `CTR-GOV1-003`, `CTR-GOV1-004`, `CTR-GOV1-007`, `CTR-GOV1-009`, `CTR-GOV1-014`, `CTR-GOV1-015`, `CTR-GOV1-016`, `CTR-GOV1-017`, `CTR-GOV1-018`, `CTR-GOV1-020`
- Method: review the V0 carry-forward matrix, compare every V0 Contract clause with its V1 owner, and reconcile the exact current authority inventory including accepted `AGENT_OPERATIONAL_LAYER_V1`
- Environment: current main `45d4835723874ac1632434baded7ae5672225389`, exact V0 and Operational Layer revisions there, and exact V1 candidate Head
- Required evidence: current Spec index; exact V0, Operational Layer, and V1 revisions and frontmatter; the complete eleven-row V0 mapping; a compatibility matrix proving which V1 clauses constrain the Operational Layer without changing its accepted meaning; proof that the accepted Operational Layer index row and bytes remain present; clause-by-clause comparison covering consumer authority, immutable adoption, primitive/Evidence/Claim types, immutable meaning, review and final accepted-Head binding, qualified Conformance result, explicit implementation authority, persistence, enforcement, emergency handling, and exhausted bootstrap exception; plus transition-validation and final-head-recheck expectations
- Expected result: all eleven V0 Contracts are retained or replaced by equivalent protection; V1 supersedes V0 only; `AGENT_OPERATIONAL_LAYER_V1` remains accepted and active without silent deletion, supersession, in-place reparenting, or semantic rewrite; future Operational Layer implementation is gated by exact dual-authority PREFLIGHT; and no consumer, identity, evidence, lineage, review-binding, implementation-authority, conformance, persistence, enforcement, emergency, or bootstrap-boundary protection disappears
- Failure condition: any V0 Contract lacks an explicit equivalent, any listed V1 owner omits a load-bearing V0 clause, the accepted Operational Layer row or bytes disappear, its accepted `governed_by` field is silently edited, V1 implicitly supersedes it, a conflict is ignored, or protection is silently weakened outside a deliberate Decision

### ACC-GOV1-010 — Targeted regression and rollout canaries

- Contracts: `CTR-GOV1-009`, `CTR-GOV1-011`, `CTR-GOV1-012`, `CTR-GOV1-013`, `CTR-GOV1-014`, `CTR-GOV1-020`
- Method: rerun the four targeted failures and later exercise the three named consumer canaries after distribution implementation
- Environment: exact implementation Head and exact adopted consumer Heads
- Required evidence: exact implementation and adopted consumer Heads; the four targeted failure-injection inputs and outputs; the three canary classification/route records; affected checks and executed results; and a negative assertion showing no fixed Agent count or unauthorized platform dependency
- Expected result: four targeted failures pass; canaries produce their distinct routes; no fixed Agent count or new platform is required
- Failure condition: any prior critical ambiguity returns, permission gap is hidden as REUSE, or rollout requires a platform not authorized here

### Contract coverage

| Contract | Acceptance |
|---|---|
| `CTR-GOV1-001` | `ACC-GOV1-001`, `ACC-GOV1-009` |
| `CTR-GOV1-002` | `ACC-GOV1-009` |
| `CTR-GOV1-003` | `ACC-GOV1-004`, `ACC-GOV1-009` |
| `CTR-GOV1-004` | `ACC-GOV1-006`, `ACC-GOV1-009` |
| `CTR-GOV1-005` | `ACC-GOV1-001` |
| `CTR-GOV1-006` | `ACC-GOV1-001` |
| `CTR-GOV1-007` | `ACC-GOV1-002` |
| `CTR-GOV1-008` | `ACC-GOV1-002` |
| `CTR-GOV1-009` | `ACC-GOV1-002`, `ACC-GOV1-010` |
| `CTR-GOV1-010` | `ACC-GOV1-002` |
| `CTR-GOV1-011` | `ACC-GOV1-003`, `ACC-GOV1-010` |
| `CTR-GOV1-012` | `ACC-GOV1-004`, `ACC-GOV1-010` |
| `CTR-GOV1-013` | `ACC-GOV1-005`, `ACC-GOV1-010` |
| `CTR-GOV1-014` | `ACC-GOV1-006`, `ACC-GOV1-010` |
| `CTR-GOV1-015` | `ACC-GOV1-006`, `ACC-GOV1-009` |
| `CTR-GOV1-016` | `ACC-GOV1-009` |
| `CTR-GOV1-017` | `ACC-GOV1-009` |
| `CTR-GOV1-018` | `ACC-GOV1-005`, `ACC-GOV1-009` |
| `CTR-GOV1-019` | `ACC-GOV1-007` |
| `CTR-GOV1-020` | `ACC-GOV1-008`, `ACC-GOV1-010` |

## 11. Alternatives and disposition

### ALT-GOV1-001 — Keep the V0 non-mechanical route unchanged

- Disposition: rejected
- Reason: four repository pilots repeatedly converted complexity, risk, or execution friction into unnecessary Spec work and allowed non-authoritative material to create obligations.
- What would reopen: evidence that the simulations misclassified the failures and the original route can close all six boundaries without three-axis routing.

### ALT-GOV1-002 — Remove formal Spec governance entirely

- Disposition: rejected
- Reason: permissions, Secrets, destructive migration, public protocols, and authority replacement still need prior normative authorization and independent review.
- What would reopen: none under the current product and security model.

### ALT-GOV1-003 — Build an enforcement platform before changing the grammar

- Disposition: rejected
- Reason: targeted resimulation required no App, Broker, WORM store, central database, or fixed Agent formation.
- What would reopen: concrete repeated bypasses that native repository controls and the accepted V1 method cannot prevent.

### ALT-GOV1-004 — Treat runtime as authority when documentation lags

- Disposition: rejected
- Reason: this allows accidental or unauthorized state to legislate permanently.
- What would reopen: none; live facts remain Observations.

### ALT-GOV1-005 — Automatically delete every live state without authority

- Disposition: rejected
- Reason: documentation gaps may coexist with real dependencies; deletion requires an authorized risk decision.
- What would reopen: an accepted Contract requiring immediate revocation for that exact state.

### ALT-GOV1-006 — Require a full primitive graph and full Contract audit for every task

- Disposition: rejected
- Reason: it recreates the paperwork and review amplification V1 is meant to fix.
- What would reopen: a controlled or release context whose risk cannot be bounded more narrowly.

## 12. Migration, compatibility, and rollback

```text
AUTHORING_MIGRATION = none; this PR is docs-only and proposed
CURRENT_BASE_RECONCILIATION = 45d4835723874ac1632434baded7ae5672225389
ACCEPTANCE_MIGRATION = atomic whole-authority V0 -> V1 transition after independent review
OPERATIONAL_LAYER_DISPOSITION = accepted and active; not superseded, amended, implemented, or reparented by this PR
OPERATIONAL_LAYER_LINEAGE = governed_by V0 retained as immutable acceptance-time lineage
FUTURE_OPERATIONAL_LAYER_WORK = re-PREFLIGHT against exact active V1 and exact accepted Operational Layer; semantic change or parent rebinding uses a separate authority action and successor when required
DISTRIBUTION_IMPLEMENTATION = separate later PR based on accepted V1 and compatible accepted Operational Layer obligations
CONSUMER_ADOPTION = exact immutable revision, repository-local review and acceptance
HISTORICAL_MIGRATION = forward-only; no bulk rewrite
COMPATIBILITY = V0 continues to govern until accepted V1 is merged; accepted AGENT_OPERATIONAL_LAYER_V1 remains active and unchanged; existing consumer pins remain unchanged until local adoption
ROLLBACK = before acceptance, close or revise this proposal; after distribution release, consumers may revert to their prior exact pin subject to their local authority
EMERGENCY_CONTAINMENT = V0 emergency boundary remains active until V1 acceptance
```

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
CURRENT_MAIN_RECONCILED = 45d4835723874ac1632434baded7ae5672225389
OPERATIONAL_LAYER_COMPATIBILITY = COMPATIBLE_NO_SEMANTIC_DELTA
OPERATIONAL_LAYER_SUPERSEDED = NO
OPERATIONAL_LAYER_REPARENTED_IN_PLACE = NO
V0_CONTRACTS_MAPPED = 11 / 11
CRITICAL_BOUNDARIES_FORMALIZED = 6 / 6
TARGETED_FAILURES_REPRESENTED = 4 / 4
ROLLOUT_CANARIES_REPRESENTED = 3 / 3
AUTHORING_READY_FOR_REVIEW = YES
READY_TO_MARK_ACCEPTED = NO
DISTRIBUTION_IMPLEMENTED = NO
CONSUMERS_CHANGED = NO
PRODUCTION_OPERATION_AUTHORIZED = NO
```
