from .varint import VarInt

class String:
    @staticmethod
    async def encode(data: str) -> bytes:
        temp = await VarInt.encode(len(data))
        encoded = temp + data.encode()

        return encoded

    @staticmethod
    async def decode(data: bytearray) -> str:
        length = await VarInt.decode(data)
        decoded = b''
        for i in range(length):
            decoded += data.pop(0).to_bytes(1, "big")

        decoded = decoded.decode()

        return decoded