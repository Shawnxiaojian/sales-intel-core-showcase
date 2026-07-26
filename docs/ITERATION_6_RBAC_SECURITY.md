# Accounts, Roles and Data Security

The private site uses two independent authorization layers:

1. The hosting allowlist determines who can reach the site.
2. Server-side business roles determine which records and actions are available.

Roles follow least privilege:

- Sales can access only customers, signals and tasks assigned to their Excel owner name.
- Managers can access only sales members in their team; contact details are masked by default.
- Administrators can manage roles, teams, writeback adapters, audit logs and pending scoring policies.

Customer and signal source files are server-only and are excluded from public client assets. Authorization is
rechecked on every API request. Role changes, denied requests, task mutations, writeback updates and scoring-policy
changes are recorded in an append-only business audit log. Secrets and credentials are never included in pages,
audit metadata or this public repository.
