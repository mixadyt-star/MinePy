from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.long import Long

class StatusPingResponse:
    @staticmethod
    async def create(payload: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x1),
            await Long.encode(payload),
            is_compressed=False,
        )
