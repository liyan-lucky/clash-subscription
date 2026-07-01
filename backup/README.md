# Backup Notes

This directory documents backup-related practices for this repository.

The `backup` branch should be kept as a recoverable baseline. Before major changes, update or recreate the backup branch from a known-good commit.

Recommended manual backup command:

```bash
git checkout main
git pull origin main
git branch -f backup main
git push origin backup --force-with-lease
```
