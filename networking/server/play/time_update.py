from typing import Tuple

from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.long import Long

class TimeUpdate:
    @staticmethod
    async def create(world_age: int, time_of_day: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x47),
            await Long.encode(world_age),
            await Long.encode(time_of_day),
        )
