from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ...networking.server import *
from ...storing import *
from ...static import *
from ..play import ids

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
    await writer.drain()

    difficulty_setting = await ServerDifficulty.create(
        config.DIFFICULTY,
    )
    log(f"ServerDifficulty: {difficulty_setting}", 2)
    writer.write(difficulty_setting)
    await writer.drain()

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
    await writer.drain()

    held_item_setting = await HeldItemChange.create(
        player.slot,
    )
    log(f"HeldItemChange: {held_item_setting}", 2)
    writer.write(held_item_setting)
    await writer.drain()

    entity_status_setting = await EntityStatus.create(
        player.eid,
        PLAYER_SET_OP_LEVEL0,
    )
    log(f"EntityStatus: {entity_status_setting}", 2)
    writer.write(entity_status_setting)
    await writer.drain()
    
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
    await writer.drain()

    player_list = []
    for username, other_player in cache.players.items():
        if (other_player.online):
            player_list.append((
                other_player.uuid,
                other_player.username,
                0,
                None,
                other_player.gamemode,
                0,
                bool(other_player.display_name),
                other_player.display_name,
            ))

    player_list_setting = await PlayerListAdd.create(
        len(player_list),
        player_list,
    )
    log(f"PlayerListAdd: {player_list_setting}", 2)
    writer.write(player_list_setting)
    await writer.drain()

    time_setting = await TimeUpdate.create(
        cache.world_ticks,
        cache.world_ticks % 24000,
    )
    log(f"TimeUpdate: {time_setting}", 2)
    writer.write(time_setting)
    await writer.drain()
    