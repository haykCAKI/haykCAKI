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

<!-- cto-cakis:begin -->
## cto-cakis
- test: `python3 -m unittest discover -s tests && python3 scripts/check_confidential.py`
- verify: CI `readme-check` green (lychee link check), then the README on the branch view on github.com renders the card and every link opens
- stack: markdown + hand-written SVG; Python stdlib scripts
- client: no
- graph: no
<!-- cto-cakis:end -->
