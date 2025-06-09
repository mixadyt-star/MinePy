import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.server.status.status_response import StatusResponse
from storing.remote import Remote
from storing.cache import Cache
from static.states import *
from config import *

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    response = await StatusResponse.create(
        VERSION_NAME,
        VERSION_PROTOCOL,
        MAX_PLAYERS_COUNT,
        cache.online,
        SERVER_DESCRIPTION,
        SERVER_IMAGE,
    )
    log(f"StatusResponse: {response}")
    writer.write(response)