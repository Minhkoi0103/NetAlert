"""Shared data contracts; refine fields with the team before implementation."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


SourceType = Literal["syslog_udp", "file", "api"]
DeviceType = Literal["router", "switch", "firewall"]


class RawEvent(BaseModel):
    source_type: SourceType
    received_at: datetime
    raw_message: str
    sender: str | None = None
    device_hint: str | None = None


class NormalizedEvent(BaseModel):
    raw_event_id: int | None = None
    device_id: str
    device_type: DeviceType
    event_time: datetime
    severity: str  # TODO: agree on the shared severity values.
    event_type: str
    message: str


class AlertGroup(BaseModel):
    group_key: str
    first_seen: datetime
    last_seen: datetime
    count: int
    severity: str
    rule_id: str
