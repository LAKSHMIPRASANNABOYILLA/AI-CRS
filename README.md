# AI-CRS — AI-Powered Automatic Code Review System

An end-to-end system that uses **OpenAI GPT-4o** to automatically review code and provide detailed, actionable feedback on bugs, security issues, performance, and best practices.

## Features

- 🤖 AI-powered code reviews via OpenAI GPT-4o
- 🖊️ Monaco editor (VS Code in the browser) for code input
- 📊 Dashboard to track all submitted reviews
- 🔍 Severity-tagged comments (info / warning / error / critical)
- ⚡ Async review processing via FastAPI background tasks
- 🐳 One-command local dev with Docker Compose

## Quick Start

```bash
export OPENAI_API_KEY=sk-your-key-here
docker compose up --build
```

| Service  | URL                          |
|----------|------------------------------|
| Frontend | http://localhost:3000         |
| Backend  | http://localhost:8000         |
| API Docs | http://localhost:8000/docs    |

## Project Structure

```
AI-CRS/
├── backend/            # FastAPI Python API
│   ├── app/
│   │   ├── api/        # Route handlers
│   │   ├── core/       # Config & settings
│   │   ├── db/         # Database layer & migrations
│   │   ├── models/     # SQLAlchemy ORM models
│   │   ├── schemas/    # Pydantic request/response schemas
│   │   └── services/   # Business logic & AI integration
│   └── tests/          # Pytest test suite
├── frontend/           # React application
│   └── src/
│       ├── components/ # CodeEditor, ReviewPanel, Dashboard
│       ├── pages/      # HomePage, ReviewPage, DashboardPage
│       ├── services/   # API client
│       ├── hooks/      # Custom React hooks
│       └── utils/      # Helper utilities
├── ai/                 # AI prompt templates & model configs
├── database/           # SQL migrations & seed data
├── docs/               # Architecture, API & setup docs
├── scripts/            # setup.sh & start.sh
├── .github/workflows/  # CI pipeline
└── docker-compose.yml  # Local development orchestration
```

## Documentation

- [Setup Guide](docs/setup.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api.md)
