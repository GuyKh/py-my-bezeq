from dataclasses import dataclass, field

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig

from .base import BaseAuthResponse


@dataclass
class UsernameLoginRequest(DataClassDictMixin):
    username: str = field(metadata=field_options(alias="UserName"))
    password: str = field(metadata=field_options(alias="Password"))
    identity_number: str = field(metadata=field_options(alias="IdentityNumber"))
    origin: str = field(metadata=field_options(alias="Origin"))

    class Config(BaseConfig):
        serialize_by_alias = True


@dataclass
class UsernameLoginResponse(BaseAuthResponse):
    have_to_change_password: bool = field(metadata=field_options(alias="Have2ChangePassword"))
