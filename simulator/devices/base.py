"""Contract shared by simulated devices."""

from typing import Protocol


class DeviceSimulator(Protocol):
    device_id: str

    def build_message(self, scenario: str) -> str:
        """Return one synthetic syslog message for a named scenario."""
        ...
