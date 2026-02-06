## Summary

Describe the **one** change this PR makes and why it matters to civic remediation.

- Type of change: bug fix / feature / docs / refactor / infra
- Scope: pipeline / agents / prompts / infra / docs / UI / other

---

## Context & motivation

Why is this change needed?

- What problem or limitation does it address?
- Is it linked to an existing issue? (e.g. #123)
- How does it help real-world civic remediation use cases?

---

## Changes

Briefly list the key changes.

- Code / config:
- Agents / prompts:
- Docs / examples:
- Other:

If relevant, mention any new commands, configs, or flags.

---

## Impact on the Singleton Pipeline

Does this PR affect any stages of the pipeline?

- Sentinel (Problem selection): yes / no — if yes, how?
- Investigator (Root-cause analysis): yes / no — if yes, how?
- Bureaucrat (Department mapping): yes / no — if yes, how?
- Engineer (Solution design): yes / no — if yes, how?
- Liaison (Funding search): yes / no — if yes, how?
- AgentOS / UI / infra: yes / no — if yes, how?

Note any expected behavior changes, new assumptions, or limitations.

---

## Testing

Explain how you tested this PR. Include copy-pasteable commands.

1. Setup:
   ```bash
   uv sync
   docker compose up -d
   ```
2. Run:
   ```bash
   uv run python -m app.main "Pollution of the Ganga River"
   ```
3. Observed behavior:
   - [ ] Describe what you saw and how it differs from main.

Add logs or screenshots if they clarify behavior.

---

## Breaking changes / migration

- Does this PR change public APIs, configs, or expected inputs? yes / no  
  - If yes, describe what users need to do to upgrade.

---

## Checklist

- [ ] My PR focuses on **one** cohesive change.
- [ ] I ran the relevant tests and pipeline flows locally.
- [ ] I updated docs, prompts, or comments where behavior changed.
- [ ] I added or updated tests where it makes sense.
- [ ] No secrets, API keys, or private data are included.
- [ ] Linked related issues or discussions (if any).
