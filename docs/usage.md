# Usage Guide

## Important Security Notice

This repository is public. Do not commit real subscription URLs, proxy passwords, API tokens, or private configuration files.

Recommended safe workflow:

1. Keep real subscription links locally.
2. Store only templates and sanitized examples in this repository.
3. Use placeholders such as `CHANGE_ME`, `example.com`, or `YOUR_SUBSCRIPTION_URL`.
4. Review every commit before pushing.

## Suggested Local Workflow

```bash
git clone https://github.com/liyan-lucky/clash-subscription.git
cd clash-subscription
```

Create or edit templates:

```bash
cp templates/config-template.yaml my-config.yaml
```

Before committing, make sure no private information is included:

```bash
git status
git diff
```

Commit safe changes only:

```bash
git add README.md docs/ rules/ templates/
git commit -m "Update Clash templates and rules"
git push origin main
```

## Recommended Branches

- `main`: stable public templates and documentation
- `backup`: backup branch for recovery
- feature branches: temporary work branches, for example `update-rules`
