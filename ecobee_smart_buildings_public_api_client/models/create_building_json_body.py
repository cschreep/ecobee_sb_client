from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.building_size import BuildingSize

if TYPE_CHECKING:
    from ..models.address_details import AddressDetails


T = TypeVar("T", bound="CreateBuildingJsonBody")


@attr.s(auto_attribs=True)
class CreateBuildingJsonBody:
    """
    Attributes:
        address_details (AddressDetails):
        name (str): The display name for the building. Must be unique within the company.
        size (BuildingSize): The values for building size are square foot ranges where 1 = 1-4999, 5000 = 5000-9999,
            10000 = 10000-19999, 20000 = 20000+, 0 = unknown
    """

    address_details: "AddressDetails"
    name: str
    size: BuildingSize
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_details = self.address_details.to_dict()

        name = self.name
        size = self.size.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addressDetails": address_details,
                "name": name,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_details import AddressDetails

        d = src_dict.copy()
        address_details = AddressDetails.from_dict(d.pop("addressDetails"))

        name = d.pop("name")

        size = BuildingSize(d.pop("size"))

        create_building_json_body = cls(
            address_details=address_details,
            name=name,
            size=size,
        )

        create_building_json_body.additional_properties = d
        return create_building_json_body

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
