---
name: marketing-youtube-publishing
description: "Publish and optimise YouTube videos: SEO titles, descriptions with a call-to-action link, chapters, tags, playlists, thumbnails text and a pinned CTA comment. Use when asked to upload videos, fix titles or descriptions, organise a playlist or course series, add a CTA to videos, or schedule comments. Drafts first; publishing or changing public metadata needs an OK unless a standing authorization covers it."
---

# YouTube publishing

Turns raw uploads or a playlist into a searchable series that sends viewers to one clear next step.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- YouTube connector: list videos and playlists, update video metadata, add to playlist, post and pin comments
- Account connector: `create_short_link` (trackable CTA link), `get_business_profile` (offer and brand voice)
- Private workspace: the content tracker

## Steps
1. **Inventory.** List the videos in scope (a playlist, a date range or the IDs given). Note current title, description, privacy status and views.
2. **One CTA.** Ask for, or read from the business profile, the single next step (book a call, free guide, course). Make a short link with `create_short_link` so clicks can be counted.
3. **Draft per video:** title under 70 characters with the main search phrase first; description of 2 short paragraphs, the CTA link in the first 2 lines, chapters (`00:00` style) when the video is over 5 minutes, 3–5 hashtags; one pinned comment that repeats the CTA.
4. **Series order.** For a course or lesson series, number the titles ("Lesson 3 – …") and set the playlist order to match.
5. **Show the drafts** as a table (old title → new title, CTA, playlist). Apply only after the OK, then re-read each video to confirm the change stuck.
6. **Shorts:** links in Shorts descriptions are not clickable. Put the CTA in the pinned comment and point to the related long video.

## Approval rules
- Draft first. Publishing, changing privacy or editing public titles needs an OK, unless the owner has written a standing authorization for this series (quote it, see `docs/ROUTINES.md`).
- Respect API quota: batch updates and stop with a clear note if the quota runs out; resume next run.
- Never delete videos or comments without an explicit OK naming them.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Table in chat or Slack: `# | Video | Old title | New title | CTA link | Status (drafted / applied / failed)`, then a line with totals. Save to `reports/YYYY-MM/YYYY-MM-DD-youtube.md`.

## Done when
- [ ] Every video in scope has a draft
- [ ] CTA link is trackable
- [ ] Changes applied only after OK, and re-checked
