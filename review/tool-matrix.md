# Tool Safety Matrix

The production MCP server is the source of truth for schemas and annotations. This matrix is the reviewer-facing summary for plugin version 0.1.0.

| Tool | Class | User-visible effect |
|---|---|---|
| `tenqual_get_connection` | Read | Confirms scopes without returning internal workspace IDs |
| `tenqual_search_tenders` | Read | Searches bounded source-backed tender data |
| `tenqual_get_tender` | Read | Returns one normalized notice and authoritative URL |
| `tenqual_list_matches` | Read | Returns customer-visible Low, Medium, and High matches |
| `tenqual_list_alerts` | Read | Lists active and paused alerts |
| `tenqual_get_usage` | Read | Shows the current UTC quota period |
| `tenqual_get_tender_documents` | Read | Shows document retrieval state and safe metadata |
| `tenqual_create_document_download` | Read-like | Creates a short-lived URL for an already authorized document |
| `tenqual_list_delivery_events` | Read | Reads a bounded, typed event feed |
| `tenqual_get_alert_draft` | Read | Reads one editable AI-generated draft |
| `tenqual_estimate_alert` | Read | Computes 30-day candidate volume without consuming quota |
| `tenqual_list_api_keys` | Read | Lists key summaries; existing secrets are never returned |
| `tenqual_list_webhooks` | Read | Lists safe webhook summaries and health |
| `tenqual_draft_alert` | Draft and external read | Optionally reads a company website and creates an inactive draft for human review |
| `tenqual_create_alert` | Write | Creates an alert, paused unless explicitly enabled |
| `tenqual_update_alert` | Write | Replaces a definition using optimistic version control |
| `tenqual_delete_alert` | Destructive | Soft-deletes after exact name and version confirmation |
| `tenqual_create_api_key` | Credential write | Returns a new secret once after explicit confirmation |
| `tenqual_revoke_api_key` | Destructive | Immediately revokes an exact named key |
| `tenqual_create_webhook` | External write | Registers a validated public HTTPS endpoint |
| `tenqual_disable_webhook` | Destructive | Immediately disables an exact named endpoint |
| `tenqual_set_alert_integration_delivery` | Write | Changes API-event and webhook delivery for one alert |

Tool responses use explicit output schemas. Arbitrary provider payloads, database records, storage paths, hashes, and internal workspace identifiers are excluded from marketplace-facing output.
