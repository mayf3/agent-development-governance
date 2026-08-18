# Adopting the governance in a consumer repository

V0 adoption is a **vendored, exact-commit dependency**. The consuming repository owns the adoption decision and keeps the imported files in its own base branch.

---

## 1. Why vendoring is the V0 default

A shared grammar is useful only when every Agent can reliably read the exact rules that govern the current code base.

Vendoring provides:

- exact bytes in every clone;
- ordinary Git review of governance updates;
- no submodule initialization dependency;
- no floating `main` or `latest` semantics;
- an accepted governance revision already present in implementation bases;
- local rollback by reverting the adoption commit.

The central repository publishes content. It does not remotely mutate consumer authority.

---

## 2. Required local files

After adoption, the consumer contains:

```text
AGENTS.md                              local thin entrypoint
.agents/README.md                      vendored shared grammar
.agents/protocol/                      vendored protocol and format
.agents/skills/spec-governance/        vendored Skill
.agents/schemas/                       vendored schemas
.agents/templates/                     vendored author/review records
.agents/tools/verify_governance.py     vendored byte/lock verifier
.agents/local/README.md                local authority and extensions
.agents/governance.lock.json           exact source commit and file digests
docs/specs/README.md                   local Spec index
```

The update tool overwrites only paths declared in the distribution manifest. It does not overwrite `.agents/local/README.md`, `AGENTS.md`, or the local Spec index when they already exist.

---

## 3. Choose an immutable source revision

Do not adopt:

```text
main
master
latest
an unqualified release page
```

Use an exact 40-hex commit. A release tag may help humans select a version, but the lock records the resolved commit.

Before the first stable release, draft commits are suitable only for pilots and must be identified as draft.

---

## 4. Prepare a proposed vendor snapshot

From a **clean checkout of this governance repository at the selected commit**:

```bash
SOURCE_COMMIT="$(git rev-parse HEAD)"

python3 tools/vendor.py \
  --target /path/to/consumer \
  --source-commit "$SOURCE_COMMIT" \
  --prepared-by <adoption-author>
```

Dry-run is the default. It lists files that would be created or replaced. The tool rejects a declared source commit that is not the current checkout `HEAD`, rejects dirty distributed source files, and refuses to overwrite an existing vendored snapshot that no longer matches its lock unless an explicit recovery override is supplied.

Apply only after inspecting the plan:

```bash
python3 tools/vendor.py \
  --target /path/to/consumer \
  --source-commit "$SOURCE_COMMIT" \
  --prepared-by <adoption-author> \
  --apply
```

This creates a **proposed** `.agents/governance.lock.json` with:

- distribution and version;
- source repository and exact commit;
- distribution manifest digest;
- preparation actor and time;
- `adoption.status = proposed`;
- `accepted_by = null` and `accepted_at = null`;
- per-file path, size, and SHA-256.

Preparing files is not acceptance. The tool deliberately does not invent acceptance metadata during PR authoring.

---

## 5. Define local authority

Edit `.agents/local/README.md` to identify:

- repository name and designated authority branch;
- Product Direction authority;
- Architecture or invariant authorities;
- default precedence;
- Spec acceptance actors;
- mechanical-exemption reviewers;
- emergency authorization actors;
- investigation and conformance persistence locations.

The imported grammar may be stricter than current practice. Local extensions may refine it, but a local file must not silently weaken the pinned distribution. A deliberate change to the governance rules is an adoption/update decision.

---

## 6. Create a docs-only adoption PR

The adoption PR contains only governance files and local authority declarations. It does not include product behavior implementation.

A repository that wants a durable adoption authority may start from `.agents/templates/GOVERNANCE_ADOPTION_SPEC_TEMPLATE.md`. The one-time adoption bootstrap does not authorize unrelated product implementation.

Recommended PR record:

```text
GOVERNANCE_DISTRIBUTION = development-governance-v0
SOURCE_REPOSITORY = mayf3/agent-development-governance
SOURCE_COMMIT = <sha>
MANIFEST_SHA256 = <sha256>
ADOPTION_MODE = vendored
LOCAL_AUTHORITY_DEFINED = YES
PRODUCT_CODE_CHANGED = NO
```

An independent reviewer checks:

- source commit and lock integrity;
- local precedence and acceptance actors;
- whether existing higher-level Product Direction is preserved;
- whether imported rules conflict with unavoidable repository constraints;
- whether the repository is honestly labeling enforcement as manual or deterministic.

An authorized local maintainer may then perform the acceptance action. Before merge, regenerate the same snapshot with acceptance metadata, preserving the original preparation fields from the proposed lock:

```bash
python3 tools/vendor.py \
  --target /path/to/consumer \
  --source-commit "$SOURCE_COMMIT" \
  --prepared-by <original-adoption-author> \
  --prepared-at <original-prepared-at> \
  --adoption-status accepted \
  --accepted-by <authorized-maintainer> \
  --apply
```

The independent reviewer rechecks the final head and confirms that the only post-review governance delta is the authorized acceptance transition or other explicitly reviewed change. The adoption becomes active only after that accepted head is merged into the repository authority branch.

---

## 7. Begin forward-only use

After adoption is in the base branch:

- use PREFLIGHT for the next non-mechanical change;
- do not bulk rewrite historical docs;
- reconcile old artifacts only when they become governing or conflict with new work;
- persist important no-change/rejected investigations;
- pilot two or three real Spec cycles before adding broad CI gates.

---

## 8. Verify vendored integrity

Run the verifier that is itself vendored into the consumer:

```bash
python3 .agents/tools/verify_governance.py --target .
```

On an authority branch where adoption must already be active, require accepted metadata as well:

```bash
python3 .agents/tools/verify_governance.py --target . --require-accepted
```

The tool checks local files and adoption metadata against `.agents/governance.lock.json`.

It does not prove:

- semantic correctness;
- Spec acceptance;
- Contract completeness;
- conformance of product code;
- branch protection.

---

## 9. Update governance

An update is another explicit docs-only adoption PR.

1. select a new exact source commit;
2. read release notes and normative changes;
3. run `vendor.py` in dry-run mode;
4. inspect the full imported diff;
5. update local extensions when needed;
6. independently review the governance delta;
7. accept and merge locally.

No upstream release changes a consumer until this process completes.

---

## 10. Rollback

Rollback is a normal Git revert of the consumer adoption/update commit.

Do not edit vendored files manually to approximate an older version. Restore the previous lock and exact imported bytes together.

---

## 11. External authority references

A consumer Spec may reference an authority in another repository only with:

```yaml
external_authorities:
  - repository: owner/repository
    authority_id: STABLE_AUTHORITY_V1
    revision: <40-hex-commit>
    relation: depends_on
```

The local Spec may freeze its dependency expectation. It may not supersede or redefine the remote authority.

---

## 12. Enforcement maturity

Adoption does not by itself create an unbypassable merge gate.

Represent actual state explicitly:

```text
ENFORCEMENT_LEVEL = MANUAL_POLICY
DISTRIBUTION_INTEGRITY_CHECK = AVAILABLE
SPEC_SYNTAX_GATE = OPTIONAL / NOT_IMPLEMENTED
BASE_BRANCH_GATE = OPTIONAL / NOT_IMPLEMENTED
REQUIRED_BRANCH_PROTECTION = repository-specific
```

Only claim a deterministic merge gate after the required checks and branch protection are genuinely active.
