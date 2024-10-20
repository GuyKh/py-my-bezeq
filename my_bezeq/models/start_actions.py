from dataclasses import dataclass, field

from mashumaro import DataClassDictMixin, field_options

from my_bezeq.models.base import BaseClientResponse

# POST api/InternetTab/GetWifiData
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
class StartAction(DataClassDictMixin):
    id: int = field(metadata=field_options(alias="Id"))
    action_name: str = field(metadata=field_options(alias="actionName"))
    action_name_to_display: str = field(metadata=field_options(alias="actionNameToDisplay"))
    action_url: str = field(metadata=field_options(alias="actionURL"))
    order: int = field(metadata=field_options(alias="Order"))


@dataclass
class StartActionsResponse(BaseClientResponse):
    start_actions: list[StartAction] = field(default_factory=list, metadata=field_options(alias="StartActions"))
