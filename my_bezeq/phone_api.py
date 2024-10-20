
from datetime import date, datetime
from typing import Optional

from my_bezeq.api_state import ApiState
from my_bezeq.commons import send_get_request, send_post_json_request
from my_bezeq.const import CALL_LOG_EXCEL_URL, CALL_LOG_URL, SEND_SMS_URL
from my_bezeq.models.call_log import GetCallLogRequest, GetCallLogResponse
from my_bezeq.models.sms import SendSMSRequest, SendSMSResponse


class PhoneApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def send_sms(self, phone: str, message: str,
                    later_send_date: Optional[datetime] = None) -> SendSMSResponse:
        self._state.require_dashboard_first()
        req = SendSMSRequest(recipient_number=phone, sms_text=message, send_later=later_send_date is not None,
                            later_send_date=later_send_date)

        return SendSMSResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, SEND_SMS_URL,
                                         json_data=req.to_dict(), use_auth=True)
        )

    async def get_call_log(self, from_date: date, to_date: date):
        self._state.require_dashboard_first()
        req = GetCallLogRequest(from_date=from_date, to_date=to_date)
        return GetCallLogResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, CALL_LOG_URL,
                                         json_data=req.to_dict(), use_auth=True)
        )

    async def get_call_log_excel(self, from_date: date, to_date: date):
        self._state.require_dashboard_first()
        response = await send_get_request(
            self._state.session, CALL_LOG_EXCEL_URL.format(
                from_date=from_date.strftime("%d/%m/%Y"),
                to_date=to_date,
                jwt_token=self._state.jwt_token), use_auth=True
        )
        return await response.read()
