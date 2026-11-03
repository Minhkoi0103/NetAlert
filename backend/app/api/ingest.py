"""Routes for JSON or file ingestion will be defined here."""

from fastapi import APIRouter

router = APIRouter(prefix="/ingest", tags=["ingest"])
