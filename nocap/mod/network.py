from mods_base import options
from unrealsdk import find_all
from nocap.mod.functions import log, parse_commands


def set_net_vars(_option: options.DropdownOption, value: str) -> None:
    if _option == None or _option.mod.is_enabled:
        if value:
            if value == "Default":
                preset_default()
            elif value == "Medium Bandwidth":
                preset_medium_bandwidth()
            elif value == "High Bandwidth":
                preset_high_bandwidth()
            elif value == "Low Tickrate":
                preset_low_tickrate()
            elif value == "High Tickrate":
                preset_high_tickrate()
            elif value == "Throttled":
                preset_throttled()


def get_current_net_vars() -> None:
    ''' print current net vars for debugging '''
    WillowCoopGameInfo = find_all("WillowCoopGameInfo")[-1]
    log(f"WillowCoopGameInfo.TotalNetBandwidth {WillowCoopGameInfo.TotalNetBandwidth}")
    log(f"WillowCoopGameInfo.MinDynamicBandwidth {WillowCoopGameInfo.MinDynamicBandwidth}")
    PlayerInteractionServer = find_all("PlayerInteractionServer")[-1]
    log(f"PlayerInteractionServer.TimeoutTime {PlayerInteractionServer.TimeoutTime}")
    GameInfo = find_all("GameInfo")[-1]
    log(f"GameInfo.AdjustedNetSpeed {GameInfo.AdjustedNetSpeed}")
    tcp = find_all("IPDrv.TCPNetDriver")[-1]
    log(f"IPDrv.TCPNetDriver.NetServerMaxTickrate {tcp.NetServerMaxTickrate}")
    log(f"IPDrv.TCPNetDriver.bClampListenServerTickRate {tcp.bClampListenServerTickRate}")
    log(f"IPDrv.TCPNetDriver.KeepAliveTime {tcp.KeepAliveTime}")
    log(f"IPDrv.TCPNetDriver.MaxInternetClientRate {tcp.MaxInternetClientRate}")
    log(f"IPDrv.TCPNetDriver.MaxClientRate {tcp.MaxClientRate}")
    log(f"IPDrv.TCPNetDriver.SpawnPrioritySeconds {tcp.SpawnPrioritySeconds}")
    log(f"IPDrv.TCPNetDriver.InitialConnectTimeout {tcp.InitialConnectTimeout}")
    log(f"IPDrv.TCPNetDriver.ConnectionTimeout {tcp.ConnectionTimeout}")
    WillowPlayerReplicationInfo = find_all("WillowPlayerReplicationInfo")[-1]
    log(f"WillowPlayerReplicationInfo.NetUpdateFrequency {WillowPlayerReplicationInfo.NetUpdateFrequency}")
    Engine = find_all("Engine")[-1]
    log(f"Engine.NetClientTicksPerSecond {Engine.NetClientTicksPerSecond}")
    steamworks = find_all("OnlineSubsystemSteamworks.IpNetDriverSteamworks")[-1]
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.NetServerMaxTickRate {steamworks.NetServerMaxTickRate}")
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.bClampListenServerTickRate {steamworks.bClampListenServerTickRate}")
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.KeepAliveTime {steamworks.KeepAliveTime}")
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.MaxInternetClientRate {steamworks.MaxInternetClientRate}")
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.MaxClientRate {steamworks.MaxClientRate}")
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.SpawnPrioritySeconds {steamworks.SpawnPrioritySeconds}")
    log(f"OnlineSubsystemSteamworks.IpNetDriverSteamworks.ConnectionTimeout {steamworks.ConnectionTimeout}")


def preset_default() -> None:
    ''' sets net vars to game defaults '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 32000",
        "set WillowCoopGameInfo MinDynamicBandwidth 4000",
        "set PlayerInteractionServer TimeoutTime 5.0",
        "set GameInfo AdjustedNetSpeed 0",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 30",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.200000",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 10000",
        "set IPDrv.TCPNetDriver MaxClientRate 15000",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 1.0",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 60.0",
        "set IPDrv.TCPNetDriver ConnectionTimeout 30.0",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 30.0",
        "set Engine NetClientTicksPerSecond 200.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 30",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.200000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 30.0"
    ]
    parse_commands(commands)
    log("Network settings: Default [Tickrate:30] [Bandwidth:32000] [Rate:10000]")
    

def preset_medium_bandwidth() -> None:
    ''' sets bandwidth cap 4x higher than default '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 128000",
        "set WillowCoopGameInfo MinDynamicBandwidth 4000",
        "set PlayerInteractionServer TimeoutTime 5.0",
        "set GameInfo AdjustedNetSpeed 0",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 30",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.200000",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 10000",
        "set IPDrv.TCPNetDriver MaxClientRate 15000",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 1.0",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 60.0",
        "set IPDrv.TCPNetDriver ConnectionTimeout 30.0",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 30.0",
        "set Engine NetClientTicksPerSecond 200.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 30",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.200000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 30.0"
    ]
    parse_commands(commands)
    log("Network settings: Medium Bandwidth [Tickrate:30] [Bandwidth:128000] [Rate:10000]")


def preset_high_bandwidth() -> None:
    ''' sets bandwidth cap 20x higher than default '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 640000",
        "set WillowCoopGameInfo MinDynamicBandwidth 4000",
        "set PlayerInteractionServer TimeoutTime 5.0",
        "set GameInfo AdjustedNetSpeed 0",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 30",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.200000",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 10000",
        "set IPDrv.TCPNetDriver MaxClientRate 15000",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 1.0",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 60.0",
        "set IPDrv.TCPNetDriver ConnectionTimeout 30.0",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 30.0",
        "set Engine NetClientTicksPerSecond 200.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 30",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.200000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 30.0"
    ]
    parse_commands(commands)
    log("Network settings: High Bandwidth [Tickrate:30] [Bandwidth:640000] [Rate:10000]")


def preset_low_tickrate() -> None:
    ''' sets net vars to low tickrate (20hz) '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 32000",
        "set WillowCoopGameInfo MinDynamicBandwidth 4000",
        "set PlayerInteractionServer TimeoutTime 5.0",
        "set GameInfo AdjustedNetSpeed 0",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 20",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.200000",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 10000",
        "set IPDrv.TCPNetDriver MaxClientRate 15000",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 1.0",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 60.0",
        "set IPDrv.TCPNetDriver ConnectionTimeout 30.0",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 20.0",
        "set Engine NetClientTicksPerSecond 200.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 20",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.200000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 30.0"
    ]
    parse_commands(commands)
    log("Network settings: Low Tickrate [Tickrate:20] [Bandwidth:32000] [Rate:10000]")


def preset_high_tickrate() -> None:
    ''' sets net vars to high tickrate (45hz) '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 128000",
        "set WillowCoopGameInfo MinDynamicBandwidth 4000",
        "set PlayerInteractionServer TimeoutTime 5.0",
        "set GameInfo AdjustedNetSpeed 0",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 45",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.200000",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 15000",
        "set IPDrv.TCPNetDriver MaxClientRate 20000",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 1.0",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 60.0",
        "set IPDrv.TCPNetDriver ConnectionTimeout 30.0",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 45.0",
        "set Engine NetClientTicksPerSecond 300.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 45",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.200000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 15000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 15000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 30.0"
    ]
    parse_commands(commands)
    log("Network settings: High Tickrate [Tickrate:45] [Bandwidth:128000] [Rate:15000]")


def preset_throttled() -> None:
    ''' sets game vars to optimize net traffic for high player counts '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 640000",
        "set WillowCoopGameInfo MinDynamicBandwidth 2000",
        "set PlayerInteractionServer TimeoutTime 60.0",
        "set GameInfo AdjustedNetSpeed 5000",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 20",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.500000",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 7000",
        "set IPDrv.TCPNetDriver MaxClientRate 10000",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 2",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 300",
        "set IPDrv.TCPNetDriver ConnectionTimeout 120",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 20",
        "set Engine NetClientTicksPerSecond 100.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 20",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.500000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 7000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 10000",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 2",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 120"
    ]
    parse_commands(commands)
    log("Network settings: Throttled [Tickrate:20] [Bandwidth:640000] [Rate:7000]")


def preset_broken() -> None:
    ''' completely unusable settings for testing: 1 bandwidth, 1 tickrate, 1 client rate '''
    commands = [
        "set WillowCoopGameInfo TotalNetBandwidth 1",
        "set WillowCoopGameInfo MinDynamicBandwidth 1",
        "set PlayerInteractionServer TimeoutTime 1.0",
        "set GameInfo AdjustedNetSpeed 0",
        "set IPDrv.TCPNetDriver NetServerMaxTickrate 1",
        "set IPDrv.TCPNetDriver bClampListenServerTickRate False",
        "set IPDrv.TCPNetDriver KeepAliveTime 0.2",
        "set IPDrv.TCPNetDriver MaxInternetClientRate 1",
        "set IPDrv.TCPNetDriver MaxClientRate 1",
        "set IPDrv.TCPNetDriver SpawnPrioritySeconds 1.0",
        "set IPDrv.TCPNetDriver InitialConnectTimeout 1.0",
        "set IPDrv.TCPNetDriver ConnectionTimeout 1.0",
        "set WillowPlayerReplicationInfo NetUpdateFrequency 1.0",
        "set Engine NetClientTicksPerSecond 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks NetServerMaxTickRate 1",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks bClampListenServerTickRate False",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks KeepAliveTime 0.2",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxInternetClientRate 1",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks MaxClientRate 1",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks SpawnPrioritySeconds 1.0",
        "set OnlineSubsystemSteamworks.IpNetDriverSteamworks ConnectionTimeout 1.0"
    ]
    parse_commands(commands)
    log("Network settings: Broken [Tickrate:1] [Bandwidth:1] [Rate:1]")