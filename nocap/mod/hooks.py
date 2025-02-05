from __future__ import annotations
from typing import TYPE_CHECKING, Any
from mods_base.mod import Game
from unrealsdk import find_all
from unrealsdk.hooks import Type, Block, add_hook, remove_hook
from unrealsdk.unreal import BoundFunction
from nocap.mod import altfixes, functions, hotfixes, vehicles
from nocap.mod.functions import log
from nocap.mod.variables import global_vars as sv

if TYPE_CHECKING:
    from common import WillowGame, WorldInfo, VehicleSpawnStationPlatform #, WillowPlayerController, WillowCoopGameInfo


# @hook("Engine.WorldInfo:GetGameSequence", Type.POST)
def get_game_sequence(obj: WorldInfo,
                        _args: None,
                        _ret: Any,
                        _func: BoundFunction,
):
    if(sv.EnableVehicleTweaks):
        if(not sv.VehicleTweaksApplied):
            vehicles.apply_vehicle_qol(True)
    if(sv.EnableFixes == 1):
        if(not sv.HotfixesApplied):
            hotfixes.spark_hotfixes(1)
    elif(sv.EnableFixes == 2):
        if(not sv.HotfixesApplied):
            hotfixes.spark_hotfixes(0)
    if Game.get_current() == Game.TPS: 
        if(not sv.TPSMissionsFixed):
            functions.fix_tps_missions()
    pass


# @hook("WillowGame.WillowPlayerController:ServerInitClientFlags", Type.PRE)
def server_init_client_flags(obj: WillowGame.WillowPlayerController,
                             _args: None,
                             _ret: None,
                             _func: BoundFunction,
):
    if(functions.is_host()):
        if obj.PlayerNum == 0: #* only run on host load-in (try obj.RemoteRole if PlayerNum causes issues)
            if(sv.EnableFixes == 3):
                if(not sv.HotfixesApplied):
                    altfixes.manual_fixes()
        else: #* only run on client join
            log(f"Assigning team to client {obj.PlayerNum}")
            WillowCoopGameInfo = find_all("WillowCoopGameInfo")[-1]
            tmp_team = functions.find_best_team()
            WillowCoopGameInfo.ChangeTeam(obj, tmp_team, True)
            functions.log_teams()
    pass


# @hook("WillowGame.WillowCoopGameInfo:InitializeTeams", Type.PRE)
def initialize_teams(obj: WillowGame.WillowCoopGameInfo,
                     _args: None,
                     _ret: None,
                     _func: BoundFunction,
):
    obj.CreateTeam(0, "Players") #* create the original teams
    obj.CreateTeam(1, "AI")

    for i in range(2, sv.TeamCount): #* create x new teams, where x = TeamCount - 2
        obj.CreateTeam(i, f"Players{i}")
    log(f"Created {sv.TeamCount} teams")

    return Block() #! do not allow original method to run


# @hook("WillowGame.VehicleSpawnStationPlatform:TriggerKismetVehicleSpawnEvents", Type.PRE)
def trigger_kismet_vehicle_spawn_events(obj: WillowGame.VehicleSpawnStationPlatform,
                        _args: VehicleSpawnStationPlatform._TriggerKismetVehicleSpawnEvents.args,
                        _ret: None,
                        _func: BoundFunction,
):
    if functions.is_host():
        if sv.EnableVehicleFixes:
            vehicles.set_vehicle_hp(_args.SpawnedVehicle)
    pass


#* toggle hooks
def add_hooks() -> None:
    add_hook(
        "WillowGame.WillowCoopGameInfo:InitializeTeams",
        Type.PRE,
        "NoCap_InitializeTeams",
        initialize_teams,
    )
    add_hook(
        "WillowGame.WillowPlayerController:ServerInitClientFlags",
        Type.PRE,
        "NoCap_ServerInitClientFlags",
        server_init_client_flags,
    )
    add_hook(
        "Engine.WorldInfo:GetGameSequence",
        Type.POST,
        "NoCap_GetGameSequence",
        get_game_sequence,
    )
    add_hook(
        "WillowGame.VehicleSpawnStationPlatform:TriggerKismetVehicleSpawnEvents",
        Type.PRE,
        "NoCap_TriggerKismetVehicleSpawnEvents",
        trigger_kismet_vehicle_spawn_events,
    )


def remove_hooks() -> None:
    remove_hook(
        "WillowGame.WillowCoopGameInfo:InitializeTeams",
        Type.PRE,
        "NoCap_InitializeTeams",
    )
    remove_hook(
        "WillowGame.WillowPlayerController:ServerInitClientFlags",
        Type.PRE,
        "NoCap_ServerInitClientFlags",
    )
    remove_hook(
        "Engine.WorldInfo:GetGameSequence",
        Type.POST,
        "NoCap_GetGameSequence",
    )
    remove_hook(
        "WillowGame.VehicleSpawnStationPlatform:TriggerKismetVehicleSpawnEvents",
        Type.PRE,
        "NoCap_TriggerKismetVehicleSpawnEvents",
    )


#* enable/disable
def enable() -> None:
    add_hooks()

def disable() -> None:
    remove_hooks()
