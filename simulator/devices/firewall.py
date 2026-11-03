"""Firewall message templates will be implemented here."""

from simulator.devices.base import DeviceSimulator


class FirewallSimulator(DeviceSimulator):
    device_id: str

    def build_message(self, scenario: str) -> str:
        raise NotImplementedError("Add firewall scenarios here")
