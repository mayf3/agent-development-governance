# Distribution versioning and release policy

The distribution is identified by three coordinates:

```text
distribution name + human-readable version + exact source commit
```

The exact commit is the machine identity used by consumers. The version is a compatibility and release-communication aid.

## Version classes

Use semantic-versioning intent:

```text
MAJOR  breaking grammar, protocol, format, or consumer-adoption change
MINOR  backward-compatible additive primitive guidance, protocol capability,
       template field, or tooling capability
PATCH  editorial correction, clarification with semantic delta NONE,
       or compatible integrity-tool fix
```

Before `1.0.0`, minor releases may still contain substantial governance evolution. Every release note must therefore classify the actual normative delta rather than relying on the version number alone.

Prerelease examples:

```text
0.1.0-draft.1
0.1.0-rc.1
```

## Release requirements

A stable release requires:

1. an accepted release-governing Spec or accepted bootstrap authority;
2. independent semantic review of the exact candidate commit;
3. authorized acceptance of the exact final head;
4. `distribution/manifest.json` current and deterministic;
5. unit and round-trip integrity tests passing;
6. a clean working tree;
7. `VERSION` and `CHANGELOG.md` updated;
8. an immutable annotated tag.

A tag is never moved. A correction creates a new version and tag.

## Consumer compatibility

An upstream release has no automatic effect on consumers. A consumer:

1. selects a new exact commit;
2. vendors it in a docs-only update PR;
3. reviews the normative and local-authority delta;
4. finalizes local adoption metadata;
5. merges the accepted update.

Rollback means reverting the complete consumer update commit, including the lock and all vendored bytes.

## Release claims

Do not claim:

```text
semantic verifier implemented
base-branch merge gate implemented
branch protection required
stable governance accepted
```

unless those properties are demonstrably active for the released revision and repository settings.
