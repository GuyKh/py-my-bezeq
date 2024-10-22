import logging
from typing import Optional

import aiohttp
from aiohttp import ClientSession

from my_bezeq.api_state import ApiState
from my_bezeq.dashboard_api import DashboardApi
from my_bezeq.electric_api import ElectricApi
from my_bezeq.generic_actions_api import GenericActionsApi
from my_bezeq.internet_api import InternetApi
from my_bezeq.invoices_api import InvoicesApi
from my_bezeq.personal_api import PersonalApi
from my_bezeq.phone_api import PhoneApi
from my_bezeq.tech_coord_api import TechCoordApi

from .auth_api import AuthApi

_LOGGER = logging.getLogger(__name__)

class MyBezeqAPI:
    def __init__(self, user_id, password, session: Optional[ClientSession] = None):
        self.user_id = user_id
        self.password = password

        if not session:
            session = aiohttp.ClientSession()

        self._state = ApiState(session)
        self.auth = AuthApi(self._state)
        self.dashboard = DashboardApi(self._state)
        self.personal = PersonalApi(self._state)
        self.internet = InternetApi(self._state)
        self.tech_coord = TechCoordApi(self._state)
        self.generic_actions = GenericActionsApi(self._state)

        self.phone = PhoneApi(self._state)
        self.electric = ElectricApi(self._state)
        self.invoices = InvoicesApi(self._state)

    async def login(self) -> str:
        await self.auth.login(self.user_id, self.password)

    def set_jwt(self, jwt_token: str) -> None:
        self._state.jwt_token = jwt_token
        self._state.is_dashboard_called = False


