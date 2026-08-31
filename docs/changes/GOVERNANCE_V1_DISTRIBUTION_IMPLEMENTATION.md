# Governance V1 distribution implementation

```text
TASK_NAME = 规则 执行
TASK_TYPE = IMPLEMENTATION
IMPLEMENTATION_BASE_COMMIT = ba537eefae6761920290379c5ec147d2856bc2ae
AUTHORITY_ACTION = REUSE
PRIMARY_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_V1@ba537eefae6761920290379c5ec147d2856bc2ae
RELATED_AUTHORITY = AGENT_OPERATIONAL_LAYER_V1@f513e88b0b9ae05ca21ec4845fda4a43e4b4e420
PLAN_LEVEL = EXEC_PLAN
ASSURANCE_LEVEL = DURABLE
```

## Goal and gap

**Goal:** make the reusable `.agents` distribution route real work according to accepted Governance V1.

**Gap:** Governance V1 is active on `main`, but the distributed grammar, protocol, four modes, templates, and tests still implement the V0 mechanical/non-mechanical single route.

## Scope

In scope:

- shared grammar, active protocol, router, and four modes;
- Change Brief, ExecPlan, Execution Mandate, Controlled Runbook, Review, and Conformance templates;
- deterministic structured route validator and schema;
- four targeted failure regressions and three canaries;
- manifest and source-repository status documentation.

Out of scope:

- consumer adoption or consumer product changes;
- Forum/auth-service/workflow-admin/Agent Core implementation;
- Operational Layer implementation;
- GitHub App, WebAuthn, merge broker, WORM store, settings, or central registry;
- stable release/tag;
- runtime, production, permission, Credential, migration, or deployment writes;
- semantic acceptance by CI.

## Implementation choices

The distribution identifier remains `development-governance-v0` for current lock/vendor compatibility. Exact source commit and version remain adoption identity. Renaming the package would create unrelated consumer migration work.

`SPEC_FORMAT_V0.md` remains the formal governing-Spec syntax. V1 changes when a formal Spec is required, not the syntax for Specs that are required.

`SPEC_GOVERNANCE_V0.md` becomes a historical pointer; V1 is active.

## Phases

1. Update grammar, protocol, router, and modes.
2. Add compact artifacts, schema, and validator.
3. Regenerate manifest and run complete tests.
4. Independently review affected V1 Contracts.

## Required evidence

```text
- exact changed files and implementation Head
- manifest matches distributed bytes
- existing and new tests pass
- negative controls fail as expected
- no consumer/runtime/product/permission/Credential/deployment/settings change
- independent affected-Contract review
```

## Done When

```text
- distributed grammar and modes implement three axes
- four targeted regressions pass
- three canaries produce distinct routes
- manifest is current
- exact Head receives independent Review
- no out-of-scope effect occurred
```

## Expansion Trigger

Re-PREFLIGHT only if implementation proves that accepted V1 lacks a required long-lived decision, the current package identity cannot safely carry V1, Operational Layer meaning must change, or a consumer must change to make source tests meaningful.

Optional platform work, extra Agent roles, and unrelated repository protection are not triggers.

## Next real action

After independent review and merge, prepare an immutable distribution revision and let each consumer separately review and adopt that exact revision. Do not bulk-update consumers.
