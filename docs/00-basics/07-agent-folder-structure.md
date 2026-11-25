# 07 · How every agent folder is built

Keep each department's own records (in your private workspace, not in this kit) in the same structure, so any person or agent can pick up any department.

```
agents/<nn>-<department>/
├── README.md       who the agent is, what it owns, connectors, rules
├── sops/           one file per process (owner, status, area, last updated)
├── scripts/        approved wording for messages and calls
├── reports/YYYY-MM/  one file per run, e.g. 2026-11-23-morning.md
├── decisions.md    dated decisions and why, newest first
└── learnings.md    what it learned about tools and process
```

To add a department: copy [template/](../../template) to `agents/<nn>-<name>/` in your private workspace and fill the README.
