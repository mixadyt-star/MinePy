from typing import Tuple

from networking.server.packet import Packet
from common_types.position import Position
from common_types.varint import VarInt

class SpawnPosition:
    @staticmethod
    async def create(location: Tuple[int, int, int]) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x46),
            await Position.encode(location),
        )
