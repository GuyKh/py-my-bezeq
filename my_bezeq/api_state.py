from aiohttp import ClientSession

from my_bezeq.exceptions import MyBezeqError


class ApiState:
    def __init__(self, session: ClientSession):
        self.is_dashboard_called = False
        self.session = session

        self.jwt_token = None
        self.subscriber_number = None
        self.is_dashboard_called = False

    def require_dashboard_first(self):
        if not self.is_dashboard_called:
            raise MyBezeqError("get_dashboard_tab() should be called before calling this method," +\
                            "Otherwise you may get empty data")
