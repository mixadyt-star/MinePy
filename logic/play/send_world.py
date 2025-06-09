import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.server.play.player_pos_and_look import PlayerPosAndLook
from networking.server.play.spawn_position import SpawnPosition
from networking.server.play.chunk_data import ChunkData
from logic.world.chunk import Chunk
from storing.player import Player
from storing.remote import Remote
from storing.cache import Cache
from logic.play import ids

async def process(writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    player: Player = cache.players[remote.username]

    chunk = await Chunk.generate(0, 0)
    for x in range(-16, 0):
        for z in range(-16, 0):
            chunk.x = x
            chunk.z = z
            chunk_packet = await ChunkData.create(
                await Chunk.pack(chunk),
            )
            log(f"Chunk data x={x} z={z} sent")
            writer.write(chunk_packet)
            await writer.drain()

    x, y, z = player.position
    yaw, pitch = player.rotation
    spawn_position_setting = await SpawnPosition.create(
        (x, y, z),
    )
    log(f"SpawnPosition: {spawn_position_setting}", 2)
    writer.write(spawn_position_setting)

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