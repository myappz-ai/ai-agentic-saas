---
name: sales-event-reminders
description: "Reminder and warm-up sequence for webinars, live sessions and booked calls: confirmation, timed reminders (for example 5h, 3h, 2h, 20m, 15m, we are live, 10 minutes in, doors closing), post-event follow-up for attendees and no-shows. Use when asked to set up or run event reminders, warm up registrants, raise show-up rate or follow up after an event. Every broadcast waits for the owner's go."
---

# Event reminders

Raises show-up with a short, well-timed sequence and stops before it becomes spam.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `list_waba_templates`, `create_waba_template`, `create_email_template`, `create_workflow`, `validate_workflow_graph`, `update_workflow_status`, `query_contacts` (by event tag)
- Private workspace: `sops/event-reminders.md`, `docs/WHATSAPP_RULES.md`

## Steps
1. **Audience:** contacts with the event tag (for example `evt-asl-registered`). Remove opt-outs and anyone tagged customer if the event is for prospects.
2. **Sequence** (default; edit per event):

   | When | Channel | Message |
   | --- | --- | --- |
   | on registration | email + WhatsApp template | confirmed, add to calendar |
   | day before | email | what you'll learn, link |
   | 5h, 3h, 2h before | WhatsApp template | short reminder with time |
   | 20m and 15m before | WhatsApp template | joining link |
   | start | WhatsApp template | we are live |
   | 10 min in | WhatsApp template | still time to join |
   | near the offer | WhatsApp template | doors closing soon |
   | after | email | replay for no-shows; next step for attendees |

3. **Templates:** check each exists and is approved (`list_waba_templates`). Draft missing ones; approval by Meta can take hours, so do this days before.
4. **Build** the workflow and leave it **inactive**. Validate it.
5. **Go:** when the owner says go, activate it, and confirm the first send in the logs.
6. **After:** tag `attended` / `no-show`, then hand to sales-lead-follow-up.

## Approval rules
- Registrant sends are held until the owner says go for this event. No extra messages beyond the agreed sequence.
- All WhatsApp sends from the official business number via approved templates.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Plan table (above) with status per row (`template ok`, `waiting approval`, `drafted`), audience size, and the go/no-go question. After the event: attended, no-show, replay views, bookings.

## Done when
- [ ] Every reminder has an approved template
- [ ] Workflow inactive until go
- [ ] Post-event tags applied
