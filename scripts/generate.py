#!/usr/bin/env python3
"""Generate a sanitized Clash-style configuration from private environment sources.

This script is intentionally designed not to include any public node source.
Put your own lawful source values in environment variables and keep them out of Git.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml", file=sys.stderr)
    raise

CONFIG_FILE = Path("config/example-sources.yml")


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def decode_source(raw: str) -> str:
    text = raw.strip()
    if not text:
        return ""
    try:
        decoded = base64.b64decode(text + "=" * (-len(text) % 4), validate=False)
        if decoded:
            guess = decoded.decode("utf-8", errors="ignore")
            if any(mark in guess for mark in ["proxies:", "proxy-groups:", "rules:"]):
                return guess
    except Exception:
        pass
    return text


def normalize_name(name: str, index: int) -> str:
    name = re.sub(r"\s+", " ", str(name or "")).strip()
    return name or f"node-{index:03d}"


def node_key(node: dict[str, Any]) -> str:
    basis = {
        "type": node.get("type"),
        "server": node.get("server"),
        "port": node.get("port"),
        "cipher": node.get("cipher"),
        "uuid": node.get("uuid"),
    }
    return hashlib.sha256(json.dumps(basis, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def load_nodes_from_text(text: str) -> list[dict[str, Any]]:
    data = yaml.safe_load(text) or {}
    if isinstance(data, dict) and isinstance(data.get("proxies"), list):
        return [x for x in data["proxies"] if isinstance(x, dict)]
    return []


def build_config(nodes: list[dict[str, Any]]) -> dict[str, Any]:
    clean_nodes = []
    seen = set()
    for index, node in enumerate(nodes, start=1):
        key = node_key(node)
        if key in seen:
            continue
        seen.add(key)
        item = dict(node)
        item["name"] = normalize_name(item.get("name", ""), len(clean_nodes) + 1)
        clean_nodes.append(item)

    names = [n["name"] for n in clean_nodes]
    return {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "proxies": clean_nodes,
        "proxy-groups": [
            {"name": "PROXY", "type": "select", "proxies": names + ["DIRECT"]},
            {"name": "AUTO", "type": "url-test", "proxies": names, "url": "http://www.gstatic.com/generate_204", "interval": 300},
        ],
        "rules": [
            "DOMAIN-SUFFIX,github.com,PROXY",
            "DOMAIN-SUFFIX,google.com,PROXY",
            "GEOIP,CN,DIRECT",
            "MATCH,PROXY",
        ],
    }


def main() -> int:
    cfg = read_yaml(CONFIG_FILE)
    nodes: list[dict[str, Any]] = []

    for source in cfg.get("sources", []):
        if not source.get("enabled", False):
            continue
        env_name = source.get("env")
        if not env_name:
            continue
        raw = os.environ.get(env_name, "")
        text = decode_source(raw)
        if text:
            nodes.extend(load_nodes_from_text(text))

    out_file = Path(cfg.get("output_file", "subscriptions/generated.yml"))
    meta_file = Path(cfg.get("metadata_file", "subscriptions/generated-meta.json"))
    out_file.parent.mkdir(parents=True, exist_ok=True)
    meta_file.parent.mkdir(parents=True, exist_ok=True)

    result = build_config(nodes)
    out_file.write_text(yaml.safe_dump(result, allow_unicode=True, sort_keys=False), encoding="utf-8")

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "node_count": len(result.get("proxies", [])),
        "sources_enabled": [s.get("name") for s in cfg.get("sources", []) if s.get("enabled")],
    }
    meta_file.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated {out_file} with {meta['node_count']} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
