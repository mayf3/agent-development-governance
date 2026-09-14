---
spec_id: AGENT_MODEL_CONVERGENCE_V1
status: proposed
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
governed_by:
  - AGENT_DEVELOPMENT_GOVERNANCE_V1
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# Historical model convergence and subtraction-first refactoring

## 1. Goal

Make retirement of obsolete models part of development, rather than repeatedly repairing historical ambiguity with permanent fallback paths.

> 同一业务语义应收敛到明确的当前模型。优先迁移、删除和重构，而不是不断增加映射与兼容。修复不仅证明新路径能工作，还要证明旧路径已退出、恢复不会将它复活。

The objective is fewer independently maintained models, authorities, entrypoints, and exceptional branches, not mechanically fewer identifiers or lines of code.

## 2. Scope and non-goals

This standard governs how the reusable development grammar identifies and reviews historical duplication during affected work: identity representations, fields, configuration keys, API/CLI entrypoints, state stores, runtimes, recovery paths, adapters, and dependency replacements.

It does not prescribe consumer identity formats or cardinality, merge `agentId`/`principalId`/`clientId`, create another canonical-ID generation, require a central registry or distributed transaction, authorize production cleanup, retire supported external contracts, rewrite historical evidence, or turn a local repair into a global census. It adds no Agent formation, platform, scoring system, approval ceremony, or new blocker class.

## 3. Authority and dependencies

```text
AUTHORITY_ACTION = NEW
PARENT = AGENT_DEVELOPMENT_GOVERNANCE_V1
PARENT_REVISION = 9dcd0c49a5932e44e2801317b6281bdc6a168d25
AUTHORING_STAGE = docs-only proposal
ACCEPTANCE_ACTOR = mayf3 or an explicitly authorized maintainer
IMPLEMENTATION_AUTHORITY = governance-distribution Contracts only, after acceptance
CONSUMER_PRODUCT_AUTHORITY = unchanged; local adoption required
```

This is a bounded new development obligation, not a reinterpretation of an existing accepted Decision. It supplements the parent without superseding or editing any accepted meaning. Product support commitments, review-source rules, proportional routing, controlled-operation safeguards, and stop controls remain governed by the parent. A conflicting consumer Contract must be resolved by its existing authority process, not overridden by this standard.

The proposal does not activate rules in `.agents/**`. Acceptance, distribution implementation/release, consumer adoption, and product migration remain separately evidenced states. This PR authorizes none of the latter operations.

## 4. Current State

### STATE-CONV-001 — A proposal exists; activation is not established

- Subject: `mayf3/agent-development-governance`.
- As of commit: `9dcd0c49a5932e44e2801317b6281bdc6a168d25`.
- Environment / observed at: remote `main`, 2026-09-15.
- Projection: Governance V1 is accepted; Issue #15 requests an additional convergence standard. This authoring change does not establish distribution activation or consumer conformance.
- Basis: `OBS-CONV-001`, `OBS-CONV-002`.

## 5. Observations

### OBS-CONV-001 — The existing grammar supplies the safety and routing boundaries

- Source revision: `9dcd0c49a5932e44e2801317b6281bdc6a168d25`.
- Environment / observed at: remote source repository, 2026-09-15.
- Method: read `AGENTS.md`, `.agents/README.md`, `.agents/local/README.md`, the accepted parent and the Spec-governance authoring rules.
- Result: local consumer authority, immutable accepted meaning, attributable mutation authorization, isolated writes, proportional review, and stopping at Done When are already required.
- Provenance: those paths at the stated revision.

### OBS-CONV-002 — The owner requests subtraction rather than permanent compatibility

- Source: [Issue #15](https://github.com/mayf3/agent-development-governance/issues/15), snapshot read 2026-09-15; owner subsequently requested a PR.
- Environment: issue and task discussion, not a production investigation.
- Method: read the proposal and distinguish its request from its reported incident.
- Result: the request covers historical IDs and the broader pattern of obsolete models remaining executable after replacement.
- Limitation: the reported Workflow/Auth/Agent Core incident was not independently reproduced here; no actual identity or successor mapping is established by this Spec.

## 6. Claims and assumptions

### CLM-CONV-001 — Explicit retirement criteria address the reported repair pattern

- Support state: INFERRED.
- Supported by evidence: `EVD-CONV-001`.
- Contradicted by evidence: none established in this authoring task.
- Uncertainty: this is a design rationale, not measured proof of reduced incidents; consumer outcomes require later observations.

## 7. Evidence relations

### EVD-CONV-001 — The requested outcome motivates a bounded development rule

- Source observations: `OBS-CONV-001`, `OBS-CONV-002`.
- Target / relation: `CLM-CONV-001` / SUPPORTS.
- Bound coordinates: the source revision and issue snapshot stated above.
- Sufficiency: supports proposing a subtraction-first rule within existing safeguards.
- Limitations: does not prove production duplication, authorize identity reassignment, or verify implementation.
- Provenance: the named repository paths and Issue #15.

## 8. Decisions

### DEC-CONV-001 — Distinguish obsolete duplication from legitimate multiplicity

- Decision owner: repository owner, proposed for acceptance.
- Decision: investigate the affected semantic boundary and its current owner before deciding what to retire; preserve distinct responsibilities and valid support obligations.
- Rejected alternative: classify every old name or multiple-ID relationship as a defect.
- Reason: historical duplicates and deliberately different entities need different treatment.

### DEC-CONV-002 — Prefer subtraction and require a compatibility exit

- Decision owner: repository owner, proposed for acceptance.
- Decision: prefer deleting unused paths, migrating real consumers and removing replacements, and consolidating duplicate logic over adding permanent fallback. Temporary bridges have explicit retirement conditions.
- Rejected alternative: make every historical representation permanently executable.
- Reason: fixing one request must not indefinitely multiply normal execution paths.

### DEC-CONV-003 — Retirement includes runtime closure without erasing history

- Decision owner: repository owner, proposed for acceptance.
- Decision: verify the current path, retired-path exclusion, and applicable restart/recovery behavior; preserve historical evidence and existing mutation safeguards.
- Rejected alternatives: declare completion after one successful request; delete records merely because their names look old.
- Reason: runtime eligibility and historical explainability are separate concerns.

### DEC-CONV-004 — Integrate into existing work rather than create another workflow

- Decision owner: repository owner, proposed for acceptance.
- Decision: place bounded convergence questions in the existing grammar, PREFLIGHT, review mode, and templates after acceptance; keep consumer adoption local and exact-revision-bound.
- Rejected alternatives: an isolated essay with no development hook; a new governance platform or approval round for routine cleanup.
- Reason: the standard should reduce maintenance work, not generate another permanent process.

## 9. Contracts

### CTR-CONV-001 — Inspect the affected historical alternatives

Basis: `DEC-CONV-001`.

For replacement, migration, identity-resolution, or conflicting-state-source work, the developer MUST identify the current representation, historical alternatives, real readers/writers/executors, and affected creation/recovery paths. The developer MUST distinguish obsolete duplication, currently supported differences, read-only history, and temporary migration bridges. Unknown coverage MUST remain unknown, not zero. Inspection MUST stay within the goal and its necessary dependencies; a global census is not the default.

### CTR-CONV-002 — Give each fact an owner; preserve distinct entities

Basis: `DEC-CONV-001`.

The design MUST identify who owns each affected fact and how consumers use it. A projection or cache MUST NOT silently become an independent authority for that same fact. Different components MAY own different eligibility conditions: `active` in one service is not by itself universal eligibility, nor proof of an illegal record when another service denies admission.

The developer MUST NOT merge identities on names, prefixes, or unverified historical mappings, impose a universal 1:1 identity rule, or generate replacement IDs merely to label them canonical. Correct stable identities and legitimate multi-credential, multi-tenant, and supported-protocol relationships MUST be preserved according to owning Contracts. Ambiguity MUST NOT be hidden by silently switching the acting identity.

### CTR-CONV-003 — Explain what complexity is removed

Basis: `DEC-CONV-002`.

A relevant repair MUST evaluate removal of unused paths, migration followed by removal, and consolidation before choosing an additional compatibility layer. The change record MUST identify which obsolete models, branches, entrypoints, or special interpretations will cease to require maintenance, or why only a bounded containment stage is currently possible. Net deleted line count is not an acceptance metric. Emergency relief MAY precede retirement, but MUST NOT be reported as final convergence while exit work remains.

### CTR-CONV-004 — A temporary bridge must be removable

Basis: `DEC-CONV-002`.

A temporary bridge MUST record its actual remaining consumer, scope, accountable owner, exit date or objectively verifiable exit condition, and removal evidence in the existing Brief/PR/ExecPlan. Speculative future consumers do not justify permanent compatibility; unknown consumers require bounded investigation.

The bridge MUST NOT create new retired-format business objects. A supported boundary MAY translate input into the current model only under the owning product's existing identity and authorization Contracts; this is not permission to remap credentials or principals silently. Expiry MUST cause an explicit disposition, not silent renewal or automatic destructive deletion. A still-supported external interface is not an obsolete bridge solely because it is old; changing its support promise requires the normal authority route.

### CTR-CONV-005 — Retire execution, preserve evidence, and prevent recreation

Basis: `DEC-CONV-003`.

A migration plan MUST cover the applicable paths that could perpetuate the retired model: new legacy references, mutable active references, old writers/executors, code/configuration/deployment entrypoints, and restart/retry/recovery/bootstrap logic. Sequencing MUST preserve owning safety Contracts and necessary rollback containment. Source-code removal alone does not establish deployed retirement.

Immutable audits, historical definitions, migrations, receipts, and necessary tombstones MAY remain readable. They MUST NOT independently grant present eligibility or revive retired writers, identities, or side effects. Execution of historical work requires the owning product's authorized migration and current eligibility checks. Retirement MUST NOT erase required provenance or silently transfer grants. Identity merges, credential/permission changes, production deletion, and destructive migration remain controlled operations under the parent; neither this standard nor an expired bridge authorizes them.

### CTR-CONV-006 — Verify new usability, old-path exit, and non-revival

Basis: `DEC-CONV-003`.

Before reporting final convergence, the developer and reviewer MUST bind the evidence to the affected scope, implementation/deployment revision, environment, and observation time, and establish:

1. the current path satisfies applicable business and safety Contracts;
2. retired representations cannot re-enter new work through affected normal or fallback paths;
3. applicable restart, recovery, retry, replay, and migration rerun paths do not recreate the retired model, duplicate work, or transfer authority improperly.

They MUST distinguish source-level completion, deployment closure, and final convergence. A remaining bridge means a bounded stage, not final retirement. Zero active legacy references/entrypoints MUST have an enumerated scope and evidence; legitimate historical records and supported interfaces MUST be listed separately. Unexecuted, unknown, and out-of-scope checks MUST NOT become zero or PASS. Grep results, test names, one successful publish, or an `active` flag alone are insufficient. An inapplicable check needs a reason, not fabricated execution.

### CTR-CONV-007 — Put conditional checks in the existing distribution

Basis: `DEC-CONV-004`.

After acceptance, the distribution implementation MUST integrate the principle into `.agents/README.md`, the affected-work check into `.agents/skills/spec-governance/modes/PREFLIGHT.md`, and exit-evidence review into `.agents/skills/spec-governance/modes/REVIEW.md`. Existing Change Brief and Review Record templates MUST conditionally cover: **retain, retire, migrate, temporary exceptions, evidence**. The distributed guidance MUST be self-contained in the existing vendored surface, not depend on a source-only `docs/specs/` path missing in consumers.

Ordinary unaffected tasks MUST NOT fill empty convergence forms. Review MUST use the parent's existing legal sources and blocker classes. Already authorized contract-preserving cleanup MUST NOT require a new product decision merely because it is refactoring. No new ledger, mandatory Agent role, scoring service, or approval workflow is required. After scoped closure, the task MUST stop unless its existing expansion trigger fires.

### CTR-CONV-008 — Keep activation and product operations separate

Basis: `DEC-CONV-004`.

The source maintainer MUST preserve accepted authority bytes and lifecycle boundaries while authoring this proposal. Distribution implementation MUST follow acceptance, update affected digests/version under existing release rules, and execute the existing integrity/route checks. Consumers MUST adopt an exact revision through their existing local process; upstream publication alone changes no consumer obligation. Source acceptance, distribution release, consumer adoption, and actual product cleanup MUST be reported separately. The standard MUST NOT supply product identity policy, authorize production mutation, weaken a support promise, or bypass an existing assurance gate.

## 10. Acceptance

The scenarios in [the authoring review](../rationale/model-convergence/SCENARIO_REVIEW.md) are design probes, not production Evidence or independent acceptance. The checks below become implementation/conformance requirements after acceptance.

### ACC-CONV-001 — Classification preserves legitimate differences

- Contracts: `CTR-CONV-001`, `CTR-CONV-002`.
- Method: review one historical-identity case, one configuration/store replacement case, and a legitimate multi-ID counterexample.
- Environment: source-authoring review; later distribution canary.
- Required evidence: exact candidate, input scenarios, classification, factual owner, bounded inventory, and recorded unknowns.
- Expected result: obsolete duplication is investigated; distinct entities and valid support remain; no universal ID shape or cardinality is invented.
- Failure condition: collapse distinct IDs, infer a successor from its name, equate service-specific `active` with universal eligibility, or report uninspected coverage as zero.

### ACC-CONV-002 — Subtraction and bounded compatibility

- Contracts: `CTR-CONV-003`, `CTR-CONV-004`.
- Method: compare migration/removal with a permanent fallback proposal and inspect one temporary bridge.
- Environment: exact change proposal and its known consumers.
- Required evidence: removed maintenance surfaces or containment boundary; bridge consumer, scope, owner, exit condition/date, and deletion proof plan.
- Expected result: unnecessary dual paths are removed; a justified bridge is bounded and creates no new retired objects.
- Failure condition: indefinite compatibility, unknown consumers treated as perpetual justification, silent expiry renewal, automatic destructive expiry, or unauthorized identity translation.

### ACC-CONV-003 — Retirement survives execution and recovery

- Contracts: `CTR-CONV-005`, `CTR-CONV-006`.
- Method: exercise current and retired entrypoints, plus applicable restart, retry/recovery, and migration rerun; reconcile active references and actual deployed versions.
- Environment: an authorized, explicitly named consumer test/deployment environment; not executed by this source-only proposal.
- Required evidence: executed commands/results at exact revisions, scoped reference counts, deployed readback where applicable, history-retention evidence, and controlled receipts for controlled effects.
- Expected result: new work succeeds; retired paths cannot execute or be recreated; historical evidence remains explainable.
- Failure condition: successful publish with an old writer still active, revival on restart, duplicate work, lost audit provenance, or unauthorized grant/identity transfer.

### ACC-CONV-004 — Completion claims reflect coverage

- Contracts: `CTR-CONV-006`.
- Method: challenge a completion record containing partial coverage, an outstanding bridge, and a source/deployment mismatch.
- Environment: exact completion record and cited observations.
- Required evidence: scope/environment/time, separate active and historical counts, explicit unknowns, and stage labels.
- Expected result: incomplete cases are described as staged or inconclusive rather than final convergence.
- Failure condition: grep-only proof, test-definition-as-execution, unknown converted to zero, or source-only cleanup reported as runtime completion.

### ACC-CONV-005 — Existing workflow hooks, no new bureaucracy

- Contracts: `CTR-CONV-007`.
- Method: inspect the eventual distribution delta and run affected/unaffected task canaries.
- Environment: exact accepted Spec and later distribution candidate.
- Required evidence: README/mode/template changes, five conditional review questions, canary decisions, and executed integrity/route results.
- Expected result: affected tasks examine retirement; unaffected tasks keep their short route; no dangling source-only link or new workflow/gate is introduced.
- Failure condition: essay-only delivery claimed as activated, mandatory empty forms, new approvals for authorized cleanup, unsupported blocker sources, or unrelated cleanup expansion.

### ACC-CONV-006 — No implicit activation or production authority

- Contracts: `CTR-CONV-008`.
- Method: inspect authoring diff, accepted-parent preservation, release/adoption records, and explicit operation scope.
- Environment: source PR, and later separately authorized distribution/consumer changes.
- Required evidence: exact diff and parent, lifecycle state, integrity/version evidence when distributed bytes change, local adoption coordinates where adoption is claimed.
- Expected result: a proposal changes no active distribution or product; later stages have their own actual evidence and existing authorization.
- Failure condition: mark author self-review as independent acceptance, alter accepted meaning in place, activate consumers by upstream merge, or treat the standard as a cleanup/credential mandate.

## 11. Alternatives and disposition

Permanent alias registries and fallback chains are rejected as the default destination; a justified, bounded migration bridge remains available. Blindly merging all IDs is rejected because distinct entities have distinct responsibilities. Immediate deletion of anything old is rejected because support, provenance, authorization, and recovery safety remain binding. A central migration platform or full census for every change is rejected as unnecessary process. A policy essay without existing workflow hooks is rejected as incomplete distribution delivery.

## 12. Migration, compatibility, and rollback

This authoring PR changes no distribution, release version, consumer, or production data. Existing `.agents/**`, `distribution/**`, and accepted Specs remain unchanged. After independent review and owner acceptance under existing rules, a separate bounded distribution change implements `CTR-CONV-007` and `CTR-CONV-008`; no new product decision is required for implementation already entailed by accepted Contracts.

Consumers then explicitly adopt the exact distribution revision. Apply the rule to the next affected task rather than rewriting historical records or scanning all repositories automatically. Keep only justified historical read compatibility; product migrations determine their own sequencing and controlled rollback. A rollback or containment event that re-enables a retired path reopens the convergence claim and cannot silently retain final-complete status.

## 13. Open questions

No unresolved normative placeholders are intentionally deferred. Owner acceptance and independent exact-candidate review are pending procedural steps, not completed results. Consumer-specific identity mappings, data-retention choices, and production operations remain outside this standard and must be resolved in their owning tasks.
