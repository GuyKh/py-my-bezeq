from dataclasses import dataclass

from my_bezeq.models.base import BaseClientResponse
from my_bezeq.models.cards import CardDetailsResponse

# POST https://my-api.bezeq.co.il/{{version}}/api/InternetTab/GetSpeeTestdCard
#
# {
#     "CardDetails":"{\"IsSpeedTestInternal\":false,\"IsSpeedOk\":false,\"IsSpeedTestSlow\":false,
#               \"IsSpeedTestError\":false,\"AverageSpeed\":null,
#               \"OoklaLink\":\"https://www.bezeq.co.il/internetandphone/internet/speedtest?internal_source=myb\&WT.isp=myb\",
#               \"GlassixSpeedTestCode\":null}",
#     "ServiceType": "SpeedTest",
#     "IsSuccessful": true,
#     "ErrorCode": "",
#     "ErrorMessage": "",
#     "ClientErrorMessage": ""
# }

@dataclass
class GetSpeedTestCard(CardDetailsResponse, BaseClientResponse):
        pass  # No additional content
