import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from networking.client.play.client_settings import ClientSettings
from storing.player import Player
from storing.remote import Remote
from storing.cache import Cache

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    client_packet = await ClientSettings.create(data)
    show_self(client_packet, 2)

    player: Player = cache.players[remote.username]
    player.locale = client_packet.locale
    player.view_distance = client_packet.view_distance
    player.chat_mode = client_packet.chat_mode
    player.chat_colors = client_packet.chat_colors
    player.displayed_skin_parts = client_packet.displayed_skin_parts
    player.main_hand = client_packet.main_hand