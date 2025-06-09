import config
from logger import *
set_verbosity_level(config.VERBOSITY_LEVEL)

import asyncio

from storing.cache import load, store
from networking import sock
import logic.keep_aliver
import logic.ticker
import logic.logic

async def _main():
    await asyncio.gather(
        logic.ticker.run(),
        logic.keep_aliver.run(),
        sock.run(config.SERVER_ADDRESS, config.SERVER_PORT),
    )
    log("Server is now running")

def main():
    cache = load()
    logic.logic.cache = cache
    logic.ticker.cache = cache
    logic.keep_aliver.cache = cache
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        err("Keyboard interrupt, storing cache")
        store(cache)

if __name__ == "__main__":
    main()