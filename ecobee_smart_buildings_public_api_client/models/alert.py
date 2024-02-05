import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert_alert_type import AlertAlertType
from ..models.alert_notification_type import AlertNotificationType
from ..models.alert_severity import AlertSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="Alert")


@attr.s(auto_attribs=True)
class Alert:
    """
    Attributes:
        acknowledge_ref (Union[Unset, str]): The unique alert identifier, required to acknowledge an alert
        alert_number (Union[Unset, int]): The ecobee alert message identifier
        alert_type (Union[Unset, AlertAlertType]): The type of alert this is: alert, demandResponse, emergency, message,
            pricing
        notification_type (Union[Unset, AlertNotificationType]): The type of alert or reminder: alert, hvac,
            furnaceFilter, humidifierFilter, dehumidifierFilter, ventilator, ac, airFilter, airCleaner, uvLamp, temp,
            lowTemp, highTemp, lowHumidity, highHumidity, auxHeat, auxOutdoor
        reminder (Union[Unset, datetime.date]): Reminder date
        severity (Union[Unset, AlertSeverity]): The alert severity: low, medium, high
        text (Union[Unset, str]): The alert message text, truncated to 500 characters
        time (Union[Unset, datetime.datetime]): The alert time and date
    """

    acknowledge_ref: Union[Unset, str] = UNSET
    alert_number: Union[Unset, int] = UNSET
    alert_type: Union[Unset, AlertAlertType] = UNSET
    notification_type: Union[Unset, AlertNotificationType] = UNSET
    reminder: Union[Unset, datetime.date] = UNSET
    severity: Union[Unset, AlertSeverity] = UNSET
    text: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acknowledge_ref = self.acknowledge_ref
        alert_number = self.alert_number
        alert_type: Union[Unset, str] = UNSET
        if not isinstance(self.alert_type, Unset):
            alert_type = self.alert_type.value

        notification_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value

        reminder: Union[Unset, str] = UNSET
        if not isinstance(self.reminder, Unset):
            reminder = self.reminder.isoformat()

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        text = self.text
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledge_ref is not UNSET:
            field_dict["acknowledgeRef"] = acknowledge_ref
        if alert_number is not UNSET:
            field_dict["alertNumber"] = alert_number
        if alert_type is not UNSET:
            field_dict["alertType"] = alert_type
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if reminder is not UNSET:
            field_dict["reminder"] = reminder
        if severity is not UNSET:
            field_dict["severity"] = severity
        if text is not UNSET:
            field_dict["text"] = text
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acknowledge_ref = d.pop("acknowledgeRef", UNSET)

        alert_number = d.pop("alertNumber", UNSET)

        _alert_type = d.pop("alertType", UNSET)
        alert_type: Union[Unset, AlertAlertType]
        if isinstance(_alert_type, Unset):
            alert_type = UNSET
        else:
            alert_type = AlertAlertType(_alert_type)

        _notification_type = d.pop("notificationType", UNSET)
        notification_type: Union[Unset, AlertNotificationType]
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = AlertNotificationType(_notification_type)

        _reminder = d.pop("reminder", UNSET)
        reminder: Union[Unset, datetime.date]
        if isinstance(_reminder, Unset):
            reminder = UNSET
        else:
            reminder = isoparse(_reminder).date()

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, AlertSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = AlertSeverity(_severity)

        text = d.pop("text", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        alert = cls(
            acknowledge_ref=acknowledge_ref,
            alert_number=alert_number,
            alert_type=alert_type,
            notification_type=notification_type,
            reminder=reminder,
            severity=severity,
            text=text,
            time=time,
        )

        alert.additional_properties = d
        return alert

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
