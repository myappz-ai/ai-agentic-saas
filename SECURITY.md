# Security policy

## Supported versions

Only the latest release and the `main` branch get fixes.

## Report a problem privately

Do not open a public issue for a security problem. Use GitHub's private reporting instead:

1. Open the **Security** tab of this repository.
2. Choose **Report a vulnerability** (https://github.com/myappz-ai/ai-agentic-saas/security/advisories/new).
3. Say what you found, where (file and line or link), and how to reproduce it.

You should get a first reply within 5 working days. Please give us a reasonable time to fix it before you share details publicly.

## What to report

- A secret, connection link or personal data committed to the repository or its history.
- A skill, hook or manifest that could make an agent send, post, spend or delete without the user's explicit OK.
- A hook or script that runs unexpected commands on a user's machine.
- A CI workflow that could leak secrets or be abused from a pull request.

## Found a secret or personal data in this repository?

Report it privately as above, even if it looks old. Do not copy it into the report. We remove it, rotate anything that could still work, and clean the history where needed.
