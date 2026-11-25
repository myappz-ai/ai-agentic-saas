---
name: micro-app-builder
description: Builds a production micro app (a small web app with team logins that replaces a messy spreadsheet or manual process) on a [Your Platform] app builder (any AI-friendly app builder with sub-accounts), following the Micro App Builder playbook. Use when someone says "build me an app", "turn this spreadsheet into an app", "make a micro app", "I need a tool for my team" or describes an app in one paragraph.
---

# Micro app builder

The full method lives in the public Micro App Builder playbook. This skill is the pointer and the guardrails.

## Step 1 – Read the playbook
Read, in this order:
1. [AGENTS.md](https://github.com/myappz-ai/micro-app-builder/blob/main/AGENTS.md)
2. [PLAYBOOK.md](https://github.com/myappz-ai/micro-app-builder/releases/latest/download/PLAYBOOK.md), the whole playbook in one file from the latest release (or read `docs/` in the repository in order)
3. If the person describes the app in one paragraph: [docs/20-one-prompt-to-app.md](https://github.com/myappz-ai/micro-app-builder/blob/main/docs/20-one-prompt-to-app.md)

## Step 2 – Check connectors
You need the **app builder connector** and the **sub-account connector**. If either is missing, tell the person they need a sub-account and both connector links, and stop. Never ask for passwords, tokens or keys.

## Step 3 – Build
Follow the playbook: plan → data layer → screens → team logins and roles → verify → publish only when the person asks.

## Rules that never change
- **Always give exact, clickable links** (see `docs/AGENT_RULES.md`): the app, its editor and its preview.
- Each app works inside one sub-account only.
- Ask before sending, posting, deleting or changing anything in a connected app.

## Done when
- [ ] The app works with a test login
- [ ] The person has the links and knows how to add team members
