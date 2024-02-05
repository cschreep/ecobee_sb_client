from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.base_hold_type import BaseHoldType

T = TypeVar("T", bound="TemperatureHoldRequestBody")


@attr.s(auto_attribs=True)
class TemperatureHoldRequestBody:
    """
    Attributes:
        desired_temperature (float):
        type (BaseHoldType): An 'indefinite' hold indicates that the hold will continue until cancelled. A
            'nextTransition' hold indicates that the hold will continue only until the next climate change on the thermostat
            schedule, eg, when the thermostat switches from 'away' to 'home'
    """

    desired_temperature: float
    type: BaseHoldType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desired_temperature = self.desired_temperature
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desiredTemperature": desired_temperature,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desired_temperature = d.pop("desiredTemperature")

        type = BaseHoldType(d.pop("type"))

        temperature_hold_request_body = cls(
            desired_temperature=desired_temperature,
            type=type,
        )

        temperature_hold_request_body.additional_properties = d
        return temperature_hold_request_body

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
