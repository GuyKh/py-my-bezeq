import logging
from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import field_options

from my_bezeq.models.cards import DetailedCard

from .base import BaseClientResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/ElectricityTab/GetElectricityTab
# {}
#
#
# {
#     "Cards": [
#         {
#             "BillingServiceId": 10,
#             "BillingServiceCode": "InternetSupportService",
#             "BillingServiceDescription": "תמיכה טכנית",
#             "CardType": "InternetSupportService",
#             "ServiceType": "InternetSupportService",
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
#             "SubTitle": "לפתרון תקלות באינטרנט >",
#             "Picture": null,
#             "Order": 0
#         },
#         {
#             "BillingServiceId": 50,
#             "BillingServiceCode": "INTERNET",
#             "BillingServiceDescription": "אינטרנט",
#             "CardType": "Internet",
#             "ServiceType": "Internet",
#             "CardDetails": "{\"Name\":\"Bfiber\",\"Speed\":\"100 מגה\",\"DownloadSpeed\":\"100\",
#                              \"UploadSpeed\":\"100\",\"BfiberStatus\":-1,\"BfiberStatusDate\":null,
#                               \"UpgradeURL\":null,\"CampaignType\":null,\"bfiberUpgradeLink\":null,
#                               \"bfiberUpgradeText\":null}",
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
#             "CardType": "Sam",
#             "ServiceType": "Sam",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 5,
#             "Title": "מכשירים מחוברים בבית",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 5
#         },
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": null,
#             "BillingServiceDescription": null,
#             "CardType": "Bnet",
#             "ServiceType": "Bnet",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": null,
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 1,
#             "Title": "המוצרים שלי",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 2
#         },
#         {
#             "BillingServiceId": null,
#             "BillingServiceCode": "810",
#             "BillingServiceDescription": null,
#             "CardType": "Isp",
#             "ServiceType": "Isp",
#             "CardDetails": null,
#             "Makat": null,
#             "Quantity": null,
#             "SN": null,
#             "Mac": null,
#             "Link": "https://self.bezeq.co.il/PurchasingProcess/ExternalAuth?Operation=IspBzkPass&ssoToken={{uuid}}",
#             "EnterLink": null,
#             "ShowMeshMgt": false,
#             "Id": 3,
#             "Title": "פרטי התחברות לספק האינטרנט בבזק",
#             "SubTitle": null,
#             "Picture": null,
#             "Order": 3
#         }
#     ],
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }

_LOGGER = logging.getLogger(__name__)


@dataclass
class GetInternetTabResponse(BaseClientResponse):
    cards: Optional[List[DetailedCard]] = field(default_factory=list, metadata=field_options(alias="Cards"))
