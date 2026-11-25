---
name: ops-support-triage
description: "Triage customer support requests from chat, email and groups: classify (how-to, bug, billing, feature request, urgent), answer how-to questions from the knowledge base, draft replies with evidence, route bugs, billing and feature requests, and post a daily support digest. Use when asked to handle support, answer a customer question, check what customers are waiting on, or for a support report. Drafts replies; a human sends."
---

# Support triage

Every customer question gets a correct, sourced answer or a clear owner, quickly.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `query_contacts`, contact notes and tags, the conversations/inbox read tool if your connector has one (if not, work from what the human pastes or forwards)
- Email connector: read and draft
- Slack: internal routing and the daily digest
- Private workspace: `knowledge/faq.md`, `knowledge/known-issues.md`, `knowledge/do-not-promise.md`, `escalation.md` (roles, not personal numbers)

## Steps
1. **Classify** each request: how-to · bug · billing · feature request · account access · urgent (payments blocked, everything down).
2. **How-to:** find the answer in the knowledge base or product docs. Reply with the steps and the matching training video or doc link. If you can't find it, say so internally and ask the support lead; don't guess.
3. **Bug:** reproduce if you can, collect evidence, then use **ops-bug-escalation**. Tell the customer you've logged it, with no promised date.
4. **Billing:** hand to **finance-collections** or the finance owner.
5. **Feature request:** log it in `knowledge/feature-requests.md` with the customer's words, then thank them.
6. **Urgent:** post to the team channel at once, tagging the escalation role.
7. **Daily digest** at the agreed time.

## Approval rules
- Draft replies; a human sends, or approves in AI Suite → Approvals.
- Account access issues: never reset passwords or read codes for a customer; point them to the reset flow.
- Legal, security or compliance questions go to the named owner, never answered by the agent.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Daily digest:

```
🛠 Support — Thu 16 Jan, 18:00 IST
Open 7 · answered today 12 · urgent 0
Waiting on us: 3 (2 bugs logged, 1 billing) [links]
Waiting on customer: 2
Top questions today: WhatsApp template approval (4), domain setup (2) → FAQ updated
```

## Done when
- [ ] Every request classified with an owner
- [ ] Answers cite a doc or video
- [ ] Digest posted
