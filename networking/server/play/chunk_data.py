from ....common_types import *
from ..packet import Packet

class ChunkData:
    @staticmethod
    async def create(data: bytes) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x20),
            data,
        )
