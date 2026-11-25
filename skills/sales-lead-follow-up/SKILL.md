---
name: sales-lead-follow-up
description: "Follow up leads fast and politely: new leads, no-shows, cancellations, quiet warm leads and unpaid proposals. Builds a prioritised list and drafts personal WhatsApp, email or call-script messages using approved templates for first contact. Use when asked to follow up leads, chase no-shows, re-engage cold leads, speed to lead, or work the sales queue. Drafts only; every send needs a human OK."
---

# Lead follow-up

Makes sure no lead goes quiet because nobody wrote back. Drafts every message; a human sends or approves.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `query_contacts`, `query_opportunities`, the bookings read tool, `list_waba_templates`, `list_waba_connections`, `create_email_template`, contact notes and tags
- Email connector: drafts only
- Private workspace: `scripts/` for message templates; `docs/WHATSAPP_RULES.md`

## Steps
1. **Build the queue**, highest value first:
   1. new leads with no reply in 15 minutes (speed to lead);
   2. no-shows and cancellations from the last 48 hours (offer two new times);
   3. hot leads with no touch in 3 days;
   4. sent proposals or payment links not paid in 3 days;
   5. warm leads quiet for 7 days.
2. **Pick the channel.** First contact on WhatsApp is an **approved template** from the business number. After the lead replies, a personal message is fine. Email for longer details.
3. **Draft** each message: their first name, one line that shows you know their context, one clear ask (a time, a yes/no), no pressure. Max 3 touches per week per lead.
4. **Queue for approval:** high-risk sends go to **AI Suite → Approvals** or are shown in chat as a numbered list to approve.
5. **Log** a note and tag on each contact (`followup-1`, `followup-2`, …) once sent.

## Approval rules
- Never send without a human OK. Approved templates still need the go for each batch.
- No cold first messages from WhatsApp Web or a personal number.
- Respect opt-outs and quiet hours (no messages 21:00–09:00 local).
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Numbered list to approve:

```
Follow-ups — Thu 16 Jan (6)
1. Riley · no-show yesterday · WhatsApp template "missed_call_reschedule"
   "Hi Riley, sorry we missed you yesterday. Would Fri 11:00 or 16:00 IST work?"
2. Jamie · payment link sent Mon, unpaid · Email draft [link]
Reply with the numbers to approve, or "all".
```

## Done when
- [ ] Queue sorted by priority
- [ ] Every message drafted with a reason
- [ ] Nothing sent without OK; notes logged after send
