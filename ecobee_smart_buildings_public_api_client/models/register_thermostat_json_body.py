from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RegisterThermostatJsonBody")


@attr.s(auto_attribs=True)
class RegisterThermostatJsonBody:
    """The unique identifier for a thermostat. ID will match the serial number on the physical thermostat.

    Attributes:
        thermostat_id (str): The unique identifier for a thermostat. The ID will match the serial number on the physical
            thermostat.
    """

    thermostat_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thermostat_id = self.thermostat_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thermostatId": thermostat_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thermostat_id = d.pop("thermostatId")

        register_thermostat_json_body = cls(
            thermostat_id=thermostat_id,
        )

        register_thermostat_json_body.additional_properties = d
        return register_thermostat_json_body

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
