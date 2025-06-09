from ....common_types import *
from ..packet import Packet

class HeldItemChange:
    @staticmethod
    async def create(slot: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x3a),
            await Byte.encode(slot),
        )
