# Civic Remediation System 🏙️

**AI agents that find civic problems, trace root causes, and secure funding to fix them.**

---

## Architecture

**Converging Singleton Pipeline** — Each stage selects ONE output to force focus:

1. **ONE Problem** → Highest impact civic issue
2. **ONE Root Cause** → The systemic failure point
3. **ONE Department** → Responsible government body
4. **ONE Solution** → Scalable technical intervention
5. **ONE Funding Source** → Matched grant or scheme

---

## Agents

| Agent | Role |
|-------|------|
| 🔭 **Sentinel** | Scans news/socials for high-impact civic failures |
| 🔎 **Investigator** | Identifies technical root cause |
| 🏛️ **Bureaucrat** | Maps responsible government body |
| 🛠️ **Engineer** | Designs modular technical solution |
| 🤝 **Liaison** | Finds matching funding sources |

---

## Stack

- **Framework**: [Agno](https://agno.com)
- **Model**: Perplexity / Mistral
- **Memory**: PostgreSQL + pgvector
- **Tracing**: LangWatch

---

## Quickstart

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install deps
uv sync

# Start database
docker compose up -d

# Run pipeline
uv run python -m app.main "Pollution of the Ganga River"

# Or use AgentOS UI
uv run -m app.agent_os
# Then visit os.agno.com
```

---

## Developer Setup

This repo uses MCP servers for enhanced DX:

- **Nia MCP** — Semantic codebase search & refactoring
- **Polydev MCP** — Persistent cross-session context

---

## Contributing

[**Join Discord**](https://discord.gg/g95mrWGm4G) · [**@AgentraLabs**](https://x.com/AgentraLabs)

MIT License
