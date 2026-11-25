---
name: finance-revenue-report
description: "Revenue and subscription report: gross, collected, refunds, outstanding, MRR, ARR, active, new and churned subscriptions, top plans, and change versus last period, for one account or across all accounts. Use for a weekly or monthly finance report, MRR or churn questions, revenue by plan, \"how much did we make\", or the finance part of the CEO brief. Read only."
---

# Revenue report

Clear numbers the owner can trust, with the definitions stated so nobody argues about what MRR means.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `get_revenue_summary`, `query_transactions`, `get_dashboard_kpis`, the finance module (subscriptions, invoices)
- Super-admin read connector (optional, many accounts): `sa_finance_overview`, `sa_agency_kpis`, `sa_rank_agencies_by_revenue`, `sa_list_plans`
- Slack and the private workspace

## Steps
1. **Period**: this week vs last, or this month vs last (dates and zone stated).
2. **Pull**: gross, collected, refunds, outstanding, invoice count, collection % ; subscriptions active, new, cancelled; MRR and ARR.
3. **Cross-check**: if two tools give different MRR for the same account (for example the dashboard vs the finance overview), report both and flag it as a data issue. Never pick one silently.
4. **Definitions** in a footnote: which subscriptions count toward MRR, currency, whether tax is included. If the platform doesn't document a formula, say "not documented".
5. **Movers**: top 5 accounts or plans by change, biggest refunds, new churn.
6. **Three takeaways** in plain words.

## Approval rules
- Read only. No refunds, plan changes or payment links from this skill.
- Numbers as reported by tools; label estimates.
- Customer names stay in the private report; Slack shows totals and account labels only if the owner prefers.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
💰 Revenue — Jan 1–31 (IST) vs Dec
Collected ₹4.8L (+12%) · Refunds ₹15k · Outstanding ₹62k
MRR ₹3.9L · Active 212 (+18 new, −7 churn, 3.3%)
Top plan: Growth (54%)
⚠ Dashboard MRR and Finance MRR differ by ₹8k on 1 account → logged
Takeaways: 1) … 2) … 3) …
```
Saved as `reports/YYYY-MM/YYYY-MM-revenue.md`.

## Done when
- [ ] Period and zone stated
- [ ] Mismatches flagged, not hidden
- [ ] Saved and posted
