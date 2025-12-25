# Roadmap

## Phase 1: MVP
- [ ] Implement CRUD endpoints for cases with basic validation.
- [ ] Persist cases to PostgreSQL (Supabase) with RLS enabled.
- [ ] Add auth hook (token verification stub) for protected routes.
- [ ] Document environment variables and local runbook updates.

## Phase 2: Moderation & Safety
- [ ] Add content moderation workflow (flagging and manual review).
- [ ] Introduce rate limiting and abuse detection for public endpoints.
- [ ] Add audit logs for create/update/delete operations.
- [ ] Configure alerting for error rates and unusual traffic patterns.

## Phase 3: Match Engine
- [ ] Implement candidate matching between reports and sightings.
- [ ] Add background jobs for periodic re-scoring of matches.
- [ ] Expose match insights via dedicated endpoints and dashboards.
- [ ] Evaluate and integrate storage for media-backed matching signals.
