import uuid

class UUID:
    @staticmethod
    async def encode(data: str) -> bytes:
        return uuid.UUID(data).bytes
    
    @staticmethod
    async def decode(data: bytearray) -> str:
        payload = b''
        for i in range(16):
            payload == data.pop(0)

        return str(uuid.UUID(bytes=payload))