from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_hold_type import BaseHoldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemperatureHoldResponseData")


@attr.s(auto_attribs=True)
class TemperatureHoldResponseData:
    """
    Attributes:
        desired_temperature (Union[Unset, float]):
        type (Union[Unset, BaseHoldType]): An 'indefinite' hold indicates that the hold will continue until cancelled. A
            'nextTransition' hold indicates that the hold will continue only until the next climate change on the thermostat
            schedule, eg, when the thermostat switches from 'away' to 'home'
    """

    desired_temperature: Union[Unset, float] = UNSET
    type: Union[Unset, BaseHoldType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desired_temperature = self.desired_temperature
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desired_temperature is not UNSET:
            field_dict["desiredTemperature"] = desired_temperature
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desired_temperature = d.pop("desiredTemperature", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, BaseHoldType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BaseHoldType(_type)

        temperature_hold_response_data = cls(
            desired_temperature=desired_temperature,
            type=type,
        )

        temperature_hold_response_data.additional_properties = d
        return temperature_hold_response_data

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
