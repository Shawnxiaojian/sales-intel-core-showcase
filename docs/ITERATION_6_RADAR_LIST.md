# Iteration 6 — Demand radar list

The demand radar interface now uses the complete deduplicated signal feed rather than a limited presentation sample.

- Complete event coverage: 22/22
- Matched company coverage: 14
- Default ordering: action urgency, then intent score
- Optional ordering: intent score strictly descending
- Search coverage: company, company short name, owner, title, and excerpt
- Owner filtering: complete, with per-owner counts and reset support
- Owner inheritance: matched signals inherit the customer owner from supported Excel owner columns
- Missing owner policy: display “待分配”; never infer an owner from the customer contact or fabricate ownership

The current source workbooks contain no owner column, so all 22 signals truthfully remain unassigned until a sales owner is added to either business workbook. The published showcase reports aggregate coverage only and does not expose production customer names or signal records.

Generation and verification run locally with no model calls or external-search credits.
