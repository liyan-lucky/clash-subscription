# Security Policy

## Public Repository Warning

This repository is public. Never upload:

- Real Clash subscription URLs
- Proxy server passwords
- Access tokens
- Private keys
- Personal account information
- Internal server addresses that should remain private

## Before Pushing

Always check changes before committing:

```bash
git status
git diff
```

If sensitive data was committed accidentally, remove it immediately and rotate the exposed secret or subscription link.
