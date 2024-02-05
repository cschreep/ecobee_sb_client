from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.base_hold_type import BaseHoldType
from ..models.fan_hold_status import FanHoldStatus

T = TypeVar("T", bound="FanHoldRequestBody")


@attr.s(auto_attribs=True)
class FanHoldRequestBody:
    """
    Attributes:
        fan (FanHoldStatus):
        type (BaseHoldType): An 'indefinite' hold indicates that the hold will continue until cancelled. A
            'nextTransition' hold indicates that the hold will continue only until the next climate change on the thermostat
            schedule, eg, when the thermostat switches from 'away' to 'home'
    """

    fan: FanHoldStatus
    type: BaseHoldType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fan = self.fan.value

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fan": fan,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fan = FanHoldStatus(d.pop("fan"))

        type = BaseHoldType(d.pop("type"))

        fan_hold_request_body = cls(
            fan=fan,
            type=type,
        )

        fan_hold_request_body.additional_properties = d
        return fan_hold_request_body

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
