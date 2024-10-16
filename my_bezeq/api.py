import logging
from datetime import date, timedelta
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
    ELECTRIC_REPORT_BY_DAY_URL,
    ELECTRIC_REPORT_BY_MONTH_URL,
    ELECTRIC_REPORT_BY_YEAR_URL,
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
from .models.electric_report import (
    ElectricReportLevel,
    GetDailyElectricReportResponse,
    GetElectricReportRequest,
    GetMonthlyElectricReportResponse,
    GetYearlyElectricReportResponse,
)
from .models.electricity_tab import GetElectricityTabRequest, GetElectricityTabResponse
from .models.feeds import GetFeedsResponse
from .models.invoice import GetInvoicesTabResponse
from .models.site_config import GetSiteConfigResponse

_LOGGER = logging.getLogger(__name__)

class MyBezeqAPI:
    def __init__(self, user_id, password, session: Optional[ClientSession] = None):
        self.user_id = user_id
        self.password = password

        if not session:
            session = aiohttp.ClientSession()
        self._session = session

        self._jwt_token = None
        self._subscriber_number = None
        self._is_dashboard_called = False

    async def login(self) -> None:
        self._jwt_token = await username_login(self._session, self.user_id, self.password)
        self._is_dashboard_called = False

    def set_jwt(self, jwt_token: str) -> None:
        self._jwt_token = jwt_token
        self._is_dashboard_called = False

    def _require_dashboard_first(self):
        if not self._is_dashboard_called:
            raise MyBezeqError("get_dashboard_tab() should be called before calling this method," +\
                            "Otherwise you may get empty data")

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

        if not self._subscriber_number:
            if len(res.customer_details.elect_subscribers) > 0:
                self._subscriber_number = res.customer_details.elect_subscribers[0].subscriber
            elif len(res.customer_details.available_subscribers) > 0:
                self._subscriber_number = res.customer_details.available_subscribers[0].subscriber_no

        self._is_dashboard_called = True
        return res

    async def get_invoice_tab(self):
        self._require_dashboard_first()

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
        self._require_dashboard_first()

        return GetElectricInvoiceTabResponse.from_dict(
            await send_post_json_request(self._session, self._jwt_token, ELECTRIC_INVOICES_URL, use_auth=True)
        )

    async def get_electricity_tab(self, subscriber_number: Optional[int | str] = None):
        if not subscriber_number:
            subscriber_number = self._subscriber_number

        if not subscriber_number:
            raise MyBezeqError("Subscriber number is required")

        self._require_dashboard_first()

        req = GetElectricityTabRequest(self._jwt_token, str(subscriber_number))
        res = GetElectricityTabResponse.from_dict(
            await send_post_json_request(
                self._session, self._jwt_token, ELECTRICITY_TAB_URL, json_data=req.to_dict(), use_auth=True
            )
        )

        if res.elect_subscribers and len(res.elect_subscribers) > 0:
            self._subscriber_number = res.elect_subscribers[0].subscriber

        return res

    async def get_elec_usage_report(self, level: ElectricReportLevel, from_date: date | str, to_date: date | str)\
            -> GetDailyElectricReportResponse | GetMonthlyElectricReportResponse | GetYearlyElectricReportResponse:
        self._require_dashboard_first()

        if isinstance(from_date, str): # "2024-10-10"
            from_date = date.fromisoformat(from_date)
        if isinstance(to_date, str):    # "2024-10-10"
            to_date = date.fromisoformat(to_date)

        req = GetElectricReportRequest(from_date, to_date, level)

        if to_date < from_date and from_date - to_date > timedelta(days=1):
            raise MyBezeqError("from_date should be before to_date")

        url = ""
        match level:
            case ElectricReportLevel.HOURLY:
                url = ELECTRIC_REPORT_BY_DAY_URL
            case ElectricReportLevel.DAILY:
                url = ELECTRIC_REPORT_BY_MONTH_URL
            case ElectricReportLevel.MONTHLY:
                url = ELECTRIC_REPORT_BY_YEAR_URL

        res = await send_post_json_request(
                self._session, self._jwt_token, url, json_data=req.to_dict(), use_auth=True
            )

        match level:
            case ElectricReportLevel.HOURLY:
                return GetDailyElectricReportResponse.from_dict(res)
            case ElectricReportLevel.DAILY:
                return GetMonthlyElectricReportResponse.from_dict(res)
            case ElectricReportLevel.MONTHLY:
                return GetYearlyElectricReportResponse.from_dict(res)
