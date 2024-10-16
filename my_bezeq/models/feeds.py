from dataclasses import dataclass, field
from typing import List

from mashumaro import field_options

from .base import BaseClientResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/InternetTab/GetFeeds
#
# {
#     "Feeds": [],
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }


@dataclass
class GetFeedsResponse(BaseClientResponse):
    feeds: List = field(default_factory=list, metadata=field_options(alias="Feeds"))
