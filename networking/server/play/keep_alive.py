from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.long import Long

class KeepAlive:
    @staticmethod
    async def create(keep_alive_id) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x1f),
            await Long.encode(keep_alive_id),
        )
