# Backup Branch Guide

This repository uses a `backup` branch as a recovery baseline.

## Manual Update

Run locally:

```bash
git checkout main
git pull origin main
git branch -f backup main
git push origin backup --force-with-lease
```

Or use the included script:

```bash
bash scripts/backup-branch.sh
```

## When to Update Backup

Update the backup branch before large changes, such as:

- Rewriting templates
- Changing workflow files
- Adding many rules
- Refactoring repository structure
