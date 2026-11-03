"""Switch message templates will be implemented here."""

from simulator.devices.base import DeviceSimulator


class SwitchSimulator(DeviceSimulator):
    device_id: str

    def build_message(self, scenario: str) -> str:
        raise NotImplementedError("Add switch scenarios here")
