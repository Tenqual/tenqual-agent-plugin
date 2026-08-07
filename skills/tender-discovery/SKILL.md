---
name: tender-discovery
description: Use Tenqual to search global procurement notices, inspect qualified matches and available documents, and manage tender alerts safely.
---

# Tenqual Tender Discovery

Use Tenqual as a discovery system. Original procurement notices remain authoritative.

## Search and qualification

1. Start with `tenqual_search_tenders` for ad hoc discovery.
2. Use a few meaningful keywords or phrases and explicit country, source, publication, or deadline filters when the user provides them.
3. Inspect promising results with `tenqual_get_tender` before making a recommendation.
4. Explain why a result is relevant using title, description, metadata, and source evidence returned by Tenqual. Do not invent missing facts.
5. Use `tenqual_list_matches` for a workspace's persisted Low, Medium, and High matches. No Fit results are intentionally unavailable to customers.

## Alert management

1. Read the current alert and usage before proposing a change.
2. Use `tenqual_estimate_alert` to show expected 30-day candidate volume before creating or materially broadening an alert.
3. Distinguish deterministic candidate retrieval from Gemini qualification. An estimate is candidate volume, not guaranteed matches.
4. Draft or describe the exact proposed definition before a write when the user has not already specified it.
5. Use optimistic versions when updating alerts. If a version conflict occurs, reread the alert and ask the user how to reconcile it.
6. Never delete an alert, revoke a credential, or disable a webhook unless the user explicitly asks for that action.

## Documents and integrations

1. Check document status after a tender has qualified.
2. Prefer Tenqual's ready documents when available; otherwise direct the user to the authoritative source notice.
3. Treat signed document URLs as short-lived and sensitive.
4. Do not create credentials or send data to a webhook unless the user explicitly requests the external connection.
5. Never display credential hashes, internal workspace identifiers, storage paths, or raw provider payloads.

## Response quality

- Keep results source-backed and state when a field or document is unavailable.
- Prefer a ranked shortlist over a noisy keyword dump.
- Include the authoritative notice URL when recommending a tender.
- Keep qualification outcomes distinct: Low, Medium, and High are visible; No Fit is not.
