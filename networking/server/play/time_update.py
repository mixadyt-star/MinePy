from ....common_types import *
from ..packet import Packet

class TimeUpdate:
    @staticmethod
    async def create(world_age: int, time_of_day: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x47),
            await Long.encode(world_age),
            await Long.encode(time_of_day),
        )
