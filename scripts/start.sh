#!/usr/bin/env bash
# start.sh – Start all services for local development

set -e

MODE=${1:-docker}

if [ "$MODE" = "docker" ]; then
  echo "==> Starting services with Docker Compose..."
  docker compose up --build
else
  echo "==> Starting services without Docker (manual mode)..."

  # Start backend
  echo "  Starting backend on http://localhost:8000 ..."
  cd backend
  source .venv/bin/activate
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &
  BACKEND_PID=$!
  deactivate
  cd ..

  # Start frontend
  echo "  Starting frontend on http://localhost:3000 ..."
  cd frontend
  npm start &
  FRONTEND_PID=$!
  cd ..

  echo ""
  echo "Services running:"
  echo "  Backend:  http://localhost:8000  (PID $BACKEND_PID)"
  echo "  Frontend: http://localhost:3000  (PID $FRONTEND_PID)"
  echo "  API Docs: http://localhost:8000/docs"
  echo ""
  echo "Press Ctrl+C to stop all services."
  wait
fi
