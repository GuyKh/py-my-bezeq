import logging

from my_bezeq.api_state import ApiState
from my_bezeq.const import PERSONAL_URL
from my_bezeq.models.personal import GetPersonalTabResponse

from .commons import send_post_json_request

_LOGGER = logging.getLogger(__name__)

class PersonalApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def get_personale_tab(self):
        self._state.require_dashboard_first()

        return GetPersonalTabResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, PERSONAL_URL, use_auth=True)
        )
