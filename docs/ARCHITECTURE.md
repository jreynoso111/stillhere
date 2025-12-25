# Architecture Overview

## High-Level Flow
- **Frontend** → sends requests to the API for case creation, lookup, and health checks.
- **API (FastAPI)** → validates requests, handles routing, and exposes versioned endpoints.
- **Services Layer** → contains business logic for cases, notifications, and background workflows.
- **Database (PostgreSQL via Supabase)** → stores case records and audit details.
- **Storage (Planned)** → will handle media assets (photos, documents) associated with cases.

## Module Responsibilities
- `app/api/` — request/response schemas and routers for public endpoints.
- `app/services/` — core business logic (validation, workflows, integrations).
- `app/models/` — data models and DTOs.
- `app/data/` — persistence helpers, queries, and seed scripts.
- `app/utils/` — shared helpers (logging, settings, error handling).
- `app/main.py` — application factory and bootstrapping.

## Security Notes
- **Row-Level Security (RLS):** enable RLS policies in Supabase to ensure least-privilege access by default.
- **Minimal Data Retention:** store only the data required for case resolution; schedule periodic reviews to prune obsolete records.
- **Transport Security:** require HTTPS for all client traffic and secure database connections (TLS) where supported.
- **Secrets Management:** load secrets from environment variables; avoid committing secrets to the repository.
