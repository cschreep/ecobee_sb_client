import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Hold")


@attr.s(auto_attribs=True)
class Hold:
    """
    Attributes:
        cool_hold_temperature (Union[Unset, float]):
        end_time (Union[Unset, datetime.datetime]):
        fan (Union[Unset, str]):
        fan_minimum_on_time (Union[Unset, int]): Minimum time for a fan to run in minutes
        heat_hold_temperature (Union[Unset, float]):
        name (Union[Unset, str]):
        is_running (Union[Unset, bool]):
        start_time (Union[Unset, datetime.datetime]):
        type (Union[Unset, str]):
    """

    cool_hold_temperature: Union[Unset, float] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    fan: Union[Unset, str] = UNSET
    fan_minimum_on_time: Union[Unset, int] = 0
    heat_hold_temperature: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    is_running: Union[Unset, bool] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cool_hold_temperature = self.cool_hold_temperature
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        fan = self.fan
        fan_minimum_on_time = self.fan_minimum_on_time
        heat_hold_temperature = self.heat_hold_temperature
        name = self.name
        is_running = self.is_running
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cool_hold_temperature is not UNSET:
            field_dict["coolHoldTemperature"] = cool_hold_temperature
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if fan is not UNSET:
            field_dict["fan"] = fan
        if fan_minimum_on_time is not UNSET:
            field_dict["fanMinimumOnTime"] = fan_minimum_on_time
        if heat_hold_temperature is not UNSET:
            field_dict["heatHoldTemperature"] = heat_hold_temperature
        if name is not UNSET:
            field_dict["name"] = name
        if is_running is not UNSET:
            field_dict["isRunning"] = is_running
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cool_hold_temperature = d.pop("coolHoldTemperature", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        fan = d.pop("fan", UNSET)

        fan_minimum_on_time = d.pop("fanMinimumOnTime", UNSET)

        heat_hold_temperature = d.pop("heatHoldTemperature", UNSET)

        name = d.pop("name", UNSET)

        is_running = d.pop("isRunning", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        type = d.pop("type", UNSET)

        hold = cls(
            cool_hold_temperature=cool_hold_temperature,
            end_time=end_time,
            fan=fan,
            fan_minimum_on_time=fan_minimum_on_time,
            heat_hold_temperature=heat_hold_temperature,
            name=name,
            is_running=is_running,
            start_time=start_time,
            type=type,
        )

        hold.additional_properties = d
        return hold

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
