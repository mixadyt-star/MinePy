from typing import Dict, Any
import asyncio
import pickle
import os

from .remote import Remote
from .player import Player

class StreamWriter:
    def __init__(self, writer: asyncio.StreamWriter):
        self.writer = writer

    def __hash__(self):
        return hash(self.writer.get_extra_info("peername"))
    
    def __eq__(self, other):
        return self.writer.get_extra_info("peername") == other.writer.get_extra_info("peername")

class Cache:
    def __init__(self):
        self.world_ticks = 0
        self.eid = 0
        self.tp_id = 0
        self.online = 0
        self.keep_alive_list: Dict[StreamWriter, int] = {}
        self.remote: Dict[Remote, int] = {}
        self.players: Dict[str, Player] = {}

def load() -> Cache:
    loaded = load_from_bytes("data\\cache.minepy")
    return loaded if (loaded is not None) else Cache()

def store(cache: Cache):
    cache.online = 0
    cache.tp_id = 0
    cache.remote = {}
    cache.keep_alive_list = {}
    for _, player in cache.players.items():
        player.online = False
    
    store_to_bytes("data\\cache.minepy", cache)

def load_from_bytes(path: str) -> Any | None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(os.path.dirname(current_dir), path)
    return pickle.load(open(file_path, "rb")) if os.path.exists(file_path) else None

def store_to_bytes(path: str, obj: Any):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), os.path.dirname(path))
    file_path = os.path.join(os.path.dirname(current_dir), path)
    os.makedirs(data_path, exist_ok=True)
    
    pickle.dump(obj, open(file_path, "wb"), pickle.HIGHEST_PROTOCOL)

def load_bytes(path: str) -> bytes | None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(os.path.dirname(current_dir), path)
    return open(file_path, "rb").read() if os.path.exists(file_path) else None

def store_bytes(path: str, data: bytes):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), os.path.dirname(path))
    file_path = os.path.join(os.path.dirname(current_dir), path)
    os.makedirs(data_path, exist_ok=True)
    
    open(file_path, "wb").write(data)

def file_exists(path: str) -> bool:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(os.path.dirname(current_dir), path)
    
    return os.path.exists(file_path)