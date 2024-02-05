from enum import Enum


class AlertAlertType(str, Enum):
    ALERT = "alert"
    DEMANDRESPONSE = "demandResponse"
    EMERGENCY = "emergency"
    MESSAGE = "message"
    PRICING = "pricing"

    def __str__(self) -> str:
        return str(self.value)
