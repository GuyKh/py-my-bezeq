
from datetime import date, timedelta
from typing import Optional

from my_bezeq.api_state import ApiState
from my_bezeq.commons import send_post_json_request
from my_bezeq.const import (
    ELECTRIC_REPORT_BY_DAY_URL,
    ELECTRIC_REPORT_BY_MONTH_URL,
    ELECTRIC_REPORT_BY_YEAR_URL,
    ELECTRICITY_TAB_URL,
)
from my_bezeq.exceptions import MyBezeqError
from my_bezeq.models.electric_report import (
    ElectricReportLevel,
    GetDailyElectricReportResponse,
    GetElectricReportRequest,
    GetMonthlyElectricReportResponse,
    GetYearlyElectricReportResponse,
)
from my_bezeq.models.electricity_tab import GetElectricityTabRequest, GetElectricityTabResponse


class ElectricApi:
    def __init__(self, state: ApiState):
        self._state = state


    async def get_electricity_tab(self, subscriber_number: Optional[int | str] = None):
        if not subscriber_number:
            subscriber_number = self._state.subscriber_number

        if not subscriber_number:
            raise MyBezeqError("Subscriber number is required")

        self._state.require_dashboard_first()

        req = GetElectricityTabRequest(self._state.jwt_token, str(subscriber_number))
        res = GetElectricityTabResponse.from_dict(
            await send_post_json_request(
                self._state.session, self._state.jwt_token, ELECTRICITY_TAB_URL, json_data=req.to_dict(), use_auth=True
            )
        )

        if res.elect_subscribers and len(res.elect_subscribers) > 0:
            self._state.subscriber_number = res.elect_subscribers[0].subscriber

        return res

    async def get_elec_usage_report(self, level: ElectricReportLevel, from_date: date | str, to_date: date | str)\
            -> GetDailyElectricReportResponse | GetMonthlyElectricReportResponse | GetYearlyElectricReportResponse:
        self._state.require_dashboard_first()

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
                self._state.session, self._state.jwt_token, url, json_data=req.to_dict(), use_auth=True
            )

        match level:
            case ElectricReportLevel.HOURLY:
                return GetDailyElectricReportResponse.from_dict(res)
            case ElectricReportLevel.DAILY:
                return GetMonthlyElectricReportResponse.from_dict(res)
            case ElectricReportLevel.MONTHLY:
                return GetYearlyElectricReportResponse.from_dict(res)
