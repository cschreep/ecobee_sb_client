from enum import IntEnum


class BuildingSize(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_5000 = 5000
    VALUE_10000 = 10000
    VALUE_20000 = 20000

    def __str__(self) -> str:
        return str(self.value)
