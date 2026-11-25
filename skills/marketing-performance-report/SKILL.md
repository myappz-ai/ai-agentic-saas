---
name: marketing-performance-report
description: "Daily, nightly or weekly marketing report: Meta ads spend, leads and cost per lead matched to CRM leads, plus organic post reach, comments and guide DMs. Use when asked how ads or posts performed, for a nightly marketing report, a weekly marketing summary, an ads audit, or to find campaigns wasting money. Read only; recommends pauses and budget moves but never changes ads."
---

# Marketing performance report

One honest report on what marketing did yesterday (or this week): paid and organic side by side, with the few actions that matter at the top.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `ads_get_ad_accounts`, `ads_get_ad_entities` (campaigns, ad sets, ads with insights), `get_ad_connection_health`, `list_ad_leads`, `query_contacts` (to match leads to CRM), `list_instagram_media`, `list_social_flows`, `get_social_flow_logs`
- YouTube connector (optional): views and comments on recent uploads
- Slack: post the report; private workspace (GitHub or Drive): save it

## Steps
1. **Health first.** `get_ad_connection_health` and `get_instagram_connection_health`. If a token is close to expiry or broken, put that at the top and keep going with what you can read.
2. **Paid.** For each active campaign in the period: spend, results, cost per result, CTR, frequency. Read the window you were asked for (default: yesterday, and the last 7 days for context).
3. **Lead quality.** Match `list_ad_leads` to `query_contacts` by email or phone (in memory only, never in the report). Classify each campaign: **GOOD** (leads reached a real conversation or booking), **HOLD** (too early, under 3 days or under 10 leads), **JUNK** (fake or unreachable leads above 30%).
4. **Organic.** Posts published in the period with reach, likes, comments, saves; for each comment-to-DM flow, comments, follows verified and guides sent (`get_social_flow_logs`).
5. **Find the actions.** At most five, ranked by money or leads at stake: pause, cut budget, scale, refresh creative (frequency over 3), fix a broken flow.
6. Save and post (see Output). If asked for a nightly report, also mark posts done in the organic tracker.

## Approval rules
- Read only. Pausing, scaling or editing a campaign needs an explicit OK for that campaign, then use **meta-lead-form-ads**.
- Never copy lead names, emails or phone numbers into the report or the repo. Counts only.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Slack message, then the same text saved as `reports/YYYY-MM/YYYY-MM-DD-marketing.md` in the private workspace:

```
📊 Marketing — Tue 14 Jan (IST)
Needs action
1. Pause "Webinar – Broad" — ₹2,400 spent, 0 bookings, 41% junk leads [link]
2. Refresh creative on "Retarget – Video" — frequency 3.8 [link]
Paid (yesterday · 7 days)
Campaign | Spend | Leads | CPL | Verdict
Organic
Post | Reach | Comments | Guides sent
Next report: Wed 23:30 IST
```

## Done when
- [ ] Connection health checked
- [ ] Every active campaign has a verdict
- [ ] Actions ranked, each with a link
- [ ] Report saved and posted
