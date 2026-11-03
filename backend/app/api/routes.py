"""API routes; ingestion and query endpoints will be added by the team."""

from fastapi import APIRouter

from app.api import alerts, events, ingest, stats

router = APIRouter()
router.include_router(ingest.router)
router.include_router(events.router)
router.include_router(alerts.router)
router.include_router(stats.router)


@router.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Indicate that the API process is running."""
    return {"status": "ok"}
