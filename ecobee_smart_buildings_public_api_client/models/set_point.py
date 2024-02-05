from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetPoint")


@attr.s(auto_attribs=True)
class SetPoint:
    """
    Attributes:
        desired_cool (Union[Unset, float]):
        desired_heat (Union[Unset, float]):
    """

    desired_cool: Union[Unset, float] = UNSET
    desired_heat: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desired_cool = self.desired_cool
        desired_heat = self.desired_heat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desired_cool is not UNSET:
            field_dict["desiredCool"] = desired_cool
        if desired_heat is not UNSET:
            field_dict["desiredHeat"] = desired_heat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desired_cool = d.pop("desiredCool", UNSET)

        desired_heat = d.pop("desiredHeat", UNSET)

        set_point = cls(
            desired_cool=desired_cool,
            desired_heat=desired_heat,
        )

        set_point.additional_properties = d
        return set_point

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
