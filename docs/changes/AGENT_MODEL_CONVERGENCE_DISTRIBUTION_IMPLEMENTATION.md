# Model Convergence distribution implementation

```text
TASK_NAME = AGENT_MODEL_CONVERGENCE_DISTRIBUTION_IMPLEMENTATION_V1
TASK_TYPE = IMPLEMENTATION
IMPLEMENTATION_BASE_COMMIT = f5456f684acb1ae8a470094f07738e0bc7ecaf3b
AUTHORITY_ACTION = REUSE
PRIMARY_AUTHORITY = AGENT_MODEL_CONVERGENCE_V1@f5456f684acb1ae8a470094f07738e0bc7ecaf3b (accepted, implementation_authority: contracts)
RELATED_AUTHORITIES = AGENT_DEVELOPMENT_GOVERNANCE_V1@f5456f684acb1ae8a470094f07738e0bc7ecaf3b, AGENT_OPERATIONAL_LAYER_V1@f5456f684acb1ae8a470094f07738e0bc7ecaf3b
PLAN_LEVEL = BRIEF
ASSURANCE_LEVEL = DURABLE
ROUTE_STAGE = IMPLEMENTATION
AUTHORITY_ACCEPTED_IN_BASE = YES
```

## Goal and gap

**Goal:** make the accepted `AGENT_MODEL_CONVERGENCE_V1` obligation real in
the active `development-governance-v0` distribution as an independently
reviewable release candidate.

**Gap:** the Spec is accepted on `main`, but the vendored grammar, modes,
and templates contain no convergence guidance; consumers cannot apply the
obligation from the distribution alone.

## Scope

In scope: `.agents/README.md`, PREFLIGHT mode, REVIEW mode, Change Brief and
Review Record templates, version/release metadata, manifest, release and
implementation/canary records, distribution-tool tests.

Out of scope: accepted Spec bytes, protocol documents, schemas, validators,
consumer repositories, product code, runtime/production state, tag and
GitHub Release publication, consumer adoption (next Goal), and activation of
any proposed authority or of the non-normative evidence-led refactoring
guide.

## Implementation choices

- Conditional, bounded placement inside the existing workflow (CTR-CONV-007):
  the grammar carries the self-contained rule, PREFLIGHT the affected-work
  probe, REVIEW the exit-evidence check, and the two templates conditional
  fields skipped when `MODEL_CONVERGENCE_APPLICABLE = NO`.
- The vendored surface stays self-contained: rules are stated inline, and a
  distribution-tool regression rejects references to source-only authority
  paths (`docs/specs/AGENT_*`, `docs/guides/`) from distributed files.
- Stable supported public facade and temporary migration bridge are kept
  distinct so that subtraction-first never means deleting supported
  compatibility.
- Parallel or multi-Agent work stays optional; all writes keep the existing
  attributable-authorization and isolated-write-surface rules.
- Version 1.0.3 -> 1.1.0 (MINOR per `docs/releases/VERSIONING.md`: additive
  guidance and template fields; first normative obligation activation, so
  PATCH is unlawful; nothing breaks, so MAJOR is unwarranted).

## Required evidence

```text
- exact changed files and candidate Head
- manifest matches distributed bytes (build_manifest.py --check)
- full unittest suite passes (distribution tools, governance routing,
  spec transitions), including the two new regressions
- six canary decisions recorded (DISTRIBUTION_CANARIES.md)
- vendor round-trip into a temporary consumer: dry-run, apply,
  verify_governance in proposed and accepted-lock forms
- independent exact-Head review of the Draft PR
```

## Done When

```text
- convergence guidance distributed and self-contained
- version surfaces coherent at 1.1.0 and manifest current
- full checks green; canaries A-F decided as specified
- Draft PR created; exact final Head independently reviewed with ACCEPT
- no consumer/product/production mutation; stop before merge/tag/publish
```

## Expansion Trigger

Re-PREFLIGHT only if implementation proves the accepted Spec lacks a required
distribution decision, a consumer must change to keep source tests
meaningful, or the distribution identity cannot carry the addition. Optional
tooling, extra validation platforms, and proposed-authority work are not
triggers.
