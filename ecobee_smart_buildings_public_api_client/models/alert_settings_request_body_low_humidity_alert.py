from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSettingsRequestBodyLowHumidityAlert")


@attr.s(auto_attribs=True)
class AlertSettingsRequestBodyLowHumidityAlert:
    """High and low humidity alert values must be separated by 5%

    Attributes:
        enabled (Union[Unset, bool]):
        value (Union[Unset, float]):
    """

    enabled: Union[Unset, bool] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        value = d.pop("value", UNSET)

        alert_settings_request_body_low_humidity_alert = cls(
            enabled=enabled,
            value=value,
        )

        alert_settings_request_body_low_humidity_alert.additional_properties = d
        return alert_settings_request_body_low_humidity_alert

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
