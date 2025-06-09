from networking.server.packet import Packet
from common_types.varint import VarInt

class ChunkData:
    @staticmethod
    async def create(data: bytes) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x20),
            data,
        )
