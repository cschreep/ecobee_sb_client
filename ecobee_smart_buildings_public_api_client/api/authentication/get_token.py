from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.auth_request_body import AuthRequestBody
from ...models.auth_response_body import AuthResponseBody
from ...models.get_token_response_400 import GetTokenResponse400
from ...models.get_token_response_401 import GetTokenResponse401
from ...models.get_token_response_403 import GetTokenResponse403
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AuthRequestBody,
) -> Dict[str, Any]:
    url = "{}/token".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuthResponseBody.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetTokenResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetTokenResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetTokenResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AuthRequestBody,
) -> Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]:
    """Get a jwt token

     JWT used to make all authenticated requests on behalf of a SmartBuildings account

    Args:
        json_body (AuthRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: AuthRequestBody,
) -> Optional[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]:
    """Get a jwt token

     JWT used to make all authenticated requests on behalf of a SmartBuildings account

    Args:
        json_body (AuthRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AuthRequestBody,
) -> Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]:
    """Get a jwt token

     JWT used to make all authenticated requests on behalf of a SmartBuildings account

    Args:
        json_body (AuthRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AuthRequestBody,
) -> Optional[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]:
    """Get a jwt token

     JWT used to make all authenticated requests on behalf of a SmartBuildings account

    Args:
        json_body (AuthRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthResponseBody, GetTokenResponse400, GetTokenResponse401, GetTokenResponse403]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
