from common_types.long import Long

class _StatusPingRequest:
    def __init__(self, payload: int):
        self.payload = payload

class StatusPingRequest:
    @staticmethod
    async def create(data: bytearray) -> _StatusPingRequest:
        return _StatusPingRequest(
            payload=await Long.decode(data),
        )
