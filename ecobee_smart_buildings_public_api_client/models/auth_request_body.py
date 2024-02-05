from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.auth_request_body_audience import AuthRequestBodyAudience
from ..models.auth_request_body_grant_type import AuthRequestBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthRequestBody")


@attr.s(auto_attribs=True)
class AuthRequestBody:
    """
    Attributes:
        audience (AuthRequestBodyAudience):
        client_id (str):
        client_secret (str):
        grant_type (AuthRequestBodyGrantType):
        scope (Union[Unset, str]): An optional list of scopes, used to check if the client has been granted permissions
            to. Example: read:thermostat read:thermostats.
    """

    audience: AuthRequestBodyAudience
    client_id: str
    client_secret: str
    grant_type: AuthRequestBodyGrantType
    scope: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audience = self.audience.value

        client_id = self.client_id
        client_secret = self.client_secret
        grant_type = self.grant_type.value

        scope = self.scope

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audience": audience,
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        audience = AuthRequestBodyAudience(d.pop("audience"))

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        grant_type = AuthRequestBodyGrantType(d.pop("grant_type"))

        scope = d.pop("scope", UNSET)

        auth_request_body = cls(
            audience=audience,
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
        )

        auth_request_body.additional_properties = d
        return auth_request_body

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
