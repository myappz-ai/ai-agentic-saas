# 01 · What an AI agent is

A chatbot **answers**. An agent **does**.

| | Chatbot | Agent |
|---|---|---|
| You ask | "Write a WhatsApp reminder" | "Send tomorrow's webinar reminder to everyone who registered" |
| It can see | Only what you paste in | Your CRM, calendar, ads account, inbox (through connectors) |
| It can do | Write text | Read data, draft, schedule, update records, report back |
| Output | A reply | A finished job, plus a report of what it did |

## The four parts of every agent

1. **The model** — the brain (Claude, ChatGPT, Grok and so on).
2. **Instructions** — who it is, what it owns, what it must never do. In this kit: the skills in `skills/`.
3. **Connectors (MCP)** — the hands. Each connector is one piece of software the agent can use.
4. **Memory** — what it has learned and decided. In your own private workspace: `decisions.md`, `learnings.md` and `reports/` (see `template/`).

Change the instructions and connectors, and the same model becomes a sales agent, a finance agent or an HR agent. That is why one chatbot can run every department.

## The loop

```
Prompt ──▶ Agent reads its SOP ──▶ uses connectors ──▶ result ──▶ report saved to your workspace
                                         │
                                 risky step? ──▶ asks a human to approve
```
