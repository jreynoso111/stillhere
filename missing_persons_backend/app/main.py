"""Entry point for the missing persons backend service."""

from __future__ import annotations

from fastapi import FastAPI

from app.api.cases import router as cases_router


def create_app() -> FastAPI:
    """Configure and return the FastAPI application instance."""

    # Indicate that this file serves as the starting point for the backend project.
    # Future configuration, middleware, and routes will build on this initial setup.
    application = FastAPI(title="Missing Persons Backend")
    # Register routers to expose the API endpoints for different domains (e.g., cases).
    application.include_router(cases_router)
    return application


app = create_app()


def main() -> None:
    """Run the FastAPI application with Uvicorn."""

    import uvicorn

    # Launch the application with hot reload enabled for development convenience.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
