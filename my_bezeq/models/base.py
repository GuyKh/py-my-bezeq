from dataclasses import dataclass, field
from typing import Optional

from mashumaro import DataClassDictMixin, field_options


@dataclass
class BaseResponse(DataClassDictMixin):
    is_successful: bool = field(metadata=field_options(alias="IsSuccessful"))
    error_code: str = field(metadata=field_options(alias="ErrorCode"))
    error_message: str = field(metadata=field_options(alias="ErrorMessage"))
    client_error_message: str = field(metadata=field_options(alias="ClientErrorMessage"))


@dataclass
class BaseAuthResponse(BaseResponse):
    jwt_token: Optional[str] = field(metadata=field_options(alias="JWTToken"))
