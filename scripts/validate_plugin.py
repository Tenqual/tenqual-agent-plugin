#!/usr/bin/env python3
"""Validate Tenqual's portable and client-specific plugin package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MCP_URL = "https://api.tenqual.com/mcp"
SECRET_PATTERNS = (
    re.compile(r"\b(?:sk|rk|tq_live)_[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"Bearer\s+[A-Za-z0-9._~-]{16,}", re.IGNORECASE),
)


def load_json(relative_path: str) -> dict[str, Any]:
    path = ROOT / relative_path
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise AssertionError(f"{relative_path}: invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise AssertionError(f"{relative_path}: root must be an object")
    return value


def require_file(relative_path: str) -> None:
    path = ROOT / relative_path
    if not path.is_file() or path.stat().st_size == 0:
        raise AssertionError(f"{relative_path}: missing or empty")


def validate_portable_manifests() -> None:
    plugin = load_json("plugin.json")
    expected_plugin_keys = {
        "$schema",
        "name",
        "version",
        "description",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
    }
    if set(plugin) != expected_plugin_keys:
        raise AssertionError("plugin.json: unexpected or missing top-level fields")
    if plugin["$schema"] != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise AssertionError("plugin.json: unsupported Agent Plugins schema")
    if plugin["name"] != "tenqual-agent-plugin":
        raise AssertionError("plugin.json: package name changed")

    mcp = load_json("mcp.json")
    expected_mcp = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
        "mcpServers": {
            "tenqual": {
                "type": "streamable-http",
                "url": MCP_URL,
            }
        },
    }
    if mcp != expected_mcp:
        raise AssertionError("mcp.json: expected one credential-free Tenqual server")


def validate_client_manifests() -> None:
    codex = load_json(".codex-plugin/plugin.json")
    claude = load_json(".claude-plugin/plugin.json")
    client_mcp = load_json(".mcp.json")

    for label, manifest in (("Codex", codex), ("Claude", claude)):
        if manifest.get("name") != "tenqual-agent-plugin":
            raise AssertionError(f"{label}: package name changed")
        if manifest.get("version") != "0.1.0":
            raise AssertionError(f"{label}: expected version 0.1.0")
        if manifest.get("mcpServers") != "./.mcp.json":
            raise AssertionError(f"{label}: must use the shared MCP config")

    server = client_mcp.get("mcpServers", {}).get("tenqual", {})
    if server != {"type": "http", "url": MCP_URL}:
        raise AssertionError(".mcp.json: expected one credential-free Tenqual server")

    interface = codex.get("interface", {})
    for field in (
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "websiteURL",
        "privacyPolicyURL",
        "termsOfServiceURL",
    ):
        if not interface.get(field):
            raise AssertionError(f"Codex: missing interface.{field}")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        raise AssertionError("Codex: defaultPrompt must contain one to three prompts")
    if any(not isinstance(prompt, str) or len(prompt) > 128 for prompt in prompts):
        raise AssertionError("Codex: invalid default prompt")
    for asset_field in ("composerIcon", "logo"):
        asset = interface.get(asset_field)
        if not isinstance(asset, str) or not asset.startswith("./assets/"):
            raise AssertionError(f"Codex: invalid {asset_field}")
        require_file(asset.removeprefix("./"))


def validate_skill_and_review() -> None:
    skill_path = ROOT / "skills/tender-discovery/SKILL.md"
    skill = skill_path.read_text(encoding="utf-8")
    if not skill.startswith("---\nname: tender-discovery\n"):
        raise AssertionError("skill: missing valid frontmatter")
    if "tenqual_list_qualified_matches" in skill:
        raise AssertionError("skill: references a retired tool name")

    cases = (ROOT / "review/openai-test-cases.md").read_text(encoding="utf-8")
    if len(re.findall(r"^### P\d+:", cases, flags=re.MULTILINE)) < 5:
        raise AssertionError("review: at least five positive cases are required")
    if len(re.findall(r"^### N\d+:", cases, flags=re.MULTILINE)) < 3:
        raise AssertionError("review: at least three negative cases are required")


def validate_repository_hygiene() -> None:
    required = (
        "AGENTS.md",
        "README.md",
        "SETUP.md",
        "SECURITY.md",
        "LICENSE",
        "CHANGELOG.md",
        "review/reviewer-account.md",
        "review/tool-matrix.md",
    )
    for path in required:
        require_file(path)

    unresolved_placeholder = "[" + "TODO:"
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if unresolved_placeholder in text:
            raise AssertionError(f"{path.relative_to(ROOT)}: unresolved placeholder")
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            raise AssertionError(f"{path.relative_to(ROOT)}: possible secret")


def main() -> int:
    checks = (
        validate_portable_manifests,
        validate_client_manifests,
        validate_skill_and_review,
        validate_repository_hygiene,
    )
    try:
        for check in checks:
            check()
    except AssertionError as error:
        print(f"plugin validation failed: {error}", file=sys.stderr)
        return 1
    print("plugin validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
