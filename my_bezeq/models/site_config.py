from dataclasses import dataclass, field
from typing import List

from mashumaro import DataClassDictMixin, field_options

from my_bezeq.models.base import BaseResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/GeneralActions/GetSiteConfig
#
# {
#     "Params": [
#         {
#             "Id": 7,
#             "ParamName": "LogOutTime",
#             "ParamValue": "20"
#         },
#         {
#             "Id": 1010,
#             "ParamName": "LAST_VERSION_CODE_IOS",
#             "ParamValue": "72.3.0.127"
#         },....
#     ],
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }


@dataclass
class Param(DataClassDictMixin):
    id: int = field(metadata=field_options(alias="Id"))
    param_name: str = field(metadata=field_options(alias="ParamName"))
    param_value: str = field(metadata=field_options(alias="ParamValue"))


@dataclass
class GetSiteConfigResponse(BaseResponse):
    params: List[Param] = field(default_factory=list, metadata=field_options(alias="Params"))
