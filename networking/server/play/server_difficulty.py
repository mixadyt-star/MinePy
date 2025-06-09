from ....common_types import *
from ..packet import Packet

class ServerDifficulty:
    @staticmethod
    async def create(difficulty: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x0d),
            await UnsignedByte.encode(difficulty),
        )
