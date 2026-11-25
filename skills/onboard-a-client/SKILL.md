---
name: onboard-a-client
description: "Onboards a new client for an agency, end to end. It covers intake, the client's own account, connecting the client's Instagram, Meta, WhatsApp and email, connecting the client's account to the agent, a readiness audit, choosing the first playbook from this kit, and a hand-over summary. Use when an agency says \"onboard a new client\", \"set up a client\", \"add <client> to my agency\", or \"get <client> ready for leads\". Status: Beta."
---

# Onboard a client (Beta)

The agency's job is to get each client from "signed" to "leads arriving" fast, without mixing up clients. Run the phases in order. Every phase ends with clickable links to what was created (see `docs/AGENT_RULES.md`).

## Phase 0 – Intake
Collect what's missing with AskUserQuestion, a few questions at a time:
- client business name, industry, city/service area
- owner name, WhatsApp number and email: for the account login and alerts, never for marketing without consent
- what they sell, the main offer, and the average sale value
- the goal for the first 30 days: Instagram leads, ad leads, or both
- monthly ad budget (if ads)
- the client's Instagram handle, Facebook Page and website/privacy-policy URL
- who at the client's side calls the leads, and when

Save the answers as a client brief in the agency's project: `Client_<Name>_Brief.md`.

## Phase 1 – The client's own account
1. Create the client's account (sub-account) in the agency dashboard. If the agency's connector has a create-account tool, use it with a preview first. Otherwise give the agency the exact dashboard link and the field values to paste.
2. Set the business profile with the brief: name, industry, timezone, logo, contact details.
3. Connect the **client's** account connector to the agent. Confirm with `get_business_profile` that it returns the client's business, not the agency's or another client's. Stop if it doesn't.

## Phase 2 – Connect the client's channels
Send the client one message (drafted for the agency to send) with the exact links and steps:
- **Instagram:** in the client's account, Settings → App Store → Instagram → **Instagram Login**, allowing every permission. Business or Creator account.
- **Meta (for ads):** Ad Launcher → Platforms → Connect with Meta. The client adds the agency as a partner on its ad account and Page in [Meta Business settings](https://business.facebook.com/settings).
- **WhatsApp Business** and the **email sender**, if the playbook needs them.

The client clicks; the agency never asks for the client's passwords.

## Phase 3 – Account setup and readiness audit
1. Run the **get-started** playbook (this kit) **inside the client's account**. It saves the client's brief, checks every channel and marks setup as done (`agentic_kit_setup`). This step is mandatory, and no playbook runs for the client without it.
2. Then run the readiness audit of the playbook the client will start with:
- the organic engine: `skills/organic-marketing/references/readiness-audit.md` in this kit
- lead-form ads: Phase 1 of `meta-lead-form-ads`

Report one ✅ / ⚠️ / ❌ table with evidence and the link to fix each ❌.

## Phase 4 – First playbook
Recommend one starting playbook based on the goal and budget, confirm it with the agency, then run it from this kit inside the client's account:
- "Setup my organic marketing engine" for organic Instagram leads, no ad budget needed. Set up the client's own private workspace and routines per `references/organic-marketing-per-client.md`.
- "Launch lead form ads" for paid leads, budget needed

The playbook's own rules apply. It runs its setup check first: test lead or live comment test first, and nothing paid goes live without the go-ahead.

## Phase 5 – Hand over
Send the agency one summary to forward to the client, in the agency's brand:
- what was set up, each with its clickable link
- what's live and what's waiting on the client
- where reports arrive and how often
- the next review date

Save it to the agency project as `Client_<Name>_Onboarding.md`.

## Rules that never change
- **Always give exact, clickable links** (see `docs/AGENT_RULES.md`). End each phase with links to everything created.
- **One client at a time.** Confirm the connector returns this client's business before every write.
- **White-label:** never show the platform's name to the client. Use the agency's brand.
- Never ask the client for passwords or one-time codes. They connect accounts themselves via login screens.
- Never send anything to the client's customers during onboarding.
- Nothing paid goes live without the agency's explicit "go ahead" for that client.

## Done when
- [ ] Client brief saved
- [ ] Client account created; its connector returns the client's business
- [ ] Channels connected for the chosen playbook
- [ ] get-started completed in the client's account (`agentic_kit_setup` exists)
- [ ] Readiness audit green
- [ ] First playbook running, with its live test passed
- [ ] Hand-over summary sent and saved

## Status
Beta. It is built from the steps used for real client accounts, and will be marked proven once 2–3 agencies have onboarded clients with it. Report what broke to the kit maintainers.
