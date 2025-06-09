import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.client.play.teleport_confirm import TeleportConfirm
from storing.player import Player
from storing.remote import Remote
from storing.cache import Cache

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    client_packet = await TeleportConfirm.create(data)
    show_self(client_packet, 2)