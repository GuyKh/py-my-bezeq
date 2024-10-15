from typing import Optional
from uuid import UUID

import aiohttp
from aiohttp import ClientSession

from .commons import send_get_request, send_post_json_request
from .const import (
    CUSTOMER_MESSAGES_URL,
    DASHBOARD_URL,
    ELECTRIC_INVOICES_PDF_URL,
    ELECTRIC_INVOICES_URL,
    ELECTRICITY_TAB_URL,
    FEEDS_URL,
    INVOICES_URL,
    SITE_CONFIG_URL,
)
from .exceptions import MyBezeqError
from .login import username_login
from .models.customer_messages import GetCustomerMessagesResponse
from .models.dashboard import GetDashboardRequest, GetDashboardResponse
from .models.electric_invoice import GetElectricInvoiceTabResponse
from .models.electricity_tab import GetElectricityTabRequest, GetElectricityTabResponse
from .models.feeds import GetFeedsResponse
from .models.invoice import GetInvoicesTabResponse
from .models.site_config import GetSiteConfigResponse


class MyBezeqAPI:
    def __init__(self, user_id, password, session: Optional[ClientSession] = None):
        self.user_id = user_id
        self.password = password

        if not session:
            session = aiohttp.ClientSession()
        self._session = session

        self._jwt_token = None
        self._subscriber_number = None

    async def login(self) -> None:
        self._jwt_token = await username_login(self._session, self.user_id, self.password)

    async def get_site_config(self) -> GetSiteConfigResponse:
        return GetSiteConfigResponse.from_dict(
            await send_post_json_request(self._session, None, SITE_CONFIG_URL, json_data={}, use_auth=False)
        )

    async def get_dashboard_tab(self):
        req = GetDashboardRequest("")  # Empty String because that's what the API expects ¯\_(ツ)_/¯

        res = GetDashboardResponse.from_dict(
            await send_post_json_request(
                self._session, self._jwt_token, DASHBOARD_URL, json_data=req.to_dict(), use_auth=True
            )
        )

        if len(res.customer_details.elect_subscribers) > 0:
            self._subscriber_number = res.customer_details.elect_subscribers[0].subscriber
        return res

    async def get_invoice_tab(self):
        return GetInvoicesTabResponse.from_dict(
            await send_post_json_request(self._session, self._jwt_token, INVOICES_URL, use_auth=True)
        )

    async def get_feeds(self):
        return GetFeedsResponse.from_dict(
            await send_post_json_request(self._session, self._jwt_token, FEEDS_URL, use_auth=True)
        )

    async def get_customer_messages(self):
        return GetCustomerMessagesResponse.from_dict(
            await send_post_json_request(self._session, self._jwt_token, CUSTOMER_MESSAGES_URL, use_auth=True)
        )

    async def get_invoice_pdf(self, invoice_id: UUID) -> bytes:
        """Get Invoice PDF response from My Bezeq API."""

        response = await send_get_request(
            self._session, ELECTRIC_INVOICES_PDF_URL.format(invoice_id=invoice_id, jwt_token=self._jwt_token)
        )
        return await response.read()

    async def get_electric_invoice_tab(self):
        return GetElectricInvoiceTabResponse.from_dict(
            await send_post_json_request(self._session, self._jwt_token, ELECTRIC_INVOICES_URL, use_auth=True)
        )

    async def get_electricity_tab(self, subscriber_number: Optional[int | str] = None):
        if not subscriber_number:
            subscriber_number = self._subscriber_number

        if not subscriber_number:
            raise MyBezeqError("Subscriber number is required")

        req = GetElectricityTabRequest(self._jwt_token, str(subscriber_number))
        res = GetElectricityTabResponse.from_dict(
            await send_post_json_request(
                self._session, self._jwt_token, ELECTRICITY_TAB_URL, json_data=req.to_dict(), use_auth=True
            )
        )

        if res.elect_subscribers and len(res.elect_subscribers) > 0:
            self._subscriber_number = res.elect_subscribers[0].subscriber

        return res
