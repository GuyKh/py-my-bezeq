from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional

from mashumaro import DataClassDictMixin, field_options
from mashumaro.types import SerializationStrategy


class ServiceType(Enum):
    ADDITIONAL_SERVICE = "AdditionalService"
    BNET = "Bnet"
    CALL_LIST = "CallList"
    CALL_LIST_VIEW = "CallListView"
    ELECTRICITY_BLOG = "ElectricityBlog"
    ELECTRICITY_MONTHLY_USED = "ElectricityMonthlyUsed"
    ELECTRICITY_MY_PACKAGE_SERVICE = "ElectricityMyPackageService"
    ELECTRICITY_PACKAGE = "ElectricityPackage"
    ELECTRICITY_PAYER = "ElectricityPayer"
    ELECTRICITY_REPORT = "ElectricityReport"
    INTERNET = "Internet"
    INTERNET_SUPPORT_SERVICE = "InternetSupportService"
    INVOICES = "Invoices"
    INVOICE_LIST = "InvoiceList"
    ISP = "Isp"
    PERSONAL = "Personal"
    PHONE = "Phone"
    PHONE_SUPPORT_SERVICE = "PhoneSupportServive"
    SPEED_TEST = "SpeedTest"
    SAM = "Sam"
    SUPPORT = "Support"
    SUPPORT_SERVICE = "SupportService"
    WIFI_DETAILS = "WifiDetails"




@dataclass
class ElectSubscriber(DataClassDictMixin):
    subscriber: str = field(metadata=field_options(alias="Subscriber"))
    is_current: bool = field(metadata=field_options(alias="IsCurrent"))
    address: str = field(metadata=field_options(alias="Address"))


@dataclass
class BaseEntity(DataClassDictMixin):
    id: int = field(metadata=field_options(alias="Id"))
    title: str = field(metadata=field_options(alias="Title"))
    sub_title: Optional[str] = field(metadata=field_options(alias="SubTitle"))
    picture: Optional[str] = field(metadata=field_options(alias="Picture"))
    order: int = field(metadata=field_options(alias="Order"))


@dataclass()
class BaseCard(BaseEntity):
    billing_service_id: Optional[str] = field(metadata=field_options(alias="BillingServiceId"))
    billing_service_code: Optional[str] = field(metadata=field_options(alias="BillingServiceCode"))
    billing_service_description: Optional[str] = field(metadata=field_options(alias="BillingServiceDescription"))
    card_type: str = field(metadata=field_options(alias="CardType"))
    makat: Optional[str] = field(metadata=field_options(alias="Makat"))
    quantity: Optional[int] = field(metadata=field_options(alias="Quantity"))
    sn: Optional[str] = field(metadata=field_options(alias="SN"))
    mac: Optional[str] = field(metadata=field_options(alias="Mac"))
    link: Optional[str] = field(metadata=field_options(alias="Link"))
    enter_link: Optional[str] = field(metadata=field_options(alias="EnterLink"))
    show_mesh_mgt: bool = field(metadata=field_options(alias="ShowMeshMgt"))


class FormattedDate(SerializationStrategy):
    def __init__(self, fmt):
        self.fmt = fmt

    def serialize(self, value: date) -> str:
        return value.strftime(self.fmt)

    def deserialize(self, value: str) -> date:
        return datetime.strptime(value, self.fmt).date()

class FormattedFloatTimestamp(SerializationStrategy):
    def serialize(self, value: datetime) -> float:
        return value.timestamp()

    def deserialize(self, value: float) -> datetime:
        return datetime.fromtimestamp(value)

class FormattedDateTime(SerializationStrategy):
    def __init__(self, fmt):
        self.fmt = fmt

    def serialize(self, value: datetime) -> str:
        return value.strftime(self.fmt)

    def deserialize(self, value: str) -> datetime:
        return datetime.strptime(value, self.fmt)
