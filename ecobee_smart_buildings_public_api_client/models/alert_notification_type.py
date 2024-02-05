from enum import Enum


class AlertNotificationType(str, Enum):
    ALERT = "alert"
    HVAC = "hvac"
    FURNACEFILTER = "furnaceFilter"
    HUMIDIFIERFILTER = "humidifierFilter"
    DEHUMIDIFIERFILTER = "dehumidifierFilter"
    VENTILATOR = "ventilator"
    AC = "ac"
    AIRFILTER = "airFilter"
    AIRCLEANER = "airCleaner"
    UVLAMP = "uvLamp"
    TEMP = "temp"
    LOWTEMP = "lowTemp"
    HIGHTEMP = "highTemp"
    LOWHUMIDITY = "lowHumidity"
    HIGHHUMIDITY = "highHumidity"
    AUXHEAT = "auxHeat"
    AUXOUTDOOR = "auxOutdoor"

    def __str__(self) -> str:
        return str(self.value)
