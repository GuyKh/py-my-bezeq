import logging
from typing import Optional

from aiohttp import ClientSession

from .commons import resolve_version, send_post_json_request
from .const import USERNAME_LOGIN_URL
from .models.username_login import UsernameLoginRequest, UsernameLoginResponse

_LOGGER = logging.getLogger(__name__)


async def username_login(
    session: ClientSession,
    username: str,
    password: str,
    identity_number: Optional[str] = None,
) -> str:
    if not identity_number:
        identity_number = username

    url = USERNAME_LOGIN_URL.format(version=await resolve_version(session))
    req = UsernameLoginRequest(username, password, identity_number, "Android")

    res = await send_post_json_request(session, None, url, json_data=req.to_dict(), use_auth=False)
    login_res = UsernameLoginResponse.from_dict(res)

    return login_res.jwt_token
