import logging
from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from my_bezeq.models.cards import DetailedCard

from .base import BaseClientResponse
from .common import ElectSubscriber

# POST https://my-api.bezeq.co.il/{{version}}/api/ElectricityTab/GetElectricityTab
# {}
#
#
# {
#     "Cards": [
#         {
#             "BillingServiceId": 60,
#             "BillingServiceCode": "ElectricityMyPackage",
#             "BillingServiceDescription": "חבילת החשמל שלי",
#             "CardType": "ElectricityMyPackageService",
#             "ServiceType": "ElectricityMyPackageService",
#             "CardDetails":"{\"Description\":\"כל השבוע, ימים א\' - ש\' בכל שעות היממה\",
#                               \"PackageName\":\"חוסכים חכם 24/7\",\"Discount\":\"7% הנחה\"}",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 1,
#             "Title": "חוסכים חכם 24/7",
#             "SubTitle": "7% הנחה",
#             "Picture": "AllDayPackage.png",
#             "Order": 1
#         },
#         {
#             "BillingServiceId": 70,
#             "BillingServiceCode": "ElectricityMonthlyUsed",
#             "BillingServiceDescription": "צריכת החשמל שלי",
#             "CardType": "ElectricityMonthlyUsed",
#             "ServiceType": "ElectricityMonthlyUsed",
#             "CardDetails": "{\"UsedAmount\":123,\"FromDate\":\"\/Date(1727730000000)\/\"}",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 2,
#             "Title": "צריכה חודשית מצטברת",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 2
#         },
#         {
#             "BillingServiceId": 20,
#             "BillingServiceCode": "ElectricityPayer",
#             "BillingServiceDescription": "פרטי משלם",
#             "CardType": "ElectricityPayer",
#             "ServiceType": "ElectricityPayer",
#             "CardDetails": "{\"ContractNumber\":\"346669815\",
#                               \"CounterNumber\":\"503-23589529\",\"HaveMoneBsisi\":false}",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 6,
#             "Title": "פרטי משלם",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 6
#         },
#         {
#             "BillingServiceId": 90,
#             "BillingServiceCode": "ElectricityBlog",
#             "BillingServiceDescription": "טיפים חשמל",
#             "CardType": "ElectricityBlog",
#             "ServiceType": "ElectricityBlog",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": "https://www.bezeq.co.il/bloghome/Benergy",
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 4,
#             "Title": " טיפים לחסכון בחשמל",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 5
#         },
#         {
#             "BillingServiceId": 90,
#             "BillingServiceCode": "ElectricityReport",
#             "BillingServiceDescription": "נתוני צריכה",
#             "CardType": "ElectricityReport",
#             "ServiceType": "ElectricityReport",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 5,
#             "Title": "נתוני צריכה",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 3
#         }
#     ],
#     "ElectSubscribers": [
#         {
#             "Subscriber": "1234",
#             "IsCurrent": true,
#             "Address": "כתובת"
#         }
#     ],
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }

_LOGGER = logging.getLogger(__name__)

@dataclass
class GetElectricityTabRequest(DataClassDictMixin):
    jwt_token: str = field(metadata=field_options(alias="JWTToken"))
    subscriber_number: str = field(metadata=field_options(alias="SubscriberNumber"))

    class Config(BaseConfig):
        serialize_by_alias = True


@dataclass
class GetElectricityTabResponse(BaseClientResponse):
    cards: Optional[List[DetailedCard]] = field(default_factory=list, metadata=field_options(alias="Cards"))
    elect_subscribers: List[ElectSubscriber] = field(
        default_factory=list, metadata=field_options(alias="ElectSubscribers")
    )
