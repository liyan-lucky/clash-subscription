#!/usr/bin/env bash
set -euo pipefail

# Update the backup branch from the current main branch.
# Usage:
#   bash scripts/backup-branch.sh

REMOTE="${REMOTE:-origin}"
MAIN_BRANCH="${MAIN_BRANCH:-main}"
BACKUP_BRANCH="${BACKUP_BRANCH:-backup}"

git checkout "$MAIN_BRANCH"
git pull "$REMOTE" "$MAIN_BRANCH"
git branch -f "$BACKUP_BRANCH" "$MAIN_BRANCH"
git push "$REMOTE" "$BACKUP_BRANCH" --force-with-lease

echo "Backup branch updated: $BACKUP_BRANCH -> $MAIN_BRANCH"
