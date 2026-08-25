---
spec_id: AGENT_OPERATIONAL_LAYER_V1
status: proposed
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

Add a bounded operational layer around the accepted development grammar so Agents can reliably select and execute recurring repository tasks and preserve durable, non-normative engineering knowledge without confusing either surface with governing authority.

```text
GOAL = discoverable task Skills plus a typed repository-local Record corpus
SUCCESS_OUTCOME = Agents can execute recurring workflows and preserve rationale while Spec authority, implementation state, review, and conformance remain semantically separate
```

## 2. Scope and non-goals

### In scope

- a normative package contract for repository-scoped Agent Skills;
- thin task-oriented Skill entrypoints that delegate shared semantics to one owning router;
- optional Skill-local `references/`, deterministic `scripts/`, tests, and provider interface metadata;
- explicit trigger, anti-trigger, input, mutation, stop, output, and completion boundaries;
- a typed, non-normative Record corpus for investigations, implementation rationale, reviews, and conformance;
- stable Record identity, coordinates, lifecycle metadata, supersession links, and archive policy;
- deterministic validation of Skill and Record structure without claiming semantic review;
- a central-distribution versus repository-local ownership boundary;
- a durable-record impact declaration for non-trivial changes.

### Out of scope

- changing the accepted semantic primitives or authority precedence;
- changing the lifecycle or meaning of governing Specs;
- making Skills, provider metadata, scripts, tests, Notes, or Records normative authority;
- treating `implemented`, `reviewed`, `verified`, or `archived` as interchangeable states;
- requiring one new Record file for every non-trivial change when an existing record already owns the rationale;
- copying DeepSeek Harness Agent Notes or Skills wholesale;
- provider-specific runtime implementation;
- implementing the protocols, templates, schemas, validators, or consumer migrations in this docs-only Spec PR;
- retroactively migrating historical consumer repositories.

## 3. Authority and dependencies

This Spec refines the accepted bootstrap authority without changing any existing Decision or Contract.

```text
PRIMARY_PARENT_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
PARENT_REVISION_AT_AUTHORING = d32b946cbbbc1baa99165d7656fc22e8823a651f
IMPLEMENTATION_AUTHORITY = contracts
EXTERNAL_AUTHORITIES = NONE
EXTERNAL_PRIOR_ART = deepseek-ai/deepseek-harness@b150a551b8d465e31e418e1b2eaf5e79bbb7d28e
AUTHORITY_CONFLICT = NONE
```

DeepSeek Harness is studied only as non-normative prior art. Its repository does not own, constrain, or supersede this repository's governance.

## 4. Current State

### STATE-OPL-001 — The distribution has one semantic Skill router but no general Skill-package contract

- Subject: reusable Skill surface in `mayf3/agent-development-governance`
- As of commit: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository `main`
- Observed at: 2026-08-25
- Projection: the distribution contains `spec-governance/SKILL.md` and four mode files, with shared invariants and read-order guidance, but does not define a reusable contract for task-oriented entrypoints, Skill-local scripts/references, provider metadata, validation, or completion semantics.
- Basis: `OBS-OPL-001`, `OBS-OPL-002`, `CLM-OPL-001`

### STATE-OPL-002 — Durable Record templates exist without a common repository corpus contract

- Subject: persistent non-Spec development records
- As of commit: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository `main`
- Observed at: 2026-08-25
- Projection: Investigation, Review, and Conformance templates exist, but there is no common Record identity schema, canonical repository-local corpus, implementation-rationale record type, archive lifecycle, supersession rule, or deterministic cross-record validator.
- Basis: `OBS-OPL-003`, `CLM-OPL-002`

### STATE-OPL-003 — DeepSeek Harness demonstrates useful operational and memory mechanisms with incompatible authority semantics

- Subject: non-normative prior art under `deepseek-ai/deepseek-harness/.agents`
- As of commit: `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Environment: public repository source
- Observed at: 2026-08-25
- Projection: task-oriented Skill packages and mechanically maintained Agent Notes provide useful discoverability, workflows, rationale, alternatives, archival, and validation; however, lifecycle moves such as `proposed` to `implemented` and in-place updates of shipped facts cannot be copied onto accepted governing authority.
- Basis: `OBS-OPL-004`, `OBS-OPL-005`, `OBS-OPL-006`, `CLM-OPL-003`

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
- Result: the distribution includes one Skill tree, but no protocol or validator defines optional `references/`, `scripts/`, tests, provider interface metadata, anti-triggers, allowed mutations, stop conditions, or done criteria for Skills generally.
- Provenance: `.agents/skills/`, `distribution/manifest.json`

### OBS-OPL-003 — Existing Record templates are typed but not governed as one corpus

- Subject: durable non-Spec templates
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: repository source
- Observed at: 2026-08-25
- Method: inspect `.agents/templates/INVESTIGATION_RECORD_TEMPLATE.md`, `REVIEW_RECORD_TEMPLATE.md`, and `CONFORMANCE_RECORD_TEMPLATE.md`
- Result: each template defines useful type-specific fields, but there is no common Record ID contract, shared path or metadata schema, implementation-rationale template, supersession closure, archive policy, or corpus validator.
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
- Strength/sufficiency: decisive for forbidding copied Note lifecycle from mutating accepted Spec meaning
- Limitations: non-normative implementation facts may still be updated or superseded
- Provenance: parent Spec and DSH prior-art paths

### EVD-OPL-004 — Stable identity requirements support stable paths plus lifecycle metadata

- Source observations: `OBS-OPL-003`, `OBS-OPL-005`, `OBS-OPL-006`
- Target: `CLM-OPL-004`
- Relation: SUPPORTS
- Bound coordinates: governance `d32b946c`; DeepSeek Harness `b150a551`
- Strength/sufficiency: inferential but sufficient for V1
- Limitations: path redirects and generated catalogs could support a different future design
- Provenance: repositories and paths named by the source observations

## 8. Decisions

### DEC-OPL-001 — Separate authority, operational workflow, and durable Record layers

- Decision owner: repository owner
- Decision: governing authority remains in Product Direction, Architecture/invariant authority, and accepted Specs; Skills execute bounded workflows; Records preserve qualified non-normative knowledge.
- Rejected alternatives: treat Skills as policy authority; infer Contracts from implementation records; use one undifferentiated `.agents` knowledge tree.
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
- Decision: every distributed Skill declares its purpose, trigger and anti-trigger, required inputs and coordinates, sources of truth, allowed and forbidden mutations, stop conditions, procedure, required output, failure output, and done criteria.
- Rejected alternative: prose that merely describes a capability without defining when execution must stop or what completion means.
- Reason: explicit operational boundaries make Skill execution auditable and reduce invented workflow.
- Owner decision remaining: NONE

### DEC-OPL-004 — Permit layered Skill packages without granting authority to auxiliary files

- Decision owner: repository owner
- Decision: a Skill package may contain `SKILL.md`, modes, references, deterministic scripts, tests, and provider interface metadata. `SKILL.md` owns the operational contract; references explain; scripts mechanize bounded checks; provider metadata aids discovery only.
- Rejected alternative: place provider-specific interface metadata or long examples inside the normative governance protocol.
- Reason: separate layers reduce context and permit tooling without creating hidden authority.
- Owner decision remaining: NONE

### DEC-OPL-005 — Establish a typed non-normative Record corpus

- Decision owner: repository owner
- Decision: V1 recognizes `investigation`, `implementation_rationale`, `review`, and `conformance` Record types. Every Record explicitly states that it is not governing authority and cannot authorize implementation or change a Contract.
- Rejected alternative: one generic Agent Note type containing decisions, reviews, implementation status, and evidence.
- Reason: type-specific Records preserve useful knowledge without collapsing the grammar.
- Owner decision remaining: NONE

### DEC-OPL-006 — Keep Record lifecycle separate and paths stable

- Decision owner: repository owner
- Decision: repository-file Records use stable type/ID paths and lifecycle metadata `active | superseded | archived`; type-specific disposition, implementation, verification, and conformance fields remain independent.
- Rejected alternative: encode lifecycle by moving every active Record among directories.
- Reason: stable paths preserve references and exact identity, while metadata remains mechanically queryable.
- Owner decision remaining: NONE

### DEC-OPL-007 — Add an Implementation Rationale Record

- Decision owner: repository owner
- Decision: an Implementation Rationale Record explains an internal implementation choice within an accepted Spec's Contracts, binds the governing Spec revision and relevant implementation coordinates, and records alternatives, consequences, and reopening conditions.
- Rejected alternative: put implementation choices into accepted Contract text or leave them only in chat and code review.
- Reason: internal choices can guide future maintenance without becoming normative system obligations.
- Owner decision remaining: NONE

### DEC-OPL-008 — Require durable-record impact accounting, not record quotas

- Decision owner: repository owner
- Decision: every non-trivial change reports `DURABLE_RECORD_IMPACT = CREATED | UPDATED | NONE`; `NONE` names the existing owner or explains why the change introduces no reusable rationale.
- Rejected alternative: require a newly created Note for every non-trivial change.
- Reason: impact accounting catches missing knowledge without producing duplicate or low-value Records.
- Owner decision remaining: NONE

### DEC-OPL-009 — Archive by future decision value and freeze sealed Records

- Decision owner: repository owner
- Decision: a Record is archived only when it is no longer likely to guide a future decision. Sealed archive content is immutable and mechanically protected; age, word count, and target quotas are discovery aids, not archive criteria.
- Rejected alternative: archive automatically after a time threshold or to maintain a target corpus size.
- Reason: rationale, negative guarantees, security rules, durable semantics, ownership boundaries, and reopening conditions may remain valuable indefinitely.
- Owner decision remaining: NONE

## 9. Contracts

### CTR-OPL-001 — Skills and Records are not governing authority

A Skill, script, test, provider metadata file, generated catalog, Record, PR discussion, or archive MUST NOT create, accept, amend, supersede, or reinterpret a governing Decision or Contract. Every distributed Skill and Record template MUST state its authority boundary. When any operational instruction conflicts with accepted authority, execution MUST stop and report the conflict.

### CTR-OPL-002 — Every Skill has a bounded invocation contract

Every distributed Skill MUST declare:

```text
purpose
use_when
do_not_use_when
required_inputs
fixed_coordinates
sources_of_truth
allowed_mutations
forbidden_actions
stop_conditions
procedure
required_output
failure_output
done_criteria
```

Missing information MAY be resolved from repository state when a deterministic read can establish it. The Skill MUST NOT begin semantic mutation while a required coordinate, authority, or write boundary remains unresolved.

### CTR-OPL-003 — Shared semantics have one owner

A task-oriented entry Skill MAY route to an owning Skill mode or protocol section. It MUST name that owner and MUST NOT duplicate shared normative semantics. If the owner changes, entrypoints MUST continue to delegate or fail validation rather than silently retaining stale copied rules.

### CTR-OPL-004 — Skill auxiliary layers remain bounded

A Skill package MAY include `modes/`, `references/`, `scripts/`, `tests/`, and `agents/<provider>.yaml`.

- `SKILL.md` MUST own the executable operational contract.
- A reference MUST NOT become required authority merely because it is linked.
- A deterministic script MUST report only the properties it actually checks.
- Provider metadata MUST be optional for governance semantics and MUST NOT weaken trigger, mutation, stop, or output rules.
- Bundled scripts MUST have focused validation and MUST NOT install dependencies or mutate remote state unless the Skill explicitly authorizes that mutation.

### CTR-OPL-005 — Record types are explicit and non-interchangeable

The Record corpus MUST distinguish at least:

```text
investigation
implementation_rationale
review
conformance
```

An Investigation Record MUST NOT grant implementation permission. An Implementation Rationale Record MUST NOT create or change a Contract. A Review Record MUST NOT perform owner acceptance. A Conformance Record MUST remain qualified to exact Spec revision, implementation revision, environment, time, and evidence.

### CTR-OPL-006 — Every Record has stable identity and coordinates

Every repository-file Record MUST have a stable `RECORD_ID`, `RECORD_TYPE`, stable repository path, owner, created time, lifecycle, related authority IDs and exact revisions where applicable, stable provenance links, and supersession fields. IDs MUST NOT be reused or renumbered. A Record MUST NOT claim “current” implementation or runtime state without the coordinates required by the accepted grammar.

V1 file-backed ID forms are:

```text
INV-YYYY-NNN   investigation
IRR-YYYY-NNN   implementation_rationale
REV-YYYY-NNN   review
CONF-YYYY-NNN  conformance
```

The canonical repository-file path form is:

```text
.agents/local/records/<record_type>/<RECORD_ID>.md
```

The lifecycle value is metadata and MUST NOT require a path move. A supersession transition MUST atomically set forward and backward links. The old Record MUST retain its historical meaning and MUST NOT be rewritten to pretend it made the successor's decision.

### CTR-OPL-007 — Record lifecycle does not collapse other state dimensions

Record lifecycle is:

```text
active | superseded | archived
```

It MUST remain separate from:

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

`archived` MUST NOT mean rejected, implemented, verified, conforming, or obsolete authority.

### CTR-OPL-008 — Implementation rationale stays within accepted Contracts

An Implementation Rationale Record MUST bind:

```text
governing_spec_id
governing_spec_revision
covered_contracts
implementation_repository
implementation_base
implementation_revision_or_branch
chosen_implementation
alternatives_considered
consequences
verification_references
reopen_conditions
```

It MUST stop and request Spec governance when the proposed rationale would alter external behavior, identity, authorization, failure, retry, timeout, transaction, lifecycle, migration, compatibility, observability, or security semantics beyond the accepted Contracts.

### CTR-OPL-009 — Non-trivial changes account for durable knowledge

Every non-trivial change under adopted governance MUST persist:

```text
DURABLE_RECORD_IMPACT = CREATED | UPDATED | NONE
```

`CREATED` and `UPDATED` MUST name the Record IDs. `NONE` MUST name the existing durable owner of the decision/rationale or state why the change is mechanical/local and adds no reusable knowledge. The rule MUST NOT require duplicate Records when an existing Record or accepted authority already owns the material.

### CTR-OPL-010 — Archive selection is semantic and sealing is mechanical

A Record MAY become `archived` only after a semantic future-value review. Records that preserve active rationale, alternatives, negative guarantees, ownership or security boundaries, durable or wire semantics, compatibility obligations, or reopening conditions MUST remain active or superseded as appropriate.

After archive sealing:

- content MUST be immutable;
- the seal manifest MUST be append-only;
- existing sealed paths and hashes MUST NOT be removed or changed;
- an archived Record MUST remain historical, non-authoritative material;
- generated catalogs MAY omit it from default active views without deleting it.

### CTR-OPL-011 — Validation claims remain honest

Deterministic tooling MAY validate package layout, metadata fields, ID patterns, stable references, type-specific required sections, supersession closure, archive seals, and declared output schemas. It MUST NOT claim to establish semantic completeness, decision quality, evidence sufficiency, independent review, acceptance, or conformance.

### CTR-OPL-012 — Central distribution and repository-local knowledge remain separate

The central distribution MAY contain the Skill-package protocol, Record-corpus protocol, schemas, templates, validators, and reusable Skills. Consumer-specific Records MUST remain in their owning repository and MUST NOT be copied back into the central distribution manifest as shared governance. A consumer update MUST preserve its local Records and local authority ownership.

## 10. Acceptance

### ACC-OPL-001 — Skill package contract validation

- Contracts: `CTR-OPL-001`, `CTR-OPL-002`, `CTR-OPL-003`, `CTR-OPL-004`, `CTR-OPL-011`
- Method: validate representative router, thin-entry, script-bearing, reference-bearing, and provider-metadata Skill fixtures; include invalid fixtures for copied owner semantics, missing stop conditions, and provider overrides
- Environment: repository unit test
- Required evidence: executed validator result bound to implementation commit
- Expected result: valid packages pass; every named invalid package fails for the intended rule
- Failure condition: a Skill with ambiguous mutation authority, no completion contract, copied shared semantics, or provider-weakened rules passes

### ACC-OPL-002 — Record corpus schema and type-boundary validation

- Contracts: `CTR-OPL-001`, `CTR-OPL-005`, `CTR-OPL-006`, `CTR-OPL-007`, `CTR-OPL-008`, `CTR-OPL-011`
- Method: validate one complete fixture of each Record type plus invalid cross-type coercions
- Environment: repository unit test
- Required evidence: executed validator result and fixture inventory bound to implementation commit
- Expected result: valid Records pass; an Investigation granting implementation permission, rationale changing a Contract, Review claiming acceptance, and unqualified Conformance each fail
- Failure condition: type-specific authority or coordinate violations pass

### ACC-OPL-003 — Stable identity and supersession closure

- Contracts: `CTR-OPL-006`, `CTR-OPL-007`
- Method: execute cross-record validation for stable IDs, duplicate IDs, backlinks, missing targets, and path/ID consistency
- Environment: temporary repository tree
- Required evidence: positive and negative executed cases
- Expected result: stable complete graphs pass and every duplicate, reused, dangling, or one-way supersession fails
- Failure condition: identity or closure defects pass

### ACC-OPL-004 — Durable-record impact gate

- Contracts: `CTR-OPL-009`, `CTR-OPL-011`
- Method: evaluate representative non-trivial and mechanical change fixtures with `CREATED`, `UPDATED`, and `NONE`
- Environment: repository unit test plus semantic review
- Required evidence: declaration, changed paths, related authority/Record IDs, and negative fixtures
- Expected result: valid ownership explanations pass; empty `NONE`, missing named Records, and duplicate-Record requirements fail
- Failure condition: the mechanism becomes either optional boilerplate or a quota that forces a new Record

### ACC-OPL-005 — Archive future-value review and tamper detection

- Contracts: `CTR-OPL-010`, `CTR-OPL-011`
- Method: semantically classify calibrated keep/archive examples, seal archived fixtures, then modify, remove, and reorder sealed entries
- Environment: repository review plus unit test
- Required evidence: classification report, append-only manifest, and executed negative tests
- Expected result: future-useful Records remain active; low-future-value Records may be sealed; every change or removal of a prior seal fails
- Failure condition: age or length decides archival, useful guardrails disappear, or sealed content can change undetected

### ACC-OPL-006 — Distribution/local ownership pilot

- Contracts: `CTR-OPL-012`, `CTR-OPL-001`
- Method: vendor a candidate distribution into a temporary consumer with pre-existing local Records, update the pin, and inspect both trees
- Environment: temporary consumer repository
- Required evidence: source commit, manifest, before/after local Record hashes, and governance diff
- Expected result: reusable protocols and tooling update while local Records remain unchanged and locally owned
- Failure condition: central vendoring overwrites, imports, or treats consumer Records as distributed authority

### ACC-OPL-007 — Independent semantic boundary review

- Contracts: all `CTR-OPL-*`
- Method: independent review of the exact Spec and implementation candidate commits
- Environment: docs-only Spec PR, then later implementation PR
- Required evidence: reviewed base/head, semantic findings, final-head recheck, and Contract-by-Contract recommendation
- Expected result: no Skill or Record can create authority, all state dimensions remain separate, and the implementation stays within this Spec
- Failure condition: the design reproduces DSH Note authority semantics, duplicates shared governance rules, or claims machine-verified semantics

### Contract coverage

| Contract | Acceptance | Evidence class | Covered |
|---|---|---|---|
| `CTR-OPL-001` | `ACC-OPL-001`, `ACC-OPL-002`, `ACC-OPL-006`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-002` | `ACC-OPL-001`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-003` | `ACC-OPL-001`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-004` | `ACC-OPL-001`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-005` | `ACC-OPL-002`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-006` | `ACC-OPL-002`, `ACC-OPL-003`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-007` | `ACC-OPL-002`, `ACC-OPL-003`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-008` | `ACC-OPL-002`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-009` | `ACC-OPL-004`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-010` | `ACC-OPL-005`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-011` | `ACC-OPL-001`, `ACC-OPL-002`, `ACC-OPL-004`, `ACC-OPL-005`, `ACC-OPL-007` | executed test / semantic review | YES |
| `CTR-OPL-012` | `ACC-OPL-006`, `ACC-OPL-007` | integration test / semantic review | YES |

## 11. Alternatives and disposition

### ALT-OPL-001 — Copy DeepSeek Harness `.agents` wholesale

- Disposition: rejected
- Reason: the repository solves a product-specific operational problem and permits non-normative Agent Note mutation semantics that cannot govern accepted authority here.
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
- What would reopen: repeated pilot evidence that impact declarations fail to catch missing durable knowledge.

### ALT-OPL-006 — Treat all Skill and Record quality as semantic review only

- Disposition: rejected
- Reason: IDs, required fields, references, output schemas, closure, and archive seals are deterministic even though completeness and decision quality are not.
- Evidence/Claims considered: `OBS-OPL-006`, `CTR-OPL-011`
- What would reopen: not applicable; semantic review remains additive rather than a substitute.

## 12. Migration, compatibility, and rollback

```text
MIGRATION = after acceptance, implement protocols/templates/validators in a separate PR, then pilot opt-in adoption in consumer repositories
COMPATIBILITY = existing Investigation, Review, and Conformance records remain valid; migration to canonical metadata is forward-only and repository-owned
ROLLBACK = revert the operational-layer distribution update and retain repository-local Records as non-authoritative files
EMERGENCY_CONTAINMENT = disable an unsafe Skill entrypoint or validator integration; durable repair returns through normal Spec governance
```

No consumer MUST bulk-migrate historical records. The first adopted implementation applies to newly created or materially updated Records. Existing stable links MUST be preserved when a repository elects to migrate an old record.

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
INDEPENDENT_REVIEW_REQUIRED = YES
READY_TO_MARK_ACCEPTED = YES
IMPLEMENTATION_IN_THIS_PR = NO
```
