from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ...networking.server import *
from ...storing import *
from ..world import *

async def process(writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    chunk = await Chunk.generate(0, 0)
    for x in range(-4, 5):
        for z in range(-4, 5):
            chunk.x = x
            chunk.z = z
            chunk_packet = await ChunkData.create(
                await Chunk.pack(chunk),
            )
            log(f"Chunk data x={x} z={z} sent")
            writer.write(chunk_packet)
            await writer.drain()