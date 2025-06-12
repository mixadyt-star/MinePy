from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ...networking.server import *
from ...storing import *
from ..play import ids
from ..world import *

async def process(writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    player: Player = cache.players[remote.username]

    for x in range(-player.view_distance, player.view_distance + 1):
        for z in range(-player.view_distance, player.view_distance + 1):
            chunk_packet = await ChunkData.create(
                await World.get_packed_chunk(x, z)
            )
            log(f"Chunk data x={x} z={z} sent")
            writer.write(chunk_packet)
            await writer.drain()
    
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
    await writer.drain()

    spawn_position_setting = await SpawnPosition.create(
        config.SPAWN_POSITION,
    )

    log(f"SpawnPosition: {spawn_position_setting}", 2)
    writer.write(spawn_position_setting)
    await writer.drain()