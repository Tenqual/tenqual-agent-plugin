# Setup

## Browser OAuth

Add `https://api.tenqual.com/mcp` as a remote MCP server in a compatible client. The client should open Tenqual in a browser, where the user:

1. Signs in with the normal Tenqual account.
2. Selects a workspace.
3. Reviews and approves the requested scopes.
4. Returns to the client after authorization.

The resulting access token is short-lived, workspace-bound, scope-bound, revocable, and valid for the Tenqual MCP resource.

## Codex

Install the published Tenqual plugin when it becomes available in the Codex plugin directory. During development, use this repository as a local plugin source. Codex reads `.codex-plugin/plugin.json` and `.mcp.json`.

## Claude

Install the published Tenqual plugin when it becomes available in the Claude plugin directory. During development, use this repository as a local plugin source. Claude reads `.claude-plugin/plugin.json` and `.mcp.json`; use `/mcp` to complete browser authentication if prompted.

## Other clients

Clients implementing the Agent Plugins 1.0 open standard can read `plugin.json` and `mcp.json`. Clients that only support raw MCP configuration can connect directly to the hosted endpoint.

## Machine integrations

Do not use human OAuth tokens for unattended CRM, webhook, or backend integrations. Create a scoped API key in Tenqual under **Integrations** and store it in the external system's secret store.
