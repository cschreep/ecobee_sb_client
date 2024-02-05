from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hold import Hold


T = TypeVar("T", bound="ThermostatEventsData")


@attr.s(auto_attribs=True)
class ThermostatEventsData:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier for a thermostat. The ID will match the serial number on the
            physical thermostat.
        current_event (Union[Unset, Hold]):
        holds (Union[Unset, List['Hold']]):
    """

    id: Union[Unset, str] = UNSET
    current_event: Union[Unset, "Hold"] = UNSET
    holds: Union[Unset, List["Hold"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        current_event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_event, Unset):
            current_event = self.current_event.to_dict()

        holds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.holds, Unset):
            holds = []
            for holds_item_data in self.holds:
                holds_item = holds_item_data.to_dict()

                holds.append(holds_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if current_event is not UNSET:
            field_dict["currentEvent"] = current_event
        if holds is not UNSET:
            field_dict["holds"] = holds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hold import Hold

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _current_event = d.pop("currentEvent", UNSET)
        current_event: Union[Unset, Hold]
        if isinstance(_current_event, Unset):
            current_event = UNSET
        else:
            current_event = Hold.from_dict(_current_event)

        holds = []
        _holds = d.pop("holds", UNSET)
        for holds_item_data in _holds or []:
            holds_item = Hold.from_dict(holds_item_data)

            holds.append(holds_item)

        thermostat_events_data = cls(
            id=id,
            current_event=current_event,
            holds=holds,
        )

        thermostat_events_data.additional_properties = d
        return thermostat_events_data

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
