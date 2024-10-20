import logging
from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from my_bezeq.models.cards import DetailedCard

from .base import BaseAuthResponse
from .common import BaseEntity, ElectSubscriber

# POST https://my-api.bezeq.co.il/{{version}}/api/Dashboard/GetDashboard
# {"PhoneNumber":""}


# {
#     "Cards": [
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "Invoices",
#             "ServiceType": "Invoices",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 4,
#             "Title": "חשבונית אחרונה",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 1
#         }
#     ],
#     "Tabs": [
#         {
#             "Id": 3,
#             "Title": "חשבוניות",
#             "SubTitle": null,
#             "Picture": "Regular.png",
#             "Order": -4,
#             "CustomerType": null,
#             "Action": null
#         }
#     ],
#     "Bars": [
#         {
#             "Id": 1,
#             "Title": "תמיכה טכנית",
#             "Link": "!701001",
#             "Name": "Support",
#             "SubTitle": null,
#             "Picture": "technichalSupport.png",
#             "Order": 1,
#             "CustomerType": null
#         }
#     ],
#     "IsDesktopBannerDisplayed": true,
#     "JWTToken": "xxx",
#     "CustomerDetails": {
#         "FirstName": "xxx",
#         "LastName": "xxx",
#         "CustomerId": "12344",
#         "HaveCyber": false,
#         "AvailableSubscribers": [],
#         "ElectSubscribers": [
#             {
#                 "Subscriber": "12345",
#                 "IsCurrent": true,
#                 "Address": " תל אביב יפו"
#             }
#         ]
#     },
#     "ShivronDetails": {
#         "HasShivronot": false,
#         "HasEstimatedTime": false,
#         "EstimatedDate": null,
#         "EstimatedTime": null,
#         "EstimatedTimeString": null,
#         "DayOfWeekHeb": null
#     },
#     "TechnicianDetails": {
#         "HasTechnician": false,
#         "TechnicianType": null,
#         "TechnicianDate": null,
#         "TechnicianFromTime": null,
#         "TechnicianToTime": null,
#         "CanCancelTechnician": false,
#         "CanChangeTechnician": false,
#         "ServiceOrderId": 0,
#         "MissionId": 0,
#         "ServiceOrderSourceId": 0,
#         "SuMissionStatusId": 0,
#         "Steps": []
#     },
#     "CmDetails": {
#         "HasCmReferral": false,
#         "IsOpenCm": false,
#         "HasAddress": false,
#         "ReferralId": 0,
#         "ReasonId": null,
#         "CityName": null,
#         "StreetName": null,
#         "HouseNumber": null,
#         "ContactMobileNumber": null
#     },
#     "ShowElectLogo": true,
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }

_LOGGER = logging.getLogger(__name__)


@dataclass
class GetDashboardRequest(DataClassDictMixin):
    phone_number: str = field(default_factory=str, metadata=field_options(alias="PhoneNumber"))

    class Config(BaseConfig):
        serialize_by_alias = True


@dataclass
class Tab(BaseEntity):
    customer_type: Optional[str] = field(metadata=field_options(alias="CustomerType"))
    action: Optional[str] = field(metadata=field_options(alias="Action"))


@dataclass
class Bar(BaseEntity):
    link: str = field(metadata=field_options(alias="Link"))
    name: str = field(metadata=field_options(alias="Name"))
    customer_type: Optional[str] = field(metadata=field_options(alias="CustomerType"))


@dataclass
class AvailableSubscriber(DataClassDictMixin):
    subscriber_no: str = field(metadata=field_options(alias="SubscriberNo"))
    is_current: bool = field(metadata=field_options(alias="IsCurrent"))

@dataclass
class CustomerDetail(DataClassDictMixin):
    first_name: str = field(metadata=field_options(alias="FirstName"))
    last_name: str = field(metadata=field_options(alias="LastName"))
    customer_id: str = field(metadata=field_options(alias="CustomerId"))
    have_cyber: bool = field(metadata=field_options(alias="HaveCyber"))
    available_subscribers: List[AvailableSubscriber] = field(
        default_factory=list, metadata=field_options(alias="AvailableSubscribers"))
    elect_subscribers: List[ElectSubscriber] = field(
        default_factory=list, metadata=field_options(alias="ElectSubscribers")
    )


@dataclass
class ShivronDetail(DataClassDictMixin):
    has_shivronot: bool = field(metadata=field_options(alias="HasShivronot"))
    has_estimated_time: bool = field(metadata=field_options(alias="HasEstimatedTime"))
    estimated_date: Optional[str] = field(metadata=field_options(alias="EstimatedDate"))
    estimated_time: Optional[str] = field(metadata=field_options(alias="EstimatedTime"))
    estimated_time_string: Optional[str] = field(metadata=field_options(alias="EstimatedTimeString"))
    day_of_week_heb: Optional[str] = field(metadata=field_options(alias="DayOfWeekHeb"))


@dataclass
class TechnicianDetail(DataClassDictMixin):
    has_technician: bool = field(metadata=field_options(alias="HasTechnician"))
    technician_type: Optional[str] = field(metadata=field_options(alias="TechnicianType"))
    technician_date: Optional[str] = field(metadata=field_options(alias="TechnicianDate"))
    technician_from_time: Optional[str] = field(metadata=field_options(alias="TechnicianFromTime"))
    technician_to_time: Optional[str] = field(metadata=field_options(alias="TechnicianToTime"))
    can_cancel_technician: bool = field(metadata=field_options(alias="CanCancelTechnician"))
    can_change_technician: bool = field(metadata=field_options(alias="CanChangeTechnician"))
    service_order_id: int = field(metadata=field_options(alias="ServiceOrderId"))
    mission_id: int = field(metadata=field_options(alias="MissionId"))
    service_order_source_id: int = field(metadata=field_options(alias="ServiceOrderSourceId"))
    su_mission_status_id: int = field(metadata=field_options(alias="SuMissionStatusId"))
    steps: List = field(default_factory=list, metadata=field_options(alias="Steps"))


@dataclass
class CmDetail(DataClassDictMixin):
    has_cm_referral: bool = field(metadata=field_options(alias="HasCmReferral"))
    is_open_cm: bool = field(metadata=field_options(alias="IsOpenCm"))
    has_address: bool = field(metadata=field_options(alias="HasAddress"))
    referral_id: int = field(metadata=field_options(alias="ReferralId"))
    reason_id: Optional[int] = field(metadata=field_options(alias="ReasonId"))
    city_name: Optional[str] = field(metadata=field_options(alias="CityName"))
    street_name: Optional[str] = field(metadata=field_options(alias="StreetName"))
    house_number: Optional[str] = field(metadata=field_options(alias="HouseNumber"))
    contact_mobile_number: Optional[str] = field(metadata=field_options(alias="ContactMobileNumber"))


@dataclass
class GetDashboardResponse(BaseAuthResponse):
    is_desktop_banner_displayed: bool = field(metadata=field_options(alias="IsDesktopBannerDisplayed"))
    customer_details: CustomerDetail = field(metadata=field_options(alias="CustomerDetails"))
    shivron_details: ShivronDetail = field(metadata=field_options(alias="ShivronDetails"))
    technician_details: TechnicianDetail = field(metadata=field_options(alias="TechnicianDetails"))
    cm_details: CmDetail = field(metadata=field_options(alias="CmDetails"))
    show_elect_logo: bool = field(metadata=field_options(alias="ShowElectLogo"))
    cards: Optional[List[DetailedCard]] = field(default_factory=list, metadata=field_options(alias="Cards"))
    tabs: List[Tab] = field(default_factory=list, metadata=field_options(alias="Tabs"))
    bars: List[Bar] = field(default_factory=list, metadata=field_options(alias="Bars"))
