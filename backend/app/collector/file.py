"""File ingestion contract. File reading is not implemented."""

from pathlib import Path

from app.schemas import RawEvent


def collect_file(path: Path) -> list[RawEvent]:
    """Read a sample file into raw events."""
    raise NotImplementedError("Implement file ingestion in this module")
