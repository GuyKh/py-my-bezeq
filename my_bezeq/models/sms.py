from dataclasses import dataclass, field
from datetime import datetime
from types import NoneType
from typing import Optional

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from my_bezeq.models.common import FormattedDateTime

from .base import BaseResponse


@dataclass
class SendSMSRequest(DataClassDictMixin):
    recipient_number: str = field(metadata=field_options(alias="recipientNumber"))
    sms_text: str = field(metadata=field_options(alias="smsText"))
    send_later: bool = field(metadata=field_options(alias="sendLater"))
    send_later: Optional[datetime] = field(metadata=field_options(alias="laterSendDate"))

    class Config(BaseConfig):
        serialize_by_alias = True
        serialization_strategy = {
            datetime: FormattedDateTime("%d/%m/%Y %H:%M"),
            type(None): lambda _: "",
            NoneType: lambda _: "",
        }

@dataclass
class SendSMSResponse(BaseResponse):
    message: str = field(metadata=field_options(alias="Message"))
    service_time_taken: Optional[str] = field(metadata=field_options(alias="ServiceTimeTaken"))
    transaction_id: str = field(metadata=field_options(alias="TransactionID"))
    api_consuming_info: list[str] = field(metadata=field_options(alias="APIConsumingInfo"))
