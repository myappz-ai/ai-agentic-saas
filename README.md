<div align="center">

# AI Agentic SaaS

### Run your whole business from one AI agent.
**AI** (Claude) × **Agentic** (Grok Bot or any agent) × **SaaS** ([Your Platform], any MCP-enabled white-label SaaS): a CEO agent, a COO agent and one agent per department, working inside your own SaaS platform account.

![Version](https://img.shields.io/badge/version-0.3.0-1f6feb?style=flat-square)
![Works with Claude](https://img.shields.io/badge/works%20with-Claude-d97757?style=flat-square)
![Works with Grok Bot](https://img.shields.io/badge/works%20with-Grok%20Bot-111111?style=flat-square)
![Works with Cursor](https://img.shields.io/badge/works%20with-Cursor-555555?style=flat-square)
![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![You approve](https://img.shields.io/badge/nothing%20goes%20out-without%20your%20OK-2da44e?style=flat-square)

</div>

---

## Start in 3 steps

1. **Install** the kit in your agent (pick yours below).
2. **Connect** your SaaS platform account ([Your Platform], any MCP-enabled platform). Paste the account's connection link into your agent's **connector settings**, never into the chat.
3. **Say "Get started".** Your agent checks the account, fills in your business details and recommends your first playbook.

> You never need to open these files. Your agent reads them for you.

## Install

| Agent | How |
|---|---|
| **Claude** (web and desktop) | *Customize → Plugins → Add marketplace → Add from a repository*, paste `https://github.com/myappz-ai/ai-agentic-saas`, turn on **AI Agentic SaaS**. Then add your account under *Customize → Connectors → Add custom connector*. |
| **Claude Code** | `/plugin marketplace add myappz-ai/ai-agentic-saas`, then `/plugin install ai-agentic-saas@myappz-ai-agentic-saas`. Set the `PLATFORM_MCP_URL` environment variable (see `.env.example`); the bundled `.mcp.json` reads it. If it is unset, the server just shows as not connected (it points at a placeholder address). |
| **ChatGPT** (not tested) | We have not verified a plugin install for ChatGPT. What works today: add your account as a custom MCP connector where your plan allows it, then upload `AGENTS.md` and the `SKILL.md` files you need to a Project. |
| **Cursor** | Open this repo. Add your account link in Cursor's MCP settings (*Customize*) or in your personal `~/.cursor/mcp.json`. The repo's `.cursor/mcp.json` only holds a placeholder: don't commit your real link. Cursor reads `AGENTS.md` automatically. |
| **Grok Bot** | Connect your platform account as a connector, then say: *"Read https://github.com/myappz-ai/ai-agentic-saas and follow AGENTS.md. Save the skills I use as your own skills."* See [the Grok Bot structure](docs/grok-bot-structure.md). |
| **Claude Desktop (skills only)** | Zip any folder in `skills/` and upload it under *Customize → Skills*. |
| **Any other agent** | Add a remote (HTTP) MCP server with your connection link, then point the agent at `AGENTS.md`. |

## The agent org chart

```
                         Founder  (you)
                            │
                     CEO Agent  ── priorities, daily brief, approval queue
                            │
                     COO Agent  ── daily rhythm, routing, blockers
                            │
   Marketing · Sales · Operations (incl. support) · Finance · HR   (+ Micro-app builder)
```

This is a structure that runs on **Grok Bot**: one bot, many connectors, one set of skills per department. Details: [docs/grok-bot-structure.md](docs/grok-bot-structure.md).

## What you get

33 skills: 3 for leadership and setup, 28 across five departments and 2 builders. Each skill says when to use it, which tools it calls, what needs your OK and what it hands back.

### Leadership and setup

| Just say | Skill | What your agent does |
|---|---|---|
| "Get started" | [get-started](skills/get-started) | Connects and checks your account, fills your business profile, recommends a first playbook |
| "CEO brief" | [ceo-daily-brief](skills/ceo-daily-brief) | One-screen daily brief across all departments, weekly priorities, what needs your yes |
| "COO check" | [coo-daily-rhythm](skills/coo-daily-rhythm) | What ran, what failed, blockers with owners, routes work to departments |

### Marketing

| Just say | Skill | What your agent does |
|---|---|---|
| "Set up organic marketing" | [organic-marketing](skills/organic-marketing) | Daily carousels and reels, comment-to-DM guides, tracker, nightly report |
| "Launch lead form ads" | [meta-lead-form-ads](skills/meta-lead-form-ads) | Meta lead ads into the CRM with instant follow-up, built as drafts |
| "How did ads and posts do?" | [marketing-performance-report](skills/marketing-performance-report) | Paid and organic report, lead quality verdicts, ranked actions |
| "Fix my YouTube playlist" | [marketing-youtube-publishing](skills/marketing-youtube-publishing) | SEO titles, descriptions, CTA links, playlists, pinned comments |
| "Give me today's content ideas" | [marketing-content-research](skills/marketing-content-research) | Viral watch and news scan turned into hooks; never posts |
| "Set up the webinar funnel" | [marketing-event-funnel](skills/marketing-event-funnel) | Registration page, form, tags, messages, tested before go-live |

### Sales

| Just say | Skill | What your agent does |
|---|---|---|
| "Booking report" | [sales-booking-report](skills/sales-booking-report) | Needs-action list, suggested hosts, 30-day show-up table |
| "Who should take this call?" | [sales-call-routing](skills/sales-call-routing) | Host suggestion by role plus a call brief |
| "Score my leads" | [sales-lead-scoring](skills/sales-lead-scoring) | Cold, warm, hot stages with CRM tags |
| "Follow up my leads" | [sales-lead-follow-up](skills/sales-lead-follow-up) | Prioritised queue and drafted messages for approval |
| "Set up webinar reminders" | [sales-event-reminders](skills/sales-event-reminders) | Timed reminder sequence, held until you say go |
| "Pipeline review" | [sales-pipeline-review](skills/sales-pipeline-review) | Deals by stage, stuck deals, forecast, actions per owner |

### Operations

| Just say | Skill | What your agent does |
|---|---|---|
| "Onboard a new client" | [onboard-a-client](skills/onboard-a-client) | Agency client onboarding, end to end |
| "Onboard this customer" | [ops-customer-onboarding](skills/ops-customer-onboarding) | Paid-to-live checklist, blockers, handoff to support |
| "Answer my support inbox" | [ops-support-triage](skills/ops-support-triage) | Classify, answer from the knowledge base, route, daily digest |
| "Log this bug" | [ops-bug-escalation](skills/ops-bug-escalation) | Reproducible bug reports with severity, tracked to verified |
| "Update the FAQ" | [ops-knowledge-base](skills/ops-knowledge-base) | FAQ, known issues, do-not-promise list, escalation by role |
| "Write a handoff" | [ops-agent-handoff](skills/ops-agent-handoff) | Handoff or knowledge-transfer document for a role |

### Finance

| Just say | Skill | What your agent does |
|---|---|---|
| "Revenue report" | [finance-revenue-report](skills/finance-revenue-report) | Collected, MRR, churn, movers, with definitions |
| "Invoice this client" | [finance-invoicing](skills/finance-invoicing) | Invoices, quotes, payment links as checked drafts |
| "Who owes us money?" | [finance-collections](skills/finance-collections) | Overdue by age, reminder ladder, drafts for approval |
| "Expense report" | [finance-expense-report](skills/finance-expense-report) | Receipts categorised, duplicates, budget vs actual |
| "Prepare the GST pack" | [finance-tax-pack](skills/finance-tax-pack) | Tax and accounts pack for the accountant; never files |

### HR

| Just say | Skill | What your agent does |
|---|---|---|
| "Hire a support executive" | [hr-hiring-pipeline](skills/hr-hiring-pipeline) | JD, scorecard, screening, stages, weekly update |
| "Schedule interviews" | [hr-interview-scheduling](skills/hr-interview-scheduling) | Slots, invites, interviewer prep, feedback |
| "Onboard our new hire" | [hr-staff-onboarding](skills/hr-staff-onboarding) | Least-privilege access, training plan, check-ins (people and agents) |
| "Who is out this week?" | [hr-leave-tracker](skills/hr-leave-tracker) | Leave requests, coverage clashes, routing updates |
| "Offboard Pat" | [hr-offboarding](skills/hr-offboarding) | Access inventory, handover, revoke on the last day |

### Builders

| Just say | Skill | What your agent does |
|---|---|---|
| "Build me an app" | [micro-app-builder](skills/micro-app-builder) | Turns a spreadsheet or process into a micro app with team logins |
| "Add this to the kit" | [add-proven-playbook](skills/add-proven-playbook) | Packages a proven workflow as a new skill |

Scheduled runs (morning brief, booking reports, nightly marketing report) follow [docs/ROUTINES.md](docs/ROUTINES.md). WhatsApp work follows [docs/WHATSAPP_RULES.md](docs/WHATSAPP_RULES.md). Tool names: [docs/TOOLS.md](docs/TOOLS.md).

## You stay in control

- Agents prepare, **you approve** anything that sends, spends or deletes.
- Real numbers only, from tools the agent actually used.
- Never paste passwords, keys or one-time codes into chat, and never commit them to any repo, private or not. Keep them in a password manager.
- Your own records (SOPs, reports, decisions) live in **your private workspace**, never in this kit. See [examples/](examples) (fake data) and [template/](template).

## Learn the ideas

Start with [docs/00-basics](docs/00-basics): what an agent is, MCP, running a business from one chatbot, why AI isn't cheap, approvals and safety.

## White-label

Partners can run this kit under their own brand. [docs/WHITE_LABEL.md](docs/WHITE_LABEL.md) lists exactly what to rename and what to keep.

## Related

- [Micro App Builder](https://github.com/myappz-ai/micro-app-builder): the full micro-app playbook (public)

---

<sub>Maintained by AI Agentic SaaS contributors. MIT licensed (see [LICENSE](LICENSE)). Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). Security: [SECURITY.md](SECURITY.md). Change log: [CHANGELOG.md](CHANGELOG.md). Rebranding it as your own? See [docs/WHITE_LABEL.md](docs/WHITE_LABEL.md).</sub>
