from ....common_types import *
from ..packet import Packet

class Disconnect:
    @staticmethod
    async def create(reason: str) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x0),
            await String.encode(reason),
            is_compressed=False,
        )
