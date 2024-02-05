from enum import Enum


class BaseFailResponseStatus(str, Enum):
    FAIL = "fail"

    def __str__(self) -> str:
        return str(self.value)
