from networking.server.packet import Packet
from common_types.unsigned_byte import UnsignedByte
from common_types.varint import VarInt

class ServerDifficulty:
    @staticmethod
    async def create(difficulty: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x0d),
            await UnsignedByte.encode(difficulty),
        )
