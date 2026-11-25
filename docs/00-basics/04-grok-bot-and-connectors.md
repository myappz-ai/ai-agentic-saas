# 04 · Grok Bot and connectors

Grok Bot is one place to ask. It reads the kit's skills for instructions and uses connectors to act. Claude, ChatGPT and Cursor work the same way.

## One bot, many connectors

```
                 ┌──────────── Grok Bot (or Claude, ChatGPT, Cursor) ────────────┐
                 │                                                               │
   SaaS platform (CRM, calendar,   Meta Ads   Slack   Gmail   Drive   Canva   GitHub   Composio (+ any app)
   WhatsApp, email, finance)
```

- Ask in plain words: "Which webinar registrants haven't been called?"
- The bot picks the connector, runs the read, and answers.
- For anything that sends, spends or changes records, it prepares the action and waits for approval.

## Why multiple connectors matter

A real question usually crosses tools:

> "Which ads brought the people who actually bought?"

That needs **Meta Ads** (which ad), the **platform CRM** (who registered, who paid) and **Slack** (post the answer). One connector can't answer it. One bot with three connectors can.

## The org structure we run on Grok Bot

See [docs/grok-bot-structure.md](../grok-bot-structure.md): a CEO agent, a COO agent and one agent per department, each a set of skills plus connectors.

## Adding a connector

1. Check [docs/CONNECTORS.md](../CONNECTORS.md): use the platform first, then official connectors, then Composio.
2. Connect it once, with the account that owns the data.
3. Test it with one harmless read before trusting it.
4. Note it in your workspace's department `README.md` so the agent knows it exists.
