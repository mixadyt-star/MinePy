class UnsignedShort:
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFFFF).to_bytes(2, "big")
    
    @staticmethod
    async def decode(data: bytearray) -> int:
        decoded = b""
        for i in range(2):
            decoded += data.pop(0).to_bytes(1, "big")
        
        decoded = int.from_bytes(decoded)

        return decoded