from dataclasses import dataclass, field
from typing import Optional

from mashumaro import field_options

from my_bezeq.models.base import BaseAuthResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/TechCoord/GetTimeWindows
#
# {
#     "TimesFrames": null,
#     "JWTToken": null,
#     "IsSuccessful": false,
#     "ErrorCode": "CANNOT_CHANGE_TECH_DATE",
#     "ErrorMessage": "Does not having technician or cannot update date",
#     "ClientErrorMessage": ""
# }

@dataclass
class GetTimeWindowsResponse(BaseAuthResponse):
    time_frames: Optional[list] = field(metadata=field_options(alias="TimesFrames"))
