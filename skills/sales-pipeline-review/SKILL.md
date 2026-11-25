---
name: sales-pipeline-review
description: "Weekly pipeline review: open deals by stage and value, deals stuck too long, deals with no next step, won and lost this week, forecast for the month, and the top actions for each salesperson. Use when asked for a pipeline review, sales forecast, weekly sales report, stuck deals or a sales team update. Read only."
---

# Pipeline review

One page that tells the team where the money is and what to do about it this week.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector (or super-admin read connector per account): `query_opportunities`, `create_pipeline` (only when asked to set up stages), `query_contacts`, `get_revenue_summary`
- Slack and the private workspace

## Steps
1. **Pull open opportunities** by pipeline and stage, with value, owner, last activity and created date.
2. **Flag:** stuck (no stage move in 14 days), no next step, past expected close date, missing value.
3. **This week:** new, won (value), lost (with reason if recorded).
4. **Forecast:** sum of open value weighted by stage probability from `sops/pipeline.md` (default: discovery 10%, proposal 40%, negotiation 70%). Say clearly that it is an estimate.
5. **Actions:** the top 3 per owner, each tied to a deal link.

## Approval rules
- Read only. Moving stages or closing deals needs the deal owner or an explicit OK.
- Report values as the CRM shows them; no invented numbers.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
📈 Pipeline — week of 13 Jan
Open: 24 deals · ₹18.4L · forecast (weighted) ₹6.1L
Won: 3 · ₹2.2L | Lost: 2 (price, timing)
Stuck 14d+: 5 [links]
Actions
Alex: send proposal to Acme Studio [link] …
```
Saved as `reports/YYYY-MM/YYYY-MM-DD-pipeline.md`.

## Done when
- [ ] Every open deal checked
- [ ] Stuck deals linked
- [ ] Actions per owner
