# Missing Persons Backend

Backend service for a missing persons platform, providing APIs to manage and retrieve case information.

## Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL (via Supabase)
- **Storage:** Planned integration for asset storage

## Local Setup
1. Create and activate a virtual environment:
   - `python -m venv .venv`
   - On macOS/Linux: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Copy environment variables template: `cp .env.example .env` (or `copy .env.example .env` on Windows)
4. Run the development server: `uvicorn app.main:app --reload`

## Current Endpoints
- `GET /cases/ping` — health check for the case service.

## Folder Structure
- `missing_persons_backend/` — Python package for the backend service.
  - `app/` — application code.
    - `api/` — FastAPI routers and endpoints.
    - `data/` — data access and seed helpers.
    - `models/` — data models and schemas.
    - `services/` — business logic and service layer.
    - `utils/` — shared utilities.
    - `main.py` — FastAPI application factory and entry point.
- `requirements.txt` — project dependencies.
