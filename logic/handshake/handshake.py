import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.client.handshake.handshake import Handshake
from storing.remote import Remote
from storing.cache import Cache
from static.states import *

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    client_packet = await Handshake.create(data)
    show_self(client_packet, 2)
    if (client_packet.intent == 1):
        cache.remote[remote] = STATUS
    else:
        cache.remote[remote] = LOGIN