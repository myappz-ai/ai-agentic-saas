---
name: hr-hiring-pipeline
description: "Run hiring for a role: write the job description and scorecard, draft the job post, screen applications against the scorecard, track candidates by stage, draft candidate emails, and post a weekly hiring update. Use when asked to hire, write a JD, screen CVs or resumes, shortlist candidates, check where candidates stand, or for a hiring report. Never rejects, offers or messages a candidate without an OK."
---

# Hiring pipeline

A fair, fast hiring process with a written scorecard, so decisions are about evidence, not memory.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Email connector: read applications, draft replies
- Account connector (optional): `create_pipeline` for a Hiring pipeline, `query_opportunities`, `create_form` for an application form, `create_page` for a careers page
- Drive or Sheets: the candidate tracker (private, access limited to the hiring team)

## Steps
1. **Role brief**: title, outcomes in the first 90 days, must-haves, nice-to-haves, pay band (kept private), location and hours.
2. **Scorecard**: 4–6 criteria, each scored 1–4 with what a 4 looks like.
3. **Job post** draft: outcomes first, then requirements, how to apply. Inclusive language, no age or gender wording.
4. **Screen** each application against the scorecard with a one-line reason per score. Mark "needs human look" when unsure.
5. **Stages**: applied → screened → interview 1 → task → interview 2 → offer → hired / rejected. Track in the private tracker or a Hiring pipeline.
6. **Emails** (drafts): acknowledgement, interview invite (hand to hr-interview-scheduling), task brief, polite rejection, offer (owner writes the numbers).
7. **Weekly update** to the hiring channel.

## Approval rules
- Rejections, offers and any candidate message need an OK.
- Candidate CVs, phone numbers and salary data never go into git or public channels. Use the private tracker.
- Don't score on age, gender, religion, photos or other protected traits.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
👥 Hiring — Support Executive (week 2)
Applied 46 · Screened 46 · Interview 1: 6 · Task: 3 · Offer: 0
Top 3 by scorecard: Candidate A (15/16), B (14), C (13) [tracker]
Drafts to approve: 5 invites, 31 rejections
Next: interviews Tue–Wed
```

## Done when
- [ ] Scorecard written before screening
- [ ] Every candidate has a stage and a reason
- [ ] Nothing sent without OK
