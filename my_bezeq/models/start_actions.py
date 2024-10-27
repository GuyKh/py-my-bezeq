from dataclasses import dataclass, field

from mashumaro import DataClassDictMixin, field_options

from my_bezeq.models.base import BaseClientResponse

# POST https://my-api.bezeq.co.il/{version}/api/GeneralActions/GetStartActions
#
# {
#     "StartActions":[
#        {
#           "Id":1,
#           "actionName":"payBill",
#           "actionNameToDisplay":"תשלום חשבונית",
#           "actionURL":"https://bpay.bezeq.co.il/identification",
#           "Order":1
#        },
#        {
#           "Id":2,
#           "actionName":"joinHok",
#           "actionNameToDisplay":"הצטרפות להוראת קבע",
#           "actionURL":"https://bmy.bezeq.co.il/actions/hok?internal_source=myb_start&WT.isp=myb_invoice",
#           "Order":2
#        },
#        {
#           "Id":3,
#           "actionName":"joinMailInvoice",
#           "actionNameToDisplay":"הצטרפות לחשבונית דיגיטלית",
#           "actionURL":"https://bmail.bezeq.co.il/",
#           "Order":3
#        }
#     ],
#     "IsSuccessful":true,
#     "ErrorCode":"",
#     "ErrorMessage":"",
#     "ClientErrorMessage":""
#  }


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
