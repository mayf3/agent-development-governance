# Agent Development Governance

A versioned development grammar, Spec-governance protocol, and reusable Agent Skill for repositories where software is designed, implemented, reviewed, and operated across many Agent sessions.

The repository exists to make this chain explicit and auditable:

```text
what we observed
→ what we think it means
→ what we decided
→ what the system must guarantee
→ what was implemented
→ what the evidence actually verifies
```

It is not a central product authority. A consuming repository adopts an exact immutable revision, vendors the files into its own base branch, and remains the owner of its Product Direction, Architecture, Specs, acceptance actors, and code.

## Current status

```text
DISTRIBUTION_VERSION = 0.2.0-draft.1
BOOTSTRAP_SPEC_STATUS = accepted
ENFORCEMENT_LEVEL = manual_policy
SEMANTIC_SPEC_VERIFIER = not_implemented
SPEC_TRANSITION_VALIDATOR = implemented_for_cross_record_lifecycle_closure
DISTRIBUTION_INTEGRITY_TOOLS = implemented
READY_TO_TAG_STABLE_RELEASE = no
```

The bootstrap candidate has received independent semantic review and authorized acceptance preparation. It remains unmerged and must pass the independent final-head recheck before merge or a stable `v0.2.0` tag.

## What is frozen in the V0 candidate

- Six entity primitives: `Goal`, `State`, `Observation`, `Claim`, `Decision`, and `Contract`.
- One first-class relational primitive: `Evidence`.
- Two entity-primitive families: epistemic (`Observation`, `Claim`, `State`) and normative (`Goal`, `Decision`, `Contract`).
- `State` is a time-indexed projection, not raw truth.
- `Evidence` is an auditable relation from qualified Observations to a specific Claim, State assertion, or Contract at a pinned Spec revision; it is not merely a file, log, test definition, or screenshot.
- Spec authority lifecycle is separate from implementation progress, verification coverage, runtime state, and conformance.
- Non-mechanical implementation requires an accepted implementation-authorizing Spec already present in the implementation PR base.
- Accepted Decision and Contract meaning is immutable under the same stable ID.
- V0 forbids partial supersession.
- Grandfathered legacy governing-Spec IDs have a retirement-only atomic transition; new active legacy IDs remain forbidden.
- External authorities may be referenced at an exact revision, but one repository may not govern or supersede another repository.
- Review recommendations are bound to exact commits and do not themselves perform acceptance.
- Vendoring records preparation and acceptance as separate states; preparing bytes never fabricates acceptance.
- Conformance is a point-in-time relation over a Spec revision, implementation commit, environment, time, and evidence.
- Rejected or no-change investigations are persisted as Investigation Records rather than being added to governing Spec lifecycle.

## Repository layout

```text
AGENTS.md
.agents/
├── README.md
├── local/
│   └── README.md
├── protocol/
│   ├── SPEC_FORMAT_V0.md
│   └── SPEC_GOVERNANCE_V0.md
├── schemas/
├── skills/
│   └── spec-governance/
│       ├── SKILL.md
│       └── modes/
│           ├── PREFLIGHT.md
│           ├── AUTHOR.md
│           ├── REVIEW.md
│           └── COMPLIANCE.md
├── tools/
│   ├── validate_spec_transition.py
│   └── verify_governance.py
└── templates/
    ├── SPEC_TEMPLATE.md
    ├── GOVERNANCE_ADOPTION_SPEC_TEMPLATE.md
    ├── REVIEW_RECORD_TEMPLATE.md
    ├── CONFORMANCE_RECORD_TEMPLATE.md
    ├── INVESTIGATION_RECORD_TEMPLATE.md
    └── consumer/

docs/
├── adoption/
├── rationale/
├── releases/
└── specs/

distribution/
└── manifest.json

tools/
├── build_manifest.py
├── vendor.py
├── verify_vendor.py
└── publish_bootstrap.sh
```

## Minimum operating loop

```text
1. Discover governing authorities.
2. Classify the work as REUSE / AMEND / SUPERSEDE / NEW.
3. Treat uncertainty about “mechanical” as NON_MECHANICAL.
4. Do not implement non-mechanical behavior without an accepted,
   implementation-authorizing Spec in the base branch.
5. Author and independently review the docs-only Spec.
6. Bind acceptance to the exact reviewed and final accepted commits.
7. Implement against the pinned Spec revision.
8. Produce Contract-by-Contract conformance evidence.
9. Report drift; never rewrite an accepted Spec to make incorrect code look conforming.
```

## Consumer model

V0 uses **vendored, commit-pinned adoption** rather than a floating branch, Git submodule, or runtime fetch.

Why:

- every clone contains the actual governance text;
- Agents can read it without initializing a submodule;
- implementation PR base branches contain the governing content;
- update PRs show the exact governance diff;
- a later change in this repository cannot silently change another repository.

A consumer pins an exact source revision and uses a two-stage local adoption record:

```json
{
  "source_repository": "mayf3/agent-development-governance",
  "source_commit": "<40-hex commit>",
  "distribution": "development-governance-v0",
  "version": "0.2.0-draft.1",
  "adoption": {
    "status": "proposed | accepted"
  }
}
```

Preparing vendored bytes does not fabricate acceptance. The authorized local acceptance action is recorded separately before the accepted head is merged.

See [`docs/adoption/CONSUMER_REPOSITORY.md`](docs/adoption/CONSUMER_REPOSITORY.md).

## What this repository does not do in V0

- It does not own any consuming repository's product decisions.
- It does not provide a central Spec registry or database.
- It does not permit per-Contract or partial supersession.
- It does not automatically accept Specs.
- It does not claim that a Skill is an unbypassable merge gate.
- It does not perform semantic review in CI.
- It does not migrate historical documents in bulk.
- It does not treat tests passing as sufficient proof without qualified execution evidence.

## Bootstrap and release

The central bootstrap Spec is:

```text
docs/specs/AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0.md
```

Before the first stable release:

1. an independent reviewer reviews the exact candidate commit;
2. the repository owner explicitly accepts the exact final head;
3. any semantic delta after review triggers a new review;
4. the bootstrap Spec becomes `accepted` in a docs-only acceptance commit;
5. `VERSION` becomes `0.2.0` and the immutable `v0.2.0` release tag is created.

## Publishing the bootstrap repository

From an authenticated environment with GitHub CLI installed, the committed bootstrap can create or reuse the target repository, push both branches, and open the Draft PR:

```bash
tools/publish_bootstrap.sh
```

Defaults:

```text
TARGET = mayf3/agent-development-governance
VISIBILITY = public
BASE = main
HEAD = agent/bootstrap-development-governance-v0
```

Set `VISIBILITY=private` before running when the repository should not be public.

## License

MIT.
