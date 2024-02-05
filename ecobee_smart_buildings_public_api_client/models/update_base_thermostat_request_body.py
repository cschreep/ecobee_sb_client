from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBaseThermostatRequestBody")


@attr.s(auto_attribs=True)
class UpdateBaseThermostatRequestBody:
    """
    Attributes:
        name (Union[Unset, str]): The name shown in the SmartBuildings web portal or mobile application. This can be set
            to a different value than what is shown on the thermostat as desired.
        thermostat_name (Union[Unset, str]): The name shown on the physical thermostat. This can be set to a different
            value than what is shown in the SmartBuildings web portal or mobile application as desired.
    """

    name: Union[Unset, str] = UNSET
    thermostat_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        thermostat_name = self.thermostat_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if thermostat_name is not UNSET:
            field_dict["thermostatName"] = thermostat_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        thermostat_name = d.pop("thermostatName", UNSET)

        update_base_thermostat_request_body = cls(
            name=name,
            thermostat_name=thermostat_name,
        )

        update_base_thermostat_request_body.additional_properties = d
        return update_base_thermostat_request_body

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
