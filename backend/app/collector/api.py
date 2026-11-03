"""JSON ingestion contract. Validation and processing are not implemented."""

from app.schemas import RawEvent


def collect_api(payload: dict[str, object]) -> RawEvent:
    """Convert one JSON payload into a RawEvent."""
    raise NotImplementedError("Implement API ingestion here")
