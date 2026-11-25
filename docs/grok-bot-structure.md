# The agent org structure (as run on Grok Bot)

This is a structure for running a company with agents on Grok Bot. You can copy it on Grok Bot, Claude, ChatGPT or Cursor: every box below is a set of skills from `skills/` plus the connectors that department needs.

```
                         Founder  (you)
                            │
                     CEO Agent  ── turns goals into priorities, reads every report, holds the approval queue
                            │
                     COO Agent  ── runs the daily rhythm, routes work, chases blockers
                            │
   ┌──────────────┬────────┴─────┬──────────────┬──────────────┐
Marketing       Sales       Operations       Finance          HR
                            (incl. support)
```

| Agent | Skills | Typical connectors | Produces |
|---|---|---|---|
| CEO | [ceo-daily-brief](../skills/ceo-daily-brief) | Email, Slack, GitHub, platform (read only) | Weekday morning brief: inbox, business pulse, department highlights, approval queue |
| COO | [coo-daily-rhythm](../skills/coo-daily-rhythm) | Slack, GitHub, platform (read only) | What ran and failed, blockers with owners, work routed to departments |
| Marketing | [organic-marketing](../skills/organic-marketing), [meta-lead-form-ads](../skills/meta-lead-form-ads), [marketing-performance-report](../skills/marketing-performance-report), [marketing-youtube-publishing](../skills/marketing-youtube-publishing), [marketing-content-research](../skills/marketing-content-research), [marketing-event-funnel](../skills/marketing-event-funnel) | Platform, Meta Ads, Instagram, YouTube, Canva, Slack | Posts and guides, lead ads, event funnels, YouTube series, nightly report |
| Sales | [sales-booking-report](../skills/sales-booking-report), [sales-call-routing](../skills/sales-call-routing), [sales-lead-scoring](../skills/sales-lead-scoring), [sales-lead-follow-up](../skills/sales-lead-follow-up), [sales-event-reminders](../skills/sales-event-reminders), [sales-pipeline-review](../skills/sales-pipeline-review) | Platform (CRM, calendar, WhatsApp), Slack | Booking reports, call briefs, lead stages, follow-up drafts, pipeline review |
| Operations | [onboard-a-client](../skills/onboard-a-client), [ops-customer-onboarding](../skills/ops-customer-onboarding), [ops-support-triage](../skills/ops-support-triage), [ops-bug-escalation](../skills/ops-bug-escalation), [ops-knowledge-base](../skills/ops-knowledge-base), [ops-agent-handoff](../skills/ops-agent-handoff) | Platform, email, Slack, private knowledge base | Onboarding checklists, support digest, bug log, knowledge base, handoffs |
| Finance | [finance-revenue-report](../skills/finance-revenue-report), [finance-invoicing](../skills/finance-invoicing), [finance-collections](../skills/finance-collections), [finance-expense-report](../skills/finance-expense-report), [finance-tax-pack](../skills/finance-tax-pack) | Platform finance, email (receipts), Sheets | Revenue report, invoice drafts, collections list, expense report, tax pack |
| HR | [hr-hiring-pipeline](../skills/hr-hiring-pipeline), [hr-interview-scheduling](../skills/hr-interview-scheduling), [hr-staff-onboarding](../skills/hr-staff-onboarding), [hr-leave-tracker](../skills/hr-leave-tracker), [hr-offboarding](../skills/hr-offboarding) | Email, calendar, Drive or Sheets, Slack | Hiring pipeline, interview slots, onboarding and offboarding checklists, leave calendar |
| Builder | [micro-app-builder](../skills/micro-app-builder) | App builder and sub-account connectors | A working micro app with team logins |

## How the departments work together

- **COO routes, CEO decides.** Department agents post their reports; the COO collects blockers each evening and the CEO brief puts anything that needs a yes at the top of the next morning.
- **Handoffs are explicit.** Marketing event funnel → Sales event reminders → Sales follow-up → Operations onboarding → Support triage → Finance invoicing and collections. Each step tags the contact so the next one can find it.
- **Same rules everywhere:** read before write, drafts before sends, one output per scheduled run, no secrets or personal data in any repo.

## How it runs on Grok Bot

1. **One bot, many connectors.** Connect the SaaS platform account first ([Your Platform]), then Slack, Gmail, Drive, Meta Ads and Composio as needed.
2. **Point the bot at this kit.** Ask: "Read https://github.com/myappz-ai/ai-agentic-saas and follow AGENTS.md." Or save the skills you use as the bot's own skills.
3. **Schedule the rhythm.** Ask the bot to create routines from [ROUTINES.md](ROUTINES.md): CEO brief every weekday morning, booking report morning and evening, marketing report nightly, COO check every evening, finance pack monthly.
4. **Keep records private.** Each department's SOPs, reports and decisions go in your own private workspace repo, laid out like [template/](../template). Never in this kit.
5. **Agents prepare, humans approve.** Anything that sends, spends or deletes waits for a yes ([AGENT_RULES.md](AGENT_RULES.md)).
