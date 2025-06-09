class Byte:
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFF).to_bytes(1, "big")
    
    @staticmethod
    async def decode(data: bytearray) -> int:
        decoded = data.pop(0).to_bytes(1, "big")
        decoded = int.from_bytes(decoded, signed=True)

        return decoded