import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.server.status.status_ping_response import StatusPingResponse
from networking.client.status.status_ping_request import StatusPingRequest
from storing.remote import Remote
from storing.cache import Cache

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    client_packet = await StatusPingRequest.create(data)
    show_self(client_packet, 2)
    response = await StatusPingResponse.create(
        client_packet.payload,
    )
    log(f"StatusPingResponse: {response}")
    writer.write(response)