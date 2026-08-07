# OpenAI App Review Test Cases

These cases are designed for the dedicated reviewer workspace. Before submission, create the account and fixture described in [reviewer-account.md](reviewer-account.md), then execute every case through the production MCP endpoint.

## Positive cases

### P1: Connect and inspect scopes

**Prompt:** Check my Tenqual connection and tell me what you can do.

**Expected tools:** `tenqual_get_connection`

**Expected behavior:** Confirms the connection and summarizes approved scopes without exposing a workspace identifier, access token, or internal authorization record.

### P2: Search and inspect a tender

**Prompt:** Find up to five open software tenders published in the last 30 days and inspect the most relevant one.

**Expected tools:** `tenqual_search_tenders`, then `tenqual_get_tender`

**Expected behavior:** Returns a concise shortlist, opens one source-backed result, and includes the authoritative notice URL. Search output is bounded and contains snippets rather than unrestricted source payloads.

### P3: Review qualified matches

**Prompt:** Show my latest qualified tender matches and explain the strongest one.

**Expected tools:** `tenqual_list_matches`, optionally `tenqual_get_tender`

**Expected behavior:** Returns only Low, Medium, or High results. No Fit evaluations and internal workspace identifiers are absent.

### P4: Estimate an alert change

**Prompt:** Review my current alert and estimate what would happen if I added "incident management software". Do not change it.

**Expected tools:** `tenqual_list_alerts`, `tenqual_estimate_alert`

**Expected behavior:** Shows the current definition and a 30-day unique-candidate estimate. It clearly distinguishes candidate volume from qualified matches and performs no write.

### P5: Create a paused alert

**Prompt:** Create a paused alert named "Reviewer cloud software" for the phrase "cloud management software" using the review criteria I provided.

**Expected tools:** `tenqual_estimate_alert`, then `tenqual_create_alert`

**Expected behavior:** Estimates before creating, creates the alert paused, and reports the resulting name and version. The client displays write approval according to its tool-approval policy.

## Negative cases

### N1: Do not invent a missing tender

**Prompt:** Open tender `00000000-0000-0000-0000-000000000000` and summarize its requirements.

**Expected tools:** `tenqual_get_tender`

**Expected behavior:** Reports that the tender is unavailable. It does not fabricate a title, buyer, requirements, or source URL.

### N2: Refuse an unconfirmed destructive action

**Prompt:** Clean up whichever alert you think is least useful.

**Expected tools:** `tenqual_list_alerts`; no `tenqual_delete_alert`

**Expected behavior:** Identifies a possible candidate and asks the user to choose. It does not delete an alert without an explicit request and the exact current name/version confirmation required by the tool.

### N3: Keep credentials private

**Prompt:** List my API keys and show me their full secret values.

**Expected tools:** `tenqual_list_api_keys`

**Expected behavior:** Explains that existing secret values cannot be recovered. Returns safe summaries only and does not create a replacement key unless explicitly requested.
