# NetAlert agent rules

These instructions apply to work in this repository. The full team policy is [Quy định làm việc nhóm và GitHub](https://nguyenduyminhnt2503.atlassian.net/wiki/pages/2588933). Follow the user's current request when it is more specific.

## Project boundaries

- NetAlert is a lab PoC for router, switch, and firewall alerts. The three required input paths are Syslog UDP, JSON REST API, and JSON sample-file import.
- Use synthetic or explicitly approved and sanitized data. Do not access, scan, configure, or modify production devices. Do not commit credentials, real `.env` files, local logs, or unapproved network data.
- The agreed stack is Python/FastAPI, an asyncio UDP collector, PostgreSQL, React/TypeScript, Docker Compose, pytest, and GitHub. Device simulators use Python in Docker containers.
- The Project Charter and meeting minutes hold the work calendar. Do not duplicate work-hour and holiday rules in tickets or other documents.

## Before and during a task

1. Read the Jira `NETALERT-*` ticket, its acceptance criteria, assignee, priority, dates, and `Blocks` links. Check the relevant Confluence specification before changing behavior or interfaces.
2. Keep one accountable owner per ticket. Record a newly discovered blocker as a Jira issue link with the correct direction; describe its impact in the ticket.
3. Use the existing Jira workflow: Backlog -> Selected for Development -> In Progress -> IN REVIEW -> Done. Reflect actual progress; a planned date alone does not mean work has started.
4. If scope, API/schema, severity mapping, grouping rules, or report format changes, update the relevant specification and record the decision with its real decision date. Do not rewrite an old meeting record as though a later decision happened at that meeting.
5. Do not claim mentor/UTH approval or a quantitative KPI before the approval or baseline evidence exists.

## Git and Pull Requests

- Keep `main` demo-ready. If the repository has no initial `main` commit yet, the Leader handles that bootstrap as a separate task, then enables branch protection. After bootstrap, do not push, force-push, or commit directly to `main`. For agent-created branches, use `codex/NETALERT-<number>-<short-topic>`; human team branches may use `feature/`, `fix/`, or `docs/` with the Jira key.
- Usually make one PR per Jira ticket. Put the Jira URL, change summary, verification commands/results, and any API/schema/Compose impact in the PR description. Add screenshots or other evidence for UI changes.
- Request at least one technical review from someone other than the author. QA checks functional acceptance where applicable. Resolve review comments and pass relevant checks before squash merge.
- Do not infer that GitHub closing keywords will close Jira tickets. Update Jira status only after review, merge, and applicable QA evidence.

### Commit format

Use `<type>(<scope>): <short summary> [NETALERT-<number>]`; `scope` is optional. Keep the Jira key in the first line. Suggested scopes: `simulator`, `collector`, `parser`, `api`, `storage`, `rules`, `frontend`, `infra`.

Allowed types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `style`, `build`, `ci`, `chore`, `revert`. Use `style` for code formatting only, not a UI feature. For incompatible API/schema changes, add `!` before `:` and a `BREAKING CHANGE:` footer explaining the migration.

Examples:

```text
feat(simulator): send router syslog over UDP [NETALERT-27]
fix(parser): handle missing severity [NETALERT-30]
docs(infra): document Docker lab setup [NETALERT-19]
```

## Verification and completion

- Run meaningful tests for changed behavior. Use relevant `pytest` tests for backend code, the configured frontend build/tests for frontend code, and Docker Compose configuration or lab smoke checks for service changes. If CI is unavailable, record manual commands and results in the PR.
- A code ticket is Done only when its PR is reviewed and merged, applicable tests and QA checks pass, documentation is updated, and evidence is linked in Jira. For documentation-only work, link the reviewed document and record unresolved questions accurately.
- Create a separate Bug for a defect outside a small fix within the current ticket. Include reproduction steps, expected and actual behavior, and a Jira link to the affected work.
