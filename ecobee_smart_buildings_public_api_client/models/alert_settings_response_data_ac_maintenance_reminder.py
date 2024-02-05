from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.alert_settings_response_data_ac_maintenance_reminder_maintenance_interval_units import (
    AlertSettingsResponseDataAcMaintenanceReminderMaintenanceIntervalUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSettingsResponseDataAcMaintenanceReminder")


@attr.s(auto_attribs=True)
class AlertSettingsResponseDataAcMaintenanceReminder:
    """
    Attributes:
        last_maintenance_date (Union[Unset, str]):  Example: 2021-02-19.
        maintenance_interval (Union[Unset, float]):
        maintenance_interval_units (Union[Unset,
            AlertSettingsResponseDataAcMaintenanceReminderMaintenanceIntervalUnits]):
        enabled (Union[Unset, bool]):
        next_reminder_date (Union[Unset, str]):  Example: 2021-02-19.
    """

    last_maintenance_date: Union[Unset, str] = UNSET
    maintenance_interval: Union[Unset, float] = UNSET
    maintenance_interval_units: Union[
        Unset, AlertSettingsResponseDataAcMaintenanceReminderMaintenanceIntervalUnits
    ] = UNSET
    enabled: Union[Unset, bool] = UNSET
    next_reminder_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_maintenance_date = self.last_maintenance_date
        maintenance_interval = self.maintenance_interval
        maintenance_interval_units: Union[Unset, str] = UNSET
        if not isinstance(self.maintenance_interval_units, Unset):
            maintenance_interval_units = self.maintenance_interval_units.value

        enabled = self.enabled
        next_reminder_date = self.next_reminder_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_maintenance_date is not UNSET:
            field_dict["lastMaintenanceDate"] = last_maintenance_date
        if maintenance_interval is not UNSET:
            field_dict["maintenanceInterval"] = maintenance_interval
        if maintenance_interval_units is not UNSET:
            field_dict["maintenanceIntervalUnits"] = maintenance_interval_units
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if next_reminder_date is not UNSET:
            field_dict["nextReminderDate"] = next_reminder_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_maintenance_date = d.pop("lastMaintenanceDate", UNSET)

        maintenance_interval = d.pop("maintenanceInterval", UNSET)

        _maintenance_interval_units = d.pop("maintenanceIntervalUnits", UNSET)
        maintenance_interval_units: Union[Unset, AlertSettingsResponseDataAcMaintenanceReminderMaintenanceIntervalUnits]
        if isinstance(_maintenance_interval_units, Unset):
            maintenance_interval_units = UNSET
        else:
            maintenance_interval_units = AlertSettingsResponseDataAcMaintenanceReminderMaintenanceIntervalUnits(
                _maintenance_interval_units
            )

        enabled = d.pop("enabled", UNSET)

        next_reminder_date = d.pop("nextReminderDate", UNSET)

        alert_settings_response_data_ac_maintenance_reminder = cls(
            last_maintenance_date=last_maintenance_date,
            maintenance_interval=maintenance_interval,
            maintenance_interval_units=maintenance_interval_units,
            enabled=enabled,
            next_reminder_date=next_reminder_date,
        )

        alert_settings_response_data_ac_maintenance_reminder.additional_properties = d
        return alert_settings_response_data_ac_maintenance_reminder

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
