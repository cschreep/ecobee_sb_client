from enum import Enum


class AuthRequestBodyGrantType(str, Enum):
    CLIENT_CREDENTIALS = "client_credentials"

    def __str__(self) -> str:
        return str(self.value)
