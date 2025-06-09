import asyncio

class VarInt:
    @staticmethod      
    async def encode(data: int) -> bytes:
        encoded = b''
        while (True):
            towrite = data & 0x7f
            data >>= 7
            if (data):
                encoded += (towrite | 0x80).to_bytes(1, "big")
            else:
                encoded += (towrite).to_bytes(1, "big")
                break
        
        return encoded
    
    @staticmethod
    async def decode(data: bytearray) -> int:
        shift = 0
        decoded = 0

        while (True):
            i = data.pop(0)
            decoded |= (i & 0x7f) << shift
            shift += 7
            if (not (i & 0x80)):
                break

        return decoded
    
    @staticmethod
    async def decode_stream(data: asyncio.StreamReader) -> int:
        shift = 0
        decoded = 0

        while (True):
            i = int.from_bytes(await data.read(1))
            decoded |= (i & 0x7f) << shift
            shift += 7
            if (not (i & 0x80)):
                break

        return decoded