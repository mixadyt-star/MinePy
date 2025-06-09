from typing import Tuple

from ....common_types import *
from ..packet import Packet

class SpawnPosition:
    @staticmethod
    async def create(location: Tuple[int, int, int]) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x46),
            await Position.encode(location),
        )
