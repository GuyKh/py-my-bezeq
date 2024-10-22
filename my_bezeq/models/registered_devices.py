from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from .base import BaseClientResponse
from .common import FormattedFloatTimestamp

# POST https://my-api.bezeq.co.il/{{version}}/api/InternetTab/GetRegisteredDevices
# {"MacList":[]}

# {
#     "RegisteredDevices": [
#         {
#             "ConnectionType": 3,
#             "ConnectionTypeText": "נתב",
#             "ConnectionTypePicUrl": "RegisteredDeviceIcon_EthernetConnection.png",
#             "DeviceType": 0,
#             "DeviceTypePicUrl": "RegisteredDeviceIcon_GeneralDevices.png",
#             "DeviceTypeName": "",
#             "DeviceName": "",
#             "HostName": "",
#             "Ipv4": "0.1.2.3",
#             "IsTracked": false,
#             "Mac": "aa:aa:aa:aa:aa:a",
#             "PolicyState": 1,
#             "SigStr": 10,
#             "Zone": "Home",
#             "ZonePicUrl": "ZoneConnected.png",
#             "DeviceClass": "",
#             "DeviceOs": "",
#             "DeviceModel": "",
#             "LastSeen": 1.7292347E+09,
#             "DeviceNameToDisplay": "Device",
#             "DeviceProduct": null
#         },
#         {
#             "ConnectionType": 3,
#             "ConnectionTypeText": "נתב",
#             "ConnectionTypePicUrl": "RegisteredDeviceIcon_EthernetConnection.png",
#             "DeviceType": 40013,
#             "DeviceTypePicUrl": "",
#             "DeviceTypeName": "TP-Link_Mesh_Linux_Deco_M5",
#             "DeviceName": "",
#             "HostName": "deco_M5",
#             "Ipv4": "1.2.3.4",
#             "IsTracked": false,
#             "Mac": "bb:bb:bb:bb:bb:bb",
#             "PolicyState": 1,
#             "SigStr": 10,
#             "Zone": "Home",
#             "ZonePicUrl": "ZoneConnected.png",
#             "DeviceClass": "Mesh",
#             "DeviceOs": "Linux",
#             "DeviceModel": "M5",
#             "LastSeen": 1.7292347E+09,
#             "DeviceNameToDisplay": "TP-Link Deco M5 Mesh",
#             "DeviceProduct": "Deco"
#         }
#     ],
#     "RegisteredSmartphones": [],
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }



@dataclass
class GetRegisteredDevicesRequest(DataClassDictMixin):
    recipient_number: list[str] = field(default_factory=list, metadata=field_options(alias="MacList"))

    class Config(BaseConfig):
        serialize_by_alias = True

@dataclass
class RegisteredDevice(DataClassDictMixin):
    connection_type: int = field(metadata=field_options(alias="ConnectionType"))
    connection_type_text: str = field(metadata=field_options(alias="ConnectionTypeText"))
    connection_type_pic_url: str = field(metadata=field_options(alias="ConnectionTypePicUrl"))
    device_type: int = field(metadata=field_options(alias="DeviceType"))
    device_type_pic_url: Optional[str] = field(metadata=field_options(alias="DeviceTypePicUrl"))
    device_type_name: Optional[str] = field(metadata=field_options(alias="DeviceTypeName"))
    device_name: Optional[str] = field(metadata=field_options(alias="DeviceName"))
    host_name: Optional[str] = field(metadata=field_options(alias="HostName"))
    ipv4: str = field(metadata=field_options(alias="Ipv4"))
    is_tracked: bool = field(metadata=field_options(alias="IsTracked"))
    mac: str = field(metadata=field_options(alias="Mac"))
    policy_state: int = field(metadata=field_options(alias="PolicyState"))
    sig_str: int = field(metadata=field_options(alias="SigStr"))
    zone: str = field(metadata=field_options(alias="Zone"))
    zone_pic_url: str = field(metadata=field_options(alias="ZonePicUrl"))
    device_class: Optional[str] = field(metadata=field_options(alias="DeviceClass"))
    device_os: Optional[str] = field(metadata=field_options(alias="DeviceOs"))
    device_model: Optional[str] = field(metadata=field_options(alias="DeviceModel"))
    last_seen: Optional[datetime] = field(
        metadata=field_options(alias="LastSeen", serialization_strategy=FormattedFloatTimestamp())
    )
    device_name_to_display: str = field(metadata=field_options(alias="DeviceNameToDisplay"))
    device_product: Optional[str] = field(metadata=field_options(alias="DeviceProduct"))

@dataclass
class GetRegisteredDevicesResponse(BaseClientResponse):
    registered_devices: List[RegisteredDevice] = field(default_factory=list,
                                                       metadata=field_options(alias="RegisteredDevices"))
    registered_smartphones: List = field(default_factory=list, metadata=field_options(alias="RegisteredSmartphones"))
