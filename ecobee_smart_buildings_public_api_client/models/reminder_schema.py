from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reminder_schema_maintenance_interval_units import ReminderSchemaMaintenanceIntervalUnits
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderSchema")


@attr.s(auto_attribs=True)
class ReminderSchema:
    """
    Attributes:
        last_maintenance_date (Union[Unset, str]):  Example: 2021-02-19.
        maintenance_interval (Union[Unset, float]):
        maintenance_interval_units (Union[Unset, ReminderSchemaMaintenanceIntervalUnits]):
        enabled (Union[Unset, bool]):
    """

    last_maintenance_date: Union[Unset, str] = UNSET
    maintenance_interval: Union[Unset, float] = UNSET
    maintenance_interval_units: Union[Unset, ReminderSchemaMaintenanceIntervalUnits] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_maintenance_date = self.last_maintenance_date
        maintenance_interval = self.maintenance_interval
        maintenance_interval_units: Union[Unset, str] = UNSET
        if not isinstance(self.maintenance_interval_units, Unset):
            maintenance_interval_units = self.maintenance_interval_units.value

        enabled = self.enabled

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_maintenance_date = d.pop("lastMaintenanceDate", UNSET)

        maintenance_interval = d.pop("maintenanceInterval", UNSET)

        _maintenance_interval_units = d.pop("maintenanceIntervalUnits", UNSET)
        maintenance_interval_units: Union[Unset, ReminderSchemaMaintenanceIntervalUnits]
        if isinstance(_maintenance_interval_units, Unset):
            maintenance_interval_units = UNSET
        else:
            maintenance_interval_units = ReminderSchemaMaintenanceIntervalUnits(_maintenance_interval_units)

        enabled = d.pop("enabled", UNSET)

        reminder_schema = cls(
            last_maintenance_date=last_maintenance_date,
            maintenance_interval=maintenance_interval,
            maintenance_interval_units=maintenance_interval_units,
            enabled=enabled,
        )

        reminder_schema.additional_properties = d
        return reminder_schema

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
