import json
from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import DataClassDictMixin, field_options

from .base import BaseAuthResponse
from .common import BaseCard

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


@dataclass
class Invoice(DataClassDictMixin):
    invoice_id: str = field(metadata=field_options(alias="InvoiceId"))
    date_period: str = field(metadata=field_options(alias="DatePeriod"))
    sum: float = field(metadata=field_options(alias="Sum"))
    invoice_number: str = field(metadata=field_options(alias="InvoiceNumber"))
    is_payed: Optional[bool] = field(metadata=field_options(alias="IsPayed"))
    pay_url: Optional[str] = field(metadata=field_options(alias="PayUrl"))
    payer_number: int = field(metadata=field_options(alias="PayerNumber"))


@dataclass
class CardDetails(DataClassDictMixin):
    have_hok: bool = field(metadata=field_options(alias="HaveHok"))
    pay_url: Optional[str] = field(metadata=field_options(alias="PayUrl"))
    invoices: List[Invoice] = field(default_factory=list, metadata=field_options(alias="Invoices"))


@dataclass
class ElectricInvoiceCard(BaseCard):
    card_details: Optional[CardDetails] = None  # We'll manually set this

    def __post_init__(self):
        # Deserialize `card_details` field from a JSON string to a `CardDetails` object
        if isinstance(self.card_details, str):
            self.card_details = CardDetails.from_dict(json.loads(self.card_details))


@dataclass
class GetElectricInvoiceTabResponse(BaseAuthResponse):
    phone_number: Optional[str] = field(metadata=field_options(alias="PhoneNumber"))
    customer_type: Optional[str] = field(metadata=field_options(alias="CustomerType"))
    current_ben: int = field(metadata=field_options(alias="CurrentBen"))
    bens: Optional[str] = field(metadata=field_options(alias="Bens"))
    cards: List[ElectricInvoiceCard] = field(default_factory=list, metadata=field_options(alias="Cards"))
