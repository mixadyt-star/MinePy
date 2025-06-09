from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ...networking.server import *
from ...storing import *
from ...static import *

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    response = await StatusResponse.create(
        config.VERSION_NAME,
        config.VERSION_PROTOCOL,
        config.MAX_PLAYERS_COUNT,
        cache.online,
        config.SERVER_DESCRIPTION,
        config.SERVER_IMAGE,
    )
    log(f"StatusResponse: {response}")
    writer.write(response)
    await writer.drain()