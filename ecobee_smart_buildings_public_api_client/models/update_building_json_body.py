from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.building_size import BuildingSize
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_details import AddressDetails


T = TypeVar("T", bound="UpdateBuildingJsonBody")


@attr.s(auto_attribs=True)
class UpdateBuildingJsonBody:
    """
    Attributes:
        address_details (Union[Unset, AddressDetails]):
        name (Union[Unset, str]):
        size (Union[Unset, BuildingSize]): The values for building size are square foot ranges where 1 = 1-4999, 5000 =
            5000-9999, 10000 = 10000-19999, 20000 = 20000+, 0 = unknown
    """

    address_details: Union[Unset, "AddressDetails"] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, BuildingSize] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_details, Unset):
            address_details = self.address_details.to_dict()

        name = self.name
        size: Union[Unset, int] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_details is not UNSET:
            field_dict["addressDetails"] = address_details
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_details import AddressDetails

        d = src_dict.copy()
        _address_details = d.pop("addressDetails", UNSET)
        address_details: Union[Unset, AddressDetails]
        if isinstance(_address_details, Unset):
            address_details = UNSET
        else:
            address_details = AddressDetails.from_dict(_address_details)

        name = d.pop("name", UNSET)

        _size = d.pop("size", UNSET)
        size: Union[Unset, BuildingSize]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = BuildingSize(_size)

        update_building_json_body = cls(
            address_details=address_details,
            name=name,
            size=size,
        )

        update_building_json_body.additional_properties = d
        return update_building_json_body

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
