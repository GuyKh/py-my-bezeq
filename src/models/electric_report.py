from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import List

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig
from mashumaro.types import SerializationStrategy

from .base import BaseResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/ElectricityTab/GetElectReportByYear
# {
#     "FromDate":"2023-10-15",
#     "ToDate":"2024-10-14",
#     "Level":3
# }
#
#
# {
#   "UsageData": [
#     {
#       "UsageMonth": "2024-09-01T00:00:00",
#       "SumAllMonth": 123.06,
#       "Subscriber": "12345",
#       "Mone": "12345"
#     },
#     {
#       "UsageMonth": "2024-10-01T00:00:00",
#       "SumAllMonth": 123.76,
#       "Subscriber": "12345",
#       "Mone": "12345"
#     }
#   ],
#   "IsSuccessful": true,
#   "ErrorCode": "",
#   "ErrorMessage": "",
#   "ClientErrorMessage": ""
# }

# POST https://my-api.bezeq.co.il/{{version}}/api/ElectricityTab/GetElectReportByMonth
# {
#     "FromDate":"2023-10-12",
#     "ToDate":"2024-10-14",
#     "Level":2
# }
#
#
# {
#   "UsageMonth": 9,
#   "SumAll": 1234.06,
#   "UsageData": [
#     {
#       "UsageDay": "2024-09-01T00:00:00+03:00",
#       "SumAllDay": 1.12,
#       "Subscriber": "12345",
#       "Mone": "12345"
#     },
#     {
#       "UsageDay": "2024-09-02T00:00:00+03:00",
#       "SumAllDay": 1.1,
#       "Subscriber": "12345",
#       "Mone": "12345"
#     },....
#   ],
#   "IsSuccessful": true,
#   "ErrorCode": "",
#   "ErrorMessage": "",
#   "ClientErrorMessage": ""
# }

# POST https://my-api.bezeq.co.il/{{version}}/api/ElectricityTab/GetElectReportByDay
# {
#     "FromDate":"2023-10-12",
#     "ToDate":"2024-10-14",
#     "Level":2
# }
#
#
# {
#   "UsageDay": 29,
#   "SumAll": 13.72,
#   "UsageData": [
#     {
#       "UsagHour": 0,
#       "SumAllHour": 0.66,
#       "Subscriber": "12345",
#       "Mone": "123456"
#     }
#   ],
#   "IsSuccessful": true,
#   "ErrorCode": "",
#   "ErrorMessage": "",
#   "ClientErrorMessage": ""
# }


class FormattedDate(SerializationStrategy):
    def __init__(self, fmt):
        self.fmt = fmt

    def serialize(self, value: date) -> str:
        return value.strftime(self.fmt)

    def deserialize(self, value: str) -> date:
        return datetime.strptime(value, self.fmt).date()


class ElectricReportLevel(Enum):
    DAY = 1
    WEEK = 2
    MONTH = 3


@dataclass
class GetElectricReportRequest(DataClassDictMixin):
    from_date: date = field(metadata=field_options(alias="FromDate"))
    to_date: date = field(metadata=field_options(alias="ToDate"))
    level: ElectricReportLevel = field(metadata=field_options(alias="Level"))

    class Config(BaseConfig):
        serialize_by_alias = True
        serialization_strategy = {date: FormattedDate("%Y-%m-%d")}


@dataclass
class UsageRecordBase(DataClassDictMixin):
    subscriber: str = field(metadata=field_options(alias="Subscriber"))
    mone: str = field(metadata=field_options(alias="Mone"))


@dataclass
class MonthlyUsageRecord(DataClassDictMixin, UsageRecordBase):
    usage_month: datetime = field(metadata=field_options(alias="UsageMonth"))
    sum_all_month: float = field(metadata=field_options(alias="SumAllMonth"))


@dataclass
class GetYearlyElectricReportResponse(BaseResponse):
    usage_data: List[MonthlyUsageRecord] = field(default_factory=list, metadata=field_options(alias="UsageData"))


@dataclass
class DailyUsage(DataClassDictMixin, UsageRecordBase):
    usage_day: datetime = field(metadata=field_options(alias="UsageDay"))
    sum_all_day: float = field(metadata=field_options(alias="SumAllDay"))


@dataclass
class GetMonthlyElectricReportResponse(BaseResponse):
    usage_month: int = field(metadata=field_options(alias="UsageMonth"))
    sum_all: float = field(metadata=field_options(alias="SumAll"))
    usage_data: List[DailyUsage] = field(default_factory=list, metadata=field_options(alias="UsageData"))


@dataclass
class HourlyUsage(DataClassDictMixin, UsageRecordBase):
    usag_hour: int = field(metadata=field_options(alias="UsagHour"))
    sum_all_hour: float = field(metadata=field_options(alias="SumAllHour"))


@dataclass
class GetDailyElectricReportResponse(BaseResponse):
    usage_day: int = field(metadata=field_options(alias="UsageDay"))
    sum_all: float = field(metadata=field_options(alias="SumAll"))
    usage_data: List[HourlyUsage] = field(default_factory=list, metadata=field_options(alias="UsageData"))
