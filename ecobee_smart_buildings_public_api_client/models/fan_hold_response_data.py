from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_hold_type import BaseHoldType
from ..models.fan_hold_status import FanHoldStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FanHoldResponseData")


@attr.s(auto_attribs=True)
class FanHoldResponseData:
    """
    Attributes:
        fan (Union[Unset, FanHoldStatus]):
        type (Union[Unset, BaseHoldType]): An 'indefinite' hold indicates that the hold will continue until cancelled. A
            'nextTransition' hold indicates that the hold will continue only until the next climate change on the thermostat
            schedule, eg, when the thermostat switches from 'away' to 'home'
    """

    fan: Union[Unset, FanHoldStatus] = UNSET
    type: Union[Unset, BaseHoldType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fan: Union[Unset, str] = UNSET
        if not isinstance(self.fan, Unset):
            fan = self.fan.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fan is not UNSET:
            field_dict["fan"] = fan
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _fan = d.pop("fan", UNSET)
        fan: Union[Unset, FanHoldStatus]
        if isinstance(_fan, Unset):
            fan = UNSET
        else:
            fan = FanHoldStatus(_fan)

        _type = d.pop("type", UNSET)
        type: Union[Unset, BaseHoldType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BaseHoldType(_type)

        fan_hold_response_data = cls(
            fan=fan,
            type=type,
        )

        fan_hold_response_data.additional_properties = d
        return fan_hold_response_data

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
