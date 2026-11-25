# Routines: how scheduled work runs

Most skills in this kit run on a schedule (a Grok Bot routine, a Claude Code routine or a cron job). These rules keep unattended runs safe.

## Rules for every routine
- **Unattended means no questions.** The run reads its instructions, does the work and posts one message. If something is missing, it says what is missing in that message.
- **Standing authorizations are quoted, not stretched.** If the owner said "post the 8 AM carousel without asking", save that sentence, with its date, in the private workspace (`decisions.md`) and have the routine quote it. Anything outside the quote still needs an OK.
- **One output per run**: one Slack message (or email) plus a report file in the private workspace under `reports/YYYY-MM/`.
- **Times in the owner's time zone**, with the zone named (for example "10:00 IST").
- **Errors are reported once.** Tell the owner or developer about a new platform error straight away, and at most once per distinct error per day.
- **Read before write.** Every routine checks the account connection first (Step 0) and stops with a clear message if it fails.

## Typical schedule (adjust to your business)

| Time | Routine | Skill |
| --- | --- | --- |
| 06:15 | Content research: trends and news to hooks | marketing-content-research |
| 08:00 | CEO morning brief (weekdays) | ceo-daily-brief |
| 08:00, 15:00, 20:00 | Organic posts with comment-to-DM | organic-marketing |
| 10:00 and 17:30 | Booking report across accounts | sales-booking-report |
| 11:00 | Ads performance check | marketing-performance-report |
| 12:00 Mon | Pipeline review | sales-pipeline-review |
| 18:00 | Support and bug digest | ops-support-triage |
| 10:00 Mon | Collections list | finance-collections |
| 10:00 Fri | Hiring pipeline update | hr-hiring-pipeline |
| 23:30 | Nightly marketing report | marketing-performance-report |
| 1st of month | Revenue, expense and tax pack | finance-revenue-report, finance-expense-report, finance-tax-pack |
