from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import field_options

from .base import BaseAuthResponse
from .common import BaseCard

# POST https://my-api.bezeq.co.il/{{version}}/api/InvoicesTab/GetInvoicesTab
#
#
# {
#     "Cards": [],
#     "PhoneNumber": null,
#     "CustomerType": null,
#     "CurrentBen": 0,
#     "Bens": null,
#     "JWTToken": null,
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }


@dataclass
class GetInvoicesTabResponse(BaseAuthResponse):
    phone_number: Optional[str] = field(metadata=field_options(alias="PhoneNumber"))
    customer_type: Optional[str] = field(metadata=field_options(alias="CustomerType"))
    current_ben: int = field(metadata=field_options(alias="CurrentBen"))
    bens: Optional[str] = field(metadata=field_options(alias="Bens"))
    cards: List[BaseCard] = field(default_factory=list, metadata=field_options(alias="Cards"))