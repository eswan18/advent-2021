from dataclasses import dataclass
from collections import deque

from bits import bits2int

@dataclass
class Literal:
    value: int

@dataclass
class Operator:
    subpackets: list[Literal]

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
        result = Literal(number)
        print(f'Parsed {result=}')
        return result
    # Operator 
    else:
        length_type_id, *_ = shift(buffer, 1)
        if length_type_id == '0':
            bit_length = int(''.join(shift(buffer, 15)), base=2)
            new_bits = shift(buffer, bit_length)
            new_buffer = deque(new_bits)
            subpackets = parse(new_buffer)
            return Operator(subpackets=subpackets)
            print(f'Parsed {result=}')
        elif length_type_id == '1':
            n_subpackets = int(''.join(shift(buffer, 11)), base=2)
            return {'S': n_subpackets}
        else:
            raise ValueError

def parse(buffer: deque) -> list['Packet']:
    pax = []
    while len(buffer) > 0:
        print(f'Parsing {"".join(buffer)}')
        header = shift(buffer, 6)
        version, type_id = parse_header(header)
        print(f'{(version, type_id)=}')
        pax.append(parse_packet(type_id, buffer))
    assert len(buffer) == 0
    return nodes
