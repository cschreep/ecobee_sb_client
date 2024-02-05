from enum import Enum


class ThermostatWeatherForecastStatus(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
