from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.thermostat_status_status import ThermostatStatusStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thermostat_status_data import ThermostatStatusData


T = TypeVar("T", bound="ThermostatStatus")


@attr.s(auto_attribs=True)
class ThermostatStatus:
    """
    Attributes:
        status (Union[Unset, ThermostatStatusStatus]):
        data (Union[Unset, ThermostatStatusData]):
    """

    status: Union[Unset, ThermostatStatusStatus] = UNSET
    data: Union[Unset, "ThermostatStatusData"] = UNSET
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
        from ..models.thermostat_status_data import ThermostatStatusData

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ThermostatStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ThermostatStatusStatus(_status)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ThermostatStatusData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ThermostatStatusData.from_dict(_data)

        thermostat_status = cls(
            status=status,
            data=data,
        )

        thermostat_status.additional_properties = d
        return thermostat_status

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
