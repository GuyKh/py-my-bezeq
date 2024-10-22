from dataclasses import dataclass, field
from typing import Optional

from mashumaro import field_options

from my_bezeq.models.base import BaseClientResponse

# POST
#
# {
#     "SsidName": null,
#     "SsidPass": null,
#     "WifiState": false,
#     "WifiPasswordStrength": 0,
#     "WifiNetworkHeader": null,
#     "WifiNetworkText": null,
#     "IsBeRouter": false,
#     "Link": null,
#     "RouterSerialNumber": null,
#     "IsBnetMode": false,
#     "IsSuccessful": false,
#     "ErrorCode": "-1",
#     "ErrorMessage": "אירעה שגיאה, נא לנסות מאוחר יותר",
#     "ClientErrorMessage": ""
# }

@dataclass
class GetWifiDataResponse(BaseClientResponse):
    ssid_name: Optional[str] = field(default=None, metadata=field_options(alias="SsidName"))
    ssid_pass: Optional[str] = field(default=None, metadata=field_options(alias="SsidPass"))
    wifi_state: bool = field(metadata=field_options(alias="WifiState"))
    wifi_password_strength: int = field(metadata=field_options(alias="WifiPasswordStrength"))
    wifi_network_header: Optional[str] = field(default=None, metadata=field_options(alias="WifiNetworkHeader"))
    wifi_network_text: Optional[str] = field(default=None, metadata=field_options(alias="WifiNetworkText"))
    is_be_router: bool = field(metadata=field_options(alias="IsBeRouter"))
    link: Optional[str] = field(default=None, metadata=field_options(alias="Link"))
    router_serial_number: Optional[str] = field(default=None, metadata=field_options(alias="RouterSerialNumber"))
    is_bnet_mode: bool = field(metadata=field_options(alias="IsBnetMode"))
