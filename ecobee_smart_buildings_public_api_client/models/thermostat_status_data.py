from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.hvac_mode import HvacMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_point import SetPoint
    from ..models.thermostat_status_data_desired_cool_range import ThermostatStatusDataDesiredCoolRange
    from ..models.thermostat_status_data_desired_heat_range import ThermostatStatusDataDesiredHeatRange
    from ..models.thermostat_status_data_running_equipment import ThermostatStatusDataRunningEquipment


T = TypeVar("T", bound="ThermostatStatusData")


@attr.s(auto_attribs=True)
class ThermostatStatusData:
    """
    Attributes:
        comfort_setting (Union[Unset, str]):  Example: Home.
        desired_cool_range (Union[Unset, ThermostatStatusDataDesiredCoolRange]): The minimum and maximum values for a
            cool setPoint
        desired_dehumidity (Union[Unset, int]): The maximum humidity value to be maintained
        desired_heat_range (Union[Unset, ThermostatStatusDataDesiredHeatRange]): The minimum and maximum values for a
            heat setPoint
        desired_humidity (Union[Unset, int]): The minimum humidity value to be maintained
        heat_cool_min_delta (Union[Unset, int]): The minimum difference between setPoints
        humidity (Union[Unset, int]):
        hvac_mode (Union[Unset, HvacMode]): The HVAC mode on a thermostat. Possible values: auto, auxHeatOnly, cool,
            heat, off.
        id (Union[Unset, str]): The unique identifier for a thermostat. The ID will match the serial number on the
            physical thermostat.
        is_connected (Union[Unset, bool]):
        is_tenant_mode (Union[Unset, bool]): Indicates whether the thermostat is currently in tenant mode
        running_equipment (Union[Unset, ThermostatStatusDataRunningEquipment]): A record of running equipment indicated
            by a boolean flag
        set_point (Union[Unset, SetPoint]):
        temperature (Union[Unset, float]):
    """

    comfort_setting: Union[Unset, str] = UNSET
    desired_cool_range: Union[Unset, "ThermostatStatusDataDesiredCoolRange"] = UNSET
    desired_dehumidity: Union[Unset, int] = UNSET
    desired_heat_range: Union[Unset, "ThermostatStatusDataDesiredHeatRange"] = UNSET
    desired_humidity: Union[Unset, int] = UNSET
    heat_cool_min_delta: Union[Unset, int] = UNSET
    humidity: Union[Unset, int] = UNSET
    hvac_mode: Union[Unset, HvacMode] = UNSET
    id: Union[Unset, str] = UNSET
    is_connected: Union[Unset, bool] = UNSET
    is_tenant_mode: Union[Unset, bool] = UNSET
    running_equipment: Union[Unset, "ThermostatStatusDataRunningEquipment"] = UNSET
    set_point: Union[Unset, "SetPoint"] = UNSET
    temperature: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comfort_setting = self.comfort_setting
        desired_cool_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.desired_cool_range, Unset):
            desired_cool_range = self.desired_cool_range.to_dict()

        desired_dehumidity = self.desired_dehumidity
        desired_heat_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.desired_heat_range, Unset):
            desired_heat_range = self.desired_heat_range.to_dict()

        desired_humidity = self.desired_humidity
        heat_cool_min_delta = self.heat_cool_min_delta
        humidity = self.humidity
        hvac_mode: Union[Unset, str] = UNSET
        if not isinstance(self.hvac_mode, Unset):
            hvac_mode = self.hvac_mode.value

        id = self.id
        is_connected = self.is_connected
        is_tenant_mode = self.is_tenant_mode
        running_equipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.running_equipment, Unset):
            running_equipment = self.running_equipment.to_dict()

        set_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.set_point, Unset):
            set_point = self.set_point.to_dict()

        temperature = self.temperature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comfort_setting is not UNSET:
            field_dict["comfortSetting"] = comfort_setting
        if desired_cool_range is not UNSET:
            field_dict["desiredCoolRange"] = desired_cool_range
        if desired_dehumidity is not UNSET:
            field_dict["desiredDehumidity"] = desired_dehumidity
        if desired_heat_range is not UNSET:
            field_dict["desiredHeatRange"] = desired_heat_range
        if desired_humidity is not UNSET:
            field_dict["desiredHumidity"] = desired_humidity
        if heat_cool_min_delta is not UNSET:
            field_dict["heatCoolMinDelta"] = heat_cool_min_delta
        if humidity is not UNSET:
            field_dict["humidity"] = humidity
        if hvac_mode is not UNSET:
            field_dict["hvacMode"] = hvac_mode
        if id is not UNSET:
            field_dict["id"] = id
        if is_connected is not UNSET:
            field_dict["isConnected"] = is_connected
        if is_tenant_mode is not UNSET:
            field_dict["isTenantMode"] = is_tenant_mode
        if running_equipment is not UNSET:
            field_dict["runningEquipment"] = running_equipment
        if set_point is not UNSET:
            field_dict["setPoint"] = set_point
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.set_point import SetPoint
        from ..models.thermostat_status_data_desired_cool_range import ThermostatStatusDataDesiredCoolRange
        from ..models.thermostat_status_data_desired_heat_range import ThermostatStatusDataDesiredHeatRange
        from ..models.thermostat_status_data_running_equipment import ThermostatStatusDataRunningEquipment

        d = src_dict.copy()
        comfort_setting = d.pop("comfortSetting", UNSET)

        _desired_cool_range = d.pop("desiredCoolRange", UNSET)
        desired_cool_range: Union[Unset, ThermostatStatusDataDesiredCoolRange]
        if isinstance(_desired_cool_range, Unset):
            desired_cool_range = UNSET
        else:
            desired_cool_range = ThermostatStatusDataDesiredCoolRange.from_dict(_desired_cool_range)

        desired_dehumidity = d.pop("desiredDehumidity", UNSET)

        _desired_heat_range = d.pop("desiredHeatRange", UNSET)
        desired_heat_range: Union[Unset, ThermostatStatusDataDesiredHeatRange]
        if isinstance(_desired_heat_range, Unset):
            desired_heat_range = UNSET
        else:
            desired_heat_range = ThermostatStatusDataDesiredHeatRange.from_dict(_desired_heat_range)

        desired_humidity = d.pop("desiredHumidity", UNSET)

        heat_cool_min_delta = d.pop("heatCoolMinDelta", UNSET)

        humidity = d.pop("humidity", UNSET)

        _hvac_mode = d.pop("hvacMode", UNSET)
        hvac_mode: Union[Unset, HvacMode]
        if isinstance(_hvac_mode, Unset):
            hvac_mode = UNSET
        else:
            hvac_mode = HvacMode(_hvac_mode)

        id = d.pop("id", UNSET)

        is_connected = d.pop("isConnected", UNSET)

        is_tenant_mode = d.pop("isTenantMode", UNSET)

        _running_equipment = d.pop("runningEquipment", UNSET)
        running_equipment: Union[Unset, ThermostatStatusDataRunningEquipment]
        if isinstance(_running_equipment, Unset):
            running_equipment = UNSET
        else:
            running_equipment = ThermostatStatusDataRunningEquipment.from_dict(_running_equipment)

        _set_point = d.pop("setPoint", UNSET)
        set_point: Union[Unset, SetPoint]
        if isinstance(_set_point, Unset):
            set_point = UNSET
        else:
            set_point = SetPoint.from_dict(_set_point)

        temperature = d.pop("temperature", UNSET)

        thermostat_status_data = cls(
            comfort_setting=comfort_setting,
            desired_cool_range=desired_cool_range,
            desired_dehumidity=desired_dehumidity,
            desired_heat_range=desired_heat_range,
            desired_humidity=desired_humidity,
            heat_cool_min_delta=heat_cool_min_delta,
            humidity=humidity,
            hvac_mode=hvac_mode,
            id=id,
            is_connected=is_connected,
            is_tenant_mode=is_tenant_mode,
            running_equipment=running_equipment,
            set_point=set_point,
            temperature=temperature,
        )

        thermostat_status_data.additional_properties = d
        return thermostat_status_data

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
