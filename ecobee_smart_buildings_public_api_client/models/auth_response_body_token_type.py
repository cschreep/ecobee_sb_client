from enum import Enum


class AuthResponseBodyTokenType(str, Enum):
    BEARER = "Bearer"

    def __str__(self) -> str:
        return str(self.value)
