"""Base entity for the Pracht Alpha integration."""

from __future__ import annotations

from homeassistant.const import CONF_HOST
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import PrachtAlphaConfigEntry, PrachtAlphaDataUpdateCoordinator


_MONO_TRANSLATION_KEYS: frozenset[str] = frozenset(
    {
        "power_car1",
        "current_car1",
        "status_car1",
        "energy_car1",
        "car1_connected",
        "car1_charging",
        "max_current_car1",
        "lock_side1",
    }
)


class PrachtAlphaEntity(CoordinatorEntity[PrachtAlphaDataUpdateCoordinator]):
    """Defines a Pracht Alpha entity."""

    _attr_has_entity_name = True

    def __init__(
        self,
        *,
        entry: PrachtAlphaConfigEntry,
        coordinator: PrachtAlphaDataUpdateCoordinator,
        description: EntityDescription,
    ) -> None:
        """Initialize the Pracht Alpha entity."""
        super().__init__(coordinator=coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry.unique_id}_{description.key}"

        all_data = coordinator.data.all_data
        is_mono = all_data.num_charging_points == 1
        model = "Alpha MONO" if is_mono else "Alpha DUO"

        if is_mono and description.translation_key in _MONO_TRANSLATION_KEYS:
            self._attr_translation_key = f"{description.translation_key}_mono"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, all_data.device_id)},
            manufacturer="Pracht",
            model=model,
            name="Pracht Alpha",
            sw_version=all_data.software_version,
            hw_version=f"M{all_data.sw_version_main_pcb} R{all_data.sw_version_modbus_rfid}",
            configuration_url=f"http://{entry.data[CONF_HOST]}",
        )
