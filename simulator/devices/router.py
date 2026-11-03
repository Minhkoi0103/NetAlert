"""Router message templates will be implemented here."""

from simulator.devices.base import DeviceSimulator


class RouterSimulator(DeviceSimulator):
    device_id: str

    def build_message(self, scenario: str) -> str:
        raise NotImplementedError("Add router scenarios here")
