# Running the Organic Marketing module for a client

Use this after Phase 4 when the client's first playbook is "Setup my organic marketing engine". The method lives in this kit (`skills/organic-marketing`). This page covers what the agency keeps **per client** so clients never mix.

## How each client gets the flow
- **Agency-run:** the agency installs this kit on its own agent once. For each client it connects **that client's** account connector, confirms `get_business_profile` returns the client, then says "Set up organic marketing". One Claude can run 10 clients this way, one client at a time.
- **Client-run:** the client installs this kit on their own agent and connects their own account. The agency supports them with this page.
- In both cases the method is this kit's `skills/organic-marketing`: carousels, the daily avatar reel (HeyGen, optional ElevenLabs voice), guides, follow-gated DM flows, cross-posts, the tracker doc and the nightly report.

## One private workspace per client
Make a private repo (or folder) for each client, named `<client>-organic-marketing`. Never put client data in this kit. It is shared and meant to be public.

```
<client>-organic-marketing/
  README.md        the client's version of the pipeline, its slots and its links
  AUTOPILOT.md     the runbook: the client's standing authorization quoted with its date, its IDs, its rules
  queue.json       30 days of carousel topics
  creators.json    the accounts the viral watch tracks (optional)
  STYLES.md        approved reel styles and avatar looks (optional)
  TRACKER.md       the client's tracker doc link and tab IDs
  routines/        a copy of each live cloud routine prompt (ID, cron, connectors)
```

The cloud routines fetch `AUTOPILOT.md` and `queue.json` from this repo through Composio's GitHub proxy. Keep them at the repo root.

## Per-client setup checklist
- [ ] The client's **own** account connector. `get_business_profile` returns the client's business.
- [ ] The client's Instagram (and LinkedIn / YouTube if used), connected by the client through login screens.
- [ ] The client's standing authorization, **in their own words**, quoted in `AUTOPILOT.md` and in every routine prompt.
- [ ] Their own Organic Marketing Tracker doc (Overview · Reels · Carousels), per this kit's `tracker-doc.md`.
- [ ] Their own reports channel. Platform errors go to the agency's developer contact, billing goes to the agency owner.
- [ ] If reels are hands-free: the client's avatar, an approved-looks list, and AI-avatar API credit with auto-reload.
- [ ] The 6 cloud routines from this kit's `cloud-routine-templates.md`, named `<Client> · <slot>`, each with only that client's connectors.
- [ ] The first post live, and a comment test from a second account passed.

## Rules
- One client per routine, per repo, per tracker doc. Never reuse a routine across clients.
- No client IDs, Slack IDs or numbers in shared kits, PRs or examples.
- White-label: the client sees the agency's brand in reports and guides.
- Recurring revenue comes from running the engine every month. Send the nightly numbers and a monthly summary from the tracker doc in the agency's brand.
