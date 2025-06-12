from abc import ABC, abstractmethod
from typing import Any
import asyncio

class CommonType(ABC):

    @staticmethod
    @abstractmethod
    async def encode(data: Any) -> bytes:
        pass

    @staticmethod
    @abstractmethod
    async def _decode(data: bytearray) -> Any:
        pass

    @staticmethod
    @abstractmethod
    async def decode(reader: asyncio.StreamReader) -> Any:
        pass