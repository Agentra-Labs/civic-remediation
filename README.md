# Civic Remediation System

A Multi-Agent Autonomous System for Civic Remediation, designed to bypass traditional bureaucratic delays by identifying, analyzing, and initiating private-sector solutions for systemic infrastructure failures.

## Overview

This system uses a team of autonomous AI agents to pipeline the process of civic remediation:

1.  **Ingestion (Sentinel)**: Identifies systemic failures from media.
2.  **Analysis (Analyst)**: Diagnoses root causes using scientific data.
3.  **Matching (Engineer)**: Finds private sector solutions/vendors.
4.  **Strategy (Strategist)**: Ranks vendors using MCDM algorithms.
5.  **Execution (Liaison)**: Drafts proposals and initiates contact (with human oversight).

## Tech Stack

- **Framework**: Agno
- **Language**: Python
- **Database**: PostgreSQL with PgVector
- **Monitoring/Testing**: LangWatch
- **Package Manager**: uv

## Setup

1.  **Install uv**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Install dependencies**:
    ```bash
    uv sync
    ```

3.  **Environment Variables**:
    Copy `.env.example` to `.env` and configure your API keys.

4.  **Run Tests**:
    ```bash
    uv run pytest
    ```

## System Architecture

The system uses an advanced **Multi-Agent Team** architecture:
- **Coordinator Agent**: Intelligently delegates tasks and synthesizes results.
- **Specialist Agents**: Sentinel, Analyst, Engineer, Strategist, Liaison.
- **Shared Memory**: All agents share context via PostgreSQL.
- **Knowledge Base**: RAG capabilities using PgVector for civic docs.
- **Reasoning**: All agents enable Chain-of-Thought (CoT) for complex problem solving.

## Prerequisites
- Python 3.12+
- `uv` package manager
- **Docker** (for PostgreSQL + PgVector)

### Start Database
The system requires a PostgreSQL database for memory and knowledge.
```bash
docker compose up -d
```

## Usage

### Run the Pipeline (Legacy Mode)
Run the sequential pipeline:
```bash
uv run python app/main.py "Pollution of the Ganga River"
```

### Run the Team (Advanced Mode)
Run the fully autonomous coordinated team:
```bash
uv run python app/main.py "Pollution of the Ganga River" team
```

### Dev Server / Playground
Start the FastAPI server:
```bash
uv run python app/serve.py
```
Open: **http://localhost:8000/docs**

### Run Scenario Tests
```bash
uv run pytest tests/scenarios/ -v
```
