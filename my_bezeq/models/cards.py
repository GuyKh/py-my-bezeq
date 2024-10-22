
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Type

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig
from mashumaro.types import SerializationStrategy

from my_bezeq.models.common import BaseCard, ServiceType

_LOGGER = logging.getLogger(__name__)

class FormattedElectricTabDate(SerializationStrategy):
    def serialize(self, value: datetime) -> str:
        return f"/Date({str(int(value.timestamp()) * 100)})/"

    def deserialize(self, value: str) -> datetime:
        return datetime.fromtimestamp(int(value[6:-2]) // 1000)

class BaseCardDetails(DataClassDictMixin):
    @classmethod
    def decode(cls, data: str) -> "BaseCardDetails":
        """Decode JSON string into the correct card detail class"""
        raise NotImplementedError("This method should be implemented in subclasses.")


@dataclass
class ElectricityMyPackageServiceCard(BaseCardDetails):
    description: str = field(metadata=field_options(alias="Description"))
    package_name: str = field(metadata=field_options(alias="PackageName"))
    discount: str = field(metadata=field_options(alias="Discount"))

    @classmethod
    def decode(cls, data: str) -> "ElectricityMyPackageServiceCard":
        """Decode JSON string for Personal card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class ElectricityMonthlyUsedCard(BaseCardDetails):
    used_amount: int = field(metadata=field_options(alias="UsedAmount"))
    from_date: datetime = field(metadata=field_options(alias="FromDate"))

    class Config(BaseConfig):
        serialize_by_alias = True
        serialization_strategy = {datetime: FormattedElectricTabDate()}

    @classmethod
    def decode(cls, data: str) -> "ElectricityMonthlyUsedCard":
        """Decode JSON string for card"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)


@dataclass
class ElectricityPayerCard(BaseCardDetails):
    contract_number: str = field(metadata=field_options(alias="ContractNumber"))
    counter_number: str = field(metadata=field_options(alias="CounterNumber"))
    have_mone_bsisi: bool = field(metadata=field_options(alias="HaveMoneBsisi"))

    @classmethod
    def decode(cls, data: str) -> "ElectricityPayerCard":
        """Decode JSON string for card"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class ElectricityPackageCard(DataClassDictMixin):
    description: str = field(metadata=field_options(alias="Description"))
    package_name: str = field(metadata=field_options(alias="PackageName"))
    discount: str = field(metadata=field_options(alias="Discount"))

    @classmethod
    def decode(cls, data: str) -> "ElectricityPackageCard":
        """Decode JSON string for card"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)


@dataclass
class User(DataClassDictMixin):
    subscriber_no: str = field(metadata=field_options(alias="SubscriberNo"))
    personal_id: str = field(metadata=field_options(alias="PersonalId"))
    username: str = field(metadata=field_options(alias="UserName"))
    last_name: str = field(metadata=field_options(alias="LastName"))
    first_name: str = field(metadata=field_options(alias="FirstName"))
    email: str = field(metadata=field_options(alias="Email"))
    contact_mobile_number: str = field(metadata=field_options(alias="ContactMobileNumber"))
    login_by_otp_only: bool = field(metadata=field_options(alias="LoginByOtpOnly"))

@dataclass
class PersonalCard(BaseCardDetails):
    user: User = field(metadata=field_options(alias="User"))
    auth_management_link: Optional[str] = field(default=None, metadata=field_options(alias="AuthManagementLink"))

    @classmethod
    def decode(cls, data: str) -> "PersonalCard":
        """Decode JSON string for card"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class Invoice(DataClassDictMixin):
    invoice_id: str = field(metadata=field_options(alias="InvoiceId"))
    date_period: str = field(metadata=field_options(alias="DatePeriod"))
    sum: float = field(metadata=field_options(alias="Sum"))
    payer_number: int = field(metadata=field_options(alias="PayerNumber"))
    invoice_number: str = field(metadata=field_options(alias="InvoiceNumber"))
    is_payed: Optional[bool] = field(default=None, metadata=field_options(alias="IsPayed"))
    pay_url: Optional[str] = field(default=None, metadata=field_options(alias="PayUrl"))

@dataclass
class InvoicesCard(BaseCardDetails):
    invoices: list[Invoice] = field(metadata=field_options(alias="Invoices"))
    have_hok: bool = field(metadata=field_options(alias="HaveHok")) # Have Hora'a Keva (Standing order)
    pay_url: Optional[str] = field(default=None, metadata=field_options(alias="PayUrl"))

    @classmethod
    def decode(cls, data: str) -> "InvoicesCard":
        """Decode JSON string for Invoice card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class InvoiceListCard(BaseCardDetails):
    invoices: list[Invoice] = field(metadata=field_options(alias="Invoices"))

    @classmethod
    def decode(cls, data: str) -> "InvoicesCard":
        """Decode JSON string for Invoice card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)


@dataclass
class InternetCard(BaseCardDetails):
    name: str = field(metadata=field_options(alias="Name"))
    speed: str = field(metadata=field_options(alias="Speed"))
    download_speed: str = field(metadata=field_options(alias="DownloadSpeed"))
    upload_speed: str = field(metadata=field_options(alias="UploadSpeed"))
    bfiber_status: int = field(metadata=field_options(alias="BfiberStatus"))
    bfiber_status_date: Optional[str] = field(default=None, metadata=field_options(alias="BfiberStatusDate"))
    upgrade_url: Optional[str] = field(default=None, metadata=field_options(alias="UpgradeURL"))
    campaign_type: Optional[str] = field(default=None, metadata=field_options(alias="CampaignType"))
    bfiber_upgrade_link: Optional[str] = field(default=None, metadata=field_options(alias="bfiberUpgradeLink"))
    bfiber_upgrade_text: Optional[str] = field(default=None, metadata=field_options(alias="bfiberUpgradeText"))

    @classmethod
    def decode(cls, data: str) -> "InternetCard":
        """Decode JSON string for Internet card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)


@dataclass
class Buffer(DataClassDictMixin):
    package_name: str = field(metadata=field_options(alias="PackageName"))
    soc: str = field(metadata=field_options(alias="Soc"))
    description: str = field(metadata=field_options(alias="Description"))
    used_units: str = field(metadata=field_options(alias="UsedUnits"))
    remaining_units: str = field(metadata=field_options(alias="RemainingUnits"))
    inclusive_amount: str = field(metadata=field_options(alias="InclusiveAmount"))
    inclusive_type: str = field(metadata=field_options(alias="InclusiveType"))
    level_code: str = field(metadata=field_options(alias="LevelCode"))
    period_name: str = field(metadata=field_options(alias="PeriodName"))
    used_units_percent: str = field(metadata=field_options(alias="UsedUnitsPercent"))

@dataclass
class PhoneCard(BaseCardDetails):
    buffers: Optional[list[Buffer]] = field(metadata=field_options(alias="Buffers"))

    @classmethod
    def decode(cls, data: str) -> "PhoneCard":
        """Decode JSON string for Buffer card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class CallRecord(DataClassDictMixin):
    call_log_type: int = field(metadata=field_options(alias="CallLogType"))
    image_name: str = field(metadata=field_options(alias="ImageName"))
    call_log_date: str = field(metadata=field_options(alias="CallLogDate"))
    call_log_phone_num: str = field(metadata=field_options(alias="CallLogPhoneNum"))
    call_log_time: str = field(metadata=field_options(alias="CallLogTime"))
    call_log_duration: str = field(metadata=field_options(alias="CallLogDuration"))

@dataclass
class CallListCard(BaseCardDetails):
    max_rows: int = field(metadata=field_options(alias="MaxRows"))
    call_records: list[CallRecord] = field(metadata=field_options(alias="CallRecords"))
    bezeq_bill_url: Optional[str] = field(default=None, metadata=field_options(alias="BezeqBillUrl"))

    @classmethod
    def decode(cls, data: str) -> "CallListCard":
        """Decode JSON string for CallLog card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class AdditionalServicesCard(BaseCardDetails):
    additional_services_lst: list[BaseCard] = field(metadata=field_options(alias="AdditionalServicesLst"))

    @classmethod
    def decode(cls, data: str) -> "AdditionalServicesCard":
        """Decode JSON string for Additional Services card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)


@dataclass
class SpeedTestCard(BaseCardDetails):
    is_speed_test_internal: bool = field(metadata=field_options(alias="IsSpeedTestInternal"))
    is_speed_ok: bool = field(metadata=field_options(alias="IsSpeedOk"))
    is_speed_test_slow: bool = field(metadata=field_options(alias="IsSpeedTestSlow"))
    is_speed_test_error: bool = field(metadata=field_options(alias="IsSpeedTestError"))
    average_speed: Optional[float] = field(default=None, metadata=field_options(alias="AverageSpeed"))
    ookla_link: str = field(metadata=field_options(alias="OoklaLink"))
    glassix_speed_test_code: Optional[str] = field(default=None, metadata=field_options(alias="GlassixSpeedTestCode"))


    @classmethod
    def decode(cls, data: str) -> "CallListCard":
        """Decode JSON string for CallLog card details"""
        decoded_data = json.loads(data)
        return cls.from_dict(decoded_data)

@dataclass
class DetailedCard(BaseCard):
    service_type: ServiceType = field(metadata=field_options(alias="ServiceType"))
    card_details: Optional[str] = field(metadata=field_options(alias="CardDetails"))

    def __post_init__(self):
        # Deserialize `card_details` field from a JSON string to a `CardDetails` object
        if isinstance(self.card_details, str):
            try:
                service_type = self.service_type
                card_details = self.card_details
                card_details_class = SERVICE_TYPE_TO_CLASS.get(service_type)
                if card_details_class and card_details:
                    self.card_details = card_details_class.decode(card_details)
            except Exception as e:
                _LOGGER.error(f"Failed to deserialize card details: {self.card_details} - {e}")

@dataclass
class CardDetailsResponse(DataClassDictMixin):
    service_type: Optional[ServiceType] = field(metadata=field_options(alias="ServiceType"))
    card_details: Optional[str] = field(metadata=field_options(alias="CardDetails"))

    def __post_init__(self):
        # Deserialize `card_details` field from a JSON string to a `CardDetails` object
        if self.service_type and isinstance(self.card_details, str):
            try:
                service_type = self.service_type
                card_details = self.card_details
                card_details_class = SERVICE_TYPE_TO_CLASS.get(service_type)
                if card_details_class and card_details:
                    self.card_details = card_details_class.decode(card_details)
            except Exception as e:
                _LOGGER.error(f"Failed to deserialize card details: {self.card_details} - {e}")

SERVICE_TYPE_TO_CLASS: dict[str, Type[BaseCardDetails]] = {
    ServiceType.ADDITIONAL_SERVICE: AdditionalServicesCard,
    ServiceType.CALL_LIST: CallListCard,
    ServiceType.ELECTRICITY_MONTHLY_USED: ElectricityMonthlyUsedCard,
    ServiceType.ELECTRICITY_MY_PACKAGE_SERVICE: ElectricityMyPackageServiceCard,
    ServiceType.ELECTRICITY_PACKAGE: ElectricityPackageCard,
    ServiceType.ELECTRICITY_PAYER: ElectricityPayerCard,
    ServiceType.INTERNET: InternetCard,
    ServiceType.INVOICES: InvoicesCard,
    ServiceType.INVOICE_LIST: InvoiceListCard,
    ServiceType.PERSONAL: PersonalCard,
    ServiceType.PHONE: PhoneCard,
    ServiceType.SPEED_TEST: SpeedTestCard,
}
