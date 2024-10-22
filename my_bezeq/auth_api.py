import logging
from typing import Optional

from my_bezeq.api_state import ApiState
from my_bezeq.models.glassix_token import GenGlassixTokenRequest, GenGlassixTokenResponse

from .commons import resolve_version, send_post_json_request
from .const import GEN_GLASSIX_TOKEN_URL, USERNAME_LOGIN_URL
from .models.username_login import UsernameLoginRequest, UsernameLoginResponse

_LOGGER = logging.getLogger(__name__)

class AuthApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def login(
        self,
        username: str,
        password: str,
        identity_number: Optional[str] = None,
    ) -> str:
        if not identity_number:
            identity_number = username

        url = USERNAME_LOGIN_URL.format(version=await resolve_version(self._state.session))
        req = UsernameLoginRequest(username, password, identity_number, "Android")

        res = await send_post_json_request(self._state.session, None, url, json_data=req.to_dict(), use_auth=False)
        login_res = UsernameLoginResponse.from_dict(res)

        self._state.jwt_token = login_res.jwt_token
        self._state.is_dashboard_called = False
        return login_res.jwt_token

    async def gen_glassix_token(self, action_id):
        self._state.require_dashboard_first()

        req = GenGlassixTokenRequest(action_id)
        return GenGlassixTokenResponse(await send_post_json_request(self._state.session, None,
                                                                   GEN_GLASSIX_TOKEN_URL, json_data=req.to_dict(),
                                                                   use_auth=False))
