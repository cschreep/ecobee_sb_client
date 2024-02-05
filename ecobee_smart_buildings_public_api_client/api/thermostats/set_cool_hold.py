from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_error_response import BaseErrorResponse
from ...models.base_fail_response import BaseFailResponse
from ...models.temperature_hold_request_body import TemperatureHoldRequestBody
from ...models.temperature_hold_response import TemperatureHoldResponse
from ...types import Response


def _get_kwargs(
    thermostat_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TemperatureHoldRequestBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/thermostats/{thermostatId}/coolHold".format(client.base_url, thermostatId=thermostat_id)

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
) -> Optional[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = TemperatureHoldResponse.from_dict(response.json())

        return response_201
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
) -> Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thermostat_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TemperatureHoldRequestBody,
) -> Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]:
    """Set a cool hold on the thermostat

     Create a cool hold on a thermostat based on a provided desired temperature. Used when thermostat
    HVAC mode is set to \"cool\" or \"auto\".

    Args:
        thermostat_id (str): The unique identifier for a thermostat. The ID will match the serial
            number on the physical thermostat.
        json_body (TemperatureHoldRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]
    """

    kwargs = _get_kwargs(
        thermostat_id=thermostat_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thermostat_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TemperatureHoldRequestBody,
) -> Optional[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]:
    """Set a cool hold on the thermostat

     Create a cool hold on a thermostat based on a provided desired temperature. Used when thermostat
    HVAC mode is set to \"cool\" or \"auto\".

    Args:
        thermostat_id (str): The unique identifier for a thermostat. The ID will match the serial
            number on the physical thermostat.
        json_body (TemperatureHoldRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]
    """

    return sync_detailed(
        thermostat_id=thermostat_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    thermostat_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TemperatureHoldRequestBody,
) -> Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]:
    """Set a cool hold on the thermostat

     Create a cool hold on a thermostat based on a provided desired temperature. Used when thermostat
    HVAC mode is set to \"cool\" or \"auto\".

    Args:
        thermostat_id (str): The unique identifier for a thermostat. The ID will match the serial
            number on the physical thermostat.
        json_body (TemperatureHoldRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]
    """

    kwargs = _get_kwargs(
        thermostat_id=thermostat_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thermostat_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TemperatureHoldRequestBody,
) -> Optional[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]:
    """Set a cool hold on the thermostat

     Create a cool hold on a thermostat based on a provided desired temperature. Used when thermostat
    HVAC mode is set to \"cool\" or \"auto\".

    Args:
        thermostat_id (str): The unique identifier for a thermostat. The ID will match the serial
            number on the physical thermostat.
        json_body (TemperatureHoldRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseErrorResponse, BaseFailResponse, TemperatureHoldResponse]]
    """

    return (
        await asyncio_detailed(
            thermostat_id=thermostat_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
