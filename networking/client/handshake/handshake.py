from common_types.unsigned_short import UnsignedShort
from common_types.string import String
from common_types.varint import VarInt

class _Handshake:
    def __init__(self, version: int, address: str, port: int, intent: int):
        self.version = version
        self.address = address,
        self.port = port
        self.intent = intent

class Handshake:
    @staticmethod
    async def create(data: bytearray) -> _Handshake:
        return _Handshake(
            version=await VarInt.decode(data),
            address=await String.decode(data),
            port=await UnsignedShort.decode(data),
            intent=await VarInt.decode(data),
        )
