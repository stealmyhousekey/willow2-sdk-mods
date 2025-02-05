from __future__ import annotations
from typing import TYPE_CHECKING
from unrealsdk import find_all, find_object
from mods_base import get_pc, options
from nocap.mod.functions import log
from nocap.mod.variables import global_vars as sv

if TYPE_CHECKING:
    from common import WillowVehicle 


def set_vehicle_qol(_option: options.BoolOption | None, value: bool) -> None:
    if(_option == None or _option.mod.is_enabled):
        if value:
            sv.EnableVehicleTweaks = value


def set_vehicle_fix(_option: options.BoolOption | None, value: bool) -> None:
    if(_option == None or _option.mod.is_enabled):
        if value:
            sv.EnableVehicleFixes = value


def set_vehicle_scaling(_option: options.SliderOption | None, value: int) -> None:
    if(_option == None or _option.mod.is_enabled):
        if value:
            sv.VehicleScaling = value


#? will fail to display options if a vehicle already exists with a player in it
def apply_vehicle_qol(value: bool):
    set_all_vss_defs()
    set_all_vssui_tags()
    set_all_vehicle_family_tags()
    set_chassis_tweaks()
    sv.VehicleTweaksApplied = True
    log("Vehicle tweaks applied")


def set_vehicle_hp(_veh: WillowVehicle):
    try:
        pc = get_pc()
        veh_class = _veh.Class.Name
        tmp_hp = pc.Pawn.GetMaxHealth()
        if pc.Pawn.Class.Name == "WillowPlayerPawn": # only scale against player health, not other vehicle health
            tmp_hp = tmp_hp * sv.VehicleScaling
        
        #? maybe just do this on _veh instead of doing a find_object()
        if veh_class == "WillowVehicle_FlyingVehicle":
            flying_hp = find_object("AttributeInitializationDefinition", "GD_Balance_HealthAndDamage.HealthAndDamage.Init_VehicleHealth")
            flying_hp.RangeRestriction.MinValue.BaseValueConstant = tmp_hp
        
        elif veh_class == "WillowVehicle_WheeledVehicle":
            wheeled_hp = find_object("AttributeInitializationDefinition", "GD_PlayerVehicleShared.HealthMultipliers.Init_PlayerVehicleHealth")
            wheeled_hp.RangeRestriction.MinValue.BaseValueConstant = tmp_hp

        log(f"Minimum health adjusted for {veh_class}: {tmp_hp}")
    except Exception as e:
        s = str(e)
        if s == "'NoneType' object has no attribute 'Class'":
            log("Vehicle failed to spawn, cannot adjust health")
        else:
            log(f"Failed to adjust vehicle health: {e}")


def set_chassis_tweaks():
    tmp_chassis = find_all("ChassisDefinition")
    for chassis in tmp_chassis:
        chassis.AllowPawnsToStandOnTopOfVehicle = True


def set_all_vss_defs():
    tmp_vss = find_all("VehicleSpawnStationGFxDefinition")
    for vss in tmp_vss: # if vss.name != "Default__VehicleSpawnStationGFxDefinition":
        vss.RequiredTags = [20]
        vss.SupportedTags = [0, 4]


def set_all_vssui_tags():
    tmp_vssui = find_all("VSSUIDefinition")
    for vssui in tmp_vssui: # if vssui.name != "Default__VSSUIDefinition":
        vssui.RequiredTags = [0, 20]
        vssui.SupportedTags = [0, 1, 2]


def set_all_vehicle_family_tags():
    tmp_vehicle_family = find_all("VehicleFamilyDefinition")
    for vehicle_family in tmp_vehicle_family: # if vehicle_family.name != "Default__VehicleFamilyDefinition":
        vehicle_family.RequiredTags = [0, 20]
        vehicle_family.SupportedTags = [0, 1, 2]
        vehicle_family.RequiredMissionCompletionToUnlock = None
        
        if vehicle_family.name == "VehicleFamily_Hovercraft":
            hc_swf = find_object("SwfMovie", "Orchid_UI_HUD_EchoPortraits.Echo-Queen") # hc_swf = None
            vehicle_family.VehiclePreviewClip=hc_swf
