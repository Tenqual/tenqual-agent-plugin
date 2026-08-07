# Reviewer Account Fixture

The marketplace reviewer account is intentionally not stored in this repository.

## Required fixture

- A dedicated Firebase user whose email is reserved for marketplace review.
- A dedicated workspace named `Tenqual Marketplace Review`.
- No MFA, email OTP, SMS OTP, or invitation step after the reviewer receives the credentials.
- One paused alert named `Marketplace review alert` with ordinary software-related keywords and all four qualification criteria populated.
- At least three current Low, Medium, or High matches visible to the workspace.
- At least one matched tender with a ready document and one that falls back to the authoritative source link.
- Free or complimentary entitlement sufficient to run all review cases without a payment card.
- OAuth consent enabled for the requested MCP scopes.

## Submission handling

Provide the email and password only in the marketplace's private reviewer credential fields. Never commit them, place them in an issue, or include them in screenshots. Verify the credentials in a fresh private browser session immediately before submission.

After approval, rotate the password and retain or remove the account according to the marketplace's ongoing-review requirements.
