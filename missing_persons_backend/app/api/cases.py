"""Endpoints related to missing persons cases."""

from __future__ import annotations

from fastapi import APIRouter

# Initialize a router dedicated to case-related endpoints.
router = APIRouter(prefix="/cases", tags=["cases"])


@router.get("/ping")
async def ping() -> dict[str, str]:
    """Simple health check for the case service."""

    # Provide a clear message that the backend project has begun and is reachable.
    return {"message": "Case service is operational — initial backend project setup in progress"}
