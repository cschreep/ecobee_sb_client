from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.auth_response_body_token_type import AuthResponseBodyTokenType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthResponseBody")


@attr.s(auto_attribs=True)
class AuthResponseBody:
    """
    Attributes:
        access_token (Union[Unset, str]):
        token_type (Union[Unset, AuthResponseBodyTokenType]):
        expires_in (Union[Unset, int]):
        scope (Union[Unset, str]):
    """

    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, AuthResponseBodyTokenType] = UNSET
    expires_in: Union[Unset, int] = UNSET
    scope: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        token_type: Union[Unset, str] = UNSET
        if not isinstance(self.token_type, Unset):
            token_type = self.token_type.value

        expires_in = self.expires_in
        scope = self.scope

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token", UNSET)

        _token_type = d.pop("token_type", UNSET)
        token_type: Union[Unset, AuthResponseBodyTokenType]
        if isinstance(_token_type, Unset):
            token_type = UNSET
        else:
            token_type = AuthResponseBodyTokenType(_token_type)

        expires_in = d.pop("expires_in", UNSET)

        scope = d.pop("scope", UNSET)

        auth_response_body = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            scope=scope,
        )

        auth_response_body.additional_properties = d
        return auth_response_body

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
