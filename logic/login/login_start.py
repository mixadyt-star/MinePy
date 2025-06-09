import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio
import time
import uuid

from networking.server.login.enable_compression import EnableCompression
from networking.server.login.login_success import LoginSuccess
from networking.server.login.disconnect import Disconnect
from networking.client.login.login_start import LoginStart
from custom_exceptions import PlayerAlreadyOnline
from storing.player import Player
from storing.remote import Remote
from storing.cache import Cache, StreamWriter
from static.entity_statuses import *
from static.gamemodes import *
from static.abilities import *
from static.states import *

async def process(data: bytearray, writer: asyncio.StreamWriter, cache: Cache, remote: Remote):
    client_packet = await LoginStart.create(data)
    show_self(client_packet, 2)
    remote.username = client_packet.username
    cache.players[remote.username] = cache.players.get(
        remote.username, Player(remote.username, str(uuid.uuid3(uuid.NAMESPACE_X500, remote.username)))
    )

    if (cache.players[remote.username].online):
        response = await Disconnect.create(
            '"Player already online"',
        )
        log(f"Disconnect: {response}")
        writer.write(response)
        await writer.drain()
        raise PlayerAlreadyOnline()
    
    response = await EnableCompression.create(
        config.COMPRESSION_THRESHOLD,
    )
    remote.compression_enabled = True
    log(f"EnableCompression: {response}")
    writer.write(response)
    await writer.drain()

    response = await LoginSuccess.create(
        cache.players[remote.username].uuid,
        remote.username,
    )
    log(f"LoginSuccess: {response}")
    cache.remote[remote] = PLAY
    cache.keep_alive_list[StreamWriter(writer)] = time.time()
    player: Player = cache.players[remote.username]
    player.online = True
    log(f"{player.username} joined the game")
    writer.write(response)
    await writer.drain()