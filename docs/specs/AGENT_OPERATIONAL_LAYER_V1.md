---
spec_id: AGENT_OPERATIONAL_LAYER_V1
status: accepted
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
  - reusable-agent-workflows
  - repository-local-development-records
governed_by:
  - AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# AGENT_OPERATIONAL_LAYER_V1

## 1. Goal

Add a bounded operational layer around the accepted development grammar so Agents can reliably select and execute recurring repository tasks and preserve durable, non-normative engineering knowledge without confusing either surface with governing authority or mutation permission.

```text
GOAL = discoverable task Skills plus a typed repository-local Record corpus
SUCCESS_OUTCOME = recurring work is executable and durable rationale is preserved while authority, write permission, implementation state, review, and conformance remain separate and auditable
```

## 2. Scope and non-goals

### In scope

- a normative package contract for repository-scoped Agent Skills;
- thin task-oriented Skill entrypoints that delegate shared semantics to one owning router;
- optional Skill-local `references/`, deterministic `scripts/`, tests, and provider interface metadata;
- explicit trigger, anti-trigger, input, authority, mutation, stop, output, failure, and completion boundaries;
- an external authority chain for every local or remote mutation performed through a Skill;
- target-coordinate rechecks, bounded credentials, confirmation, idempotency, retry, unknown-outcome, and compensation rules for side effects;
- a typed, non-normative Record corpus for investigations, implementation rationale, reviews, and conformance;
- stable Record identity, exact coordinates, type-specific mutability, lifecycle metadata, supersession links, and archive policy;
- immutable Review and Conformance attestations with correction-by-supersession;
- type-specific archive eligibility that keeps a current Review or Conformance attestation available for later correction;
- immutable retention of the immediate-successor edge established before a superseded Record is sealed;
- deterministic validation of machine-declared Skill and Record structure without claiming semantic review;
- an explicit semantic-review layer for prose-level authority and meaning;
- a central-distribution versus repository-local ownership boundary;
- set-valued durable-record impact accounting for non-trivial changes;
- forward-only applicability and migration rules for legacy repository records;
- break-glass archive tombstoning/redaction and downgrade compatibility.

### Out of scope

- changing the accepted semantic primitives or authority precedence;
- changing the lifecycle or meaning of governing Specs;
- making Skills, provider metadata, scripts, tests, Notes, Records, or impact declarations normative authority;
- letting a Skill create its own mutation permission;
- treating `implemented`, `reviewed`, `accepted`, `verified`, `conforming`, or `archived` as interchangeable states;
- allowing a mutable branch name to support a durable implementation claim;
- allowing a current Review or Conformance attestation to be sealed before it has a successor;
- creating a new supersession edge to an already archived Record;
- deleting or rewriting a pre-seal supersession edge when its predecessor is archived;
- requiring one new Record file for every non-trivial change when an existing durable owner already covers the knowledge;
- copying DeepSeek Harness Agent Notes or Skills wholesale;
- provider-specific runtime implementation;
- implementing the protocols, templates, schemas, validators, archive ledger, or consumer migrations in this docs-only Spec PR;
- retroactively converting untouched historical records at adoption time;
- claiming that deterministic tooling can detect arbitrary prose-level semantic violations.

## 3. Authority and dependencies

This Spec refines the accepted bootstrap authority without changing any existing Decision or Contract.

```text
PRIMARY_PARENT_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
PARENT_REVISION_AT_AUTHORING = d32b946cbbbc1baa99165d7656fc22e8823a651f
IMPLEMENTATION_AUTHORITY = contracts
EXTERNAL_AUTHORITIES = NONE
EXTERNAL_PRIOR_ART = deepseek-ai/deepseek-harness@b150a551b8d465e31e418e1b2eaf5e79bbb7d28e
AUTHORITY_CONFLICT = NONE
AMENDMENT_REVIEW_ID = 5020251145
AMENDMENT_REVIEWED_HEAD = 02be9c8521154d7808f3f3d4ba06728394f43659
FOLLOWUP_REVIEW_ID = 5036091214
FOLLOWUP_REVIEWED_HEAD = 28402fde238cd1c4bc1f8f0c7ab9def29e572ee6
LINEAGE_REVIEW_ID = 5057378137
LINEAGE_REVIEWED_HEAD = aad4897da82f751c1d02e2ccf2fb05a7ea0f736d
```

DeepSeek Harness is studied only as non-normative prior art. Its repository does not own, constrain, or supersede this repository's governance.

A Skill operational contract is subordinate to accepted authority and to an explicit, persistently recorded owner action where that action is required. A Skill may describe and further narrow an available write scope; it cannot create, broaden, or substitute for that scope.

## 4. Current State

### STATE-OPL-001 — The distribution has one semantic Skill router but no general Skill-package contract

- Subject: reusable Skill surface in `mayf3/agent-development-governance`
- As of commit: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository `main`
- Observed at: 2026-08-25
- Projection: the distribution contains `spec-governance/SKILL.md` and four mode files, with shared invariants and read-order guidance, but does not define a reusable contract for task-oriented entrypoints, Skill-local scripts/references, provider metadata, validation, write authorization, or completion semantics.
- Basis: `OBS-OPL-001`, `OBS-OPL-002`, `CLM-OPL-001`

### STATE-OPL-002 — Durable Record templates exist without a common repository corpus contract

- Subject: persistent non-Spec development records
- As of commit: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository `main`
- Observed at: 2026-08-25
- Projection: Investigation, Review, and Conformance templates exist, but there is no common Record identity schema, canonical repository-local corpus, implementation-rationale record type, type-specific mutability, archive lifecycle, legacy applicability rule, supersession closure, or deterministic cross-record validator.
- Basis: `OBS-OPL-003`, `CLM-OPL-002`

### STATE-OPL-003 — DeepSeek Harness demonstrates useful operational and memory mechanisms with incompatible authority semantics

- Subject: non-normative prior art under `deepseek-ai/deepseek-harness/.agents`
- As of commit: `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Environment: public repository source
- Observed at: 2026-08-25
- Projection: task-oriented Skill packages and mechanically maintained Agent Notes provide useful discoverability, workflows, rationale, alternatives, archival, and validation; however, lifecycle moves such as `proposed` to `implemented` and in-place updates of shipped facts cannot be copied onto accepted governing authority or immutable attestations.
- Basis: `OBS-OPL-004`, `OBS-OPL-005`, `OBS-OPL-006`, `CLM-OPL-003`

### STATE-OPL-004 — Independent review found five closure gaps in the first proposed Head

- Subject: Draft PR #3 proposed Spec at `02be9c8521154d7808f3f3d4ba06728394f43659`
- As of artifact: GitHub review `5020251145`
- Environment: independent semantic review
- Observed at: 2026-08-25
- Projection: the direction and primitive boundaries passed, while mutation authority, Record immutability, archive/rollback closure, legacy applicability, and deterministic-versus-semantic Acceptance required revision.
- Basis: `OBS-OPL-007`, `CLM-OPL-005`, `EVD-OPL-005`

### STATE-OPL-005 — Follow-up review isolated one attestation-archive contradiction

- Subject: Draft PR #3 amended Spec at `28402fde238cd1c4bc1f8f0c7ab9def29e572ee6`
- As of artifact: GitHub review `5036091214`
- Environment: independent semantic review
- Observed at: 2026-08-27
- Projection: the five earlier blocker areas passed, but allowing an active Review or Conformance Record to move directly to `archived` conflicted with the requirement that every later attestation correction supersede the erroneous Record.
- Basis: `OBS-OPL-008`, `CLM-OPL-005`, `EVD-OPL-006`

### STATE-OPL-006 — Lineage re-review found one temporal contradiction in the archive rule

- Subject: Draft PR #3 amended Spec at `aad4897da82f751c1d02e2ccf2fb05a7ea0f736d`
- As of artifact: GitHub review `5057378137`
- Environment: independent semantic review
- Observed at: 2026-08-29
- Projection: type-specific archive eligibility and current-head correction passed, but an absolute prohibition on an archived Record being a `supersedes` target also prohibited the pre-existing immediate-successor edge that must survive sealing.
- Basis: `OBS-OPL-009`, `CLM-OPL-005`, `EVD-OPL-007`

## 5. Observations

### OBS-OPL-001 — Current Skill routing centralizes governance semantics

- Subject: `spec-governance` Skill
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository source
- Observed at: 2026-08-25
- Method: inspect `.agents/skills/spec-governance/SKILL.md` and its `modes/`
- Result: one Skill owns shared invariants and routes exactly one primary mode among `PREFLIGHT`, `AUTHOR`, `REVIEW`, and `COMPLIANCE`.
- Provenance: `.agents/skills/spec-governance/SKILL.md`

### OBS-OPL-002 — Current Skill distribution has no reusable package schema

- Subject: distributed `.agents/skills/` tree
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository source
- Observed at: 2026-08-25
- Method: inspect repository tree and `distribution/manifest.json`
- Result: the distribution includes one Skill tree, but no protocol or validator defines optional `references/`, `scripts/`, tests, provider interface metadata, anti-triggers, mutation-authority references, allowed mutations, stop conditions, or done criteria for Skills generally.
- Provenance: `.agents/skills/`, `distribution/manifest.json`

### OBS-OPL-003 — Existing Record templates are typed but not governed as one corpus

- Subject: durable non-Spec templates
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository source
- Observed at: 2026-08-25
- Method: inspect `.agents/templates/INVESTIGATION_RECORD_TEMPLATE.md`, `REVIEW_RECORD_TEMPLATE.md`, and `CONFORMANCE_RECORD_TEMPLATE.md`
- Result: each template defines useful type-specific fields, but there is no common Record ID contract, shared path or metadata schema, implementation-rationale template, mutability matrix, supersession closure, archive policy, legacy adoption boundary, or corpus validator.
- Provenance: `.agents/templates/`

### OBS-OPL-004 — DeepSeek Harness uses task-oriented Skill packages

- Subject: `.agents/skills/`
- Repository/source: `deepseek-ai/deepseek-harness`
- Commit/artifact: `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Environment: public repository source
- Observed at: 2026-08-25
- Method: inspect the recursive Skill tree and representative `SKILL.md` files
- Result: the repository exposes narrow task Skills such as code review, pre-push checks, simplification discovery, note archival, documentation, and translation; some packages also carry `references/`, deterministic scripts, and `agents/openai.yaml`.
- Provenance: `.agents/skills/`

### OBS-OPL-005 — DeepSeek Harness Agent Notes preserve rationale and alternatives through explicit lifecycle rules

- Subject: `.agents/notes/`
- Repository/source: `deepseek-ai/deepseek-harness`
- Commit/artifact: `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Environment: public repository source
- Observed at: 2026-08-25
- Method: inspect `.agents/notes/README.md`, lifecycle `AGENTS.md` files, and representative notes
- Result: notes encode lifecycle and class, require `Problem`, lifecycle-specific decision/proposal sections, alternatives, and consequences or risks, and preserve rejected rationale only while it prevents a plausible mistake.
- Provenance: `.agents/notes/README.md`, `.agents/notes/implemented/AGENTS.md`

### OBS-OPL-006 — DeepSeek Harness mechanically validates and freezes archived notes

- Subject: Agent Note structural and archive tooling
- Repository/source: `deepseek-ai/deepseek-harness`
- Commit/artifact: `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Environment: public repository source
- Observed at: 2026-08-25
- Method: inspect `scripts/agent-note-tree.ts`, archive tooling, and `dsh-archive-agent-notes`
- Result: closed lifecycle/class sets, filename rules, complete artifacts, archive metadata, content hashes, and append-only seals are mechanically checked; archive selection itself remains semantic and based on future decision value rather than age or word count.
- Provenance: `scripts/agent-note-tree.ts`, `scripts/archived-agent-notes.ts`, `.agents/skills/dsh-archive-agent-notes/SKILL.md`

### OBS-OPL-007 — Review 5020251145 identified five precise semantic blockers

- Subject: `AGENT_OPERATIONAL_LAYER_V1` first proposed Head
- Repository/source: `mayf3/agent-development-governance` Draft PR #3
- Commit/artifact: `02be9c8521154d7808f3f3d4ba06728394f43659`, review `5020251145`
- Environment: independent REVIEW mode
- Observed at: 2026-08-25
- Method: review authority, primitive boundaries, Contracts, Acceptance coverage, and immutability against the accepted bootstrap authority
- Result: `SPEC_REVIEW = REVISE` with blockers for Skill self-authorization, attestation mutability, archive/rollback closure, legacy applicability, and overclaimed deterministic Acceptance.
- Provenance: PR #3 review `5020251145`

### OBS-OPL-008 — Review 5036091214 found one contradiction in archived attestation correction

- Subject: `AGENT_OPERATIONAL_LAYER_V1` amended Head
- Repository/source: `mayf3/agent-development-governance` Draft PR #3
- Commit/artifact: `28402fde238cd1c4bc1f8f0c7ab9def29e572ee6`, review `5036091214`
- Environment: independent REVIEW mode
- Observed at: 2026-08-27
- Method: re-review the five prior blocker areas and test lifecycle, correction, and archive Contracts against one another
- Result: the prior blocker areas passed, but `active -> archived` for Review and Conformance could seal the only legal correction target even though attestation correction was required to use `supersedes`.
- Provenance: PR #3 review `5036091214`

### OBS-OPL-009 — Review 5057378137 found one contradiction in retained sealed lineage edges

- Subject: `AGENT_OPERATIONAL_LAYER_V1` type-specific archive amendment
- Repository/source: `mayf3/agent-development-governance` Draft PR #3
- Commit/artifact: `aad4897da82f751c1d02e2ccf2fb05a7ea0f736d`, review `5057378137`
- Environment: independent REVIEW mode
- Observed at: 2026-08-29
- Method: construct the required `A active -> B supersedes A -> A superseded -> A archived` final state and evaluate every lifecycle, backlink, lineage, and archive Contract against it
- Result: the positive archived-attestation state required `B.supersedes = A` to remain, while an unqualified sentence simultaneously prohibited archived `A` from being named as any `supersedes` target.
- Provenance: PR #3 review `5057378137`

## 6. Claims and assumptions

### CLM-OPL-001 — Thin task entrypoints improve discovery without requiring duplicated governance semantics

- Support state: SUPPORTED
- Supported by evidence: `EVD-OPL-001`
- Contradicted by evidence: none known
- Uncertainty: provider discovery quality differs, so aliases may be unnecessary in some runtimes.

### CLM-OPL-002 — A typed corpus is safer than one generic Agent Note type in this governance model

- Support state: SUPPORTED
- Supported by evidence: `EVD-OPL-002`
- Contradicted by evidence: none known
- Uncertainty: pilot repositories may justify additional Record types, but new types require explicit governance.

### CLM-OPL-003 — DeepSeek Harness mechanisms are reusable only after separating operational memory from normative authority

- Support state: SUPPORTED
- Supported by evidence: `EVD-OPL-003`
- Contradicted by evidence: none known
- Uncertainty: archive implementation details may change after consumer pilots.

### CLM-OPL-004 — Stable Record paths with lifecycle metadata fit this governance better than lifecycle-encoded path moves

- Support state: INFERRED
- Supported by evidence: `EVD-OPL-004`
- Contradicted by evidence: none known
- Uncertainty: a later machine-readable catalog may provide equally stable redirects for path moves.

### CLM-OPL-005 — Operational safety requires explicit authority, immutability, lifecycle, compatibility, review-layer, and attestation-lineage closure

- Support state: SUPPORTED
- Supported by evidence: `EVD-OPL-005`, `EVD-OPL-006`, `EVD-OPL-007`
- Contradicted by evidence: none known
- Uncertainty: exact schema field names and ledger encodings remain implementation choices constrained by the Contracts below.

## 7. Evidence relations

### EVD-OPL-001 — Current routing and DSH task Skills support thin task entrypoints

- Source observations: `OBS-OPL-001`, `OBS-OPL-002`, `OBS-OPL-004`
- Target: `CLM-OPL-001`
- Relation: SUPPORTS
- Bound coordinates: governance `d32b946c`; DeepSeek Harness `b150a551`
- Strength/sufficiency: sufficient for a bounded package contract
- Limitations: does not establish the best provider-specific discovery metadata
- Provenance: repositories and paths named by the source observations

### EVD-OPL-002 — Existing typed templates and Agent Note overlap support a typed Record corpus

- Source observations: `OBS-OPL-003`, `OBS-OPL-005`
- Target: `CLM-OPL-002`
- Relation: SUPPORTS
- Bound coordinates: governance `d32b946c`; DeepSeek Harness `b150a551`
- Strength/sufficiency: strong for keeping Investigation, Review, Conformance, and Implementation Rationale distinct
- Limitations: does not preclude future additional types
- Provenance: repositories and paths named by the source observations

### EVD-OPL-003 — Authority immutability and DSH note mutation semantics support an explicit non-authority boundary

- Source observations: `OBS-OPL-005`, `OBS-OPL-006`
- Target: `CLM-OPL-003`
- Relation: SUPPORTS
- Bound coordinates: DeepSeek Harness `b150a551`; parent authority `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0`
- Strength/sufficiency: decisive for forbidding copied Note lifecycle from mutating accepted Spec meaning or attestations
- Limitations: permitted append-only updates to non-attestation Records still require type-specific rules
- Provenance: parent Spec and DSH prior-art paths

### EVD-OPL-004 — Stable identity requirements support stable paths plus lifecycle metadata

- Source observations: `OBS-OPL-003`, `OBS-OPL-005`, `OBS-OPL-006`
- Target: `CLM-OPL-004`
- Relation: SUPPORTS
- Bound coordinates: governance `d32b946c`; DeepSeek Harness `b150a551`
- Strength/sufficiency: inferential but sufficient for V1
- Limitations: path redirects and generated catalogs could support a different future design
- Provenance: repositories and paths named by the source observations

### EVD-OPL-005 — Independent review supports the five closure requirements

- Source observations: `OBS-OPL-007`
- Target: `CLM-OPL-005`
- Relation: SUPPORTS
- Bound coordinates: Draft PR #3, reviewed Head `02be9c8521154d7808f3f3d4ba06728394f43659`, review `5020251145`
- Strength/sufficiency: decisive for first amendment scope
- Limitations: the first amended Head required a new independent review
- Provenance: PR #3 review `5020251145`

### EVD-OPL-006 — Follow-up review supports type-specific attestation archive eligibility

- Source observations: `OBS-OPL-008`
- Target: `CLM-OPL-005`
- Relation: SUPPORTS
- Bound coordinates: Draft PR #3, reviewed Head `28402fde238cd1c4bc1f8f0c7ab9def29e572ee6`, review `5036091214`
- Strength/sufficiency: decisive for keeping a current Review or Conformance attestation unsealed until superseded
- Limitations: the type-specific amendment required another independent review
- Provenance: PR #3 review `5036091214`

### EVD-OPL-007 — Lineage review supports retaining only the pre-seal immediate-successor edge

- Source observations: `OBS-OPL-009`
- Target: `CLM-OPL-005`
- Relation: SUPPORTS
- Bound coordinates: Draft PR #3, reviewed Head `aad4897da82f751c1d02e2ccf2fb05a7ea0f736d`, review `5057378137`
- Strength/sufficiency: decisive for distinguishing an immutable edge established before sealing from a prohibited edge created after archival
- Limitations: this amended Head requires another independent review
- Provenance: PR #3 review `5057378137`

## 8. Decisions

### DEC-OPL-001 — Separate authority, operational workflow, and durable Record layers

- Decision owner: repository owner
- Decision: governing authority remains in Product Direction, Architecture/invariant authority, and accepted Specs; explicit owner actions may authorize bounded execution; Skills execute only within an externally available scope; Records preserve qualified non-normative knowledge.
- Rejected alternatives: treat Skills as policy or write authority; infer Contracts from implementation records; use one undifferentiated `.agents` knowledge tree.
- Reason: the separation preserves the accepted grammar while making recurring work and durable rationale easier to execute and retrieve.
- Owner decision remaining: NONE

### DEC-OPL-002 — Use one semantic owner with optional thin task entrypoints

- Decision owner: repository owner
- Decision: shared semantics remain in the owning router or protocol. A task-facing Skill MAY delegate to one exact router mode, but MUST NOT copy or independently reinterpret shared normative rules.
- Rejected alternatives: one giant always-loaded Skill; four or more independently maintained copies of the same governance semantics.
- Reason: narrow entrypoints improve discovery and context budgets while one owner prevents semantic drift.
- Owner decision remaining: NONE

### DEC-OPL-003 — Define Skills as executable operational contracts

- Decision owner: repository owner
- Decision: every distributed Skill declares its purpose, trigger and anti-trigger, required inputs and coordinates, sources of truth, mutation-authority inputs, allowed and forbidden mutations, stop conditions, procedure, required output, failure output, and done criteria.
- Rejected alternative: prose that merely describes a capability without defining authority, stop, failure, or completion semantics.
- Reason: explicit operational boundaries make Skill execution auditable and reduce invented workflow.
- Owner decision remaining: NONE

### DEC-OPL-004 — Permit layered Skill packages without granting authority to auxiliary files

- Decision owner: repository owner
- Decision: a Skill package may contain `SKILL.md`, modes, references, deterministic scripts, tests, and provider interface metadata. `SKILL.md` owns the operational contract but remains non-authoritative; references explain; scripts mechanize bounded checks; provider metadata aids discovery only.
- Rejected alternative: let a script, reference, or provider file introduce mutation permission or normative meaning.
- Reason: separate layers reduce context and permit tooling without hidden authority.
- Owner decision remaining: NONE

### DEC-OPL-005 — Establish a typed non-normative Record corpus

- Decision owner: repository owner
- Decision: V1 recognizes `investigation`, `implementation_rationale`, `review`, and `conformance` Record types. Every Record explicitly declares `authority_effect: none` and is subject to type-specific mutability.
- Rejected alternative: one generic Agent Note type containing decisions, reviews, implementation status, and evidence.
- Reason: type-specific Records preserve useful knowledge without collapsing the grammar.
- Owner decision remaining: NONE

### DEC-OPL-006 — Keep paths stable and make lifecycle and archive-edge eligibility type-specific

- Decision owner: repository owner
- Decision: V1-managed repository-file Records use stable type/ID paths and lifecycle metadata `active | superseded | archived`. Investigation and Implementation Rationale Records may move directly from `active` to `archived` after closure and future-value review. Review and Conformance Records may be archived only after they are superseded. A superseded Record retains exactly the immediate-successor relation established before sealing; archival forbids new successor relations rather than deleting that historical edge. `archived` is otherwise terminal for every type.
- Rejected alternative: permit ad hoc transitions, seal a current attestation, delete the supersession edge on archive, or add a separate correction relation later.
- Reason: stable paths preserve references, while type-specific archive eligibility and immutable pre-seal edges keep correction lineages reachable without allowing post-archive mutation.
- Owner decision remaining: NONE

### DEC-OPL-007 — Add an Implementation Rationale Record

- Decision owner: repository owner
- Decision: an Implementation Rationale Record explains an internal implementation choice within an accepted Spec's Contracts, binds the governing Spec revision and exact implementation commits for every durable claim, and records alternatives, consequences, and reopening conditions.
- Rejected alternative: put implementation choices into accepted Contract text, bind durable claims only to a branch, or leave rationale only in chat and code review.
- Reason: internal choices can guide future maintenance without becoming normative system obligations.
- Owner decision remaining: NONE

### DEC-OPL-008 — Require set-valued durable-record impact accounting, not record quotas

- Decision owner: repository owner
- Decision: every non-trivial change persists one impact declaration that may simultaneously name created and updated Records, exact change coordinates, actor/time, existing durable owners, and a bounded no-new-record reason.
- Rejected alternative: a single `CREATED | UPDATED | NONE` enum or a requirement to create a new Note for every non-trivial change.
- Reason: set-valued accounting represents real changes and catches missing knowledge without producing duplicates.
- Owner decision remaining: NONE

### DEC-OPL-009 — Archive by future decision value, preserve current attestations and sealed lineage edges, and retain a break-glass audit path

- Decision owner: repository owner
- Decision: archive selection remains semantic and type-specific. Closed Investigation and Implementation Rationale Records may seal when they lose future decision value. A Review or Conformance attestation may seal only after a successor has superseded it and the correction lineage remains reachable. The pre-seal immediate-successor edge is part of the sealed historical state and remains immutable. Ordinary sealed content is otherwise immutable. Unsafe content may be replaced only through an owner-authorized append-only redaction/tombstone ledger that preserves path and hash evidence without retaining dangerous bytes in the active tree.
- Rejected alternative: archive automatically by age/size, seal a current attestation, remove or rewrite established lineage edges at sealing, forbid legally or operationally required removal, or permit ordinary edits under a redaction label.
- Reason: future-useful rationale, current attestations, and established correction history must remain available while secrets, personal data, malware, and legally removable content need a narrow auditable escape hatch.
- Owner decision remaining: NONE

### DEC-OPL-010 — Mutation authority originates outside the Skill

- Decision owner: repository owner
- Decision: a Skill may only consume and narrow mutation permission established by an exact accepted authority and/or an explicit persistent owner action as required for the task. Effective write scope is the intersection of that permission, the task request, the execution identity and credential scope, the target coordinates, and the Skill's own narrower declaration.
- Rejected alternative: permit `SKILL.md`, a script, or provider metadata to authorize its own installation, deployment, remote write, or irreversible action.
- Reason: a non-authoritative operational artifact cannot be the source of the permission that lets it mutate state.
- Owner decision remaining: NONE

### DEC-OPL-011 — Attestations are immutable and corrections extend the current unsealed lineage head

- Decision owner: repository owner
- Decision: Review recommendation/findings/coordinates and Conformance evaluation tuple/result/evidence are immutable after creation except for atomic lifecycle/backlink metadata. Investigation and Implementation Rationale updates are limited to the append-only fields specified below. A Review or Conformance correction creates a new Record that supersedes the current active, unsealed head of the same correction lineage. Only superseded predecessors may later be archived, and their already established immediate-successor edges survive sealing unchanged. No correction created after archival may target an archived predecessor.
- Rejected alternative: rely on Git history, correct an archived predecessor directly, remove a pre-existing lineage edge at archival, or allow the current durable artifact under one `RECORD_ID` to present a different review or conformance claim.
- Reason: durable attestations must remain stable at exact coordinates, and every correction chain must retain one legal target, one visibly current head, and an immutable path through sealed predecessors.
- Owner decision remaining: NONE

### DEC-OPL-012 — Apply V1 forward from an exact local adoption boundary

- Decision owner: repository owner
- Decision: V1 canonical schema and paths apply to Records created after the local adoption commit and to legacy Records explicitly migrated before material update. Untouched legacy records remain valid, non-authoritative historical artifacts with an explicit `legacy_unmanaged` classification and do not claim V1 conformance.
- Rejected alternative: fail every consumer immediately at adoption or silently exempt all later edits to legacy files.
- Reason: forward-only adoption preserves history without making the new contract optional.
- Owner decision remaining: NONE

### DEC-OPL-013 — Separate deterministic validation from semantic review

- Decision owner: repository owner
- Decision: deterministic tooling validates explicit machine-declared structure and relations; independent semantic review evaluates prose-level authority, hidden authorization, copied or reinterpreted meaning, Contract changes, false owner acceptance, and misleading completeness claims.
- Rejected alternative: ask a schema validator to infer arbitrary semantic meaning or make all structure review-only.
- Reason: honest enforcement requires each layer to claim only what it can establish.
- Owner decision remaining: NONE

## 9. Contracts

### CTR-OPL-001 — Skills and Records are not governing or mutation authority

A Skill, script, test, provider metadata file, generated catalog, Record, impact declaration, PR discussion, or archive MUST NOT create, accept, amend, supersede, or reinterpret a governing Decision or Contract. It also MUST NOT create or broaden mutation permission. Every distributed Skill and Record template MUST machine-declare `authority_effect: none` and explain its authority boundary. When operational instructions conflict with accepted authority or an explicit owner action, execution MUST stop and report the conflict.

### CTR-OPL-002 — Every Skill has a bounded invocation contract

Every distributed Skill MUST declare:

```text
purpose
use_when
do_not_use_when
required_inputs
fixed_coordinates
sources_of_truth
authority_effect = none
mutation_authority_inputs
allowed_mutations
forbidden_actions
stop_conditions
procedure
required_output
failure_output
done_criteria
```

Missing information MAY be resolved from repository state when a deterministic read can establish it. No mutation, including an otherwise mechanical local change, MAY begin while a required authority reference, owner-action reference, target coordinate, execution identity, credential scope, or effective write boundary remains unresolved. Read-only investigation MAY continue when it cannot itself create a side effect or expose credentials.

### CTR-OPL-003 — Shared semantics have one owner

A task-oriented entry Skill MAY route to an owning Skill mode or protocol section. It MUST name an exact machine-resolvable delegation target in the same distributed revision and MUST NOT duplicate shared normative semantics. If the owner changes, entrypoints MUST continue to delegate or fail validation rather than silently retaining stale copied rules.

### CTR-OPL-004 — Skill auxiliary layers remain bounded

A Skill package MAY include `modes/`, `references/`, `scripts/`, `tests/`, and `agents/<provider>.yaml`.

- `SKILL.md` MUST own the executable operational contract but MUST remain subordinate to accepted authority and owner actions.
- A reference MUST NOT become required authority merely because it is linked.
- A deterministic script MUST report only the properties it actually checks.
- Provider metadata MUST be optional for governance semantics and MUST NOT weaken trigger, authority, mutation, stop, failure, or output rules.
- Bundled scripts MUST have focused validation and MUST NOT install dependencies or mutate local or remote state merely because the Skill mentions that action.
- Any auxiliary layer that declares `authority_effect` other than `none`, supplies its own owner approval, broadens credential scope, or overrides the owning contract MUST fail deterministic validation.

### CTR-OPL-005 — Record types are explicit and non-interchangeable

The Record corpus MUST distinguish at least:

```text
investigation
implementation_rationale
review
conformance
```

An Investigation Record MUST NOT grant implementation permission. An Implementation Rationale Record MUST NOT create or change a Contract. A Review Record MUST NOT perform owner acceptance. A Conformance Record MUST remain qualified to exact Spec revision, implementation revision, environment, time, and evidence. Every Record MUST declare `authority_effect: none`; a machine field claiming any other authority effect is invalid, while prose-level coercion remains a semantic-review concern.

### CTR-OPL-006 — Every V1-managed Record has stable identity and exact coordinates

A `V1-managed Record` is either created after the repository's exact local adoption commit or explicitly migrated under `CTR-OPL-015`. Every V1-managed repository-file Record MUST have a stable `RECORD_ID`, `RECORD_TYPE`, stable repository path, owner, creator, created time, lifecycle, authority effect, related authority IDs and exact revisions where applicable, stable provenance links, supersession fields, and format version. IDs MUST NOT be reused or renumbered. A Record MUST NOT claim current implementation or runtime state without the coordinates required by the accepted grammar.

V1 file-backed ID forms are:

```text
INV-YYYY-NNN   investigation
IRR-YYYY-NNN   implementation_rationale
REV-YYYY-NNN   review
CONF-YYYY-NNN  conformance
```

The canonical V1 path form is:

```text
.agents/local/records/<record_type>/<RECORD_ID>.md
```

Durable implementation claims MUST bind a 40-hex implementation commit. A branch MAY be recorded only as informational discovery context and MUST NOT substitute for the commit. The lifecycle value is metadata and MUST NOT require a path move. Duplicate IDs across canonical Records, legacy aliases, redirect entries, or migrated sources MUST fail validation.

### CTR-OPL-007 — Record lifecycle is type-specific, closed, and separate from other dimensions

The only legal lifecycle transitions are:

```text
investigation:
  active -> superseded
  active -> archived
  superseded -> archived

implementation_rationale:
  active -> superseded
  active -> archived
  superseded -> archived

review:
  active -> superseded
  superseded -> archived
  active -> archived = FORBIDDEN

conformance:
  active -> superseded
  superseded -> archived
  active -> archived = FORBIDDEN

all record types:
  archived -> <none>
```

For Investigation and Implementation Rationale, `active -> archived` is allowed only after the type-specific work is closed and future-value review finds no active decision value. For Review and Conformance, a current `active` attestation MUST remain unsealed so a later correction can supersede it. A Review or Conformance Record MAY enter `archived` only after it is `superseded`, its forward and backward supersession links were atomically established while both Records were unsealed, and its correction lineage reaches exactly one active, unarchived head without cycles or ambiguity.

`archived` is terminal: an archived Record MUST NOT be edited or returned to active. After a Record enters `archived`, no new `supersedes` relation MAY be created that targets it. For a Record archived from `superseded`, the one immediate-successor relation established atomically before sealing MUST remain intact and immutable. That retained relation is valid only when the archived Record's sealed `superseded_by` backlink names the same immediate successor and that successor's `supersedes` field names the archived Record. Removing, replacing, or adding another immediate-successor edge after sealing is forbidden.

Every later correction MUST target the active, unarchived head of the lineage. It MAY cite an older archived predecessor through `historical_sources` or `related_records`; that citation does not create a new supersession edge or make the archived predecessor current.

Record lifecycle MUST remain separate from:

```text
investigation disposition
implementation progress
verification coverage
review recommendation
acceptance action
conformance result
runtime state
Spec lifecycle
```

`archived` MUST NOT mean rejected, implemented, accepted, verified, conforming, or obsolete authority.

### CTR-OPL-008 — Implementation rationale stays within accepted Contracts

An Implementation Rationale Record MUST bind:

```text
governing_spec_id
governing_spec_revision
covered_contracts
implementation_repository
implementation_base_commit
implementation_commits
informational_branch_or_pr
chosen_implementation
alternatives_considered
consequences
verification_references
reopen_conditions
```

Every durable claim that an implementation exists, behaves a certain way, or received verification MUST identify the exact implementation commit. A branch or PR MAY help locate work but is not evidence of a durable state. The Record MUST stop and request Spec governance when the rationale would alter external behavior, identity, authorization, failure, retry, timeout, transaction, lifecycle, migration, compatibility, observability, or security semantics beyond the accepted Contracts.

### CTR-OPL-009 — Non-trivial changes persist a set-valued durable-record impact declaration

Every non-trivial change under adopted governance MUST persist the following declaration in the pull request body under the exact heading `## Durable Record Impact`:

```yaml
actor: <identity>
recorded_at: <timestamp>
repository: <owner/repository>
base_commit: <40-hex>
head_commit: <40-hex candidate or final head>
persistent_surface: <pull-request URL>
created_records: [<RECORD_ID>...]
updated_records: [<RECORD_ID>...]
existing_durable_owners: [<authority or RECORD_ID>...]
no_new_record_reason: <text or null>
```

`created_records` and `updated_records` MAY both be non-empty. When both are empty, `existing_durable_owners` and/or `no_new_record_reason` MUST explain why no new durable Record is required. A declaration MUST name the canonical persistent location for every created or updated Record. It MUST NOT require duplicate Records when accepted authority or an existing Record already owns the material.

When a permitted emergency action has no pull request, the same structure MUST be persisted in the incident record or in `.agents/local/change-impact/<HEAD_OR_INCIDENT_ID>.yaml`, with a stable link added to the eventual reconciliation PR.

### CTR-OPL-010 — Archive selection is semantic, sealing is mechanical, and unsafe content has a narrow redaction path

A closed Investigation or Implementation Rationale Record MAY become `archived` after a semantic future-value review. An active Review or Conformance Record MUST NOT be archived, regardless of apparent age or future value. A Review or Conformance Record MAY be archived only after it is superseded and its lineage satisfies `CTR-OPL-007`. Records that preserve active rationale, alternatives, negative guarantees, ownership or security boundaries, durable or wire semantics, compatibility obligations, reopening conditions, or a current attestation MUST remain active or superseded as appropriate.

Ordinary archive sealing MUST provide:

```text
record format version
seal manifest version
minimum compatible reader/verifier version
stable path
content hash
sealed_at
sealed_by
future-value review reference
retained immediate successor or NONE
retained successor-edge fingerprint or NONE
```

When a Record is sealed from `superseded`, its manifest entry MUST bind the pre-existing `superseded_by` value and the matching immediate successor's `supersedes` reference. The seal verifier MUST reject deletion, replacement, mismatch, or a second successor edge. When a Record is sealed directly from `active` under a type that permits that transition, both retained-edge fields MUST be `NONE`.

The seal manifest MUST be append-only. Existing ordinary sealed paths, hashes, retained-edge bindings, and meanings MUST NOT be removed, changed, reordered into a different meaning, or silently accepted after mismatch.

A sealed artifact containing a credential, secret, personal data, malicious content, or material subject to a lawful removal requirement MAY be removed from the active tree only through a break-glass action that:

1. has explicit owner authorization and an incident, privacy, security, or legal reference;
2. records an append-only redaction entry containing the original path and hash, actor, approver, timestamp, reason class, replacement tombstone path/hash, and repository-history purge status, without reproducing the unsafe bytes;
3. replaces the current artifact with a deterministic tombstone and performs history/cache purge when the hazard requires it;
4. preserves the original seal entry and overlays the authorized redaction entry so the verifier can distinguish sanctioned removal from tampering;
5. cannot be used to revise rationale, recommendation, evidence, result, or retained lineage edges.

While any sealed or redacted corpus exists, a rollback or downgrade MUST retain a compatible reader and seal/redaction verifier. A consumer MUST NOT adopt or revert to a distribution revision below the recorded minimum compatible reader/verifier version unless an accepted migration exports the corpus to another verifiable format and proves every seal/redaction entry remains readable and checkable.

### CTR-OPL-011 — Deterministic validation and semantic review are separate, mandatory layers

Deterministic tooling MAY validate only explicit machine-declared properties, including:

- package layout, metadata fields, enums, and ID/path patterns;
- exact delegation references and distributed-file existence;
- `authority_effect: none` and forbidden machine-declared authority effects;
- required side-effect authorization/runtime fields and coordinate formats;
- exact commit formats, declared output schemas, and impact-declaration structure;
- type-specific required sections, archive eligibility, and allowed lifecycle transitions;
- duplicate IDs, stable references, redirects, supersession closure, and attestation-lineage head uniqueness;
- whether a supersession edge was established before sealing, whether its two directions match, and whether it remains immutable afterward;
- rejection of a new post-archive edge, a missing retained edge, a changed immediate successor, or a second successor;
- immutable-field fingerprints or equivalent attestation-change detection;
- archive seals, redaction-ledger structure, and reader-version compatibility.

It MUST NOT claim to establish semantic completeness, decision quality, evidence sufficiency, independent review, acceptance, conformance, absence of copied meaning, absence of hidden authorization in prose, or absence of Contract reinterpretation.

Independent semantic review MUST evaluate at least:

- copied, contradicted, or independently reinterpreted governance meaning;
- prose that grants hidden write authority or broadens an owner action;
- rationale that changes a Contract;
- a Review that performs or falsely reports owner acceptance;
- a Conformance Record that overstates evidence or result;
- archive classification that hides a current or still-correctable attestation;
- lineage wording or handling that either permits a new post-archive correction target or destroys a pre-seal correction edge;
- misleading claims that deterministic validation proves semantic correctness.

A release or adoption candidate fails if either a machine-detectable violation passes deterministic validation or a semantic violation is found by the required independent review.

### CTR-OPL-012 — Central distribution and repository-local knowledge remain separate

The central distribution MAY contain the Skill-package protocol, Record-corpus protocol, schemas, templates, validators, reader/verifier compatibility code, and reusable Skills. Consumer-specific Records, impact declarations, redirect maps, seal manifests, and redaction ledgers MUST remain in their owning repository and MUST NOT be copied back into the central distribution manifest as shared governance. A consumer update MUST preserve local Records, local redaction/seal state, and local authority ownership.

### CTR-OPL-013 — Side-effecting Skills require external authorization and safe execution semantics

Before any local or remote mutation, a side-effecting Skill invocation MUST resolve and persist:

```text
accepted_authority_reference
owner_action_reference_or_not_required_reason
execution_actor
execution_identity
credential_scope
target_coordinates
requested_mutation
skill_declared_narrower_scope
confirmation_boundary
pre_mutation_recheck
retry_class
idempotency_mechanism
unknown_outcome_probe
rollback_or_compensation
```

`accepted_authority_reference` MUST identify an exact accepted authority revision and relevant Contract for a durable behavior change. `owner_action_reference` MUST identify a persistent action with actor, timestamp, target, scope, and expiry or one-use boundary when repository policy or the operation requires owner authorization. Neither may be supplied or fabricated solely by the Skill package.

Effective mutation scope is the intersection of all resolved scopes. Immediately before each irreversible or externally visible mutation, the Skill MUST re-read the target coordinates and authorization boundary. Drift, scope expansion, expired authorization, or credential mismatch MUST stop execution.

Remote mutation with an ambiguous outcome MUST NOT be blindly retried. The Skill MUST use the declared idempotency mechanism or first reconcile the target through the unknown-outcome probe, then report whether the operation is confirmed applied, confirmed absent, or unresolved. An unresolved outcome MUST remain a blocker for dependent actions.

### CTR-OPL-014 — Record mutability is type-specific and attestations are correction-by-supersession

The following fields are immutable for every V1-managed Record after creation, except that lifecycle and link metadata may change only through a valid atomic transition:

```text
RECORD_ID
RECORD_TYPE
authority_effect
created_at
created_by
original authority and source coordinates
```

Type-specific rules are:

| Record type | Permitted in-place change while `active` | Requires a new Record |
|---|---|---|
| `investigation` | append timestamped Observations, Claims, Evidence, alternatives, related links, and one transition from `open` to a final disposition; append a correction entry without deleting the original statement | replacement of a final disposition or historical Observation/Claim/alternative; a different investigated question |
| `implementation_rationale` | append exact implementation commits, verification references, newly observed consequences, and reopening information while governing Spec revision, covered Contracts, and chosen implementation remain unchanged | changed governing revision or Contract set, changed chosen implementation, rewritten alternative/rationale, or correction that changes the original decision |
| `review` | no substantive in-place change; only valid lifecycle/backlink metadata | any correction to reviewed base/head, reviewer identity, recommendation, finding, evidence, or conclusion |
| `conformance` | no substantive in-place change; only valid lifecycle/backlink metadata | any correction to Spec revision, implementation commit, environment, evaluated time, Contract result, evidence, aggregate result, or conclusion |

A correction of a Review or Conformance attestation MUST create a new Record whose `supersedes` points to the current active, unarchived head of the same correction lineage and whose reason explains the correction. The old active head receives the atomic backlink, becomes `superseded`, and retains its original attestation. It MAY be archived only afterward under `CTR-OPL-007` and `CTR-OPL-010`; the bidirectional immediate-successor edge established by that correction remains part of the sealed historical state.

If an error is discovered in an already archived predecessor, a newly created correction MUST still supersede the current active head; it MUST NOT create a new `supersedes` edge to the archived predecessor. The archived predecessor MAY be named in `historical_sources` to explain the origin of the correction. Its retained pre-seal `superseded_by` backlink and the matching immediate successor's `supersedes` reference remain sealed and visibly non-current through the reachable supersession chain. A correction is invalid if, at creation time, its target is already archived, if it creates multiple active heads, or if it leaves an archived erroneous attestation without a reachable active successor.

A later Conformance evaluation at different coordinates does not automatically supersede the earlier valid evaluation; it uses `related_records` unless it corrects the same evaluation tuple.

### CTR-OPL-015 — V1 applicability and legacy migration are explicit and forward-only

The consuming repository MUST record the exact commit at which this operational layer becomes locally adopted. Records are classified as:

```text
v1_managed        created after adoption or explicitly migrated
legacy_unmanaged  pre-adoption artifact not yet materially updated
redirect_stub     non-Record path-preservation artifact created by migration
```

An untouched `legacy_unmanaged` artifact remains valid historical, non-authoritative material. It is excluded from V1 required-field/path validation, but discovery and collision checks MUST ensure that its path, any legacy identifier, and any redirect alias do not collide with a V1-managed `RECORD_ID`. It MUST NOT claim V1 conformance or satisfy a post-adoption requirement to create/update a V1-managed Record.

A material update is any semantic change to authority context, coordinates, Observation, Claim, Evidence, alternative, disposition, chosen implementation, covered Contract, review recommendation/finding, conformance result/evidence, lifecycle, or supersession relation. Formatting, spelling, or link repair with independently classified semantic delta `NONE` is not material.

Before a legacy Investigation or Implementation Rationale receives a material update, the repository MUST migrate it atomically. A legacy Review or Conformance attestation is never substantively migrated in place; a new V1-managed Record references the legacy source and preserves it unchanged.

An elected file migration MUST:

1. record the legacy path and source blob hash;
2. assign or preserve one unique V1 `RECORD_ID`;
3. move the canonical content to the V1 path without creating a duplicate Record;
4. preserve historical links through an append-only redirect map and, when needed, a minimal old-path stub containing no `RECORD_ID` and no duplicate body;
5. validate every redirect target, ID/alias collision, and source hash;
6. keep the legacy identifier as an alias when it cannot be the V1 ID.

Broken redirects, duplicate IDs, copied canonical bodies at both paths, missing source hashes, or a material legacy edit without migration MUST fail deterministic validation.

## 10. Acceptance

### ACC-OPL-001 — Deterministic Skill package validation

- Contracts: `CTR-OPL-001`, `CTR-OPL-002`, `CTR-OPL-003`, `CTR-OPL-004`, `CTR-OPL-011`, `CTR-OPL-013`
- Method: validate representative router, thin-entry, script-bearing, reference-bearing, provider-metadata, read-only, local-mutation, and remote-mutation fixtures
- Environment: repository unit test
- Required evidence: executed validator result bound to implementation commit; negative fixtures for missing exact delegation, non-`none` machine authority effect, unresolved mutation fields, provider override, malformed coordinates, and missing unknown-outcome policy
- Expected result: machine-valid packages pass and every explicit structural violation fails for the intended rule
- Failure condition: a machine-detectable Skill violation passes; prose-level semantic safety is evaluated separately by `ACC-OPL-007`

### ACC-OPL-002 — Deterministic Record corpus, mutability, and type-specific lifecycle validation

- Contracts: `CTR-OPL-005`, `CTR-OPL-006`, `CTR-OPL-007`, `CTR-OPL-008`, `CTR-OPL-011`, `CTR-OPL-014`
- Method: validate one complete fixture of each Record type, immutable-field fingerprints or equivalent before/after pairs, exact implementation commits, and legal/illegal lifecycle transitions
- Environment: repository unit test
- Required evidence: executed validator result and fixture inventory bound to implementation commit, including `active Investigation -> archived`, `active Implementation Rationale -> archived`, `active Review -> archived`, `active Conformance -> archived`, `A active -> B supersedes A -> A archived` with retained matching edges, and post-archive edge mutation cases
- Expected result: valid Records and permitted append-only updates pass; closed Investigation/Rationale direct archive passes; active Review/Conformance direct archive fails; Review/Conformance supersession followed by archive with sealed `A.superseded_by = B` and retained `B.supersedes = A` passes; a new `C.supersedes = A` created after `A` is archived fails; removal or change of the retained `B <-> A` edge fails; changed attestations, mutable-branch-only claims, and forbidden field changes fail
- Failure condition: a machine-detectable Record, attestation mutation, type-specific lifecycle, retained-edge, or post-archive edge-creation violation passes; hidden prose coercion is evaluated separately by `ACC-OPL-008`

### ACC-OPL-003 — Stable identity, supersession, and attestation-lineage closure

- Contracts: `CTR-OPL-006`, `CTR-OPL-007`, `CTR-OPL-014`, `CTR-OPL-015`
- Method: execute cross-record validation for stable IDs, duplicate IDs/aliases, backlinks, missing targets, path/ID consistency, archived terminal state, historical-source references, retained pre-seal edges, and Review/Conformance correction lineages
- Environment: temporary repository tree
- Required evidence: positive and negative executed cases, including `A active -> B supersedes A -> A archived`, a late `C` correction targeting active `B` while citing archived `A`, and attempts to create or alter an edge to archived `A`
- Expected result: stable complete graphs pass; every attestation lineage has exactly one active unarchived head; archived `A` retains exactly the sealed matching `A.superseded_by = B` / `B.supersedes = A` immediate-successor edge and reaches the active head; `C.supersedes = B` with archived `A` only in `historical_sources` passes; duplicate, reused, dangling, one-way, mismatched sealed backlink, new direct post-archive supersession, retained-edge deletion/change, second successor, zero/multiple-head, cycle, or invalid historical-source relations fail
- Failure condition: identity, transition, temporal-edge, or closure defects pass, or an archived erroneous attestation can appear current because no reachable active successor exists

### ACC-OPL-004 — Durable-record impact persistence and set semantics

- Contracts: `CTR-OPL-009`, `CTR-OPL-011`
- Method: evaluate pull-request fixtures where one change creates and updates Records simultaneously, reuses an existing owner, makes no new Record, and uses the emergency fallback surface
- Environment: repository unit test plus exact-Head inspection
- Required evidence: actor/time, repository, base/head, persistent surface, canonical Record locations, created/updated sets, and negative fixtures
- Expected result: valid mixed sets and justified empty sets pass; missing coordinates, mutable/unresolved head, nonexistent Record paths, and empty explanations fail
- Failure condition: a machine-detectable impact declaration violation passes or the declaration cannot represent both creation and update

### ACC-OPL-005 — Archive future-value review, attestation eligibility, sealing, and break-glass redaction

- Contracts: `CTR-OPL-007`, `CTR-OPL-010`, `CTR-OPL-011`
- Method: semantically classify calibrated keep/archive examples; attempt to archive active and superseded examples of every Record type; seal eligible fixtures; test retained pre-seal edges and new post-archive edges; attempt ordinary modification/removal; execute authorized and unauthorized redaction/tombstone fixtures
- Environment: repository semantic review plus unit test
- Required evidence: future-value classification report, type/lifecycle inventory, append-only manifest, retained-edge fingerprints, redaction ledger, tombstone hashes, actor/approver/time/reason, and executed negative tests
- Expected result: future-useful Records remain active; closed Investigation/Rationale may seal; active Review/Conformance archive fails; superseded Review/Conformance may seal while their pre-existing immediate-successor edges remain intact and their lineages remain reachable; creating a new successor edge after archive, deleting or changing the retained edge, or adding a second successor fails; ordinary tampering fails; exact authorized hazardous-content redaction succeeds without exposing unsafe bytes; a redaction used to revise meaning or lineage fails
- Failure condition: age/length alone decides archive, a current attestation seals, useful guardrails disappear, ordinary sealed content or retained lineage changes, an archived false attestation looks current, or the break-glass path becomes a general edit mechanism

### ACC-OPL-006 — Distribution/local ownership pilot

- Contracts: `CTR-OPL-012`, `CTR-OPL-001`, `CTR-OPL-015`
- Method: vendor a candidate distribution into a temporary consumer with pre-existing local Records, redirects, seals, and a redaction ledger; update the pin and inspect both trees
- Environment: temporary consumer repository
- Required evidence: source commit, manifest, adoption commit, before/after local hashes, and governance diff
- Expected result: reusable protocols/tooling update while local Records and archive state remain unchanged and locally owned
- Failure condition: central vendoring overwrites, imports, or treats consumer records/ledgers as distributed authority

### ACC-OPL-007 — Independent semantic review of Skill authority and delegation

- Contracts: `CTR-OPL-001`, `CTR-OPL-002`, `CTR-OPL-003`, `CTR-OPL-004`, `CTR-OPL-011`, `CTR-OPL-013`
- Method: independently review exact candidate Skill/protocol revisions and representative side-effecting Skills after deterministic validation
- Environment: exact implementation candidate commit
- Required evidence: reviewed base/head, reviewer identity, findings, final-head recheck, accepted authority/owner-action references, and target/write-scope analysis
- Expected result: no prose copies or reinterprets owner semantics, grants hidden mutation permission, broadens credentials/targets, or disguises an unresolved write outcome
- Failure condition: an independent semantic reviewer finds copied meaning, hidden authorization, scope broadening, or misleading validation claims

### ACC-OPL-008 — Independent semantic review of Record type and sealed-lineage boundaries

- Contracts: `CTR-OPL-005`, `CTR-OPL-008`, `CTR-OPL-011`, `CTR-OPL-014`
- Method: independently review exact Record templates/protocol revisions and representative Records after deterministic validation
- Environment: exact implementation candidate commit and pilot Records
- Required evidence: reviewed coordinates, type-by-type findings, Contract references, attestation-lineage/archive analysis, pre-seal versus post-archive edge timing, and final-head recheck
- Expected result: no Investigation grants implementation permission, no Implementation Rationale changes a Contract, no Review performs or falsely reports owner acceptance, no Conformance overstates evidence or result, no archive decision hides the current correctable attestation, and no wording destroys an established sealed edge or permits a new correction to target an archived predecessor
- Failure condition: an independent semantic reviewer finds a prose-level authority/type coercion or an archive/lineage interpretation that defeats correction or immutability semantics even though structure passed

### ACC-OPL-009 — Side-effect coordinate drift and unknown-outcome recovery

- Contracts: `CTR-OPL-002`, `CTR-OPL-013`
- Method: run a controlled side-effect harness with target drift before mutation, expired owner action, overbroad credential, idempotent retry, ambiguous first response, and reconciliation probe
- Environment: isolated local or test remote target
- Required evidence: exact before/after coordinates, authorization references, credential scope, operation key, probe result, and final classification
- Expected result: drift/expiry/scope mismatch stop before mutation; known idempotent retry is safe; ambiguous outcome is probed before retry; unresolved outcome blocks dependent work
- Failure condition: mutation proceeds after drift or unresolved authority, credentials exceed scope, or ambiguous remote state is blindly retried

### ACC-OPL-010 — Legacy applicability and migration fixtures

- Contracts: `CTR-OPL-006`, `CTR-OPL-012`, `CTR-OPL-015`
- Method: validate untouched legacy, semantic-delta-none legacy edit, migrated Investigation/Rationale, new Review/Conformance referencing legacy attestations, duplicate-ID, copied-body, missing-source-hash, and broken-redirect fixtures
- Environment: temporary pre/post-adoption repository trees
- Required evidence: adoption commit, source blob hashes, redirect map, aliases, canonical paths, and executed results
- Expected result: untouched legacy remains valid and unmanaged; non-material repair remains legacy; material update migrates or creates a new V1 Record; every collision, duplicate, or broken redirect fails
- Failure condition: adoption immediately invalidates untouched history, material legacy changes bypass V1, or migration creates duplicate identity/content

### ACC-OPL-011 — Rollback and downgrade preserve archive verification

- Contracts: `CTR-OPL-010`, `CTR-OPL-012`
- Method: create sealed and redacted corpora, including retained supersession-edge fingerprints; attempt downgrade below the minimum reader/verifier version, retain a compatibility verifier in one case, and perform an accepted export migration in another
- Environment: temporary consumer repository
- Required evidence: format/manifest/minimum-reader versions, before/after verification output, migration authority, and complete seal/redaction/retained-edge inventory
- Expected result: unsafe downgrade is rejected; compatible retained verifier succeeds; accepted export migration proves every entry and retained lineage edge before old tooling is removed
- Failure condition: a rollback leaves any sealed or redacted artifact or retained correction edge unreadable or unverifiable

### Contract coverage

| Contract | Acceptance | Evidence class | Covered |
|---|---|---|---|
| `CTR-OPL-001` | `ACC-OPL-001`, `ACC-OPL-006`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-002` | `ACC-OPL-001`, `ACC-OPL-007`, `ACC-OPL-009` | executed test / semantic review | YES |
| `CTR-OPL-003` | `ACC-OPL-001`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-004` | `ACC-OPL-001`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-005` | `ACC-OPL-002`, `ACC-OPL-008` | executed test / semantic review | YES |
| `CTR-OPL-006` | `ACC-OPL-002`, `ACC-OPL-003`, `ACC-OPL-010` | executed test | YES |
| `CTR-OPL-007` | `ACC-OPL-002`, `ACC-OPL-003`, `ACC-OPL-005` | executed test / semantic review | YES |
| `CTR-OPL-008` | `ACC-OPL-002`, `ACC-OPL-008` | executed test / semantic review | YES |
| `CTR-OPL-009` | `ACC-OPL-004` | executed test / inspection | YES |
| `CTR-OPL-010` | `ACC-OPL-005`, `ACC-OPL-011` | executed test / semantic review | YES |
| `CTR-OPL-011` | `ACC-OPL-001`, `ACC-OPL-002`, `ACC-OPL-004`, `ACC-OPL-005`, `ACC-OPL-007`, `ACC-OPL-008` | executed test / semantic review | YES |
| `CTR-OPL-012` | `ACC-OPL-006`, `ACC-OPL-010`, `ACC-OPL-011` | integration test | YES |
| `CTR-OPL-013` | `ACC-OPL-001`, `ACC-OPL-007`, `ACC-OPL-009` | executed test / semantic review | YES |
| `CTR-OPL-014` | `ACC-OPL-002`, `ACC-OPL-003`, `ACC-OPL-008` | executed test / semantic review | YES |
| `CTR-OPL-015` | `ACC-OPL-003`, `ACC-OPL-006`, `ACC-OPL-010` | executed test / integration test | YES |

## 11. Alternatives and disposition

### ALT-OPL-001 — Copy DeepSeek Harness `.agents` wholesale

- Disposition: rejected
- Reason: the repository solves a product-specific operational problem and permits non-normative Agent Note mutation semantics that cannot govern accepted authority or immutable attestations here.
- Evidence/Claims considered: `OBS-OPL-004`, `OBS-OPL-005`, `OBS-OPL-006`, `CLM-OPL-003`
- What would reopen: never as a wholesale copy; individual mechanisms remain eligible through explicit Contracts.

### ALT-OPL-002 — Add only more modes to `spec-governance`

- Disposition: rejected
- Reason: code review, release, pre-push, record maintenance, and similar operational tasks have distinct triggers, mutations, stop conditions, and outputs; one always-loaded router would grow beyond Spec governance.
- Evidence/Claims considered: `OBS-OPL-001`, `OBS-OPL-004`, `CLM-OPL-001`
- What would reopen: evidence that provider discovery and context budgets handle one large router better than bounded task Skills.

### ALT-OPL-003 — Introduce one generic Agent Note type

- Disposition: rejected
- Reason: it would overlap Investigation, Review, and Conformance Records and invite Decision, implementation state, review, and evidence to be collapsed.
- Evidence/Claims considered: `OBS-OPL-003`, `OBS-OPL-005`, `CLM-OPL-002`
- What would reopen: a future type system that proves the generic container cannot blur authority or state dimensions.

### ALT-OPL-004 — Encode Record lifecycle in directory moves

- Disposition: rejected for V1
- Reason: repository governance relies on stable identities and exact links; metadata provides lifecycle without changing stable paths.
- Evidence/Claims considered: `CLM-OPL-004`
- What would reopen: deterministic redirect/catalog tooling that preserves exact identity and inbound references across moves.

### ALT-OPL-005 — Require a new Record for every non-trivial PR

- Disposition: rejected
- Reason: the rule would create duplicates when an accepted authority or existing Record already owns the rationale.
- Evidence/Claims considered: `DEC-OPL-008`
- What would reopen: repeated pilot evidence that set-valued impact declarations fail to catch missing durable knowledge.

### ALT-OPL-006 — Treat all Skill and Record quality as semantic review only

- Disposition: rejected
- Reason: IDs, required fields, explicit authority-effect fields, exact coordinates, references, output schemas, closure, redirects, and archive seals are deterministic even though completeness and decision quality are not.
- Evidence/Claims considered: `OBS-OPL-006`, `CTR-OPL-011`
- What would reopen: not applicable; semantic review remains mandatory and additive rather than a substitute.

### ALT-OPL-007 — Let each Skill authorize the side effects it describes

- Disposition: rejected
- Reason: a non-authoritative workflow artifact would become the source of its own write permission and could broaden targets or credentials without accepted authority or owner action.
- Evidence/Claims considered: `OBS-OPL-007`, `DEC-OPL-010`
- What would reopen: never under the accepted authority model.

### ALT-OPL-008 — Permit Review and Conformance corrections in place because Git retains history

- Disposition: rejected
- Reason: the current durable artifact under one stable ID would present a different attestation, forcing readers to reconstruct which version was intended from Git history.
- Evidence/Claims considered: `OBS-OPL-007`, `DEC-OPL-011`
- What would reopen: a future immutable append-only storage model where each attestation version has an independently addressable stable identity.

### ALT-OPL-009 — Make archives absolutely undeletable without a hazardous-content exception

- Disposition: rejected
- Reason: credentials, personal data, malicious payloads, and lawful removal obligations may require current-tree and history purge; ordinary edit immutability must coexist with an auditable break-glass path.
- Evidence/Claims considered: `OBS-OPL-007`, `DEC-OPL-009`
- What would reopen: not applicable; the exception remains narrow and owner-authorized.

### ALT-OPL-010 — Allow current attestations to archive and add a separate archived-correction ledger

- Disposition: rejected for V1
- Reason: an external correction relation would introduce new precedence, query, atomicity, compatibility, and verifier semantics. Keeping the current Review or Conformance head unsealed until superseded closes the contradiction with a smaller state machine.
- Evidence/Claims considered: `OBS-OPL-008`, `EVD-OPL-006`, `DEC-OPL-006`, `DEC-OPL-011`
- What would reopen: evidence from pilots that retaining current attestations unsealed causes unacceptable corpus or operational cost that cannot be addressed by indexing.

### ALT-OPL-011 — Delete or convert a supersession edge when its predecessor is archived

- Disposition: rejected
- Reason: removing or changing the pre-seal `successor.supersedes = predecessor` edge would break its matching backlink, lineage reachability, correction history, and sealed immutability. The correct distinction is temporal: retain the edge established before sealing and prohibit creation of a new edge after archival.
- Evidence/Claims considered: `OBS-OPL-009`, `EVD-OPL-007`, `DEC-OPL-006`, `DEC-OPL-011`
- What would reopen: only a future whole-lineage storage model that preserves equivalent immutable bidirectional identity and query semantics under a new accepted Spec.

## 12. Migration, compatibility, and rollback

```text
MIGRATION = after acceptance, implement protocols/templates/validators in a separate PR, then pilot opt-in adoption in consumer repositories at an exact local adoption commit
COMPATIBILITY = untouched pre-adoption records remain legacy_unmanaged; V1 applies to new and explicitly migrated Records; exact redirect and collision rules preserve historical references
ROLLBACK = a repository with no sealed/redacted corpus may revert the distribution update; a repository with such a corpus must retain a compatible reader/verifier or complete an accepted verifiable export migration first
EMERGENCY_CONTAINMENT = disable an unsafe Skill entrypoint or validator integration; hazardous archived content uses the owner-authorized tombstone/redaction process; durable repair returns through normal Spec governance
```

No consumer MUST bulk-migrate untouched historical records. A material post-adoption update triggers the type-specific migration or new-Record rules in `CTR-OPL-015`. Review and Conformance attestations remain immutable and active until superseded; only superseded attestations may be archived. A pre-seal immediate-successor edge remains sealed and immutable after the predecessor is archived, while later corrections target only the current active head. Consumer updates and rollbacks MUST preserve local Record, redirect, seal, redaction, retained-edge, and attestation-lineage state.

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
PRIOR_REVIEW_IDS = 5020251145, 5036091214, 5057378137
PRIOR_REVIEW_RESULTS = REVISE, REVISE, REVISE
PRIOR_REVIEW_BLOCKERS_ADDRESSED = 7
INDEPENDENT_REVIEW_REQUIRED = YES
AUTHORING_READY_FOR_REVIEW = YES
READY_TO_MARK_ACCEPTED = YES
IMPLEMENTATION_IN_THIS_PR = NO
```
