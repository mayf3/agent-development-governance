# Changelog

## Unreleased

- No changes yet.

## 1.0.1 — 2026-09-03

- allow an accepted predecessor and a proposed whole-authority successor to
  coexist while the successor declares future replacement intent;
- keep the predecessor active and unbacklinked until authorized acceptance;
- preserve atomic accepted-successor lifecycle closure and reject premature
  predecessor retirement or backlink mutation;
- add transition-validator regression tests for proposal coexistence, premature
  transition, missing predecessor, and final atomic acceptance;
- clarify the Spec format, active protocol, adoption template, and schema
  description without changing accepted Product Authority;
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
