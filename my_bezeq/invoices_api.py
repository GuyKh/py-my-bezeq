
from uuid import UUID

from my_bezeq.api_state import ApiState
from my_bezeq.commons import send_get_request, send_post_json_request
from my_bezeq.const import (
    ELECTRIC_INVOICES_URL,
    GET_INVOICES_EXCEL_URL,
    GET_INVOICES_PDF_URL,
    INVOICES_URL,
)
from my_bezeq.models.electric_invoice import GetElectricInvoiceTabResponse
from my_bezeq.models.invoice import GetInvoicesTabResponse


class InvoicesApi:
    def __init__(self, state: ApiState):
        self._state = state

    async def get_invoice_tab(self):
        self._state.require_dashboard_first()

        return GetInvoicesTabResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, INVOICES_URL, use_auth=True)
        )


    async def get_electric_invoice_tab(self):
        self._state.require_dashboard_first()

        return GetElectricInvoiceTabResponse.from_dict(
            await send_post_json_request(self._state.session, self._state.jwt_token, ELECTRIC_INVOICES_URL,
                                         use_auth=True)
        )


    async def get_invoice_pdf(self, invoice_id: UUID | str) -> bytes:
        """Get Invoice PDF response from My Bezeq API."""
        invoice_id = UUID(invoice_id)

        self._state.require_dashboard_first()
        response = await send_get_request(
            self._state.session, GET_INVOICES_PDF_URL.format(invoice_id=invoice_id,
                                                                  jwt_token=self._state.jwt_token)
        )
        return await response.read()

    async def get_invoice_xls(self, invoice_id: UUID | str) -> bytes:
        """Get Invoice Excel Spreadsheet(XLS) response from My Bezeq API."""
        invoice_id = UUID(invoice_id)

        self._state.require_dashboard_first()
        response = await send_get_request(
            self._state.session, GET_INVOICES_EXCEL_URL.format(invoice_id=invoice_id,
                                                                  jwt_token=self._state.jwt_token)
        )
        return await response.read()
