from dataclasses import dataclass, field

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from my_bezeq.models.cards import CardDetailsResponse
from my_bezeq.models.common import ServiceType

from .base import BaseClientResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/Dashboard/GetCardData
# {"ServiceType":"Phone"}
#
# {
#     "CardDetails": "{\"Buffers\":[\{
#         \"PackageName\":\"חבילת 50 דקות \",
#         \"Soc\":\"OMD337\",
#         \"Description\":\"50 דקות קו טלפון\",
#         \"UsedUnits\":\"0\",
#         \"RemainingUnits\":\"0\",
#         \"InclusiveAmount\":\"50\",
#         \"InclusiveType\":\"דקות\",
#         \"LevelCode\":\"C\",
#         \"PeriodName\":\"ללא\",
#         \"UsedUnitsPercent\":\"0\"}]}",
#     "ServiceType": "Phone",
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }


@dataclass
class GetCardDataRequest(DataClassDictMixin):
    service_type: ServiceType = field(metadata=field_options(alias="ServiceType"))

    class Config(BaseConfig):
        serialize_by_alias = True


@dataclass
class GetCardDataResponse(CardDetailsResponse, BaseClientResponse):
        pass  # No additional content
