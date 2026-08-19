#!/usr/bin/env bash
set -euo pipefail

OWNER="${OWNER:-mayf3}"
REPOSITORY="${REPOSITORY:-agent-development-governance}"
VISIBILITY="${VISIBILITY:-public}"
REMOTE="${REMOTE:-origin}"
FEATURE_BRANCH="${FEATURE_BRANCH:-agent/bootstrap-development-governance-v0}"
BASE_BRANCH="${BASE_BRANCH:-main}"
FULL_NAME="${OWNER}/${REPOSITORY}"

case "${VISIBILITY}" in
  public|private|internal) ;;
  *) echo "VISIBILITY must be public, private, or internal" >&2; exit 2 ;;
esac

command -v gh >/dev/null 2>&1 || {
  echo "GitHub CLI 'gh' is required." >&2
  exit 2
}

gh auth status >/dev/null

ROOT="$(git rev-parse --show-toplevel)"
cd "${ROOT}"

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Working tree must be clean before publishing." >&2
  exit 2
fi

if ! git show-ref --verify --quiet "refs/heads/${BASE_BRANCH}"; then
  echo "Missing local base branch: ${BASE_BRANCH}" >&2
  exit 2
fi
if ! git show-ref --verify --quiet "refs/heads/${FEATURE_BRANCH}"; then
  echo "Missing local feature branch: ${FEATURE_BRANCH}" >&2
  exit 2
fi

if gh repo view "${FULL_NAME}" >/dev/null 2>&1; then
  echo "Repository already exists: ${FULL_NAME}"
else
  gh repo create "${FULL_NAME}" \
    "--${VISIBILITY}" \
    --description "Versioned development grammar and Spec governance for Agent-developed repositories" \
    --source . \
    --remote "${REMOTE}"
fi

if ! git remote get-url "${REMOTE}" >/dev/null 2>&1; then
  git remote add "${REMOTE}" "https://github.com/${FULL_NAME}.git"
fi

REMOTE_URL="$(git remote get-url "${REMOTE}")"
case "${REMOTE_URL}" in
  *"github.com/${FULL_NAME}.git"|*"github.com:${FULL_NAME}.git") ;;
  *)
    echo "Remote ${REMOTE} does not target ${FULL_NAME}: ${REMOTE_URL}" >&2
    exit 2
    ;;
esac

git push -u "${REMOTE}" "${BASE_BRANCH}"
git push -u "${REMOTE}" "${FEATURE_BRANCH}"

if gh pr view --repo "${FULL_NAME}" "${FEATURE_BRANCH}" >/dev/null 2>&1; then
  echo "A pull request already exists for ${FEATURE_BRANCH}."
else
  gh pr create \
    --repo "${FULL_NAME}" \
    --draft \
    --base "${BASE_BRANCH}" \
    --head "${FEATURE_BRANCH}" \
    --title "docs: establish Agent Development Governance V0" \
    --body-file docs/bootstrap/DRAFT_PR_BODY.md
fi

echo "Published ${FULL_NAME} with Draft PR from ${FEATURE_BRANCH} to ${BASE_BRANCH}."
