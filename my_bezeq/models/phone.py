from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import field_options

from my_bezeq.models.cards import DetailedCard

from .base import BaseResponse

# POST
#
# {
#     "Cards": [
#         {
#             "BillingServiceId": 10,
#             "BillingServiceCode": "phonesupport",
#             "BillingServiceDescription": "תמיכה טכנית",
#             "CardType": "PhoneSupportService",
#             "ServiceType": "PhoneSupportService",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": "https://www.bezeq.co.il/serviceandsupport/solutions/",
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 0,
#             "Title": "תמיכה טכנית ופתרון תקלות",
#             "SubTitle": "לפתרון תקלות בטלפון >",
#             "Picture": null,
#             "Order": 0
#         },
#         {
#             "BillingServiceId": 10,
#             "BillingServiceCode": "FIX_LINE",
#             "BillingServiceDescription": "קו טלפון",
#             "CardType": "Phone",
#             "ServiceType": "Phone",
#             "CardDetails": "{\"Buffers\":[{
#                   \"PackageName\":\"חבילת דקות 50 \",
#                   \"Soc\":\"1234\",
#                   \"Description\":\"50 דקות קו טלפון\",
#                   \"UsedUnits\":\"0\",
#                   \"RemainingUnits\":\"0\",
#                   \"InclusiveAmount\":\"50\",
#                   \"InclusiveType\":\"דקות\",
#                   \"LevelCode\":\"C\",
#                   \"PeriodName\":\"ללא\",
#                   \"UsedUnitsPercent\":\"0\"}
#               ]}",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 1,
#             "Title": "החבילה שלי",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 1
#         },
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "CallList",
#             "ServiceType": "CallList",
#             "CardDetails": "...,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 2,
#             "Title": "שיחות אחרונות",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 2
#         },
#         {
#             "BillingServiceId": 10,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "CallListView",
#             "ServiceType": "CallListView",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 3,
#             "Title": "שיחות יוצאות",
#             "SubTitle": "לפירוט השיחות היוצאות",
#             "Picture": null,
#             "Order": 3
#         },
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "AdditionalService",
#             "ServiceType": "AdditionalService",
#             "CardDetails": "...",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 4,
#             "Title": "השירותים על הקו",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 4
#         }
#     ],
#     "PhoneNumber": "12345",
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }

@dataclass
class GetPhoneTabResponse(BaseResponse):
    phone_number: str = field(metadata=field_options(alias="PhoneNumber"))
    cards: Optional[List[DetailedCard]] = field(default_factory=list, metadata=field_options(alias="Cards"))
