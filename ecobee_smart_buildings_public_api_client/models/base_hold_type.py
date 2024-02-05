from enum import Enum


class BaseHoldType(str, Enum):
    INDEFINITE = "indefinite"
    NEXTTRANSITION = "nextTransition"

    def __str__(self) -> str:
        return str(self.value)
