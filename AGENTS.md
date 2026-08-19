# Agent entrypoint

Before doing non-mechanical work in this repository:

1. read `.agents/README.md`;
2. read `.agents/local/README.md`;
3. read the governing authority under `docs/specs/`;
4. read `.agents/skills/spec-governance/SKILL.md` and only the selected mode file.

Hard rules:

- do not treat this bootstrap candidate as accepted merely because it exists;
- do not change accepted Decision or Contract meaning under the same stable ID;
- do not combine a normative Spec change with implementation of that changed behavior;
- report authority conflict or drift instead of silently choosing the newest-looking file;
- current V0 enforcement is a manual policy plus distribution-integrity checks, not a semantic CI merge gate.
