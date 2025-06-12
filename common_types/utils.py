def multi_pop(data: bytearray, num: int) -> bytes:
    return b''.join(data.pop(0).to_bytes(1, "big") for _ in range(num))