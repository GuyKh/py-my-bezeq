from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import field_options

from my_bezeq.models.common import BaseCard

from .base import BaseResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/CustomerMessages/GetCustomerMessages
#
# {"pushMsgList":[],"pushMsgCodesList":[],"MessagesCards":[{
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": null,
#             "ServiceType": null,
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": "",
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 4,
#             "Title": "showSpamMes",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 3
#         }],"IsSuccessful":true,"ErrorCode":"","ErrorMessage":"",
#   "Message":"","ServiceTimeTaken":null,"TransactionID":"","APIConsumingInfo":[]}


@dataclass
class GetCustomerMessagesResponse(BaseResponse):
    service_time_taken: Optional[int] = field(metadata=field_options(alias="ServiceTimeTaken"))
    transaction_id: str = field(metadata=field_options(alias="TransactionID"))
    push_msg_list: List = field(default_factory=list, metadata=field_options(alias="pushMsgList"))
    push_msg_codes_list: List = field(default_factory=list, metadata=field_options(alias="pushMsgCodesList"))
    message_cards: List[BaseCard] = field(default_factory=list, metadata=field_options(alias="MessagesCards"))
    message: str = field(default_factory=str, metadata=field_options(alias="Message"))
    APIConsumingInfo: str = field(default_factory=str, metadata=field_options(alias="APIConsumingInfo"))
