## Summary

Establish the initial candidate for a reusable Agent Development Governance distribution.

This change creates a repository-level development grammar and Spec-governance foundation that other repositories may adopt at an exact commit without surrendering local product authority.

## What is included

- six entity primitives split into epistemic and normative families, plus first-class relational primitive `Evidence`;
- time-indexed State, qualified Claims, stable `EVD-*` relations, and executed-result Observation rules;
- Product Direction / Architecture / Spec authority precedence;
- exact external-authority references and no cross-repository supersession;
- accepted-meaning immutability, strictly additive amendment seam, and whole-Spec supersession;
- separate Spec lifecycle, implementation progress, verification coverage, and conformance;
- Program versus implementation authority;
- PREFLIGHT / AUTHOR / REVIEW / COMPLIANCE mode files;
- commit-bound review and authorized acceptance;
- Investigation Records for rejected/no-change/reuse outcomes;
- vendored exact-commit consumer adoption with a two-stage proposed/accepted lock;
- deterministic distribution manifest, local integrity verifier, source-checkout validation, and tamper-safe update behavior;
- consumer, Spec, review, conformance, and investigation templates;
- release and adoption guidance.

## Authority boundary

```text
CENTRAL_PRODUCT_AUTHORITY_OVER_CONSUMERS = NONE
CONSUMER_ADOPTION = explicit + local + exact-commit + reviewed
UPSTREAM_AUTO_UPDATE = NO
```

The central repository publishes a versioned distribution. Each consumer remains the owner of its Product Direction, Architecture, Specs, acceptance actors, code, and runtime.

## Bootstrap exception

This is the one-time initial repository creation. The proposed bootstrap Spec and its bounded foundational implementation coexist because no accepted authority could pre-exist the repository.

```text
BOOTSTRAP_EXCEPTION = INITIAL_REPOSITORY_CREATION_ONLY
REUSABLE_AFTER_ACCEPTANCE = NO
```

The candidate remains proposed and must not be tagged stable until independently reviewed and explicitly accepted by an authorized maintainer.

## Validation

```text
DISTRIBUTION_MANIFEST = CURRENT
UNIT_TESTS = 11 PASS
PYTHON_COMPILE = PASS
MARKDOWN_LOCAL_LINKS = PASS
JSON_PARSE = PASS
GIT_DIFF_CHECK = PASS
SEMANTIC_REVIEW = REQUIRED
```

## Deliberately not implemented

- semantic Spec review in CI;
- a complete deterministic Spec parser;
- an unbypassable base-branch merge gate;
- branch protection configuration;
- central Spec registry or database;
- partial or per-Contract supersession;
- automatic consumer updates;
- bulk history migration.

## Requested review

Review the exact bootstrap commit and return:

```text
DEVELOPMENT_GOVERNANCE_BOOTSTRAP_REVIEW = ACCEPT | REVISE
READY_TO_MARK_ACCEPTED = YES | NO
REVIEWED_BASE_COMMIT = <sha>
REVIEWED_SPEC_COMMIT = <sha>
REVIEWER_ID = <identity>
```

Any semantic delta after that review requires a new review. The final accepted head must be independently rechecked before merge and stable release.
