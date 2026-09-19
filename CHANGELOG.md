# Changelog

## Unreleased

- No changes yet.

## 1.1.0 — 2026-09-19

- distribute the accepted `AGENT_MODEL_CONVERGENCE_V1` development obligation
  into the vendored grammar for the first time (REUSE implementation of its
  distribution Contracts; accepted Spec bytes unchanged):
  - `.agents/README.md` gains a self-contained model-convergence and
    retirement section: affected-work trigger, the same-responsibility
    duplication test, preserved distinct entities, RETAIN / RETIRE / MIGRATE /
    TEMPORARY_BRIDGE dispositions, subtraction-first preference, stable
    supported public facade versus temporary migration bridge, and retirement
    without historical-evidence deletion;
  - PREFLIGHT mode gains a conditional affected-work convergence probe with
    six bounded questions; unrelated tasks keep the short route with no
    global census, empty matrix, or new approval;
  - REVIEW mode gains a conditional convergence-exit review: new path usable,
    retired executable path excluded from normal/fallback/recovery routes,
    recovery non-revival, unknown coverage stays unknown, and retirement is
    not historical-evidence deletion;
  - Change Brief and Review Record templates gain conditional convergence
    fields that are skipped when `MODEL_CONVERGENCE_APPLICABLE = NO`;
- parallel or multi-Agent work remains optional; actual writes still follow
  the existing attributable-authorization and isolated-write-surface rules;
  no new ledger, mandatory Agent role, scoring service, approval workflow, or
  blocker class is introduced, and no proposed authority
  (`AGENT_RELEASE_RECOVERY_ASSURANCE_V1`, `AGENT_REPOSITORY_QUALITY_V1`,
  GitHub enforcement) or the non-normative evidence-led refactoring guide is
  activated;
- add distribution-tool regressions for vendored-surface self-containment
  (no source-only authority-path references) and convergence-surface
  presence; six distribution canary decisions recorded under
  `docs/rationale/model-convergence/DISTRIBUTION_CANARIES.md`;
- version surfaces 1.0.3 -> 1.1.0 (MINOR: backward-compatible additive
  guidance and template fields per `docs/releases/VERSIONING.md`); release
  doc added; manifest rebuilt.

## 1.0.3 — 2026-09-05

- extend the transition validator to raw, unnormalized whole-authority
  successor chains of any legal depth: a superseded record may backlink a
  successor that is itself superseded, provided every chain terminates at an
  accepted authority (cycles and proposed-chain terminations are rejected);
- accept raw historical superseded records that predate the current
  frontmatter schema and omit the `governed_by`/`supersedes` array fields
  (treated as empty); active proposed/accepted records still require
  well-formed arrays;
- keep every existing rejection unchanged: premature predecessor retirement,
  premature backlinks, nonexistent predecessors/successors, multiple
  successors, cycles, forked current authority, mutation of accepted
  normative fields, partial supersession, and reactivation of superseded
  authority;
- reject a superseded successor carrying a newly activated supersession edge;
- add the real three-generation consumer chain
  (`AGENT_REPO_KNOWLEDGE_GOVERNANCE_V1` -> `AGENT_DEVELOPMENT_GOVERNANCE_ADOPTION_V0`
  -> `AGENT_DEVELOPMENT_GOVERNANCE_ADOPTION_V1`) as a regression fixture;
- carry forward the v1.0.2 publication-remediation record; the v1.0.0,
  v1.0.1, and v1.0.2 tags remain immutable historical releases.

## 1.0.2 — 2026-09-03

- carry forward the v1.0.1 proposed-successor transition fix without changing
  validator or accepted Product Authority semantics;
- repair the stable-publication record after v1.0.1 was published without
  closing its required named-consumer release-note gate on the exact final Head;
- explicitly record that `mayf3/svc-workflow` PR #22 remains a separate Draft
  consumer adoption and is not modified, accepted, marked Ready, or merged by
  this upstream release;
- require PR #22 to re-vendor the exact reviewed v1.0.2 tag commit and rerun
  repository-local tests, independent audit, and Owner acceptance;
- retain the v1.0.0 and v1.0.1 tags as immutable historical releases; do not
  move, overwrite, or retroactively relabel either tag.

## 1.0.1 — 2026-09-03

- allow an accepted predecessor and a proposed whole-authority successor to
  coexist while the successor declares future replacement intent;
- keep the predecessor active and unbacklinked until authorized acceptance;
- preserve atomic accepted-successor lifecycle closure and reject premature
  predecessor retirement or backlink mutation;
- add transition-validator regression tests for proposal coexistence, premature
  transition, missing predecessor, and final atomic acceptance;
- clarify the adoption template and schema description without changing any
  accepted authority Spec bytes;
- retain v1.0.0 as an immutable historical release and require consumers blocked
  by this defect to adopt a newly reviewed exact v1.0.1 revision.

## 1.0.0 — 2026-09-01

- publish the first stable Governance V1 distribution as `v1.0.0`;

- implement independent Authority, Plan, and Assurance routing;
- separate Product Authority from one-operation Execution Mandates;
- add compact Change Brief, ExecPlan, Execution Mandate, and Controlled Runbook artifacts;
- formalize load-bearing `SPEC_GAP`, Evidence reviewability, live authority gaps, and candidate/Base movement;
- close Reviewer blocker classes and legal source namespaces;
- make affected-Contract review default while retaining full audits for controlled, release, and unbounded surfaces;
- add deterministic route-consistency validation without claiming semantic review;
- add four targeted regressions and three route-distinct canaries;
- keep consumer adoption exact-commit, local, and forward-only;
- do not implement Operational Layer, modify consumers, or create a governance platform.

## 0.2.0-draft.1

- add narrow legacy-authority retirement and cross-record transition validation;
- retain strict active IDs, accepted semantic immutability, and no partial supersession.

## 0.1.0-draft.1

- initial semantic grammar, Spec lifecycle, four Skill modes, templates, exact-source vendoring, manifest integrity, and qualified conformance.
