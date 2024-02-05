from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_error_response import BaseErrorResponse
from ...models.base_fail_response import BaseFailResponse
from ...models.building import Building
from ...types import Response


def _get_kwargs(
    building_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/buildings/{buildingId}".format(client.base_url, buildingId=building_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[BaseErrorResponse, BaseFailResponse, Building]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Building.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = BaseErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = BaseErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = BaseErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = BaseFailResponse.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = BaseErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = BaseErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[BaseErrorResponse, BaseFailResponse, Building]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    building_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BaseErrorResponse, BaseFailResponse, Building]]:
    """Get a summary of a building

     Get the details of a specific building

    Args:
        building_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, Building]]
    """

    kwargs = _get_kwargs(
        building_id=building_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    building_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BaseErrorResponse, BaseFailResponse, Building]]:
    """Get a summary of a building

     Get the details of a specific building

    Args:
        building_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, Building]]
    """

    return sync_detailed(
        building_id=building_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    building_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BaseErrorResponse, BaseFailResponse, Building]]:
    """Get a summary of a building

     Get the details of a specific building

    Args:
        building_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, Building]]
    """

    kwargs = _get_kwargs(
        building_id=building_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    building_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BaseErrorResponse, BaseFailResponse, Building]]:
    """Get a summary of a building

     Get the details of a specific building

    Args:
        building_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, Building]]
    """

    return (
        await asyncio_detailed(
            building_id=building_id,
            client=client,
        )
    ).parsed
