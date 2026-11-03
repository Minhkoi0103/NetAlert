"""Persistence interface; SQL and migrations will be added later."""

from typing import Protocol

from app.schemas import AlertGroup, NormalizedEvent, RawEvent


class EventRepository(Protocol):
    def save_raw_event(self, event: RawEvent) -> int: ...

    def save_normalized_event(self, event: NormalizedEvent) -> int: ...

    def save_alert_group(self, group: AlertGroup) -> int: ...

    def list_events(self, limit: int, offset: int) -> list[NormalizedEvent]: ...
