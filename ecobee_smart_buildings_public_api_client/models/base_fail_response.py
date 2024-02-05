from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_fail_response_status import BaseFailResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_fail_response_data import BaseFailResponseData


T = TypeVar("T", bound="BaseFailResponse")


@attr.s(auto_attribs=True)
class BaseFailResponse:
    """
    Attributes:
        status (Union[Unset, BaseFailResponseStatus]):
        data (Union[Unset, BaseFailResponseData]):
    """

    status: Union[Unset, BaseFailResponseStatus] = UNSET
    data: Union[Unset, "BaseFailResponseData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_fail_response_data import BaseFailResponseData

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, BaseFailResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BaseFailResponseStatus(_status)

        _data = d.pop("data", UNSET)
        data: Union[Unset, BaseFailResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BaseFailResponseData.from_dict(_data)

        base_fail_response = cls(
            status=status,
            data=data,
        )

        base_fail_response.additional_properties = d
        return base_fail_response

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
