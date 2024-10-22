import logging

from my_bezeq.api_state import ApiState
from my_bezeq.const import MENU_URL, SITE_CONFIG_URL, START_ACTIONS_URL
from my_bezeq.models.menu import GetMenuResponse
from my_bezeq.models.site_config import GetSiteConfigResponse
from my_bezeq.models.start_actions import StartActionsResponse

from .commons import send_post_json_request

_LOGGER = logging.getLogger(__name__)

class GenericActionsApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def get_site_config(self) -> GetSiteConfigResponse:
        return GetSiteConfigResponse.from_dict(
            await send_post_json_request(self._state.session, None, SITE_CONFIG_URL, json_data={}, use_auth=False)
        )

    async def get_start_actions(self) -> StartActionsResponse:
        return StartActionsResponse.from_dict(
            await send_post_json_request(self._state.session, None, START_ACTIONS_URL, use_auth=False)
        )

    async def get_menu(self) -> StartActionsResponse:
        return GetMenuResponse.from_dict(
            await send_post_json_request(self._state.session, None, MENU_URL, use_auth=False)
        )
