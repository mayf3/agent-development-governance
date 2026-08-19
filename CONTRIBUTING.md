# Contributing

This repository publishes governance rules that other repositories may vendor as local authority. Changes therefore require more discipline than ordinary documentation edits.

## Before changing normative content

1. Read `AGENTS.md`, `.agents/README.md`, and `.agents/local/README.md`.
2. Run the Spec-governance Skill in `PREFLIGHT` mode.
3. Identify whether the work is `REUSE`, `AMEND`, `SUPERSEDE`, or `NEW`.
4. Do not mix a normative governance change with unrelated tooling or product work.

The bootstrap Spec is still `proposed`. Until it is independently reviewed and accepted, this repository is a candidate distribution rather than a stable authority release.

## Pull request boundaries

A normative governance PR should:

- state the exact authority and stable IDs it changes;
- preserve accepted Decision and Contract meaning under existing IDs;
- use new stable IDs for strictly additive accepted amendments;
- use a new Spec and whole-Spec supersession when existing meaning changes;
- include an independent semantic review bound to exact commits;
- leave product-specific rules in the consuming repository.

Tooling PRs must state whether they affect only distribution integrity or also change governance semantics. Passing tests does not substitute for semantic review.

## Validation

Run:

```bash
python3 tools/build_manifest.py
python3 tools/build_manifest.py --check
python3 -m unittest discover -s tests -v
python3 -m py_compile tools/*.py .agents/tools/*.py tests/*.py
git diff --check
```

After committing a candidate, exercise a real clean-checkout vendor round trip using the exact `HEAD` commit.

## Release discipline

- Draft versions use a prerelease suffix.
- Stable tags are immutable.
- A changed governance meaning receives a new release version.
- Release notes identify normative changes separately from tooling or editorial changes.
- A release is not stable until the bootstrap or superseding release authority is accepted by an authorized maintainer.

See `docs/releases/VERSIONING.md`.
