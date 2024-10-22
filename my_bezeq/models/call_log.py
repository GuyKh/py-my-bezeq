from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from my_bezeq.models.common import FormattedDate

from .base import BaseClientResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/PhoneTab/GetCallLog
# {"FromDate":"2021-01-01","ToDate":"2021-01-01"}
#
# {
#     "CallRecords": null,
#     "PhoneNumber": "12345",
#     "FromDate": "13/10/2024",
#     "ToDate": "20/10/2024",
#     "IsSuccessful": false,
#     "ErrorCode": "108",
#     "ErrorMessage": "CALL_LOG_EMPTY",
#     "ClientErrorMessage": ""
# }


@dataclass
class GetCallLogRequest(DataClassDictMixin):
    from_date: date = field(metadata=field_options(alias="FromDate"))
    to_date: date = field(metadata=field_options(alias="ToDate"))

    class Config(BaseConfig):
        serialize_by_alias = True
        serialization_strategy = {date: FormattedDate("%d/%m/%Y")}


@dataclass
class GetCallLogResponse(BaseClientResponse):
    call_rercords: Optional[list] = field(metadata=field_options(alias="CallRecords"))
    phone_number: str = field(metadata=field_options(alias="PhoneNumber"))
    from_date: date = field(metadata=field_options(alias="FromDate"))
    to_date: date = field(metadata=field_options(alias="ToDate"))
