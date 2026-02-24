# Architecture Overview

## System Components

```
┌─────────────────────────────────────────────────────┐
│                    User / Browser                   │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP
┌──────────────────────▼──────────────────────────────┐
│              Frontend (React, port 3000)            │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │  CodeEditor │  │ ReviewPanel  │  │ Dashboard  │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │ REST API
┌──────────────────────▼──────────────────────────────┐
│              Backend (FastAPI, port 8000)           │
│  ┌──────────┐  ┌─────────────┐  ┌───────────────┐   │
│  │  Routes  │  │  Services   │  │  AI Service   │   │
│  └──────────┘  └─────────────┘  └───────┬───────┘   │
└────────────────────────────────────────┼────────────┘
                                         │ OpenAI API
┌────────────────────────────────────────▼────────────┐
│                PostgreSQL Database                  │
└─────────────────────────────────────────────────────┘
```

## Data Flow

1. User submits code via the **CodeEditor** component.
2. Frontend calls `POST /api/v1/reviews` on the Backend.
3. Backend creates a `Review` record (status=`pending`) and triggers a background task.
4. Background task calls the **AIService** which sends the code to OpenAI GPT-4o.
5. GPT-4o returns a structured JSON review (summary + comments).
6. Backend stores comments in `review_comments` and updates status to `completed`.
7. Frontend polls or refetches the review and shows results in **ReviewPanel**.

## Directory Structure

```
AI-CRS/
├── backend/        # FastAPI Python backend
├── frontend/       # React frontend
├── ai/             # AI prompt templates & utilities
├── database/       # SQL migrations & seed data
├── docs/           # Documentation
├── scripts/        # Setup & start scripts
├── .github/        # CI/CD workflows
└── docker-compose.yml
```
