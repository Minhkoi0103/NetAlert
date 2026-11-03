"""Syslog/UDP collector contract. Network listening is not implemented."""

from app.schemas import RawEvent


async def collect_syslog(payload: bytes, sender: str) -> RawEvent:
    """Convert one received datagram into a RawEvent."""
    raise NotImplementedError("Implement syslog collection in this module")
