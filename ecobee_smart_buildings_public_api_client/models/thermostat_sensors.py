from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.thermostat_sensors_status import ThermostatSensorsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thermostat_sensors_data import ThermostatSensorsData


T = TypeVar("T", bound="ThermostatSensors")


@attr.s(auto_attribs=True)
class ThermostatSensors:
    """
    Attributes:
        status (Union[Unset, ThermostatSensorsStatus]):
        data (Union[Unset, ThermostatSensorsData]):
    """

    status: Union[Unset, ThermostatSensorsStatus] = UNSET
    data: Union[Unset, "ThermostatSensorsData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.thermostat_sensors_data import ThermostatSensorsData

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ThermostatSensorsStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ThermostatSensorsStatus(_status)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ThermostatSensorsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ThermostatSensorsData.from_dict(_data)

        thermostat_sensors = cls(
            status=status,
            data=data,
        )

        thermostat_sensors.additional_properties = d
        return thermostat_sensors

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
