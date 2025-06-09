from ..logger import *
from .. import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from ..logic.logic import new_session

async def run(address: str, port: int):
    server = await asyncio.start_server(new_session, address, port)
    log(f"Started server at {address}:{port}")
    async with server:
        log("Server is serving forever")
        await server.serve_forever()