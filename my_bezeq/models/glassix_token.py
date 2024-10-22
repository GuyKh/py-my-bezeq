
from dataclasses import dataclass, field
from uuid import UUID

from mashumaro import field_options
from mashumaro.config import BaseConfig

from my_bezeq.models.base import BaseClientResponse

# POST https://my-api.bezeq.co.il/v72.3/api/Auth/GenGlassixToken
# {Action: "701003"}

# {
#     "token": "{uuid}",
#     "Status": 0,
#     "Reason": "Success",
#     "ErrorCode": "0",
#     "ErrorMessage": "Success",
#     "IsSuccessful": true,
#     "ClientErrorMessage": ""
# }

@dataclass
class GenGlassixTokenRequest(BaseClientResponse):
    action: str = field(metadata=field_options(alias="Action"))

    class Config(BaseConfig):
        serialize_by_alias = True

@dataclass
class GenGlassixTokenResponse(BaseClientResponse):
    token: UUID = field(metadata=field_options(alias="token"))
    status: int = field(metadata=field_options(alias="Status"))
