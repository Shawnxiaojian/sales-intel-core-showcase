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
- Signal-source filtering: complete, by signal type and exact source domain
- Evidence filtering: complete, by A/B/C/D evidence grade
- Combined filters: source, evidence, owner, key-person level, search, and sort can be applied together
- Filter transparency: each source and evidence option displays its event count; the result footer shows matching/total events and active-filter count
- Empty-state policy: impossible filter combinations return a clear reset prompt instead of stale rows
- Source traceability: source-site label and evidence grade appear in both the list and signal detail panel
- Linked detail completeness: selecting a row updates score, momentum, stage, owner, key person, evidence, exact source, match method/confidence, discovery/capture/publication times, reasoning, recommended action, and original URL
- Filter-safe selection: when filters remove the selected signal, the first remaining result is selected automatically
- Empty-result safety: when no signal matches, the detail panel switches to an explicit empty state and never displays stale customer information
- Detail navigation: previous/next controls move through the currently filtered and sorted result set
- Provenance separation: opportunity-signal evidence and key-person/contact evidence are separate first-class records and never share a substitute URL
- Multiple key people: one company may carry independent HR, procurement, technical, finance, or other contact records, each with its own role, phone, verification state, and source URL
- Sales-verified correction: a confirmed call result may override stale imported provenance without editing the two sales-facing workbooks
- Missing-source safety: a contact without reliable provenance is labelled “来源待核验” instead of linking to the company’s tender or news event
- Mobile completion: desktop signal rows become compact mobile cards with only company, source/evidence, title, urgency, and score
- Mobile detail safety: the linked detail panel uses a single-column layout and appears before the result list
- Mobile interaction: selecting a signal scrolls the user to its updated detail panel
- Narrow-screen fallback: filters and metrics switch to one column at 390px, with no horizontal page overflow
- Touch targets: filters, detail navigation, contact-source links, and opportunity-source links use mobile-sized controls

The current source workbooks contain no owner column, so all 22 signals truthfully remain unassigned until a sales owner is added to either business workbook. The published showcase reports aggregate coverage only and does not expose production customer names or signal records.

Generation and verification run locally with no model calls or external-search credits.
