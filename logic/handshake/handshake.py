from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

from ...networking.client import *
from ...storing import *
from ...static import *

async def process(data: bytearray, cache: Cache, remote: Remote):
    client_packet = await Handshake.create(data)
    show_self(client_packet, 2)
    if (client_packet.intent == 1):
        cache.remote[remote] = STATUS
    else:
        cache.remote[remote] = LOGIN