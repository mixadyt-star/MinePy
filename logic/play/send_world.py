from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ...networking.server import *
from ...storing import *
from ..world import *

async def process(writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    for x in range(-8, 9):
        for z in range(-8, 9):
            chunk_packet = await ChunkData.create(
                await World.get_packed_chunk(x, z)
            )
            log(f"Chunk data x={x} z={z} sent")
            writer.write(chunk_packet)
            await writer.drain()