import logging

from my_bezeq.api_state import ApiState
from my_bezeq.const import (
    EXTENDERS_DETAILS_URL,
    FEEDS_URL,
    INTERNET_TAB_URL,
    REGISTERED_DEVICES_URL,
    SPEED_TEST_CARD_URL,
    WIFI_DATA_URL,
)
from my_bezeq.models.extender_details import GetExtendersDetailsResponse
from my_bezeq.models.feeds import GetFeedsResponse
from my_bezeq.models.internet_tab import GetInternetTabResponse
from my_bezeq.models.registered_devices import GetRegisteredDevicesRequest, GetRegisteredDevicesResponse
from my_bezeq.models.speed_test_card import GetSpeedTestCard
from my_bezeq.models.wifi_data import GetWifiDataResponse

from .commons import send_post_json_request

_LOGGER = logging.getLogger(__name__)

class InternetApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def get_feeds(self):
        self._state.require_dashboard_first()
        return GetFeedsResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, FEEDS_URL, use_auth=True)
        )

    async def get_registered_devices(self):
        self._state.require_dashboard_first()
        req = GetRegisteredDevicesRequest()
        return GetRegisteredDevicesResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, REGISTERED_DEVICES_URL,
                                         json_data=req.to_dict(), use_auth=True))

    async def get_internet_tab(self):
        self._state.require_dashboard_first()
        return GetInternetTabResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, INTERNET_TAB_URL, use_auth=True)
        )


    async def get_speed_test_card(self):
        self._state.require_dashboard_first()
        return GetSpeedTestCard.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, SPEED_TEST_CARD_URL, use_auth=True)
        )


    async def get_wifi_data(self):
        self._state.require_dashboard_first()
        return GetWifiDataResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, WIFI_DATA_URL, use_auth=True)
        )


    async def get_extender_details(self):
        self._state.require_dashboard_first()
        return GetExtendersDetailsResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, EXTENDERS_DETAILS_URL,
                                         use_auth=True)
        )
