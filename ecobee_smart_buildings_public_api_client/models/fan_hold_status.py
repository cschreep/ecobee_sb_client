from enum import Enum


class FanHoldStatus(str, Enum):
    ON = "on"
    AUTO = "auto"

    def __str__(self) -> str:
        return str(self.value)
