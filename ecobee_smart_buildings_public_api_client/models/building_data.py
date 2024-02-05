from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.building_size import BuildingSize
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuildingData")


@attr.s(auto_attribs=True)
class BuildingData:
    """
    Attributes:
        address (str): The building's street address Default: ''.
        city (str): City where the building is located Default: ''.
        country (str): This should be the ISO 3166-1 alpha-2 country code. It must be uppercase. Default: ''. Example:
            US.
        latitude (float): Latitude coordinate for the building
        longitude (float): Longitude coordinate for the building
        postal_code (str): Postal information for the building
        state (str): The state or province where the building is located. We recommend the 2 character short form for
            this field, eg, CA or NY, when possible to be consistent with the SmartBuildings application format. Default:
            ''. Example: CA.
        time_zone (str): The time zone where the building is located. This should be the tz/zoneinfo string as defined
            in the IANA time zone database. See https://www.iana.org/time-zones or
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. Example: America/New_York.
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        size (Union[Unset, BuildingSize]): The values for building size are square foot ranges where 1 = 1-4999, 5000 =
            5000-9999, 10000 = 10000-19999, 20000 = 20000+, 0 = unknown
    """

    latitude: float
    longitude: float
    postal_code: str
    time_zone: str
    address: str = ""
    city: str = ""
    country: str = ""
    state: str = ""
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, BuildingSize] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        city = self.city
        country = self.country
        latitude = self.latitude
        longitude = self.longitude
        postal_code = self.postal_code
        state = self.state
        time_zone = self.time_zone
        id = self.id
        name = self.name
        size: Union[Unset, int] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "city": city,
                "country": country,
                "latitude": latitude,
                "longitude": longitude,
                "postalCode": postal_code,
                "state": state,
                "timeZone": time_zone,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        city = d.pop("city")

        country = d.pop("country")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        postal_code = d.pop("postalCode")

        state = d.pop("state")

        time_zone = d.pop("timeZone")

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _size = d.pop("size", UNSET)
        size: Union[Unset, BuildingSize]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = BuildingSize(_size)

        building_data = cls(
            address=address,
            city=city,
            country=country,
            latitude=latitude,
            longitude=longitude,
            postal_code=postal_code,
            state=state,
            time_zone=time_zone,
            id=id,
            name=name,
            size=size,
        )

        building_data.additional_properties = d
        return building_data

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
