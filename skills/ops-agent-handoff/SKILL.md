---
name: ops-agent-handoff
description: "Write a handoff or knowledge-transfer document when work moves between people or agents: role and boundaries, rules of engagement, what they need to know, in-flight items with owner and next step, FAQ, gaps to confirm and sources. Use when onboarding a new agent or staff member to a role, moving a client from onboarding to support, covering for someone, or when asked for a handoff or KT doc. Writes to the private workspace."
---

# Agent handoff

So the next person or agent can pick up the work on day one without asking the same questions again.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Private workspace: `handoffs/` folder
- Account connector and Slack: read the current state of in-flight items
- Knowledge base (ops-knowledge-base) for the facts

## Steps
Write `handoffs/<role>-handoff.md` with these sections:
1. **How to use this document** (who it is for, last updated, by whom).
2. **The business in one page**: products, plans, who is who **by role**.
3. **Your role and boundaries**: what you own, what you hand to whom, and when.
4. **Rules of engagement**: greeting and tone, message format, speed, evidence, never promise, own the issue, separate number and browser profile per agent.
5. **What you need to know**: link to the knowledge base sections rather than copying them.
6. **In-flight items**: item, customer label, status, next step, owner, due date. Use the CRM link, not contact details.
7. **FAQ** for this role.
8. **Suggested first-week sequence.**
9. **Gaps to confirm** before relying on them.
10. **Sources** actually opened, and document control (version, date).

Then ask the receiving person or agent to read it and list anything unclear.

## Approval rules
- No passwords, logins, keys or personal contact details in the handoff. Point to the password manager and the CRM.
- Only facts from sources you opened; mark the rest TBD.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
A markdown file in the private workspace, plus a Slack note: "Handoff for <role> ready: [link] · 6 in-flight items · 3 gaps to confirm".

## Done when
- [ ] All 10 sections present
- [ ] In-flight items each have an owner and next step
- [ ] Receiver confirmed they read it
