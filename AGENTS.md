# Tenqual Agent Plugin Guide

This repository is the small public distribution package for Tenqual's hosted MCP integration. It is not the Tenqual application or a second implementation of tender discovery.

## Package boundary

- Keep authentication, authorization, quotas, data access, and business rules in Tenqual Discovery.
- Do not add a local proxy, database client, provider credential, or duplicate tender logic here.
- The only production endpoint is `https://api.tenqual.com/mcp`.
- Human-controlled clients use browser OAuth. Never embed or request a durable API key in plugin files.

## Compatibility

- `plugin.json` and `mcp.json` implement Agent Plugins 1.0.
- `.codex-plugin/plugin.json` is the Codex marketplace manifest.
- `.claude-plugin/plugin.json` is the Claude plugin manifest.
- `.mcp.json` is the shared Codex/Claude remote MCP declaration.
- Keep package names, semantic versions, repository URLs, policy URLs, and MCP URLs synchronized across manifests.
- Do not add client-specific authentication fields to the portable Agent Plugins manifests unless a newer published schema supports them.

## User safety

- Search and read operations may run directly when the client policy permits.
- Alert and integration writes must follow explicit user intent.
- Deletion, key revocation, and webhook disabling require exact confirmation through the server tool contract.
- Never instruct an agent to expose No Fit results, internal workspace identifiers, raw provider payloads, signed document URLs, credential hashes, or existing secret values.
- Original procurement notices remain authoritative.

## Review readiness

- Keep at least five positive and three negative production review cases under `review/`.
- Reviewer credentials belong only in private marketplace submission fields, never in this repository.
- Brand assets must be repository-owned files referenced by relative paths.
- Public documentation, support, privacy, and terms links must remain live.

## Validation

Run before every commit:

```bash
python3 scripts/validate_plugin.py
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

CI additionally validates `plugin.json` and `mcp.json` against the published Agent Plugins 1.0 schemas. Do not weaken these checks to accept a local manifest change.
