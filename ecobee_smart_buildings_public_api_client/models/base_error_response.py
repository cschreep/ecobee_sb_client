from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_error_response_status import BaseErrorResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_error_response_data import BaseErrorResponseData
    from ..models.base_error_response_message import BaseErrorResponseMessage


T = TypeVar("T", bound="BaseErrorResponse")


@attr.s(auto_attribs=True)
class BaseErrorResponse:
    """
    Attributes:
        status (BaseErrorResponseStatus):
        message (BaseErrorResponseMessage):
        code (Union[Unset, int]):
        data (Union[Unset, BaseErrorResponseData]):
    """

    status: BaseErrorResponseStatus
    message: "BaseErrorResponseMessage"
    code: Union[Unset, int] = UNSET
    data: Union[Unset, "BaseErrorResponseData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        message = self.message.to_dict()

        code = self.code
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "message": message,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_error_response_data import BaseErrorResponseData
        from ..models.base_error_response_message import BaseErrorResponseMessage

        d = src_dict.copy()
        status = BaseErrorResponseStatus(d.pop("status"))

        message = BaseErrorResponseMessage.from_dict(d.pop("message"))

        code = d.pop("code", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, BaseErrorResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BaseErrorResponseData.from_dict(_data)

        base_error_response = cls(
            status=status,
            message=message,
            code=code,
            data=data,
        )

        base_error_response.additional_properties = d
        return base_error_response

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
