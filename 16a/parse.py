from collections import deque

from bits import bits2int

def shift(dq: deque, n: int = 1) -> list:
    l = []
    for _ in range(n):
        l.append(dq.popleft())
    return l

def parse_header(header: list[str]) -> tuple[int, int]:
    assert len(header) == 6
    header = ''.join(header)
    version = bits2int(header[:3])
    type_id = bits2int(header[3:])
    return version, type_id

def parse_content(type_id: int, buffer: deque):
    ...
