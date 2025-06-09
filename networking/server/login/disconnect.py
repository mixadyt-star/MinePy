from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.string import String

class Disconnect:
    @staticmethod
    async def create(reason: str) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x0),
            await String.encode(reason),
            is_compressed=False,
        )
