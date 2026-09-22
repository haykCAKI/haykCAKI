# haykCAKI

The GitHub profile repository for `haykCAKI` — the `README.md` rendered on the
profile page.

## Confidentiality

No client name and no link to a private repository may reach `README.md` or
`assets/*.svg`. `python3 scripts/check_confidential.py` enforces it against
`.github/confidential.json`: client words stored as SHA-256 hashes, and the
allowlist of public repos. Never write a client name in plain text anywhere in
this repo, including tests.

## Agent skills

### Issue tracker

Issues live as GitHub issues in `haykCAKI/haykCAKI`, managed with the `gh` CLI.
See `docs/agents/issue-tracker.md`.

### Triage labels

The five canonical triage roles, each label string equal to its name.
See `docs/agents/triage-labels.md`.

### Domain docs

Single-context — `CONTEXT.md` and `docs/adr/` at the repo root.
See `docs/agents/domain.md`.
