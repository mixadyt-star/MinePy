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