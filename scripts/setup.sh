#!/usr/bin/env bash
# setup.sh – One-time local development environment setup

set -e

echo "==> AI-CRS Local Development Setup"

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "Python 3 is required. Aborting."; exit 1; }
command -v node    >/dev/null 2>&1 || { echo "Node.js is required. Aborting."; exit 1; }
command -v docker  >/dev/null 2>&1 || { echo "Docker is required. Aborting."; exit 1; }

# Backend
echo "==> Setting up backend..."
cd backend
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --quiet -r requirements.txt
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "  Created backend/.env from .env.example – please fill in your OPENAI_API_KEY"
fi
deactivate
cd ..

# Frontend
echo "==> Installing frontend dependencies..."
cd frontend
if [ ! -f ".env" ]; then
  cp .env.example .env
fi
npm install --silent
cd ..

echo ""
echo "Setup complete! Next steps:"
echo "  1. Edit backend/.env and set OPENAI_API_KEY"
echo "  2. Run ./scripts/start.sh  (or docker compose up)"
