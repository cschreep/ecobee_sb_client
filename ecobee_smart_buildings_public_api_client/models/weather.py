import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.weather_sky import WeatherSky
from ..types import UNSET, Unset

T = TypeVar("T", bound="Weather")


@attr.s(auto_attribs=True)
class Weather:
    """
    Attributes:
        condition (Union[Unset, str]):
        date (Union[Unset, datetime.datetime]):
        dew_point (Union[Unset, float]):
        pressure (Union[Unset, float]): Barometric pressure
        probability_of_precipitation (Union[Unset, int]):
        relative_humidity (Union[Unset, int]):
        sky (Union[Unset, WeatherSky]): Description of the cloud cover condition
        temperature (Union[Unset, float]):
        temperature_high (Union[Unset, float]):
        temperature_low (Union[Unset, float]):
        wind_bearing (Union[Unset, int]): The wind bearing in degrees
        wind_direction (Union[Unset, str]): The cardinal direction of the wind Example: NW.
        wind_speed (Union[Unset, int]): Wind speed in miles per hour
    """

    condition: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    dew_point: Union[Unset, float] = UNSET
    pressure: Union[Unset, float] = UNSET
    probability_of_precipitation: Union[Unset, int] = UNSET
    relative_humidity: Union[Unset, int] = UNSET
    sky: Union[Unset, WeatherSky] = UNSET
    temperature: Union[Unset, float] = UNSET
    temperature_high: Union[Unset, float] = UNSET
    temperature_low: Union[Unset, float] = UNSET
    wind_bearing: Union[Unset, int] = UNSET
    wind_direction: Union[Unset, str] = UNSET
    wind_speed: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition = self.condition
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        dew_point = self.dew_point
        pressure = self.pressure
        probability_of_precipitation = self.probability_of_precipitation
        relative_humidity = self.relative_humidity
        sky: Union[Unset, str] = UNSET
        if not isinstance(self.sky, Unset):
            sky = self.sky.value

        temperature = self.temperature
        temperature_high = self.temperature_high
        temperature_low = self.temperature_low
        wind_bearing = self.wind_bearing
        wind_direction = self.wind_direction
        wind_speed = self.wind_speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition is not UNSET:
            field_dict["condition"] = condition
        if date is not UNSET:
            field_dict["date"] = date
        if dew_point is not UNSET:
            field_dict["dewPoint"] = dew_point
        if pressure is not UNSET:
            field_dict["pressure"] = pressure
        if probability_of_precipitation is not UNSET:
            field_dict["probabilityOfPrecipitation"] = probability_of_precipitation
        if relative_humidity is not UNSET:
            field_dict["relativeHumidity"] = relative_humidity
        if sky is not UNSET:
            field_dict["sky"] = sky
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if temperature_high is not UNSET:
            field_dict["temperatureHigh"] = temperature_high
        if temperature_low is not UNSET:
            field_dict["temperatureLow"] = temperature_low
        if wind_bearing is not UNSET:
            field_dict["windBearing"] = wind_bearing
        if wind_direction is not UNSET:
            field_dict["windDirection"] = wind_direction
        if wind_speed is not UNSET:
            field_dict["windSpeed"] = wind_speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        condition = d.pop("condition", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        dew_point = d.pop("dewPoint", UNSET)

        pressure = d.pop("pressure", UNSET)

        probability_of_precipitation = d.pop("probabilityOfPrecipitation", UNSET)

        relative_humidity = d.pop("relativeHumidity", UNSET)

        _sky = d.pop("sky", UNSET)
        sky: Union[Unset, WeatherSky]
        if isinstance(_sky, Unset):
            sky = UNSET
        else:
            sky = WeatherSky(_sky)

        temperature = d.pop("temperature", UNSET)

        temperature_high = d.pop("temperatureHigh", UNSET)

        temperature_low = d.pop("temperatureLow", UNSET)

        wind_bearing = d.pop("windBearing", UNSET)

        wind_direction = d.pop("windDirection", UNSET)

        wind_speed = d.pop("windSpeed", UNSET)

        weather = cls(
            condition=condition,
            date=date,
            dew_point=dew_point,
            pressure=pressure,
            probability_of_precipitation=probability_of_precipitation,
            relative_humidity=relative_humidity,
            sky=sky,
            temperature=temperature,
            temperature_high=temperature_high,
            temperature_low=temperature_low,
            wind_bearing=wind_bearing,
            wind_direction=wind_direction,
            wind_speed=wind_speed,
        )

        weather.additional_properties = d
        return weather

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
