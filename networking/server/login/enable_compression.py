from networking.server.packet import Packet
from common_types.varint import VarInt

class EnableCompression:
    @staticmethod
    async def create(threshold: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x3),
            await VarInt.encode(threshold),
            is_compressed=False,
        )
