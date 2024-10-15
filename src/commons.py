import http
import logging
from datetime import datetime
from json import JSONDecodeError
from typing import Any, Optional

from aiohttp import ClientError, ClientResponse, ClientSession

from .const import VERSION_URL
from .exceptions import MyBezeqError, MyBezeqUnauthorizedError, MyBezeqVersionError
from .models.base import BaseResponse

_LOGGER = logging.getLogger(__name__)


async def parse_error_response(resp, response_content):
    _LOGGER.warning(f"Failed call: (Code {resp.status}): {resp.reason} -> {response_content}")
    try:
        json_resp = await resp.json(content_type=None)
        base_response = BaseResponse.from_dict(json_resp)
        raise MyBezeqError(f"Error My Bezeq API: {base_response.error_code} - {base_response.error_message}")
    except Exception as e:
        raise MyBezeqError(f"Error My Bezeq API: {resp.status}): {resp.reason} - {e}")


HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=utf-8",
    "Origin": "https://my.bezeq.co.il",
    "Referer": "https://my.bezeq.co.il/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/128.0.0.0 Safari/537.36",
}

AUTH_HEADERS = HEADERS.copy()

version: Optional[str] = None
version_fetch_datetime: Optional[datetime] = None


def get_auth_headers(token: str) -> dict:
    AUTH_HEADERS["Authorization"] = f"{token}"
    return AUTH_HEADERS


async def send_get_request(session: ClientSession, url: str) -> ClientResponse:
    url = url.format(version=await resolve_version(session))

    try:
        resp: ClientResponse = await session.get(url)
    except TimeoutError as ex:
        raise MyBezeqError(f"Failed to communicate with My Bezeq API due to time out: ({str(ex)})")
    except ClientError as ex:
        raise MyBezeqError(f"Failed to communicate with My Bezeq API due to ClientError: ({str(ex)})")
    except JSONDecodeError as ex:
        raise MyBezeqError(f"Received invalid response from My Bezeq API: {str(ex)}")

    return resp


async def resolve_version(session: ClientSession) -> str:
    global version
    global version_fetch_datetime

    if not version or not version_fetch_datetime or (datetime.now() - version_fetch_datetime).seconds > 3600:
        try:
            resp: ClientResponse = await session.get(VERSION_URL)
            json_resp: dict = await resp.json(content_type=None)
        except ClientError as ex:
            _LOGGER.warning(f"Failed to fetch version from My Bezeq API: {str(ex)}")
            if not version:
                raise MyBezeqVersionError(f"Failed to fetch version from My Bezeq API: {str(ex)}")
            return version

        if resp.status != http.HTTPStatus.OK or "version" not in json_resp:
            _LOGGER.warning(f"Failed to fetch version from My Bezeq API: {json_resp}")
            if not version:
                raise MyBezeqVersionError(f"Failed to fetch version from My Bezeq API: {json_resp}")
            return version

        version = json_resp["version"]
        split = version.split(".")
        if len(split) != 3:
            if not version:
                raise MyBezeqVersionError(f"Failed to calculate version from My Bezeq API: {json_resp}")
            version = version

        _LOGGER.debug(f"Fetched version: {version}")
        version = f"v{split[0]}.{split[1]}"
        version_fetch_datetime = datetime.now()

    return version


async def send_post_json_request(
    session: ClientSession,
    token: str | None,
    url: str,
    timeout: Optional[int] = 60,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
    json_data: Optional[dict] = None,
    use_auth: Optional[bool] = True,
) -> dict[str, Any]:
    resp = await send_post_request(data, headers, json_data, session, timeout, token, url, use_auth)

    json = await resp.json(content_type=None)

    _LOGGER.debug(f"Got JSON Response: {json}")
    return json


async def send_post_request(data, headers, json_data, session, timeout, token, url, use_auth):
    try:
        if use_auth and not token:
            raise MyBezeqUnauthorizedError("No JWT token provided")

        if not headers:
            headers = HEADERS if not use_auth else get_auth_headers(token)

        if use_auth and not headers.get("Authorization"):
            headers["Authorization"] = f"{token}"

        if not timeout:
            timeout = session.timeout

        url = url.format(version=await resolve_version(session))
        _LOGGER.debug(f"Sending POST request to {url} with data: {json_data}")
        resp = await session.post(url=url, data=data, json=json_data, headers=headers, timeout=timeout)
    except TimeoutError as ex:
        raise MyBezeqError(f"Failed to communicate with My Bezeq API due to time out: ({str(ex)})")
    except ClientError as ex:
        raise MyBezeqError(f"Failed to communicate with My Bezeq API due to ClientError: ({str(ex)})")
    except JSONDecodeError as ex:
        raise MyBezeqError(f"Received invalid response from My Bezeq API: {str(ex)}")
    if resp.status == http.HTTPStatus.UNAUTHORIZED:
        raise MyBezeqUnauthorizedError("Unauthorized request, please check your JWT token")
    if resp.status != http.HTTPStatus.OK:
        await parse_error_response(resp, await resp.content)
    return resp
