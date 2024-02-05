from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThermostatStatusDataRunningEquipment")


@attr.s(auto_attribs=True)
class ThermostatStatusDataRunningEquipment:
    """A record of running equipment indicated by a boolean flag

    Attributes:
        fan (Union[Unset, bool]):
        comp_cool_1 (Union[Unset, bool]):
        comp_cool_2 (Union[Unset, bool]):
        heat_pump (Union[Unset, bool]):
        heat_pump_2 (Union[Unset, bool]):
        heat_pump_3 (Union[Unset, bool]):
        aux_heat_1 (Union[Unset, bool]):
        aux_heat_2 (Union[Unset, bool]):
        aux_heat_3 (Union[Unset, bool]):
        comp_hot_water (Union[Unset, bool]):
        aux_hot_water (Union[Unset, bool]):
        humidifier (Union[Unset, bool]):
        dehumidifier (Union[Unset, bool]):
        ventilator (Union[Unset, bool]):
        economizer (Union[Unset, bool]):
    """

    fan: Union[Unset, bool] = UNSET
    comp_cool_1: Union[Unset, bool] = UNSET
    comp_cool_2: Union[Unset, bool] = UNSET
    heat_pump: Union[Unset, bool] = UNSET
    heat_pump_2: Union[Unset, bool] = UNSET
    heat_pump_3: Union[Unset, bool] = UNSET
    aux_heat_1: Union[Unset, bool] = UNSET
    aux_heat_2: Union[Unset, bool] = UNSET
    aux_heat_3: Union[Unset, bool] = UNSET
    comp_hot_water: Union[Unset, bool] = UNSET
    aux_hot_water: Union[Unset, bool] = UNSET
    humidifier: Union[Unset, bool] = UNSET
    dehumidifier: Union[Unset, bool] = UNSET
    ventilator: Union[Unset, bool] = UNSET
    economizer: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fan = self.fan
        comp_cool_1 = self.comp_cool_1
        comp_cool_2 = self.comp_cool_2
        heat_pump = self.heat_pump
        heat_pump_2 = self.heat_pump_2
        heat_pump_3 = self.heat_pump_3
        aux_heat_1 = self.aux_heat_1
        aux_heat_2 = self.aux_heat_2
        aux_heat_3 = self.aux_heat_3
        comp_hot_water = self.comp_hot_water
        aux_hot_water = self.aux_hot_water
        humidifier = self.humidifier
        dehumidifier = self.dehumidifier
        ventilator = self.ventilator
        economizer = self.economizer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fan is not UNSET:
            field_dict["fan"] = fan
        if comp_cool_1 is not UNSET:
            field_dict["compCool1"] = comp_cool_1
        if comp_cool_2 is not UNSET:
            field_dict["compCool2"] = comp_cool_2
        if heat_pump is not UNSET:
            field_dict["heatPump"] = heat_pump
        if heat_pump_2 is not UNSET:
            field_dict["heatPump2"] = heat_pump_2
        if heat_pump_3 is not UNSET:
            field_dict["heatPump3"] = heat_pump_3
        if aux_heat_1 is not UNSET:
            field_dict["auxHeat1"] = aux_heat_1
        if aux_heat_2 is not UNSET:
            field_dict["auxHeat2"] = aux_heat_2
        if aux_heat_3 is not UNSET:
            field_dict["auxHeat3"] = aux_heat_3
        if comp_hot_water is not UNSET:
            field_dict["compHotWater"] = comp_hot_water
        if aux_hot_water is not UNSET:
            field_dict["auxHotWater"] = aux_hot_water
        if humidifier is not UNSET:
            field_dict["humidifier"] = humidifier
        if dehumidifier is not UNSET:
            field_dict["dehumidifier"] = dehumidifier
        if ventilator is not UNSET:
            field_dict["ventilator"] = ventilator
        if economizer is not UNSET:
            field_dict["economizer"] = economizer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fan = d.pop("fan", UNSET)

        comp_cool_1 = d.pop("compCool1", UNSET)

        comp_cool_2 = d.pop("compCool2", UNSET)

        heat_pump = d.pop("heatPump", UNSET)

        heat_pump_2 = d.pop("heatPump2", UNSET)

        heat_pump_3 = d.pop("heatPump3", UNSET)

        aux_heat_1 = d.pop("auxHeat1", UNSET)

        aux_heat_2 = d.pop("auxHeat2", UNSET)

        aux_heat_3 = d.pop("auxHeat3", UNSET)

        comp_hot_water = d.pop("compHotWater", UNSET)

        aux_hot_water = d.pop("auxHotWater", UNSET)

        humidifier = d.pop("humidifier", UNSET)

        dehumidifier = d.pop("dehumidifier", UNSET)

        ventilator = d.pop("ventilator", UNSET)

        economizer = d.pop("economizer", UNSET)

        thermostat_status_data_running_equipment = cls(
            fan=fan,
            comp_cool_1=comp_cool_1,
            comp_cool_2=comp_cool_2,
            heat_pump=heat_pump,
            heat_pump_2=heat_pump_2,
            heat_pump_3=heat_pump_3,
            aux_heat_1=aux_heat_1,
            aux_heat_2=aux_heat_2,
            aux_heat_3=aux_heat_3,
            comp_hot_water=comp_hot_water,
            aux_hot_water=aux_hot_water,
            humidifier=humidifier,
            dehumidifier=dehumidifier,
            ventilator=ventilator,
            economizer=economizer,
        )

        thermostat_status_data_running_equipment.additional_properties = d
        return thermostat_status_data_running_equipment

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
