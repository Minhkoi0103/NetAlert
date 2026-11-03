"""Threshold contract. Threshold evaluation is not implemented."""

from app.schemas import AlertGroup


def threshold_exceeded(group: AlertGroup) -> bool:
    """Evaluate a group against a configured threshold."""
    raise NotImplementedError("Implement threshold evaluation here")
