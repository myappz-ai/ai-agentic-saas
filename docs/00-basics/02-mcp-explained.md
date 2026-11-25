# 02 · MCP: how a chatbot handles your software

**MCP (Model Context Protocol)** is a standard plug. Software that offers an MCP server tells the chatbot: "here are the things you can do in me, and here is what each one needs."

Think of it like USB: the chatbot is the laptop, each MCP server is a device you plug in.

## What a connector gives the agent

| Kind of tool | Example | Risk |
|---|---|---|
| **Read** | List today's bookings, get ad spend, read a form's submissions | Safe, runs straight away |
| **Write** | Create a contact, draft a campaign, update a deal stage | Shows a preview, runs after a yes |
| **Send / spend** | Send WhatsApp, launch an ad, refund a payment | Goes to an approval queue, a human approves |

## What you typically connect

- **Your SaaS platform ([Your Platform])** — CRM, pipelines, forms, funnels, calendar, WhatsApp, email, workflows, finance. One connector, hundreds of tools.
- **Meta Ads** — campaigns, ad sets, ads, insights.
- **Slack, Gmail, Google Drive, Canva** — reports, files, designs.
- **GitHub** — your private workspace repo: SOPs in, reports out.
- **Composio** — a bridge to apps that have no official connector yet.

Full list and the order to use them in: [docs/CONNECTORS.md](../CONNECTORS.md).

## How a request flows

```
"How many people booked a call today?"
   │
   ▼
Chatbot picks the platform connector ──▶ calls the bookings tool for today
   │
   ▼
Gets the rows back ──▶ counts them ──▶ answers with the number and the list
```

No dashboard opened. No export. No spreadsheet. That is "handling software using MCP".
