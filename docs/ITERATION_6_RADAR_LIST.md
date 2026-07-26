# Iteration 6 — Demand radar list

The demand radar interface now uses the complete deduplicated signal feed rather than a limited presentation sample.

- Complete event coverage: 22/22
- Matched company coverage: 14
- Validated action recommendation coverage: 22/22
- Traceable source coverage: 22/22
- Default ordering: action urgency first, then intent score descending within each urgency level
- Optional ordering: intent score strictly descending, then action urgency for equal scores
- Search coverage: company name, commonly used company short name, owner, signal title, and signal excerpt
- Search normalization: case-insensitive and whitespace-insensitive
- Supported interactions: unified search, source filter, sorting switch, and linked detail view

Search acceptance is complete at 5/5 cases, including company short names and owner names. The published showcase reports aggregate coverage only and does not expose production customer names or sensitive source records.

The list generation and verification step runs locally, requiring no model calls or external-search credits.
