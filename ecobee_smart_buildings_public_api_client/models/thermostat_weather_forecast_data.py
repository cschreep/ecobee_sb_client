from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weather import Weather


T = TypeVar("T", bound="ThermostatWeatherForecastData")


@attr.s(auto_attribs=True)
class ThermostatWeatherForecastData:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier for a thermostat. The ID will match the serial number on the
            physical thermostat.
        items (Union[Unset, List['Weather']]):
    """

    id: Union[Unset, str] = UNSET
    items: Union[Unset, List["Weather"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.weather import Weather

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Weather.from_dict(items_item_data)

            items.append(items_item)

        thermostat_weather_forecast_data = cls(
            id=id,
            items=items,
        )

        thermostat_weather_forecast_data.additional_properties = d
        return thermostat_weather_forecast_data

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
