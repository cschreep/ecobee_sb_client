from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sensor_capability import SensorCapability


T = TypeVar("T", bound="Sensor")


@attr.s(auto_attribs=True)
class Sensor:
    """
    Attributes:
        capability (Union[Unset, List['SensorCapability']]):
        code (Union[Unset, str]):
        id (Union[Unset, str]):
        is_in_use (Union[Unset, bool]):
        name (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    capability: Union[Unset, List["SensorCapability"]] = UNSET
    code: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_in_use: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capability: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.capability, Unset):
            capability = []
            for capability_item_data in self.capability:
                capability_item = capability_item_data.to_dict()

                capability.append(capability_item)

        code = self.code
        id = self.id
        is_in_use = self.is_in_use
        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capability is not UNSET:
            field_dict["capability"] = capability
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if is_in_use is not UNSET:
            field_dict["isInUse"] = is_in_use
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sensor_capability import SensorCapability

        d = src_dict.copy()
        capability = []
        _capability = d.pop("capability", UNSET)
        for capability_item_data in _capability or []:
            capability_item = SensorCapability.from_dict(capability_item_data)

            capability.append(capability_item)

        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        is_in_use = d.pop("isInUse", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        sensor = cls(
            capability=capability,
            code=code,
            id=id,
            is_in_use=is_in_use,
            name=name,
            type=type,
        )

        sensor.additional_properties = d
        return sensor

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
