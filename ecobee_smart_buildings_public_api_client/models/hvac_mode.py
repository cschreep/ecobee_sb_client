from enum import Enum


class HvacMode(str, Enum):
    HEAT = "heat"
    COOL = "cool"
    AUTO = "auto"
    OFF = "off"
    AUXHEATONLY = "auxHeatOnly"

    def __str__(self) -> str:
        return str(self.value)
