# 03 · Run your whole business from one chatbot

You do not need a different app per department. You need **one chatbot**, **the right connectors**, and **one folder of instructions per department**.

## How one chatbot becomes seven agents

| Department | What the agent reads | Connectors it uses | What it produces |
|---|---|---|---|
| CEO | Every department's reports | GitHub, Slack | Weekly priorities, approvals |
| COO | Every SOP and open task | Slack, platform, GitHub | Daily rhythm, blockers chased |
| Marketing | `skills/organic-marketing`, `skills/meta-lead-form-ads` | Meta Ads, platform, Canva | Campaigns staged, content, ad reports |
| Sales | `skills/sales-*` (booking report, routing, scoring, follow-up, reminders, pipeline) | Platform (CRM, calendar, WhatsApp), Slack | Lead scoring, reminders, booking reports |
| Operations | `skills/onboard-a-client`, `skills/ops-*` (onboarding, support, bugs, knowledge base, handoffs) | Platform, Slack | Client onboarding, support replies |
| Finance | `skills/finance-*` (revenue, invoicing, collections, expenses, tax pack) | Platform finance tools | Revenue, invoices, expense reports |
| HR | `skills/hr-*` (hiring, interviews, onboarding, leave, offboarding) | Platform HR tools | Hiring pipeline, leave, onboarding |

## A day in the business

| Time (IST) | Who | What happens |
|---|---|---|
| Morning | Sales Agent | Reads bookings across accounts, posts the daily booking report to Slack, saves it to your workspace |
| Morning | Marketing Agent | Pulls yesterday's spend and leads, flags ads over the cost limit |
| Day | Operations Agent | Answers support questions from the knowledge base, escalates what it can't |
| Evening | Sales Agent | Evening booking report, host suggestions for tomorrow's calls |
| Evening | COO Agent | Reads every report, lists what is blocked and who must act |
| Anytime | CEO | Asks the bot one question, gets the answer from live data |

Sample: [examples/reports/](../../examples/reports) shows what a daily sales report looks like (fake data).

## The rule that makes it work

Every agent writes down what it did. SOPs say **how**, reports say **what happened**, decisions say **why**. The next agent (or person) picks up from the written record, not from memory.
