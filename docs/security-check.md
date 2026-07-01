# Security Check

This repository includes a basic GitHub Actions workflow that checks for obvious sensitive proxy/subscription patterns.

It is not a perfect secret scanner. Always manually review changes before pushing.

Checked examples include:

- `ss://`
- `vmess://`
- `vless://`
- `trojan://`
- URLs containing `token=`, `password=`, `passwd=`, `apikey=`, or `api_key=`

Some safe example files are excluded from the check to avoid false positives.
