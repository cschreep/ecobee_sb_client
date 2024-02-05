from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThermostatStatusDataDesiredCoolRange")


@attr.s(auto_attribs=True)
class ThermostatStatusDataDesiredCoolRange:
    """The minimum and maximum values for a cool setPoint

    Attributes:
        min_ (Union[Unset, float]):
        max_ (Union[Unset, float]):
    """

    min_: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_
        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        thermostat_status_data_desired_cool_range = cls(
            min_=min_,
            max_=max_,
        )

        thermostat_status_data_desired_cool_range.additional_properties = d
        return thermostat_status_data_desired_cool_range

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
