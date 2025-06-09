from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.string import String

class LoginSuccess:
    @staticmethod
    async def create(uuid: str, name: str) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x2),
            await String.encode(uuid),
            await String.encode(name),
        )
