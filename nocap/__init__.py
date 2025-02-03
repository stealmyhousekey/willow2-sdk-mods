# This project is licensed under the GNU General Public License v3.0.

# NoCap - Copyright (c) 2024-2025 stealmyhousekey
# CoopPatch - Copyright (c) 2018 RobethX / RobChiocchio

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from __future__ import annotations
from mods_base import options, keybind
from mods_base.mod import CoopSupport, Game
from mods_base.mod_factory import build_mod
from nocap import altfixes, hooks, functions, hotfixes, network, vehicles
from nocap.functions import log
from nocap.variables import global_vars as sv


#* mod toggles
def on_enable() -> None:
    log("Enabled", True)
    hooks.enable()
    functions.set_logging(None, MISC_OPTIONS.children[0].value)
    functions.set_lobby_size(None, UNCAP_OPTION.value)
    functions.set_enemy_scaling(None, SCALING_OPTION.value)
    network.set_net_vars(None, NETWORK_OPTION.value)
    hotfixes.set_hotfix(None, FIX_OPTION.value)
    vehicles.set_vehicle_qol(None, VEHICLE_OPTIONS.children[0].value)
    vehicles.set_vehicle_fix(None, VEHICLE_OPTIONS.children[1].value)
    vehicles.set_vehicle_scaling(None, VEHICLE_OPTIONS.children[2].value)
    pass

def on_disable() -> None:
    hooks.disable()
    log("Disabled  [WARNING: Some settings may persist until game restart]", True)
    pass


#* options
UNCAP_OPTION = options.SliderOption(
    identifier="Team Count",
    description="Set the maximum number of teams allowed in the lobby.\nWARNING: Lobbies with more than 32 players (8 teams) may experience synchronization issues.",
    value=4,
    min_value=2,
    max_value=16,
    on_change=functions.set_lobby_size,
)

NETWORK_OPTION = options.DropdownOption(
    identifier="Network Settings",
    description="Adjust network settings for optimal experience.\n(See console for more information)",
    value="High Bandwidth",
    choices=[
        ("Default"),
        ("Medium Bandwidth"),
        ("High Bandwidth"),
        ("Low Tickrate"),
        ("High Tickrate"),
        ("Throttled"),
        # ("Broken")
    ],
    on_change=network.set_net_vars,
)

FIX_OPTION = options.DropdownOption(
    identifier="Enable CoopPatch Fixes",
    description="Apply Robeth's CoopPatch fixes for health, experience, kill skills, etc.\nWARNING: Must be disabled to use hotfix TextMods.",
    value="Hotfix",
    choices=[
        ("Disabled"),
        ("Hotfix"),
        ("Hotfix (Offline)"),
        ("Experimental")
    ],
    on_change=hotfixes.set_hotfix
)

SCALING_OPTION = options.BoolOption(
    identifier="Enable Max Scaling",
    description="Enable 4-player enemy scaling.\n(Maximum allowed by game)",
    value=True,
    on_change=functions.set_enemy_scaling,
)

VEHICLE_OPTIONS = options.NestedOption(
    "Vehicle Options",
    children=[
            options.BoolOption(
                identifier="Enable Vehicle Tweaks",
                description="Allows all vehicles to be spawned at any vehicle digistruct terminal, and allows players to stand on top of vehicles.",
                value=True,
                on_change=vehicles.set_vehicle_qol,
            ),
            options.BoolOption(
                identifier="Enable Health Fix",
                description="Fixes the 20hp vehicle bug by scaling minimum vehicle health based on the host's max health.",
                value=True,
                on_change=vehicles.set_vehicle_fix,
            ),
            options.SliderOption(
                identifier="Health Fix Scaling",
                description="Set the scaling factor for player vehicle health.\nVehicle health = Host's Max Health * ScalingFactor",
                value=10,
                min_value=1,
                max_value=25,
                on_change=vehicles.set_vehicle_scaling,
            )
    ],
)

MISC_OPTIONS = options.NestedOption(
    "Miscellaneous Options",
    children=[
        options.BoolOption(
            identifier="Enable Logging",
            description="Enable console logging for NoCap.",
            value=True,
            on_change=functions.set_logging,
        )
    ]
)


#* keybinds
@keybind("Reapply fixes", "Period", description="Reapply the current NoCap fixes manually.")
def reapply_fixes() -> None:
    if(sv.EnableFixes == 1): # game fixes
        hotfixes.spark_hotfixes(1)
    elif(sv.EnableFixes == 2):
        hotfixes.spark_hotfixes(0)
    elif(sv.EnableFixes == 3):
        altfixes.manual_fixes()
    if(sv.EnableVehicleTweaks): # vehicle tweaks
        vehicles.apply_vehicle_qol(True)
    if(Game.get_current() == Game.TPS): # TPS mission fixes
        functions.fix_tps_missions()


#* build 
mod = build_mod(
    options=[UNCAP_OPTION, NETWORK_OPTION, FIX_OPTION, SCALING_OPTION, VEHICLE_OPTIONS, MISC_OPTIONS],
    keybinds=[reapply_fixes],
    on_enable=on_enable,
    on_disable=on_disable,
    coop_support=CoopSupport.RequiresAllPlayers, # technically hostside
)
