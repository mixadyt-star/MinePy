class Long:
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFFFFFFFFFFFFFFFF).to_bytes(8, "big")
    
    @staticmethod
    async def decode(data: bytearray) -> int:
        decoded = b""
        for i in range(8):
            decoded += data.pop(0).to_bytes(1, "big")
            
        decoded = int.from_bytes(decoded, signed=True)

        return decoded