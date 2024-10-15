class MyBezeqError(Exception):
    """Exception raised for errors in My Bezeq API."""

    def __init__(self, error):
        self.error = error
        super().__init__(self.error)


class MyBezeqUnauthorizedError(MyBezeqError):
    """Exception raised for unauthorized requests in My Bezeq API."""

    def __init__(self, error):
        super().__init__(error)


class MyBezeqVersionError(MyBezeqError):
    """Exception raised for version fetch errors in My Bezeq API."""

    def __init__(self, error):
        super().__init__(error)


class MyBezeqLoginError(MyBezeqError):
    """Exception raised for login errors in My Bezeq API."""

    def __init__(self, error):
        super().__init__(error)
