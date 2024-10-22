import logging
from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import field_options

from my_bezeq.models.cards import DetailedCard

from .base import BaseAuthResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/InvoicesTab/GetElectInvoiceTab
#
# {
#     "Cards": [
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "Invoices",
#             "ServiceType": "Invoices",
#             "CardDetails": "{\"Invoices\":[{\"InvoiceId\":\"aaaa-0eed-425f-889a-4735f235fd5c\",
#                               \"DatePeriod\":\"2024 ספטמבר\",\"Sum\":123.4,
#                               \"InvoiceNumber\":\"1234\",\"IsPayed\":null,
#                               \"PayUrl\":null,\"PayerNumber\":1}],\"HaveHok\":true,\"PayUrl\":null}",
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 1,
#             "Title": "חשבונית אחרונה",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 0
#         }
#     ],
#     "PhoneNumber": null,
#     "CustomerType": null,
#     "CurrentBen": 0,
#     "Bens": null,
#     "JWTToken": "xxxx",
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }

_LOGGER = logging.getLogger(__name__)

@dataclass
class GetElectricInvoiceTabResponse(BaseAuthResponse):
    phone_number: Optional[str] = field(metadata=field_options(alias="PhoneNumber"))
    customer_type: Optional[str] = field(metadata=field_options(alias="CustomerType"))
    current_ben: int = field(metadata=field_options(alias="CurrentBen"))
    bens: Optional[str] = field(metadata=field_options(alias="Bens"))
    cards: Optional[List[DetailedCard]] = field(default_factory=list, metadata=field_options(alias="Cards"))
