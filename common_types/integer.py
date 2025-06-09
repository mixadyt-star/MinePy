class Integer:
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFFFFFFFF).to_bytes(4, "big")
    
    @staticmethod
    async def decode(data: bytearray) -> int:
        decoded = b""
        for i in range(4):
            decoded += data.pop(0).to_bytes(1, "big")
            
        decoded = int.from_bytes(decoded, signed=True)

        return decoded