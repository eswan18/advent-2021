from dataclasses import dataclass
from collections import deque

from bits import bits2int

@dataclass
class Literal:
    value: int

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
    if type_id == 4:
        number_bits = []
        consumed = 6
        while True:
            continuation, *number = shift(buffer, 5)
            number_bits.extend(number)
            consumed += 5
            if continuation == '0':
                overstep = consumed % 4
                if overstep:
                    n_ignored = 4 - overstep
                    shift(buffer, n_ignored)
                break
        number = int(''.join(number_bits), base=2)
        return Literal(number)
            
    #elif type_id == 6:
    else:
        raise ValueError

