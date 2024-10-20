from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import field_options

from my_bezeq.models.cards import DetailedCard

from .base import BaseResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/InvoicesTab/GetInvoicesTab
#
#
# {
#     "Cards": [
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "Personal",
#             "ServiceType": "Personal",
#             "CardDetails": "{
#                       \"User\":{
#                               \"SubscriberNo\":\"\",
#                               \"PersonalId\":\"1234\",
#                               \"UserName\":\"1234\",
#                               \"LastName\":\"שם\",
#                               \"FirstName\":\"מחא\",
#                               \"Email\":\"me@gmail.com\",
#                               \"ContactMobileNumber\":\"052345\",
#                               \"LoginByOtpOnly\":false},
#                   \"AuthManagementLink\":null}",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 1,
#             "Title": "איזור אישי",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": null
#         }
#     ],
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }


@dataclass
class GetPersonalTabResponse(BaseResponse):
    cards: Optional[List[DetailedCard]] = field(default_factory=list, metadata=field_options(alias="Cards"))
