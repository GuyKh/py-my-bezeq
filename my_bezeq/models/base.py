from dataclasses import dataclass, field
from typing import Optional

from mashumaro import DataClassDictMixin, field_options


@dataclass
class BaseResponse(DataClassDictMixin):
    is_successful: bool = field(metadata=field_options(alias="IsSuccessful"), repr=False)
    error_code: str = field(metadata=field_options(alias="ErrorCode"), repr=False)
    error_message: str = field(metadata=field_options(alias="ErrorMessage"), repr=False)

@dataclass
class BaseClientResponse(BaseResponse):
    client_error_message: str = field(metadata=field_options(alias="ClientErrorMessage"), repr=False)


@dataclass
class BaseAuthResponse(BaseClientResponse):
    jwt_token: Optional[str] = field(metadata=field_options(alias="JWTToken"), repr=False)
