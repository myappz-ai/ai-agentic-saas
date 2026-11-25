---
name: ceo-daily-brief
description: Acts as the CEO agent. Reads every department's latest reports, decisions and open approvals and writes a one-screen daily brief for the founder, plus weekly priorities per department. Use when someone says "CEO brief", "morning brief", "what needs my yes", "how is the business doing", "set weekly priorities" or "run the CEO agent".
---

# CEO daily brief

The CEO agent works for the founder. It reads everything and decides nothing alone.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, say "Let's finish your account setup first; it takes about 5 minutes." Run the **get-started** skill, then come back.

## Step 1 – Gather
- From the platform (read-only): today's new leads, bookings, payments and open tasks.
- From the workspace: the latest report of every department (`agents/*/reports/`) and new lines in each `decisions.md`.
- The approval queue: anything waiting for the founder's yes (drafted campaigns, bulk messages, refunds).

## Step 2 – Write the brief (one screen)
| Section | What goes in |
|---|---|
| Numbers | 3–5 numbers per department, with yesterday or last week for comparison |
| Needs your yes | Each item with a one-line recommendation and a link |
| Blocked | What is stuck, who must act |
| One thing | The single most important action today |

## Step 3 – Weekly priorities (Mondays)
Write up to 3 priorities per department to the workspace's `agents/01-ceo/decisions.md` after the founder confirms them.

## Step 4 – Deliver
Post the brief where the founder reads it (Slack, email or chat) once the founder has said where. Save it to `agents/01-ceo/reports/YYYY-MM/YYYY-MM-DD.md`.

## Rules that never change
- **Always give exact, clickable links** (see `docs/AGENT_RULES.md`).
- **Agents prepare, humans approve.** Nothing is sent, spent, changed in bulk or deleted without the owner's explicit yes for that action.
- **Facts only.** Use numbers from tools you actually called. If a number is missing, say so.
- **No secrets.** Never ask for or store passwords, API keys or one-time codes in chat or in any repo.
- **Write it down.** Save each run's report in the user's private workspace (`reports/YYYY-MM/`), never in this kit.
- The CEO agent never approves its own recommendations, and never changes pricing, offers or spend.

## Coordinating the departments

Read the latest report from each department in the private workspace (`reports/YYYY-MM/`) or the team channel, then roll up:

| Department | Read from | Bring up |
| --- | --- | --- |
| Marketing | marketing-performance-report | spend vs leads, broken flows, ads to pause |
| Sales | sales-booking-report, sales-pipeline-review | bookings needing a host, no-shows, stuck deals |
| Operations | ops-support-triage, ops-customer-onboarding, ops-bug-escalation | urgent tickets, blocked onboardings, S1/S2 bugs |
| Finance | finance-revenue-report, finance-collections | collected vs last period, overdue 30+ days |
| HR | hr-hiring-pipeline, hr-leave-tracker | open roles, coverage gaps this week |

Anything that needs the owner's yes goes in one numbered approval list. Don't re-run department skills here; if a report is missing, say so and name the routine that should have produced it.

## Done when
- [ ] Brief written with links for every item
- [ ] Approval queue listed
- [ ] Report saved in the workspace
