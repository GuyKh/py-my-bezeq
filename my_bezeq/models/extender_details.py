from dataclasses import dataclass, field

from mashumaro import field_options

from my_bezeq.models.base import BaseClientResponse
from my_bezeq.models.cards import CardDetailsResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/InternetTab/GetExtendersDetails
#
# {
#     "CardDetails": null,
#     "ServiceType": null,
#     "Link": null,
#     "IsSuccessful": false,
#     "ErrorCode": "no extenders",
#     "ErrorMessage": "GEN01",
#     "ClientErrorMessage": ""
# }

@dataclass
class GetExtendersDetailsResponse(CardDetailsResponse, BaseClientResponse):
        link: str = field(metadata=field_options(alias="Link"))
