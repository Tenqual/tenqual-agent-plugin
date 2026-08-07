# Tenqual Agent Plugin

Tenqual connects AI agents to a global tender discovery service. The plugin uses Tenqual's hosted Model Context Protocol endpoint to search procurement notices, inspect qualified matches and available tender documents, and manage tender alerts.

## Connect

The hosted MCP endpoint is:

```text
https://api.tenqual.com/mcp
```

Compatible clients open Tenqual in the browser for OAuth sign-in, workspace selection, and scope approval. The plugin contains no API key or customer credential.

Tenqual also supports durable, scoped API keys for backend services, CRM integrations, and scripts. Human-controlled agent clients should use browser OAuth.

## Package formats

This repository intentionally supports three compatible package surfaces:

- `plugin.json` and `mcp.json` implement [Agent Plugins 1.0](https://agent-plugins.org/).
- `.codex-plugin/plugin.json` contains Codex marketplace metadata.
- `.claude-plugin/plugin.json` contains Claude plugin metadata.

All three connect to the same hosted MCP server. Authentication, authorization, quotas, and business rules are enforced by Tenqual Discovery rather than duplicated in the plugin.

## Capabilities

- Search worldwide tender notices by keyword, phrase, country, source, and date.
- Inspect source-backed tender metadata and available documents.
- Review Low, Medium, and High qualified matches.
- Estimate, create, update, pause, resume, and delete tender alerts.
- Inspect monthly evaluation usage.
- Configure scoped API credentials and webhooks with explicit write approval.

Tenqual does not submit bids or make procurement decisions. Original source notices remain authoritative.

## Development

Run the repository checks before publishing:

```bash
python3 scripts/validate_plugin.py
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

See [SETUP.md](SETUP.md) for client setup and [review/openai-test-cases.md](review/openai-test-cases.md) for the marketplace review plan.

## Support and policies

- Documentation: https://tenqual.com/docs/ai-agents
- Support: support@tenqual.com
- Privacy: https://tenqual.com/privacy
- Terms: https://tenqual.com/terms
