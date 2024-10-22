import logging

from my_bezeq.api_state import ApiState
from my_bezeq.commons import send_post_json_request
from my_bezeq.const import TIME_WINDOWS_URL
from my_bezeq.models.time_windows import GetTimeWindowsResponse

_LOGGER = logging.getLogger(__name__)

class TechCoordApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def get_time_windows(self):
        self._state.require_dashboard_first()

        return GetTimeWindowsResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, TIME_WINDOWS_URL,
                                         use_auth=True)
        )
