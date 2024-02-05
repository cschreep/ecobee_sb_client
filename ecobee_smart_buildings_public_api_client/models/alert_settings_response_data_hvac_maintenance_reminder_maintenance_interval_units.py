from enum import Enum


class AlertSettingsResponseDataHvacMaintenanceReminderMaintenanceIntervalUnits(str, Enum):
    MONTH = "month"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
