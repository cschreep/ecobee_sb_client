from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_settings_request_body_high_humidity_alert import AlertSettingsRequestBodyHighHumidityAlert
    from ..models.alert_settings_request_body_high_temperature_alert import AlertSettingsRequestBodyHighTemperatureAlert
    from ..models.alert_settings_request_body_low_humidity_alert import AlertSettingsRequestBodyLowHumidityAlert
    from ..models.alert_settings_request_body_low_temperature_alert import AlertSettingsRequestBodyLowTemperatureAlert
    from ..models.reminder_schema import ReminderSchema


T = TypeVar("T", bound="AlertSettingsRequestBody")


@attr.s(auto_attribs=True)
class AlertSettingsRequestBody:
    """
    Attributes:
        low_temperature_alert (Union[Unset, AlertSettingsRequestBodyLowTemperatureAlert]): High and low temperature
            alert values must be separated by the heatCoolMinDelta found in the thermostat status
        high_temperature_alert (Union[Unset, AlertSettingsRequestBodyHighTemperatureAlert]): High and low temperature
            alert values must be separated by the heatCoolMinDelta found in the thermostat status
        low_humidity_alert (Union[Unset, AlertSettingsRequestBodyLowHumidityAlert]): High and low humidity alert values
            must be separated by 5%
        high_humidity_alert (Union[Unset, AlertSettingsRequestBodyHighHumidityAlert]): High and low humidity alert
            values must be separated by 5%
        ac_maintenance_reminder (Union[Unset, ReminderSchema]):
        hvac_maintenance_reminder (Union[Unset, ReminderSchema]):
    """

    low_temperature_alert: Union[Unset, "AlertSettingsRequestBodyLowTemperatureAlert"] = UNSET
    high_temperature_alert: Union[Unset, "AlertSettingsRequestBodyHighTemperatureAlert"] = UNSET
    low_humidity_alert: Union[Unset, "AlertSettingsRequestBodyLowHumidityAlert"] = UNSET
    high_humidity_alert: Union[Unset, "AlertSettingsRequestBodyHighHumidityAlert"] = UNSET
    ac_maintenance_reminder: Union[Unset, "ReminderSchema"] = UNSET
    hvac_maintenance_reminder: Union[Unset, "ReminderSchema"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        low_temperature_alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.low_temperature_alert, Unset):
            low_temperature_alert = self.low_temperature_alert.to_dict()

        high_temperature_alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.high_temperature_alert, Unset):
            high_temperature_alert = self.high_temperature_alert.to_dict()

        low_humidity_alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.low_humidity_alert, Unset):
            low_humidity_alert = self.low_humidity_alert.to_dict()

        high_humidity_alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.high_humidity_alert, Unset):
            high_humidity_alert = self.high_humidity_alert.to_dict()

        ac_maintenance_reminder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ac_maintenance_reminder, Unset):
            ac_maintenance_reminder = self.ac_maintenance_reminder.to_dict()

        hvac_maintenance_reminder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hvac_maintenance_reminder, Unset):
            hvac_maintenance_reminder = self.hvac_maintenance_reminder.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if low_temperature_alert is not UNSET:
            field_dict["lowTemperatureAlert"] = low_temperature_alert
        if high_temperature_alert is not UNSET:
            field_dict["highTemperatureAlert"] = high_temperature_alert
        if low_humidity_alert is not UNSET:
            field_dict["lowHumidityAlert"] = low_humidity_alert
        if high_humidity_alert is not UNSET:
            field_dict["highHumidityAlert"] = high_humidity_alert
        if ac_maintenance_reminder is not UNSET:
            field_dict["acMaintenanceReminder"] = ac_maintenance_reminder
        if hvac_maintenance_reminder is not UNSET:
            field_dict["hvacMaintenanceReminder"] = hvac_maintenance_reminder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_settings_request_body_high_humidity_alert import AlertSettingsRequestBodyHighHumidityAlert
        from ..models.alert_settings_request_body_high_temperature_alert import (
            AlertSettingsRequestBodyHighTemperatureAlert,
        )
        from ..models.alert_settings_request_body_low_humidity_alert import AlertSettingsRequestBodyLowHumidityAlert
        from ..models.alert_settings_request_body_low_temperature_alert import (
            AlertSettingsRequestBodyLowTemperatureAlert,
        )
        from ..models.reminder_schema import ReminderSchema

        d = src_dict.copy()
        _low_temperature_alert = d.pop("lowTemperatureAlert", UNSET)
        low_temperature_alert: Union[Unset, AlertSettingsRequestBodyLowTemperatureAlert]
        if isinstance(_low_temperature_alert, Unset):
            low_temperature_alert = UNSET
        else:
            low_temperature_alert = AlertSettingsRequestBodyLowTemperatureAlert.from_dict(_low_temperature_alert)

        _high_temperature_alert = d.pop("highTemperatureAlert", UNSET)
        high_temperature_alert: Union[Unset, AlertSettingsRequestBodyHighTemperatureAlert]
        if isinstance(_high_temperature_alert, Unset):
            high_temperature_alert = UNSET
        else:
            high_temperature_alert = AlertSettingsRequestBodyHighTemperatureAlert.from_dict(_high_temperature_alert)

        _low_humidity_alert = d.pop("lowHumidityAlert", UNSET)
        low_humidity_alert: Union[Unset, AlertSettingsRequestBodyLowHumidityAlert]
        if isinstance(_low_humidity_alert, Unset):
            low_humidity_alert = UNSET
        else:
            low_humidity_alert = AlertSettingsRequestBodyLowHumidityAlert.from_dict(_low_humidity_alert)

        _high_humidity_alert = d.pop("highHumidityAlert", UNSET)
        high_humidity_alert: Union[Unset, AlertSettingsRequestBodyHighHumidityAlert]
        if isinstance(_high_humidity_alert, Unset):
            high_humidity_alert = UNSET
        else:
            high_humidity_alert = AlertSettingsRequestBodyHighHumidityAlert.from_dict(_high_humidity_alert)

        _ac_maintenance_reminder = d.pop("acMaintenanceReminder", UNSET)
        ac_maintenance_reminder: Union[Unset, ReminderSchema]
        if isinstance(_ac_maintenance_reminder, Unset):
            ac_maintenance_reminder = UNSET
        else:
            ac_maintenance_reminder = ReminderSchema.from_dict(_ac_maintenance_reminder)

        _hvac_maintenance_reminder = d.pop("hvacMaintenanceReminder", UNSET)
        hvac_maintenance_reminder: Union[Unset, ReminderSchema]
        if isinstance(_hvac_maintenance_reminder, Unset):
            hvac_maintenance_reminder = UNSET
        else:
            hvac_maintenance_reminder = ReminderSchema.from_dict(_hvac_maintenance_reminder)

        alert_settings_request_body = cls(
            low_temperature_alert=low_temperature_alert,
            high_temperature_alert=high_temperature_alert,
            low_humidity_alert=low_humidity_alert,
            high_humidity_alert=high_humidity_alert,
            ac_maintenance_reminder=ac_maintenance_reminder,
            hvac_maintenance_reminder=hvac_maintenance_reminder,
        )

        alert_settings_request_body.additional_properties = d
        return alert_settings_request_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
