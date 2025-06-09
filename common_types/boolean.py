class Boolean:
    @staticmethod
    async def encode(data: bool) -> bytes:
        return int(data).to_bytes(1, "big")
    
    @staticmethod
    async def decode(data: bytearray) -> bool:
        return bool(data.pop(0))