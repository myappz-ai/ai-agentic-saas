---
name: ops-bug-escalation
description: "Turn a customer problem into a clean bug report developers can act on: steps to reproduce, expected versus actual, evidence, affected accounts, severity, and a tracked status that support can quote back to the customer. Use when something in the product is broken, a customer reports an error, a routine hits a platform error, or to chase open bugs. Posts internally only."
---

# Bug escalation

Fewer back-and-forth messages with developers, and customers who always know where their issue stands.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Slack (developer channel) or your issue tracker
- Account connector: read tools for the affected feature, to reproduce safely
- Private workspace: `knowledge/known-issues.md` (the bug log)

## Steps
1. **Check the log first.** If the bug is already in `known-issues.md`, add the new customer as affected and stop.
2. **Reproduce** with read tools or a test record. Never test on a customer's live data without their OK.
3. **Write the report:**
   - title (what is broken, where);
   - steps to reproduce, numbered;
   - expected vs actual;
   - evidence: screenshot, error text, time with zone, request ID if shown;
   - affected: number of accounts, plan type (no customer contact details);
   - severity: **S1** money or data at risk / everything down · **S2** a main feature broken, no workaround · **S3** workaround exists · **S4** cosmetic.
4. **Post once** in the developer channel. Repeat errors from routines: at most once per distinct error per day.
5. **Track:** add to the log with status (`reported`, `in progress`, `fixed`, `verified`). When fixed, verify it, then draft the customer update.

## Approval rules
- Internal only. Customer updates are drafts and never promise a fix date.
- Strip tokens, keys and personal data from screenshots and error text before posting.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
🐞 S2 — Payment link page shows blank after domain change
Steps: 1) … 2) … 3) …
Expected: checkout loads · Actual: blank page, console 404
Evidence: [screenshot] 16 Jan 11:42 IST
Affected: 2 accounts (agency plan) · Workaround: use default domain
```
Bug log row: `date | title | severity | affected | status | link`.

## Done when
- [ ] Duplicate check done
- [ ] Report has steps, evidence and severity
- [ ] Logged and tracked to verified
