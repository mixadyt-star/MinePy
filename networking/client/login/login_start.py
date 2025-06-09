from ....common_types import *

class _LoginStart:
    def __init__(self, username: str):
        self.username = username

class LoginStart:
    @staticmethod
    async def create(data: bytearray) -> _LoginStart:
        return _LoginStart(
            username=await String.decode(data),
        )
