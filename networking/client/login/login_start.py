from common_types.string import String

class _LoginStart:
    def __init__(self, username: str):
        self.username = username

class LoginStart:
    @staticmethod
    async def create(data: bytearray) -> _LoginStart:
        return _LoginStart(
            username=await String.decode(data),
        )
