# Local Development Setup

## Prerequisites

- Python 3.11+
- Node.js 20+
- Docker & Docker Compose (recommended)
- An [OpenAI API key](https://platform.openai.com/api-keys)

---

## Quick Start (Docker)

```bash
# 1. Clone the repository
git clone https://github.com/LAKSHMIPRASANNABOYILLA/AI-CRS.git
cd AI-CRS

# 2. Set your OpenAI API key
export OPENAI_API_KEY=sk-your-key-here

# 3. Start all services
docker compose up --build
```

| Service  | URL                         |
|----------|-----------------------------|
| Frontend | http://localhost:3000        |
| Backend  | http://localhost:8000        |
| API Docs | http://localhost:8000/docs   |

---

## Manual Setup (without Docker)

```bash
# 1. Run the setup script
./scripts/setup.sh

# 2. Edit backend/.env and set OPENAI_API_KEY

# 3. Start a local PostgreSQL database (or use Docker just for DB)
docker compose up db -d

# 4. Start all services
./scripts/start.sh local
```

---

## Running Tests

```bash
# Backend tests
cd backend
source .venv/bin/activate
pytest tests/ -v

# Frontend tests
cd frontend
npm test
```

---

## Environment Variables

### Backend (`backend/.env`)

| Variable                     | Description                     | Default              |
|------------------------------|---------------------------------|----------------------|
| `DATABASE_URL`               | PostgreSQL connection string    | (see .env.example)   |
| `OPENAI_API_KEY`             | Your OpenAI API key             | **required**         |
| `OPENAI_MODEL`               | GPT model to use                | `gpt-4o`             |
| `SECRET_KEY`                 | JWT signing secret              | **change in prod**   |
| `CORS_ORIGINS`               | Allowed frontend origins        | `http://localhost:3000` |

### Frontend (`frontend/.env`)

| Variable             | Description          | Default                        |
|----------------------|----------------------|--------------------------------|
| `REACT_APP_API_URL`  | Backend API base URL | `http://localhost:8000/api/v1` |
