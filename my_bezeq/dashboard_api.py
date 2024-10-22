import logging

from my_bezeq.api_state import ApiState
from my_bezeq.const import CARD_DATA_URL, CUSTOMER_MESSAGES_URL, DASHBOARD_URL
from my_bezeq.models.card_data import GetCardDataRequest, GetCardDataResponse
from my_bezeq.models.common import ServiceType
from my_bezeq.models.customer_messages import GetCustomerMessagesResponse
from my_bezeq.models.dashboard import GetDashboardRequest, GetDashboardResponse

from .commons import send_post_json_request

_LOGGER = logging.getLogger(__name__)

class DashboardApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def get_dashboard_tab(self):
        req = GetDashboardRequest("")  # Empty String because that's what the API expects ¯\_(ツ)_/¯

        res = GetDashboardResponse.from_dict(
            await send_post_json_request(
                self._state.session, self._state.jwt_token, DASHBOARD_URL, json_data=req.to_dict(), use_auth=True
            )
        )

        if not self._state.subscriber_number:
            if len(res.customer_details.elect_subscribers) > 0:
                self._state.subscriber_number = res.customer_details.elect_subscribers[0].subscriber
            elif len(res.customer_details.available_subscribers) > 0:
                self._state.subscriber_number = res.customer_details.available_subscribers[0].subscriber_no

        self._state.is_dashboard_called = True
        return res


    async def get_customer_messages(self):
        self._state.require_dashboard_first()
        return GetCustomerMessagesResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, CUSTOMER_MESSAGES_URL,
                                         use_auth=True)
        )


    async def get_card_data(self, service_type: ServiceType | str):
        self._state.require_dashboard_first()
        service_type = ServiceType(service_type)

        GetCardDataRequest(service_type)
        return GetCardDataResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, CARD_DATA_URL,
                                         use_auth=True)
        )
