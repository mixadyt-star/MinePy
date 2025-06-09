from .logger import *
from . import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from .logic import ticker, keep_aliver, logic
from .storing import load, store
from .networking import sock

async def _main():
    await asyncio.gather(
        logic.ticker.run(),
        logic.keep_aliver.run(),
        sock.run(config.SERVER_ADDRESS, config.SERVER_PORT),
    )
    log("Server is now running")

def main():
    cache = load()
    logic.cache = cache
    ticker.cache = cache
    keep_aliver.cache = cache
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        err("Keyboard interrupt, storing cache")
        store(cache)

if __name__ == "__main__":
    main()