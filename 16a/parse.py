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

def parse_packet(type_id: int, buffer: deque):
    # Literal
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
    # Operator 
    else:
        length_type_id, *_ = shift(buffer, 1)
        if length_type_id == '0':
            total_length = int(''.join(shift(buffer, 15)), base=2)
            return {'L': total_length}
        elif length_type_id == '1':
            n_subpackets = int(''.join(shift(buffer, 11)), base=2)
            return {'S': n_subpackets}
        else:
            raise ValueError

def parse(buffer: deque):
    while True:
        header = shift(buffer, 6)
        version, type_id = parse_header(header)
        print(f'{(version, type_id)=}')
        print(f'{buffer=}')
        x = parse_packet(type_id, buffer)
        print(f'{x=}')
        print(f'{buffer=}')
        break
    assert len(buffer) == 0
