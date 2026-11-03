"""Alert grouping contract. Grouping logic is not implemented."""

from app.schemas import AlertGroup, NormalizedEvent


def group_event(event: NormalizedEvent, existing: AlertGroup | None) -> AlertGroup:
    """Create or update an alert group for an event."""
    raise NotImplementedError("Implement grouping rules here")
