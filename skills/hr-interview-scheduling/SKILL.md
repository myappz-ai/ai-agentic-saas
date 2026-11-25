---
name: hr-interview-scheduling
description: "Schedule interviews and internal meetings: find slots that work for interviewers and candidates, create a booking link or event type, draft invites with the agenda and joining details, send reminders, and collect interviewer scorecards after. Use when asked to set up interviews, book a meeting with a candidate, reschedule, or collect interview feedback. Invites to outside people need an OK."
---

# Interview scheduling

Interviews that happen on time with prepared interviewers and written feedback within a day.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Calendar connector (Google or Outlook): free/busy and events
- Account connector: `list_event_types`, `create_calendar_event_type` (a booking link for interview slots)
- Email connector: draft invites and reminders

## Steps
1. **Panel and length**: who interviews, 30 or 45 minutes, video link source.
2. **Slots**: read free/busy for the panel over the next 5 working days, in the candidate's and the panel's time zones. Offer 3 slots, or a booking link limited to those windows.
3. **Invite draft**: role, time with zone, who they'll meet, agenda, what to prepare, how to reschedule.
4. **Prep for interviewers**: CV link (private tracker), scorecard, 3 questions per criterion.
5. **Reminders**: 24h and 1h before (drafts or calendar reminders).
6. **After**: ask each interviewer for their scorecard within 24h; chase once; update the tracker.

## Approval rules
- Sending invites to candidates needs an OK unless the owner has authorised standard interview invites in writing.
- Never move an interviewer's existing meetings.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
📆 Interview — Candidate A, Support Executive
Proposed: Tue 21 Jan 11:00 IST · Wed 22 Jan 15:00 IST · Thu 23 Jan 10:30 IST
Panel: Ops lead, Support lead · 45 min · video
Invite draft ready — approve to send?
```

## Done when
- [ ] Times shown with zones
- [ ] Panel has scorecards
- [ ] Feedback collected within 24h
