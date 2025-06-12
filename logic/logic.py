from ..logger import *
from .. import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio
import zlib

from ..custom_exceptions import *
from ..common_types import *
from ..storing import *
from ..static import *
from . import *

cache: Cache = None

async def new_session(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    global cache

    remote = Remote(*writer.get_extra_info("peername"))
    cache.remote[remote] = HANDSHAKING
    log(f"New connection {remote.address}:{remote.port}", 2)

    while (True):
        try:
            if (cache.remote[remote] != STATUS and cache.remote[remote] != HANDSHAKING and remote.compression_enabled):
                compressed_length = await VarInt.decode(reader)

                packet_length = await VarInt.decode(reader)
                if (packet_length == 0):
                    packet_length = compressed_length - 1
                    if (packet_length <= 0):
                        raise ValueError("Packet length is zero")
                    
                    id = await VarInt.decode(reader)
                    # buffer = reader
                    buffer = asyncio.StreamReader()
                    buffer.feed_data(await reader.read(packet_length - 1))
                    buffer.feed_eof()
                else:
                    compressed_data = await reader.read(compressed_length - len(await VarInt.encode(packet_length)))
                    uncompressed_data = bytearray(zlib.decompress(compressed_data))
                    id = await VarInt.decode(uncompressed_data)
                    
                    buffer = asyncio.StreamReader()
                    buffer.feed_data(uncompressed_data)
                    buffer.feed_eof()
            else:
                packet_length = await VarInt.decode(reader)
                if (packet_length <= 0):
                    raise ValueError("Packet length is zero")

                id = await VarInt.decode(reader)
                # buffer = reader
                buffer = asyncio.StreamReader()
                buffer.feed_data(await reader.read(packet_length - 1))
                buffer.feed_eof()

            if (cache.remote[remote] == HANDSHAKING):
                if (id == 0x0):
                    await handshake.process(buffer, cache, remote)

            elif (cache.remote[remote] == STATUS):
                if (id == 0x0):
                    await status_request.process(writer, cache, remote)
                elif (id == 0x1):
                    await status_ping_request.process(buffer, writer, cache, remote)
            
            elif (cache.remote[remote] == LOGIN):
                if (id == 0x0):
                    await login_start.process(buffer, writer, cache, remote)
                    await setting_player.process(writer, cache, remote)
                elif (id == 0x1):
                    raise NotImplemented("Login encryption not implemented")
                
            elif (cache.remote[remote] == PLAY):
                if (id == 0x0):
                    await teleport_confirm.process(buffer, writer, cache, remote)
                elif (id == 0x4):
                    await client_settings.process(buffer, cache, remote)
                    await send_world.process(writer, cache, remote)

        except PlayerAlreadyOnline:
            break

        except ServerIsFull:
            break

        except Exception as e:
            # raise e
            warn(str(e), 2)
            if (remote.username):
                cache.players[remote.username].online = False
                cache.keep_alive_list.pop(StreamWriter(writer))
                cache.online -= 1
                log(f"{remote.username} has left the game")
            break

    writer.close()
    log(f"Disconnected {remote.address}:{remote.port}", 2)