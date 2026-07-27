# Iteration 6 — Key-person intelligence

Telegram text and voice transcripts can now feed one structured recognition layer for customer key-person information.

The system distinguishes the internal sales owner from the customer-side key person and extracts job title, department, normalized seniority, decision role, contact status, and confidence. Generic honorifics are not treated as management titles; uncertain cases remain unconfirmed and request at most one clarification.

The radar interface now supports key-person seniority filtering and shows key-person context separately from the internal owner. Processing and validation run locally with no external-search credits or model calls.
