from __future__ import annotations
from typing import Optional
from mods_base import get_pc, options, ENGINE
from unrealsdk import logging, find_all
from nocap.variables import global_vars as sv


def set_logging(_option: options.BoolOption | None, value: bool) -> None:
    if(_option is None or _option.mod.is_enabled):
        if value == True:
            sv.EnableLogging = True
        else:
            sv.EnableLogging = False


def log(message: str, force: Optional[bool] = False ) -> None:
    if sv.EnableLogging or force:
        logging.info(f"[NoCap] {message}")


def is_host():
    return ENGINE.GetCurrentWorldInfo().NetMode == 2


def parse_commands(commands: list[str]) -> None:
    for command in commands:
        PC = get_pc()
        if PC is not None:
            PC.ServerRCon(command) # previously ENGINE.GamePlayers[0].Actor.ServerRCon(command)


def show_message(message: str) -> None:
    tcm = get_pc().GetTextChatMovie()
    tcm.AddChatMessageInternal("NoCap", message)


def log_teams() -> None:
    WillowCoopGameInfo = find_all("WillowCoopGameInfo")[-1]
    if WillowCoopGameInfo is None:
        return
    team_sizes = []
    for team in WillowCoopGameInfo.Teams:
        team_sizes.append((team.TeamIndex, team.Size))
    log(f"Teams: {team_sizes}")


def find_best_team() -> int:
    ''' allow up to 3 players in team 0, then begin filling team 1, then team 2, etc. '''
    WillowCoopGameInfo = find_all("WillowCoopGameInfo")[-1] # find WillowCoopGameInfo
    if WillowCoopGameInfo is None:
        return 0
    
    team_sizes = [] # build team size list (team index, team size)
    for team in WillowCoopGameInfo.Teams:
        team_sizes.append((team.TeamIndex, team.Size))
    if len(team_sizes) == 0:
        return 0
    
    #? debug pick a random team with space
    # random_team = randint(0, len(team_sizes) - 1)
    # if team_sizes[random_team][1] < 4:
    #     log(f"Found team with space: {random_team}")
    #     return random_team
    #? end debug
    
    if team_sizes[0][1] < 4: # allow up to 3 players in team 0
        log("Found team with space: 0")
        return 0
    
    for i in range(1, len(team_sizes)): # after, check for available slots sequentially
        if team_sizes[i][1] < 4:
            log(f"Found team with space: {i}")
            return i
    return 0


def set_lobby_size(_option: options.IntOption | None, value: int) -> None:
    if(_option == None or _option.mod.is_enabled):
        if value:
            sv.TeamCount = value
            player_count = value * 4
            commands = [
                f"set WillowOnlineGameSettings NumPublicConnections {player_count}", # robeth val: 64
                "set GameInfo MaxPlayers 0", # leaving at robeth val for now
                "set GameInfo MaxPlayersAllowed 512" # leaving at robeth val for now
            ]
            parse_commands(commands)
            if isinstance(player_count, int): # avoid errant decimal double print at launch
                log(f"Lobby size adjusted to {player_count}")


def set_enemy_scaling(_option: options.BoolOption | None, value: bool) -> None:
    if(_option is None or _option.mod.is_enabled):
        if value:
            sv.EnableMaxScaling = value
            commands = [
                "set Engine.GameInfo EffectiveNumPlayers 4"
            ]
            parse_commands(commands)
            log(f"Enemy scaling adjusted to maximum [EffectiveNumPlayers: 4]")