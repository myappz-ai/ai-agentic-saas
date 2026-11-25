---
name: marketing-event-funnel
description: "Build the funnel for a webinar, workshop or launch event: registration page and form, thank-you page, CRM tags, confirmation and reminder messages, and the tracking link for ads and posts. Use when asked to set up a webinar, event registration, launch page, masterclass funnel or registrant automation. Builds drafts; publishing, activating automations and sending to registrants need an OK."
---

# Event funnel

From "we have a webinar on the 20th" to a tested funnel that collects registrants and tags them correctly.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `create_funnel`, `create_page`, `write_page_html`, `publish_site`, `create_form`, `create_short_link`, `create_workflow`, `validate_workflow_graph`, `update_workflow_status`, `list_waba_templates`, `create_waba_template`, `create_email_template`, `list_event_types`
- Slack: status updates

## Steps
1. **Brief.** Event name, date and time with zone, host, offer, who it is for, capacity, joining link source. Write it down before building.
2. **Tags.** Create a tag set like `evt-<short-name>-registered`, `-attended`, `-no-show`, `-vip`. Every step below uses these.
3. **Pages.** Registration page (headline, 3 benefits, date, form), thank-you page (add-to-calendar, what happens next). Draft with `create_page`/`write_page_html`; share preview links.
4. **Form** with `create_form`: name, email, phone with country code, one qualifying question. It must apply the `registered` tag.
5. **Messages.** Confirmation (instant), then the reminder sequence from **sales-event-reminders**. Use approved WhatsApp templates only (`docs/WHATSAPP_RULES.md`); create drafts for missing ones.
6. **Automation.** `create_workflow` for form submit → tag → confirmation. Check it with `validate_workflow_graph`. Leave it **inactive**.
7. **Test** with a fictional contact (e.g. Test Registrant, test@example.com): submit, check the tag and the confirmation. Delete the test contact afterwards.
8. **Ask for go-live.** Show links and the checklist; after the OK, `publish_site` and `update_workflow_status` to active, then share the trackable link for ads and posts.

## Approval rules
- Pages stay unpublished and workflows inactive until the owner says go.
- Registrant broadcasts are held until the owner says go, even with approved templates.
- Use only fictional test contacts; remove them after the test.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Checklist in chat or Slack:

```
🎟 Event funnel — "Agency Systems Live" · 20 Jan, 19:00 IST
☑ Registration page (preview) [link]
☑ Form → tag evt-asl-registered (tested)
☐ Reminder templates: 2 approved, 1 waiting
☐ Workflow inactive — waiting for your go
Tracking link: [short link]
```

## Done when
- [ ] Brief written
- [ ] Test registration passed and test contact removed
- [ ] Nothing live without OK
