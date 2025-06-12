from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ...networking.server import *
from ...networking.client import *
from ...storing import *

async def process(buffer: asyncio.StreamReader, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    client_packet = await StatusPingRequest.create(buffer)
    show_self(client_packet, 2)
    response = await StatusPingResponse.create(
        client_packet.payload,
    )
    log(f"StatusPingResponse: {response}")
    writer.write(response)
    await writer.drain()