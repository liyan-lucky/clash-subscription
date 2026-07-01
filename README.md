# Clash Subscription

A simple repository for storing and managing Clash subscription-related configuration, templates, rules, and notes.

## Overview

This repository is intended to organize Clash subscription resources in a clear and maintainable way.

Recommended uses:

- Store Clash configuration templates
- Keep subscription conversion notes
- Manage custom rule providers
- Track proxy rule changes
- Save backup and recovery instructions

## Repository Structure

```text
.
├── README.md
├── .gitignore
├── LICENSE
├── docs/
│   └── usage.md
├── rules/
│   └── README.md
├── templates/
│   └── config-template.yaml
└── subscriptions/
    └── .gitkeep
```

## Notes

Do not commit private subscription URLs, tokens, passwords, or any sensitive proxy information.

Use placeholders in public examples, for example:

```yaml
proxies:
  - name: example-node
    type: ss
    server: example.com
    port: 8388
    cipher: aes-256-gcm
    password: CHANGE_ME
```

## Quick Start

1. Put reusable configuration templates in `templates/`.
2. Put custom rule files or rule notes in `rules/`.
3. Put usage documents in `docs/`.
4. Keep real private subscription links outside this public repository.

## License

This project is licensed under the MIT License.