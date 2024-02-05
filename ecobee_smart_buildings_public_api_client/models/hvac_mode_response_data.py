from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.hvac_mode import HvacMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="HvacModeResponseData")


@attr.s(auto_attribs=True)
class HvacModeResponseData:
    """
    Attributes:
        hvac_mode (Union[Unset, HvacMode]): The HVAC mode on a thermostat. Possible values: auto, auxHeatOnly, cool,
            heat, off.
    """

    hvac_mode: Union[Unset, HvacMode] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hvac_mode: Union[Unset, str] = UNSET
        if not isinstance(self.hvac_mode, Unset):
            hvac_mode = self.hvac_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hvac_mode is not UNSET:
            field_dict["hvacMode"] = hvac_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _hvac_mode = d.pop("hvacMode", UNSET)
        hvac_mode: Union[Unset, HvacMode]
        if isinstance(_hvac_mode, Unset):
            hvac_mode = UNSET
        else:
            hvac_mode = HvacMode(_hvac_mode)

        hvac_mode_response_data = cls(
            hvac_mode=hvac_mode,
        )

        hvac_mode_response_data.additional_properties = d
        return hvac_mode_response_data

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
