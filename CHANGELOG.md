# Changelog

## 0.2.0-draft.1

Backward-compatible governance capability:

- permit an already-existing accepted legacy governing-Spec ID in a narrow, strict-ID-disjoint class to become schema-valid only in its superseded historical state;
- allow strict successors to reference exact legacy whole-authority IDs solely for atomic retirement;
- keep proposed/accepted IDs, `governed_by`, external authority IDs, and successors on strict `_V<number>` identifiers;
- add a distributed cross-record transition validator and positive/negative fixtures for existence, whole-authority closure, backlinks, and active-legacy-set monotonicity;
- retain the prohibition on new legacy Specs, accepted semantic mutation, and partial supersession.

## 0.1.0-draft.1

Initial bootstrap candidate:

- six entity primitives split into epistemic and normative families, plus first-class relational primitive `Evidence`;
- authority precedence, local adoption, cross-repository reference boundary, and whole-Spec supersession;
- immutable accepted Decision and Contract meaning;
- separate Spec lifecycle, implementation progress, verification coverage, and qualified conformance;
- PREFLIGHT, AUTHOR, REVIEW, and COMPLIANCE Skill modes;
- Spec, review, conformance, investigation, and consumer templates;
- deterministic distribution manifest, source-commit-verified vendoring, two-stage adoption metadata, tamper-safe updates, and a vendored local-byte verifier;
- no claim of semantic CI or unbypassable merge gate.
