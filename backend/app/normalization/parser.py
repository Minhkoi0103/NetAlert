"""Parser contract. Mapping rules are not implemented."""

from app.schemas import NormalizedEvent, RawEvent


def normalize_event(event: RawEvent) -> NormalizedEvent:
    """Map a raw event to the shared event schema."""
    raise NotImplementedError("Implement parsing and normalization here")
