---
spec_id: AGENT_SIX_PACK_DELIVERY_PROFILE_V1
status: proposed
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
  - reusable-agent-workflows
  - software-delivery-six-pack
governed_by:
  - AGENT_DEVELOPMENT_GOVERNANCE_V1
  - AGENT_OPERATIONAL_LAYER_V1
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# AGENT_SIX_PACK_DELIVERY_PROFILE_V1

## 1. Goal

Define a faithful six-role software-delivery profile, informed by Robert C. Martin's SwarmForge `six-pack`, for work that has already passed repository-local Governance PREFLIGHT.

```text
GOAL = authorized software work moves through six explicit professional responsibilities without one Agent silently owning specification, implementation, cleanup, architecture, hardening, and final verification at once
SUCCESS_OUTCOME = the selected delivery profile produces a traceable exact-commit chain from behavior specification through independent user-facing verification while Product Authority, execution permission, candidate state, Evidence, and Owner merge remain separate
```

The default role sequence is:

```text
specifier
-> coder
-> cleaner
-> architect
-> hardender
-> QA
```

## 2. Scope and non-goals

### In scope

- one explicit software-delivery profile with six real runtime roles;
- the exact default role order `specifier -> coder -> cleaner -> architect -> hardender -> QA`;
- role-specific `Owns`, `Does Not Own`, entry, exit, handoff, and failure boundaries;
- one isolated worktree or equivalent isolated write surface per writing role;
- exact-commit, task-stable, durable handoff records and restart-safe inbox state;
- a two-call unchanged-candidate self-audit gate before each forward Git handoff;
- forward handoff, backward correction, batch receive, and terminal broadcast rules;
- behavior specification, TDD implementation, structure-preserving cleanup, architectural review, mutation hardening, and user-facing QA;
- repository-approved pinned verification tools and manifests;
- final exact-Head independent review and separate Owner merge decision;
- two real pilot canaries before general consumer distribution.

### Profile applicability

This profile is intended for non-trivial software delivery, including:

- new or changed externally observable behavior;
- public API, protocol, compatibility, lifecycle, permission, security, or durable-data behavior;
- substantial internal implementation or architectural work whose failure can create a durable regression;
- work for which mutation hardening or independent end-to-end verification can change the merge decision.

Pure governance authoring, release metadata, exact-coordinate updates, adoption preparation, spelling-only changes, and emergency containment do not automatically enter this profile. Their Governance route remains controlled by `AGENT_DEVELOPMENT_GOVERNANCE_V1`.

Once this profile is selected for a task during the V1 pilot, all six stages are required. A stage MUST NOT be silently skipped, merged away, or declared complete by another stage. A different delivery profile requires a separate explicit authority or Owner-approved pilot decision; it is not an ad hoc per-role shortcut.

### Out of scope

- changing the semantic primitives, authority precedence, three-axis PREFLIGHT, Blocker taxonomy, or stop rules of `AGENT_DEVELOPMENT_GOVERNANCE_V1`;
- changing accepted `AGENT_OPERATIONAL_LAYER_V1` Contracts in place;
- making a role prompt, Gherkin file, test, handoff, queue, commit, or QA result into Product Authority;
- assigning fixed model providers, fixed Agent IDs, fixed machines, or fixed credentials to the six roles;
- permitting `--yolo`, `bypassPermissions`, self-issued mutation permission, or broad credential bypass;
- letting a role write directly to an active main checkout;
- fetching mutable upstream `main`, branch tips, or latest tool versions during a governed run;
- implementing the runtime, queue daemon, dashboard, helper scripts, provider adapters, or consumer adoption in this docs-only Spec PR;
- modifying product code, consumers, runtime, permissions, Grants, Credentials, Secrets, GitHub settings, or production state;
- allowing QA to modify a candidate and then certify that modified Head as independently verified without a correction loop;
- auto-merging a terminal handoff to the authority branch.

### Prior-art fidelity and required adaptations

The profile retains these SwarmForge six-pack ideas:

```text
six named roles and fixed forward order
explicit Owns / Does Not Own boundaries
role-specific worktrees
commit-based handoff
restart-safe file-backed inbox lifecycle
task and batch receive modes
back-propagation of structural changes
two-call unchanged-candidate self-audit
Gherkin and end-to-end specification
TDD implementation
cleanup before architecture review
architecture before mutation hardening
mutation hardening before final QA
terminal completion broadcast
```

The following adaptations are required by higher local authority:

```text
original specifier-on-master write -> dedicated isolated specifier write surface
moving branch / latest dependency  -> exact immutable revision and manifest
--yolo / bypassPermissions         -> forbidden without a valid narrower mandate
QA fix-and-self-certify            -> correction handoff and new final verification
pack completion                    -> still separate from Owner merge and acceptance
private/internal API QA shortcut   -> forbidden; use the supported public user boundary
```

## 3. Authority and dependencies

```text
AUTHORITY_ACTION = NEW
PRIMARY_PARENT_AUTHORITY = AGENT_OPERATIONAL_LAYER_V1
CO_GOVERNING_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_V1
IMPLEMENTATION_AUTHORITY = contracts
EXTERNAL_AUTHORITIES = NONE
AUTHORITY_CONFLICT = NONE

NON_NORMATIVE_PRIOR_ART =
  unclebob/swarm-forge six-pack@581abcd87eed09991bc891e2cbdcbde2e5f5f58c
  unclebob/swarm-forge main@d1e401aeb45fa5281f2a6a4b2627d3dea2ca8f8c
```

`AGENT_DEVELOPMENT_GOVERNANCE_V1` decides whether work is authorized, whether Product Authority must change, how much planning and assurance are required, what Evidence is load-bearing, and when work must stop.

`AGENT_OPERATIONAL_LAYER_V1` owns the subordinate operational boundary: Skills and execution artifacts may guide and constrain work but cannot create Product Authority or their own mutation permission.

This Spec creates a new bounded delivery profile under those authorities. SwarmForge is prior art only. Its repository, prompts, branches, scripts, and conventions do not own or supersede local Product Authority.

## 4. Current State

### STATE-SIX-001 — Governance decides whether work may proceed, but no accepted full delivery topology exists

- Subject: reusable development distribution in `mayf3/agent-development-governance`
- As of commit/artifact: `4a08770792ce96c1183dbf97c908950c6ba492a3`
- Environment: repository `main`
- Observed at: 2026-09-03
- Projection: Governance V1 separates Authority, Plan, and Assurance and requires exact coordinates, valid mutation authorization, Evidence reviewability, and `DONE_WHEN -> STOP`; the accepted Operational Layer defines Skills and Records, but no accepted Contract defines a full multi-role software-delivery topology.
- Basis: `OBS-SIX-001`, `OBS-SIX-002`, `CLM-SIX-001`

### STATE-SIX-002 — SwarmForge six-pack provides a mature six-role delivery sequence and durable handoff model

- Subject: `unclebob/swarm-forge` six-pack and shared runtime
- As of commit/artifact: six-pack `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`; main `d1e401aeb45fa5281f2a6a4b2627d3dea2ca8f8c`
- Environment: public repository source
- Observed at: 2026-09-03
- Projection: the source defines six distinct roles in a fixed sequence, role-specific worktrees, durable file-backed handoffs, a self-audit challenge, batch and reverse propagation, mutation hardening, and final QA.
- Basis: `OBS-SIX-003` through `OBS-SIX-009`, `CLM-SIX-002`, `CLM-SIX-003`

### STATE-SIX-003 — Direct copying would conflict with accepted local governance

- Subject: compatibility between SwarmForge prior art and accepted local governance
- As of commit/artifact: local Governance `4a08770792ce96c1183dbf97c908950c6ba492a3`; prior art coordinates above
- Environment: comparative design review
- Observed at: 2026-09-03
- Projection: moving branch downloads, latest-tool acquisition, a writing role on the master checkout, permission-bypass modes, and QA self-certification after fixes cannot be copied without violating exact-revision, write-isolation, mandate, and independent-review requirements.
- Basis: `OBS-SIX-002`, `OBS-SIX-009`, `OBS-SIX-010`, `CLM-SIX-004`

## 5. Observations

### OBS-SIX-001 — Governance V1 separates authority, planning, assurance, and stopping

- Subject: accepted development governance
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `4a08770792ce96c1183dbf97c908950c6ba492a3`
- Environment: repository source
- Observed at: 2026-09-03
- Method: inspect `.agents/README.md`, `.agents/protocol/SPEC_GOVERNANCE_V1.md`, and accepted `AGENT_DEVELOPMENT_GOVERNANCE_V1`
- Result: Product Authority, Execution Mandate, Plan level, Assurance level, Evidence reviewability, exact candidate coordinates, load-bearing gaps, and stop conditions are separately governed.
- Provenance: named repository paths and accepted Spec

### OBS-SIX-002 — Operational Layer forbids operational artifacts from becoming authority

- Subject: accepted operational boundary
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `AGENT_OPERATIONAL_LAYER_V1` at `4a08770792ce96c1183dbf97c908950c6ba492a3`
- Environment: repository source
- Observed at: 2026-09-03
- Method: inspect Goal, scope, Decisions, and Contracts
- Result: Skills, scripts, tests, provider metadata, Records, and review artifacts remain subordinate to accepted Product Authority and externally available mutation permission.
- Provenance: `docs/specs/AGENT_OPERATIONAL_LAYER_V1.md`

### OBS-SIX-003 — Six-pack defines six named roles in one fixed forward pipeline

- Subject: six-pack topology
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect `README.md` and `swarmforge/swarmforge.conf`
- Result: the pack declares `specifier -> coder -> cleaner -> architect -> hardender -> QA`, with task receive for the first two roles and batch receive for later quality roles.
- Provenance: `README.md`, `swarmforge/swarmforge.conf`

### OBS-SIX-004 — Role prompts separate ownership and forbidden work

- Subject: role specialization
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect all six files under `swarmforge/roles/`
- Result: specification, coding, cleanup, architecture, mutation hardening, and QA are separately owned; each role explicitly excludes work owned by later or earlier stages.
- Provenance: `specifier.prompt`, `coder.prompt`, `cleaner.prompt`, `architect.prompt`, `hardender.prompt`, `QA.prompt`

### OBS-SIX-005 — Specifier produces behavior specifications and an end-to-end QA procedure

- Subject: behavior-definition stage
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect `swarmforge/roles/specifier.prompt`
- Result: the role converts user intent into concise Gherkin acceptance behavior and a user-interface QA suite while avoiding unnecessary implementation prescription.
- Provenance: `swarmforge/roles/specifier.prompt`

### OBS-SIX-006 — The middle roles deliberately partition implementation, cleanup, architecture, and hardening

- Subject: engineering quality stages
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect coder, cleaner, architect, and hardender role prompts
- Result: coder owns TDD and minimal implementation; cleaner owns behavior-preserving local cleanup; architect owns boundaries, dependency direction, information hiding, and property testing; hardender owns mutation and related test-effectiveness hardening.
- Provenance: four named role prompt files

### OBS-SIX-007 — QA owns final user-facing verification

- Subject: terminal quality gate
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect `swarmforge/roles/QA.prompt`
- Result: QA executes accepted specifications, generated acceptance tests, end-to-end user-facing procedures, property tests when present, architecture-sensitive workflows, and release checks; the role may fix discovered bugs in the original source.
- Provenance: `swarmforge/roles/QA.prompt`

### OBS-SIX-008 — Handoffs are durable, commit-bound, restart-safe queue items

- Subject: inter-role handoff protocol
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: main `d1e401aeb45fa5281f2a6a4b2627d3dea2ca8f8c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect `swarmforge/handoff-protocol.md` and shared handoff scripts
- Result: agents write validated outbound files; a daemon delivers them to `inbox/new`; helpers move work through `in_process` and `completed`; exact commits and timestamps support restart and audit.
- Provenance: `swarmforge/handoff-protocol.md`, `swarmforge/scripts/`

### OBS-SIX-009 — First Git handoff triggers an unchanged-candidate audit challenge

- Subject: sender self-audit gate
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: main `d1e401aeb45fa5281f2a6a4b2627d3dea2ca8f8c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect `swarm_handoff.sh` protocol and implementation references
- Result: the first valid Git handoff records the exact candidate and returns `AUDIT_REQUIRED`; only a repeated unchanged candidate may be queued, and candidate changes invalidate the challenge.
- Provenance: `swarmforge/handoff-protocol.md`, `swarmforge/scripts/swarm_handoff.bb`

### OBS-SIX-010 — SwarmForge source acquisition and permission defaults are not exact-revision governance

- Subject: source and execution safety differences
- Repository/source: `unclebob/swarm-forge`
- Commit/artifact: six-pack `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`; main `d1e401aeb45fa5281f2a6a4b2627d3dea2ca8f8c`
- Environment: public repository source
- Observed at: 2026-09-03
- Method: inspect `swarm`, `get-swarm-forge`, shared engineering article, and six-pack configuration
- Result: default composition downloads branch archives and shared `main`, startup guidance asks for latest tools, the pack assigns specifier to master, and some agents use permission-bypass modes.
- Provenance: `swarm`, `get-swarm-forge`, `swarmforge/constitution/articles/engineering.prompt`, `swarmforge/swarmforge.conf`

## 6. Claims and assumptions

### CLM-SIX-001 — A delivery profile belongs below Governance and Operational Layer authority

- Support state: SUPPORTED
- Supported by evidence: `EVD-SIX-001`
- Contradicted by evidence: none known
- Uncertainty: the runtime encoding remains an implementation choice.

### CLM-SIX-002 — Six distinct roles reduce judgment contamination across software-delivery concerns

- Support state: INFERRED
- Supported by evidence: `EVD-SIX-002`
- Contradicted by evidence: no local pilot yet
- Uncertainty: the net cost and defect reduction must be measured on real local canaries.

### CLM-SIX-003 — Durable exact-commit handoff is safer than chat-only continuation

- Support state: SUPPORTED
- Supported by evidence: `EVD-SIX-003`
- Contradicted by evidence: none known
- Uncertainty: exact queue storage and daemon technology remain implementation choices.

### CLM-SIX-004 — Faithful six-role adoption requires explicit local safety adaptations

- Support state: SUPPORTED
- Supported by evidence: `EVD-SIX-004`
- Contradicted by evidence: none known
- Uncertainty: a future sandbox may safely permit additional automation, but it cannot weaken accepted authority.

### CLM-SIX-005 — The first local version should preserve all six stages before considering compression

- Support state: OPEN_ASSUMPTION
- Supported by evidence: `EVD-SIX-005`
- Contradicted by evidence: previous simulations warned against making six roles a universal governance condition
- Uncertainty: pilot Evidence may later support merging roles or defining another profile; this Spec limits the six-stage requirement to tasks that select this profile.

## 7. Evidence relations

### EVD-SIX-001 — Accepted local authority supports a subordinate delivery profile

- Source observations: `OBS-SIX-001`, `OBS-SIX-002`
- Target: `CLM-SIX-001`
- Relation: SUPPORTS
- Bound coordinates: local governance `4a08770792ce96c1183dbf97c908950c6ba492a3`
- Strength/sufficiency: decisive for keeping the profile non-authoritative and mandate-bound
- Limitations: does not choose the six-role topology
- Provenance: accepted local Specs and distributed grammar

### EVD-SIX-002 — Role separation supports six professional checkpoints

- Source observations: `OBS-SIX-003`, `OBS-SIX-004`, `OBS-SIX-005`, `OBS-SIX-006`, `OBS-SIX-007`
- Target: `CLM-SIX-002`
- Relation: SUPPORTS
- Bound coordinates: six-pack `581abcd87eed09991bc891e2cbdcbde2e5f5f58c`
- Strength/sufficiency: sufficient to justify a faithful pilot profile
- Limitations: static source inspection does not establish local throughput or defect reduction
- Provenance: six-pack README, configuration, and role prompts

### EVD-SIX-003 — File-backed handoff lifecycle supports durable continuation

- Source observations: `OBS-SIX-008`, `OBS-SIX-009`
- Target: `CLM-SIX-003`
- Relation: SUPPORTS
- Bound coordinates: shared main `d1e401aeb45fa5281f2a6a4b2627d3dea2ca8f8c`
- Strength/sufficiency: strong for exact-candidate and restart requirements
- Limitations: does not prove the Babashka daemon is the only valid implementation
- Provenance: handoff protocol and scripts

### EVD-SIX-004 — Local authority and prior-art differences require adaptation

- Source observations: `OBS-SIX-001`, `OBS-SIX-002`, `OBS-SIX-007`, `OBS-SIX-010`
- Target: `CLM-SIX-004`
- Relation: SUPPORTS
- Bound coordinates: local `4a08770792ce96c1183dbf97c908950c6ba492a3`; upstream coordinates above
- Strength/sufficiency: decisive for exact pinning, write isolation, mandate checks, and QA re-verification
- Limitations: provider-specific sandbox details are not decided here
- Provenance: named local and prior-art paths

### EVD-SIX-005 — User direction and mature prior art support preserving six stages for the pilot

- Source observations: `OBS-SIX-003` through `OBS-SIX-009`
- Target: `CLM-SIX-005`
- Relation: SUPPORTS
- Bound coordinates: current authoring task and upstream source coordinates
- Strength/sufficiency: sufficient for a proposed pilot decision, not yet sufficient for general rollout
- Limitations: the claim remains an explicit pilot assumption until real canaries execute
- Provenance: authoring mandate and prior-art inspection

## 8. Decisions

### DEC-SIX-001 — Create a distinct six-pack delivery profile

- Decision owner: repository owner
- Decision: define `AGENT_SIX_PACK_DELIVERY_PROFILE_V1` as a subordinate governing Spec for software delivery after Governance PREFLIGHT.
- Rejected alternatives: copy six-pack prompts without authority integration; encode the profile only in a task prompt; amend Operational Layer prose in place.
- Reason: the delivery topology is a bounded long-lived decision that deserves an explicit child authority without changing parent meaning.
- Owner decision remaining: NONE

### DEC-SIX-002 — Preserve six real roles and the original forward order

- Decision owner: repository owner
- Decision: a task that selects this profile uses six distinct runtime roles in the fixed order `specifier -> coder -> cleaner -> architect -> hardender -> QA`.
- Rejected alternatives: begin with three compressed roles; treat the six names as one Agent's internal checklist; dynamically skip stages during the V1 pilot.
- Reason: the pilot should first test the mature prior-art separation before local optimization.
- Owner decision remaining: NONE

### DEC-SIX-003 — Make role identity operational, not Product Authority

- Decision owner: repository owner
- Decision: role names, Agent IDs, providers, models, and machines are runtime configuration. Role prompts and handoffs have `authority_effect: none` and remain subordinate to Product Authority and Execution Mandate.
- Rejected alternatives: make the specifier a product legislator; make six Agent availability a global governance precondition.
- Reason: delivery specialization must not silently change who owns long-lived decisions.
- Owner decision remaining: NONE

### DEC-SIX-004 — Use one isolated write surface per role

- Decision owner: repository owner
- Decision: all six roles use dedicated isolated worktrees or equivalent isolated write surfaces bound to exact parents; no writing role operates in the active main checkout.
- Rejected alternative: preserve the upstream specifier-on-master arrangement.
- Reason: accepted local governance makes write isolation mandatory for all mutations.
- Owner decision remaining: NONE

### DEC-SIX-005 — Preserve the original professional ownership split

- Decision owner: repository owner
- Decision: retain the six role responsibilities defined below, including explicit `Does Not Own` boundaries and stage-specific verification.
- Rejected alternative: ask every Agent for a broad full review at every stage.
- Reason: concern-specific ownership makes findings attributable and reduces repeated open-ended review.
- Owner decision remaining: NONE

### DEC-SIX-006 — Use durable exact-commit handoffs with task-stable identity

- Decision owner: repository owner
- Decision: every forward or backward handoff names a stable task, sender, recipient, exact full commit, exact parent/base, affected authority/Contracts, artifacts, and stage Evidence. Durable queue state survives lost notifications and Agent restarts.
- Rejected alternatives: chat-only summaries; branch-name handoffs; unvalidated abbreviated SHAs as the authority coordinate.
- Reason: the candidate itself, not the sender's narrative, must be the handoff object.
- Owner decision remaining: NONE

### DEC-SIX-007 — Require unchanged-candidate sender self-audit before forward handoff

- Decision owner: repository owner
- Decision: the first valid forward Git handoff records the exact candidate and returns `AUDIT_REQUIRED`; only a second submission of the unchanged candidate may enter the recipient queue. Any tree, commit, task, authority, or Evidence change invalidates the challenge.
- Rejected alternative: send immediately after tests pass.
- Reason: a deliberate second look catches omissions while binding the check to the current candidate.
- Owner decision remaining: NONE

### DEC-SIX-008 — Preserve task/batch receiving and backward convergence

- Decision owner: repository owner
- Decision: the default receive and propagation profile is:

```text
specifier  task   forward-only
coder      task   forward-only
cleaner    batch  back-one
architect  batch  back-all
hardender  batch  forward-only
QA         batch  back-all terminal broadcast
```

Backward copies are merge-only state convergence. A correction request is explicit work and returns to the earliest affected owning role before moving forward again.
- Rejected alternative: each role keeps an unrelated branch and relies on a final conflict-heavy merge.
- Reason: structural improvements should propagate without turning reverse synchronization into new feature work.
- Owner decision remaining: NONE

### DEC-SIX-009 — Pin tools and prior-art inputs to exact revisions

- Decision owner: repository owner
- Decision: runtime implementation MUST vendor or resolve all profile prompts, helpers, schemas, and verification tools at exact immutable revisions recorded in a manifest. A governed task MUST NOT fetch moving branch tips or “latest available” tools during execution.
- Rejected alternative: copy SwarmForge's default branch composition and latest-tool acquisition unchanged.
- Reason: exact Evidence and replay require stable bytes.
- Owner decision remaining: NONE

### DEC-SIX-010 — Forbid permission bypass as a profile default

- Decision owner: repository owner
- Decision: no role receives `--yolo`, `bypassPermissions`, or equivalent broad bypass from the delivery profile. Any exceptional permission is separately authorized by a valid Execution Mandate and remains narrower than accepted Product Authority.
- Rejected alternative: preserve upstream provider flags literally.
- Reason: a delivery profile cannot authorize its own escape from mutation controls.
- Owner decision remaining: NONE

### DEC-SIX-011 — Make QA correction invalidate final verification

- Decision owner: repository owner
- Decision: QA may diagnose and prepare a minimal fix, but any QA-owned candidate mutation invalidates the current final verification. The task returns to the earliest affected role, replays all affected downstream stages, and ends with a fresh QA run in which QA does not modify the certified exact Head.
- Rejected alternative: QA fixes a bug and immediately self-certifies the new Head.
- Reason: the final attestation must be independent of the bytes it certifies.
- Owner decision remaining: NONE

### DEC-SIX-012 — Pilot before distribution implementation or role compression

- Decision owner: repository owner
- Decision: after this Spec is accepted, implementation occurs in a separate PR and must run two real canaries before stable distribution: one medium internal feature and one new public-interface feature. V1 does not merge or skip roles based only on opinion or unused capacity.
- Rejected alternative: immediately alter all consumers or optimize the role count before observing the full chain.
- Reason: real Evidence should determine whether any stage lacks decision impact.
- Owner decision remaining: NONE

## 9. Contracts

### CTR-SIX-001 — The profile remains subordinate to Product Authority and Execution Mandate

No role, prompt, Gherkin file, test, architecture note, mutation result, QA procedure, handoff, queue record, dashboard state, or commit MAY create, accept, amend, supersede, or reinterpret Product Authority. Every profile artifact MUST declare or inherit `authority_effect: none`. A valid Execution Mandate is required for mutation and cannot change Product Contracts.

### CTR-SIX-002 — Profile selection is explicit and six stages are mandatory once selected

The task route MUST record `DELIVERY_PROFILE = SIX_PACK_V1` before candidate work begins. The profile MAY be selected only after Governance PREFLIGHT has resolved the applicable Authority action, Plan level, Assurance level, Product Authority, and mutation authorization. Once selected during the V1 pilot, the task MUST pass through all six roles in order. A stage skip, merge, replacement, or reordering MUST fail unless a separately accepted delivery-profile authority permits it.

### CTR-SIX-003 — Six distinct runtime roles and write surfaces are required

The runtime MUST instantiate distinct `specifier`, `coder`, `cleaner`, `architect`, `hardender`, and `QA` roles. Each writing role MUST operate in its own isolated worktree or equivalent isolated write surface bound to an exact parent and isolated ref. No profile role MAY mutate the active main checkout. Specific Agent IDs, models, backends, and machines remain configuration and MUST NOT alter role ownership.

### CTR-SIX-004 — Specifier owns behavior specification but not product legislation

Specifier MUST:

- read the exact accepted Product Authority and task mandate;
- express externally observable behavior, examples, failure cases, and acceptance criteria in concise deterministic form;
- produce Gherkin-compatible behavior specifications when the repository supports the Acceptance Pipeline;
- produce an end-to-end QA procedure through the supported public user boundary;
- avoid unnecessary implementation prescription;
- stop with `SPEC_GAP_DEPENDENCY = LOAD_BEARING` and `NEXT_ACTION = RE_PREFLIGHT` when required behavior is not decided by accepted authority.

Specifier MUST NOT invent a Product Contract, accept a Spec, modify product implementation, run mutation hardening, or declare final conformance.

For an API-first product, the supported public API is a user-facing boundary; privileged internal APIs, test-only service hooks, and direct persistence access are not valid end-to-end substitutes.

### CTR-SIX-005 — Coder owns TDD and minimal implementation

Coder MUST start from the exact accepted behavior specification, write focused unit tests that fail for plausible wrong implementations, implement only enough production behavior to satisfy accepted behavior, and run unit plus generated acceptance tests before handoff. Coder MUST keep environment-specific behavior behind narrow adapters when practical.

Coder MUST NOT redefine acceptance behavior, perform broad cleanup, own architectural restructuring, run mutation hardening, or certify final QA.

### CTR-SIX-006 — Cleaner preserves behavior while improving local structure

Cleaner MUST preserve accepted observable behavior and passing acceptance/unit tests while improving local names, cohesion, duplication, complexity, test readability, stale comments, dead code, and testability. Cleaner MAY split mixed-duty local functions or files and move behavior behind small adapter boundaries when behavior remains unchanged.

Cleaner MUST NOT introduce new behavior, alter Product Contracts, own high-level dependency direction, or perform mutation testing.

### CTR-SIX-007 — Architect owns system boundaries and dependency direction

Architect MUST evaluate module boundaries, dependency direction, information hiding, framework and persistence leakage, import cycles, accidental public APIs, and adapter/domain duplication. High-level domain answers MUST be called rather than reimplemented by IO-near adapters. Architect MUST add or improve property tests and lightweight architecture checks when they can reject a relevant wrong structure.

Architect MUST preserve accepted behavior and MUST NOT create new Product Authority or replace hardender's mutation gate.

### CTR-SIX-008 — Hardender owns test-effectiveness hardening

Hardender MUST evaluate whether tests reject plausible wrong implementations through repository-approved differential language mutation, Gherkin mutation when applicable, and related CRAP/DRY checks. Hardening MUST target changed or affected behavior, preserve tool manifests, and keep hardening tests distinct from unit and acceptance tests. The default changed-file CRAP gate is 10 or below, except a documented single-question branch construct that does not hide mixed duties.

Hardender MUST NOT invent behavior, change accepted examples merely to kill mutants, or bypass pinned tool requirements.

### CTR-SIX-009 — QA owns final independent user-facing verification

QA MUST verify the exact candidate against accepted behavior specifications, generated acceptance tests, the specifier's end-to-end QA procedure, unit tests, property tests when present, architecture-sensitive workflows, required manifests, and release checks. End-to-end verification MUST use the supported public user boundary and MUST NOT use a privileged internal bypass.

A valid final QA receipt MUST bind the exact candidate Head/tree, environment, procedures, results, limitations, and artifacts. QA MUST NOT declare Owner acceptance or merge authority.

### CTR-SIX-010 — Role ownership is closed and explicit

Every role prompt or machine-readable role definition MUST declare `Owns`, `Does Not Own`, required inputs, permitted mutations, required checks, handoff target, failure output, and done criteria consistent with `CTR-SIX-004` through `CTR-SIX-009`. A role MUST stop and report when asked to perform another role's exclusive decision rather than silently broadening scope.

### CTR-SIX-011 — Handoffs bind exact candidate state

Every Git handoff MUST contain or machine-bind:

```text
handoff_id
task_id
from_role
to_role_or_roles
priority
handoff_type
base_head
candidate_head_full_sha
candidate_tree
accepted_authority_revisions
affected_contracts
artifacts
executed_stage_evidence
created_at
audit_challenge_id
```

Branch names, chat summaries, short ambiguous SHAs, or “latest” references MUST NOT substitute for exact commit/tree coordinates. The helper MAY render a short display abbreviation but MUST retain the full SHA as the authority coordinate.

### CTR-SIX-012 — Queue state is durable, restart-safe, and single-owned

The implementation MUST provide at least:

```text
outbox/tmp
outbox
sent
failed
inbox/new
inbox/in_process
inbox/completed
audit_pending
```

File or record location is the durable queue state. Wake-up notifications are lossy hints only. Helper tooling, not Agents, owns atomic queue transitions, timestamps, duplicate suppression, restart recovery, and refusal of ambiguous multiple-in-process states. Runtime queue state MUST NOT be committed as product source.

### CTR-SIX-013 — Forward handoff requires a two-call unchanged-candidate audit

On the first valid forward Git handoff attempt for a sender/task/candidate tuple, the helper MUST persist the exact challenge, increment the task audit count once, leave the task in process, and return `AUDIT_REQUIRED` without delivery. The sender MUST re-read the complete inbound task, authority, constraints, role ownership, changed files, tests, boundaries, and failure cases. A second attempt MAY deliver only when task identity, candidate Head/tree, authority coordinates, artifacts, and Evidence remain unchanged. Any change invalidates the old challenge and requires a new audit.

This gate is author self-check, not independent review.

### CTR-SIX-014 — Handoff progression and correction are deterministic

Normal forward progression MUST be:

```text
specifier -> coder -> cleaner -> architect -> hardender -> QA
```

Every stage commits before forward handoff. A forward role MUST hand off even when its only changes are structural, test, manifest, formatting, or audit artifacts required by the profile. Back-propagation copies are merge-only and MUST NOT create duplicate forward work. A substantive correction request MUST identify the earliest affected owning role, preserve the stable task ID, and then replay all affected downstream stages.

The implementation MUST provide helper-owned merge/replay semantics and MUST reject ad hoc invented merge commands when the helper owns the transition.

### CTR-SIX-015 — Receive modes and terminal broadcast preserve convergence

The default receive modes and propagation tokens in `DEC-SIX-008` MUST be represented in configuration and validated. Equal-priority batch roles MUST process helper-delivered items in deterministic order. Final QA completion MUST broadcast the exact terminal candidate to the other five roles as merge-only state convergence; recipients MUST NOT re-forward terminal copies. Terminal broadcast completes the profile lane but does not merge to main.

### CTR-SIX-016 — All profile bytes and tools are exactly pinned

Every distributed prompt, constitution article, helper, schema, role configuration, and verification tool MUST be identified by exact immutable source revision and deterministic manifest hash. Runtime startup MUST fail closed when required bytes do not match. It MUST NOT silently fetch a moving branch, install “latest” tooling, or substitute a cached/preinstalled executable whose identity is not part of the accepted local toolchain record.

### CTR-SIX-017 — The profile cannot grant permission bypass

The profile MUST NOT configure `--yolo`, `bypassPermissions`, unrestricted shell, credential escalation, or equivalent broad bypass as a role default. A task-specific exception requires a valid attributable Execution Mandate that binds actor, target, environment, exact operation or operation class, allowed and forbidden effects, Secrets handling, abort conditions, receipt, validity, and attempt bounds. The effective permission remains the intersection of accepted authority, mandate, identity, credentials, target coordinates, and the role's narrower scope.

### CTR-SIX-018 — Specification gaps and public-interface changes return to Governance

When any role discovers that current work depends on a new or changed long-lived behavior not decided by accepted Product Authority, it MUST stop dependent work, record the Observation and affected boundary, and return `SPEC_GAP_DEPENDENCY = LOAD_BEARING`, readiness `NO`, and `NEXT_ACTION = RE_PREFLIGHT`. Calling an exported or consumer-dependent interface an “implementation detail” MUST NOT bypass this rule. The role MAY identify questions and counterexamples but MUST NOT author the missing Product Contract unless separately assigned the valid authoring route.

### CTR-SIX-019 — Candidate mutation invalidates downstream attestations

Any candidate Head/tree change after a stage receipt invalidates that receipt for the changed and transitively affected surface. The correction MUST return to the earliest affected owning role and replay every affected downstream stage. When QA changes product, test, configuration, or behavior-defining bytes, the current QA receipt is invalid and a later QA run over an unchanged exact candidate is required. Unaffected prior Evidence MAY be reused only when an explicit impact check shows its bound tuple is unchanged.

### CTR-SIX-020 — Final integration remains independently reviewed and Owner-controlled

Profile completion requires:

```text
six stage receipts
terminal exact candidate Head/tree
final QA receipt on an unchanged candidate
handoff/manifest consistency
no unresolved load-bearing SPEC_GAP
DONE_WHEN satisfied
```

For Durable or Controlled work, a legally independent Reviewer MUST perform the applicable exact-Head affected-Contract or complete review after terminal QA. Owner acceptance, Ready transition, and merge remain separate actions. Neither terminal broadcast nor QA success MAY auto-merge or self-authorize main-branch mutation.

### CTR-SIX-021 — Pilot Evidence precedes stable rollout or role compression

Before stable distribution implementation is published, two real canaries MUST complete the full profile:

1. a medium internal feature with no new public Product Contract after PREFLIGHT;
2. a new public-interface feature that must demonstrate load-bearing gap detection, valid Product Authority closure, implementation, hardening, and final QA.

For each stage, the pilot record MUST state what unique defect, ambiguity, regression, or merge decision the stage changed; elapsed time; handback count; candidate changes; false-pass detections; tool failures; and unresolved limitations. No role may be removed, merged, or skipped in V1 solely because it produced no code in one canary.

### CTR-SIX-022 — Completion stops the lane and forbids infrastructure drift

The task record MUST define `DONE_WHEN`, `EXPANSION_TRIGGER`, and `NEXT_REAL_ACTION`. When `DONE_WHEN` is met and no `EXPANSION_TRIGGER` fired, all six roles and orchestration MUST stop. Idle Agents, optional dashboard features, additional mutation experiments, broader platform work, or an available provider are not expansion triggers. Runtime implementation, provider integration, dashboards, and consumer rollout require separate tasks within accepted authority.

## 10. Acceptance

### ACC-SIX-001 — Authority and profile-selection gate rejects unauthorized delivery

- Contracts: `CTR-SIX-001`, `CTR-SIX-002`, `CTR-SIX-018`, `CTR-SIX-022`
- Method: run positive and negative route fixtures for profile selection, unresolved Product Authority, invalid mandate, stage skip, load-bearing public-interface gap, and completed `DONE_WHEN`.
- Environment: clean candidate checkout with the exact route validator and profile schema
- Inputs/configuration: one valid selected profile; one task lacking valid mutation authorization; one task with unresolved `AMEND_OR_NEW_PENDING_OWNERSHIP`; one task skipping architect; one public export mislabeled implementation detail; one completed task attempting platform expansion.
- Required evidence: fixture inputs, exact validator revision, stdout/stderr, exit codes, and result matrix bound to candidate commit
- Expected result: only the fully authorized six-stage route passes; unresolved authority, invalid mandate, skipped stage, demoted public interface, and post-completion expansion fail.
- Failure condition: any operational artifact creates authority, any invalid route passes, or a valid selected six-stage route is rejected.

### ACC-SIX-002 — Topology and role-ownership checks reject collapsed or reordered roles

- Contracts: `CTR-SIX-003`, `CTR-SIX-004`, `CTR-SIX-005`, `CTR-SIX-006`, `CTR-SIX-007`, `CTR-SIX-008`, `CTR-SIX-009`, `CTR-SIX-010`
- Method: validate role definitions and inject missing, duplicated, reordered, merged, and overreaching-role configurations.
- Environment: clean candidate checkout
- Inputs/configuration: canonical six roles; coder claiming architecture ownership; cleaner introducing behavior; architect running final QA; hardender changing examples to kill mutants; QA claiming Owner acceptance; merged cleaner/architect role.
- Required evidence: parsed role definitions, validation output, exact configuration bytes, and rejection results
- Expected result: canonical ownership passes and every ownership/topology mutation fails.
- Failure condition: a selected profile can run without six distinct role identities or a role can claim another role's exclusive decision.

### ACC-SIX-003 — Specifier and coder pipeline rejects authority invention and test-free implementation

- Contracts: `CTR-SIX-004`, `CTR-SIX-005`, `CTR-SIX-018`
- Method: execute one accepted-behavior slice and one missing-authority public behavior slice through specifier and coder fixtures.
- Environment: pilot repository clean worktrees
- Inputs/configuration: accepted behavior with plausible wrong implementation; public behavior not covered by authority; Gherkin/acceptance procedure; focused unit tests.
- Required evidence: exact behavior spec, generated acceptance artifacts, failing-before/passing-after unit tests, SPEC_GAP output, and commits
- Expected result: accepted behavior proceeds with tests; missing Product Authority stops before implementation and returns to PREFLIGHT.
- Failure condition: specifier invents the missing Contract, coder implements before the gap closes, or code passes without a focused failing test for the changed behavior.

### ACC-SIX-004 — Cleaner, architect, and hardender provide distinct quality Evidence

- Contracts: `CTR-SIX-006`, `CTR-SIX-007`, `CTR-SIX-008`, `CTR-SIX-021`
- Method: seed a candidate with one local duplication/complexity defect, one dependency-direction or adapter/domain duplication defect, and one test-surviving behavior mutation.
- Environment: medium internal-feature canary
- Inputs/configuration: exact seeded candidate and repository-approved pinned tools
- Required evidence: stage-by-stage commits, tests before/after, architecture check, mutation survivor/kill record, CRAP/DRY outputs, and stage decision-impact record
- Expected result: cleaner fixes the local structural defect without behavior change; architect fixes the boundary defect; hardender adds or improves tests that kill the surviving mutation.
- Failure condition: the wrong stage silently owns the correction, accepted behavior changes without PREFLIGHT, the mutation remains undetected without a limitation, or all three stages produce indistinguishable open-ended review.

### ACC-SIX-005 — QA certification is invalidated by QA-owned mutation

- Contracts: `CTR-SIX-009`, `CTR-SIX-019`, `CTR-SIX-020`
- Method: run final QA on a candidate containing a user-facing defect; let QA prepare a fix; verify that certification fails and the task returns to the earliest affected role; then replay affected stages and run QA without further mutation.
- Environment: public-interface canary
- Inputs/configuration: exact pre-fix and post-fix Heads, user-facing QA procedure, affected-stage map
- Required evidence: failing QA result, QA fix commit, invalidation record, correction handoff, replayed receipts, and final unchanged-candidate QA receipt
- Expected result: the QA-authored change cannot certify itself; only the later unchanged exact Head may receive final QA PASS.
- Failure condition: QA modifies bytes and immediately certifies them, or unaffected Evidence is discarded without impact analysis.

### ACC-SIX-006 — Worktree and durable queue survive lost notifications and restart

- Contracts: `CTR-SIX-003`, `CTR-SIX-011`, `CTR-SIX-012`, `CTR-SIX-014`, `CTR-SIX-015`
- Method: launch six isolated role worktrees; queue multiple task/batch handoffs; suppress wake-up notifications; restart at least two role processes and the handoff service; inject an interrupted multi-recipient delivery.
- Environment: isolated integration test repository
- Inputs/configuration: canonical profile, equal-priority batch items, terminal broadcast, duplicate-delivery interruption
- Required evidence: worktree map, queue trees and headers before/after, exact commit ancestry, duplicate-suppression result, restart logs, and terminal convergence
- Expected result: no role writes main; durable inbox state recovers; each recipient gets one copy; batch order is deterministic; terminal copies are merge-only.
- Failure condition: notification loss drops work, restart duplicates delivery, queue state becomes ambiguous, or a role writes outside its assigned surface.

### ACC-SIX-007 — Two-call self-audit is exact-candidate bound

- Contracts: `CTR-SIX-011`, `CTR-SIX-013`
- Method: submit a valid handoff once, resubmit unchanged, then repeat with candidate, task, authority, artifact, and Evidence changes between calls.
- Environment: handoff helper integration tests
- Inputs/configuration: canonical handoff plus five changed-field variants
- Required evidence: audit-pending records, task audit counts, delivery results, rejection diagnostics, and exact candidate coordinates
- Expected result: first call returns `AUDIT_REQUIRED`; unchanged second call delivers once; every changed tuple invalidates the old challenge and requires a new audit.
- Failure condition: first call delivers, changed candidate reuses a prior challenge, audit count increments repeatedly for an unchanged retry, or self-audit is labeled independent review.

### ACC-SIX-008 — Exact pinning and permission safety reject moving or bypassed inputs

- Contracts: `CTR-SIX-016`, `CTR-SIX-017`
- Method: verify the manifest and startup with exact pinned bytes, then inject a moving branch reference, changed helper bytes, a latest-tool request, `--yolo`, `bypassPermissions`, and an incomplete exceptional mandate.
- Environment: clean candidate checkout and sandboxed launcher tests
- Inputs/configuration: canonical manifest; tampered and unsafe configurations
- Required evidence: hashes, source revisions, launcher/validator output, mandate fixture, and exit codes
- Expected result: exact pinned configuration passes; every mutable, tampered, bypassed, or incompletely authorized configuration fails closed.
- Failure condition: startup downloads unreviewed moving bytes, permission bypass is enabled by profile default, or an incomplete mandate authorizes it.

### ACC-SIX-009 — Two real canaries complete the full six-stage chain

- Contracts: `CTR-SIX-002`, `CTR-SIX-004`, `CTR-SIX-005`, `CTR-SIX-006`, `CTR-SIX-007`, `CTR-SIX-008`, `CTR-SIX-009`, `CTR-SIX-014`, `CTR-SIX-019`, `CTR-SIX-020`, `CTR-SIX-021`
- Method: run the medium internal-feature and new public-interface canaries through all six roles and the required final exact-Head review.
- Environment: two repository-local pilot workspaces using pinned profile implementation
- Inputs/configuration: accepted internal behavior; public-interface proposal with an initial load-bearing gap; exact Owner decisions and mandates
- Required evidence: complete task and handoff history, six role receipts per canary, candidate ancestry, review record, stage decision-impact matrix, timings, handbacks, defects, mutation results, QA results, and Owner disposition
- Expected result: both tasks traverse all six roles; the public-interface canary stops for authority closure before code; both finish with exact-Head review and no automatic merge.
- Failure condition: a role is skipped, the public gap is implemented before acceptance, role Evidence is not candidate-bound, or terminal QA bypasses independent review/Owner merge.

### ACC-SIX-010 — Stop rule prevents post-completion platform expansion

- Contracts: `CTR-SIX-020`, `CTR-SIX-021`, `CTR-SIX-022`
- Method: after both canaries meet `DONE_WHEN`, inject suggestions to add a dashboard, new daemon features, more providers, broader mutation experiments, consumer rollout, and role compression.
- Environment: pilot review
- Inputs/configuration: completed canary records with no fired expansion trigger
- Required evidence: Goal/Gap, DONE_WHEN evaluation, EXPANSION_TRIGGER evaluation, NEXT_REAL_ACTION, and rejected expansion outputs
- Expected result: current lanes return `STOP`; implementation, rollout, or alternative topology becomes a separate PREFLIGHT task.
- Failure condition: idle Agents or optional infrastructure keep the completed task open, or the pilot silently merges/removes roles without new authority.

### Contract coverage

| Contract | Acceptance | Evidence class | Covered |
|---|---|---|---|
| `CTR-SIX-001` | `ACC-SIX-001` | route fixtures | YES |
| `CTR-SIX-002` | `ACC-SIX-001`, `ACC-SIX-002`, `ACC-SIX-009` | route/config/pilot | YES |
| `CTR-SIX-003` | `ACC-SIX-002`, `ACC-SIX-006` | config/integration | YES |
| `CTR-SIX-004` | `ACC-SIX-002`, `ACC-SIX-003`, `ACC-SIX-009` | role/pilot | YES |
| `CTR-SIX-005` | `ACC-SIX-002`, `ACC-SIX-003`, `ACC-SIX-009` | role/tests/pilot | YES |
| `CTR-SIX-006` | `ACC-SIX-002`, `ACC-SIX-004`, `ACC-SIX-009` | role/quality/pilot | YES |
| `CTR-SIX-007` | `ACC-SIX-002`, `ACC-SIX-004`, `ACC-SIX-009` | role/architecture/pilot | YES |
| `CTR-SIX-008` | `ACC-SIX-002`, `ACC-SIX-004`, `ACC-SIX-009` | role/mutation/pilot | YES |
| `CTR-SIX-009` | `ACC-SIX-002`, `ACC-SIX-005`, `ACC-SIX-009` | role/QA/pilot | YES |
| `CTR-SIX-010` | `ACC-SIX-002` | role schema | YES |
| `CTR-SIX-011` | `ACC-SIX-006`, `ACC-SIX-007` | integration | YES |
| `CTR-SIX-012` | `ACC-SIX-006` | restart/queue | YES |
| `CTR-SIX-013` | `ACC-SIX-007` | handoff negative controls | YES |
| `CTR-SIX-014` | `ACC-SIX-006`, `ACC-SIX-009` | integration/pilot | YES |
| `CTR-SIX-015` | `ACC-SIX-006` | batch/terminal integration | YES |
| `CTR-SIX-016` | `ACC-SIX-008` | manifest/startup | YES |
| `CTR-SIX-017` | `ACC-SIX-008` | permission negative controls | YES |
| `CTR-SIX-018` | `ACC-SIX-001`, `ACC-SIX-003` | route/spec-gap | YES |
| `CTR-SIX-019` | `ACC-SIX-005`, `ACC-SIX-009` | correction/pilot | YES |
| `CTR-SIX-020` | `ACC-SIX-005`, `ACC-SIX-009`, `ACC-SIX-010` | QA/review/stop | YES |
| `CTR-SIX-021` | `ACC-SIX-004`, `ACC-SIX-009`, `ACC-SIX-010` | pilot evidence | YES |
| `CTR-SIX-022` | `ACC-SIX-001`, `ACC-SIX-010` | route/stop | YES |

## 11. Alternatives and disposition

### ALT-SIX-001 — One universal Agent performs every concern

- Disposition: rejected
- Reason: specification, implementation, structural cleanup, architecture, test hardening, and final verification can mutually rationalize the same mistake.
- Evidence/Claims considered: `CLM-SIX-002`
- What would reopen: controlled pilot evidence showing equal or better defect rejection and independence with fewer roles.

### ALT-SIX-002 — Start immediately with a compressed three-role profile

- Disposition: rejected for V1 pilot
- Reason: compression before observing the original six would discard the prior-art design without local evidence.
- Evidence/Claims considered: `CLM-SIX-005`
- What would reopen: completed six-stage canaries showing specific adjacent roles have no distinct decision impact.

### ALT-SIX-003 — Copy SwarmForge branch composition and latest-tool behavior unchanged

- Disposition: rejected
- Reason: mutable source and latest tools conflict with exact-revision Evidence and consumer-local adoption.
- Evidence/Claims considered: `CLM-SIX-004`
- What would reopen: none while accepted exact-revision Contracts remain active.

### ALT-SIX-004 — Preserve specifier on master and permission-bypass flags

- Disposition: rejected
- Reason: all mutations require isolated write surfaces and valid attributable authorization.
- Evidence/Claims considered: `EVD-SIX-004`
- What would reopen: a separate accepted authority that changes those safety Contracts.

### ALT-SIX-005 — Use chat summaries instead of durable handoffs

- Disposition: rejected
- Reason: chat cannot reliably bind exact candidate bytes, survive notification loss, or provide queue/restart state.
- Evidence/Claims considered: `CLM-SIX-003`
- What would reopen: a different durable exact-candidate transport with equivalent guarantees.

### ALT-SIX-006 — Let QA fix and immediately approve the modified candidate

- Disposition: rejected
- Reason: the final verifier would become author of the bytes it certifies and the old Evidence tuple would no longer match.
- Evidence/Claims considered: `EVD-SIX-004`
- What would reopen: none for Durable or Controlled work under current independent-review rules.

### ALT-SIX-007 — Force six roles for every repository mutation

- Disposition: rejected
- Reason: the profile governs selected non-trivial software delivery, not governance authoring, release metadata, spelling-only changes, adoption records, or emergency containment by default.
- Evidence/Claims considered: accepted three-axis Governance and prior simulation warnings
- What would reopen: a separate delivery-profile authority for another task class.

## 12. Migration, compatibility, and rollback

```text
MIGRATION =
  docs-only proposal now;
  after acceptance, implement runtime/profile distribution in a separate exact-Head PR;
  run two full six-stage canaries before stable release or consumer rollout

COMPATIBILITY =
  AGENT_DEVELOPMENT_GOVERNANCE_V1 remains the routing authority;
  AGENT_OPERATIONAL_LAYER_V1 remains accepted and unchanged;
  existing consumers and tasks do not adopt this profile automatically;
  no historical task, review, or Record is rewritten

ROLLBACK =
  before consumer adoption, stop using the implementation candidate and keep existing governance/runtime unchanged;
  after pilot adoption, disable the profile through a separately authorized operational rollback while preserving handoff and Evidence records;
  Contract changes require a new authority action rather than silent prompt edits

EMERGENCY_CONTAINMENT =
  profile runtime may be stopped or isolated under the accepted containment rule;
  containment does not authorize product behavior, role compression, or permanent workflow semantics
```

## 13. Open questions

The following are implementation choices constrained by the Contracts, not normative gaps:

```text
- queue storage technology and daemon language
- dashboard technology
- provider adapters and model selection
- exact schema serialization for handoffs and receipts
- supported pinned mutation/CRAP/DRY tools per language
- exact pilot repositories and feature slices, selected by a later valid mandate
```

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
READY_TO_MARK_ACCEPTED = NO
IMPLEMENTATION_IN_THIS_PR = NO
CONSUMER_ADOPTION_IN_THIS_PR = NO
RUNTIME_OR_PRODUCTION_WRITE = NO
```