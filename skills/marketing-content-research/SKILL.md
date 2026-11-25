---
name: marketing-content-research
description: "Morning content research: watch chosen creators for posts going viral and scan official news sources from the last 48 hours, then turn the best items into scroll-stopping hooks and post ideas with a call to action. Use when asked for content ideas, trending topics, what competitors posted, viral posts to remix, or a daily idea digest. Never posts anything; output is one message."
---

# Content research

Feeds the posting calendar with a short list of strong, sourced ideas every morning.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- A web reader or scraping connector for public posts and news pages
- Account connector: `get_business_brief` (audience and offer)
- Private workspace: `creators.json` (accounts and thresholds) and `queue.json` (ideas already used)
- Slack: one message per run

## Steps
1. **Read the brief**: audience, offer, banned topics. Read `queue.json` so you don't repeat an idea.
2. **Viral watch.** For each creator in `creators.json`, fetch posts from the last 48 hours. Flag any over the thresholds (for example 1,000 likes or 200 comments). Keep a running list of the accounts.
3. **News scan.** Read only the official sources listed in the brief (product blogs, release notes, newsroom pages) for items from the last 48 hours. Skip rumours and reposts.
4. **Score** each item 1–5 for audience fit and novelty. Keep the top 3–5.
5. **Write** for each: a hook (under 12 words), the angle for this audience, format (carousel, reel, short), and a comment keyword plus gift idea for the CTA.
6. Add the picks to `queue.json` with status `suggested`.

## Approval rules
- Never post, comment, follow or DM. Research only.
- Credit the source; never copy someone else's post word for word.
- Only public pages; no logged-in scraping of private accounts.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
One Slack message:

```
🔥 Ideas — Wed 15 Jan, 06:15 IST
1. Hook: "Your agency doesn't need more clients" · Carousel · Keyword: SYSTEM
   Why: new automation feature launched yesterday [source link]
2. …
Viral this morning: @example_creator reel, 4.2k likes [link]
```

## Done when
- [ ] Sources are from the last 48 hours and linked
- [ ] No idea repeats one in queue.json
- [ ] Nothing was posted
