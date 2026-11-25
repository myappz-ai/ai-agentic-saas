---
name: ops-customer-onboarding
description: "Onboard a new paying customer onto your SaaS or service: welcome, plan and payment check, account or sub-account setup, channel connections (WhatsApp, Meta, email, calendar), integrations, training videos in order, a first-week checklist and a clean handoff to support. Use when a deal is won, a customer asks how to get started, an onboarding is stuck, or to report onboarding status. Drafts customer messages; a human sends them."
---

# Customer onboarding

Takes a customer from paid to live in the first week, and makes sure nobody is promised something the product doesn't do.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `query_contacts`, contact notes and tags, `get_channel_readiness`, `list_waba_connections`, `query_integrations`, `list_event_types`, `query_transactions`
- Slack or your team chat: internal updates; email or WhatsApp (drafts) for the customer
- Private workspace: `sops/onboarding.md`, `knowledge/faq.md`, `knowledge/do-not-promise.md`

## Steps
1. **Kick-off note** in the CRM: plan, paid date, who the customer is, what "live" means for them (for example "first WhatsApp campaign sent").
2. **Checklist** (tag each step `onb-<step>` when done):
   1. payment confirmed and plan correct;
   2. account or sub-account created, branding and domain set;
   3. channels connected and healthy (`get_channel_readiness`): WhatsApp Business number, Meta page and ad account, email sender, calendar;
   4. integrations they need (`query_integrations`);
   5. staff added with the right roles;
   6. first workflow or campaign built and tested;
   7. training: send the core videos in order, one per day, with a small task each.
3. **Daily check:** which step is blocked and why. Customer-side blockers get a polite nudge draft; our-side blockers go to **ops-bug-escalation** or the owner.
4. **Speak carefully:** greet formally, short sectioned messages, evidence (screenshot or link) for every claim, never promise dates or features from `do-not-promise.md`.
5. **Handoff to support** when the checklist is done: write a handoff note with **ops-agent-handoff**, tag `onb-complete`, tell the customer who to contact next.

## Approval rules
- Customer messages are drafts until a human sends them, unless a standing authorization covers that channel.
- Never ask the customer to share passwords or one-time codes in chat. Use the platform's own invite or connect flows.
- Never promise a feature, date or refund; route those to the owner.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Status table per customer, posted daily while onboarding is open:

```
🧩 Onboarding — Acme Studio (day 3 of 7)
☑ Paid · ☑ Account · ☐ WhatsApp (waiting for Meta verification) · ☑ Calendar
Blocker: business verification pending — customer side, nudge drafted [link]
Next: training video 3, first workflow test
```

## Done when
- [ ] Checklist tags applied
- [ ] Every blocker has an owner
- [ ] Handoff note written at the end
