from enum import Enum


class AuthRequestBodyAudience(str, Enum):
    HTTPSAPI_SB_ECOBEE_COM = "https://api.sb.ecobee.com"

    def __str__(self) -> str:
        return str(self.value)
