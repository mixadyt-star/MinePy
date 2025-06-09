import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.server.play.player_pos_and_look import PlayerPosAndLook
from networking.server.play.server_difficulty import ServerDifficulty
from networking.server.play.player_abilities import PlayerAbilities
from networking.server.play.held_item_change import HeldItemChange
from networking.server.play.unlock_recipies import UnlockRecepies
from networking.server.play.player_list_add import PlayerListAdd
from networking.server.play.spawn_position import SpawnPosition
from networking.server.play.entity_status import EntityStatus
from networking.server.play.time_update import TimeUpdate
from networking.server.play.join_game import JoinGame
from storing.player import Player
from storing.remote import Remote
from storing.cache import Cache
from static import entity_statuses
from static.abilities import *
from logic.play import ids

async def process(writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    player: Player = cache.players[remote.username]

    if (player.eid is None):
        player.eid = await ids.generate_eid(cache)

    join_game_packet = await JoinGame.create(
        player.eid,
        player.gamemode,
        player.dimension,
        config.DIFFICULTY,
        config.MAX_PLAYERS_COUNT,
        config.LEVEL_TYPE,
        config.REDUCED_DEBUG_INFO,
    )
    log(f"JoinGame: {join_game_packet}", 2)
    writer.write(join_game_packet)
    

    difficulty_setting = await ServerDifficulty.create(
        config.DIFFICULTY,
    )
    log(f"ServerDifficulty: {difficulty_setting}", 2)
    writer.write(difficulty_setting)
    

    flags = 0
    if (player.invulnerable):
        flags |= INVULNERABLE
    if (player.flying):
        flags |= FLYING
    if (player.allow_flying):
        flags |= ALLOW_FLYING
    if (player.instant_crash):
        flags |= CREATIVE_MODE
    player_abilities_setting = await PlayerAbilities.create(
        flags,
        config.FLYING_SPEED,
        config.FIELD_VIEW,
    )
    log(f"PlayerAbilities: {player_abilities_setting}", 2)
    writer.write(player_abilities_setting)
    

    held_item_setting = await HeldItemChange.create(
        player.slot,
    )
    log(f"HeldItemChange: {held_item_setting}", 2)
    writer.write(held_item_setting)
    

    entity_status_setting = await EntityStatus.create(
        player.eid,
        entity_statuses.PLAYER_SET_OP_LEVEL0,
    )
    log(f"EntityStatus: {entity_status_setting}", 2)
    writer.write(entity_status_setting)
    
    recipies_setting = await UnlockRecepies.create(
        0,
        config.CRAFT_BOOK_OPEN,
        config.FILTERING_CRAFTABLE,
        0,
        [],
        0,
        [],
    )
    log(f"UnlockRecepies: {recipies_setting}", 2)
    writer.write(recipies_setting)

    player_list_setting = await PlayerListAdd.create(
        1,
        [(
            player.uuid,
            player.username,
            0,
            None,
            player.gamemode,
            0,
            bool(player.display_name),
            player.display_name,
        )]
    )
    log(f"PlayerListAdd: {player_list_setting}", 2)
    writer.write(player_list_setting)
    

    time_setting = await TimeUpdate.create(
        cache.world_ticks,
        cache.world_ticks % 24000,
    )
    log(f"TimeUpdate: {time_setting}", 2)
    writer.write(time_setting)
    
    x, y, z = player.position
    yaw, pitch = player.rotation

    pos_and_view_setting = await PlayerPosAndLook.create(
        x,
        y,
        z,
        yaw,
        pitch,
        0,
        await ids.generate_tp_id(cache),
    )
    log(f"PlayerPosAndView: {pos_and_view_setting}", 2)
    writer.write(pos_and_view_setting)

    spawn_position_setting = await SpawnPosition.create(
        (x, y, z),
    )
    log(f"SpawnPosition: {spawn_position_setting}", 2)
    writer.write(spawn_position_setting)
    
    