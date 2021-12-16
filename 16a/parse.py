from dataclasses import dataclass
from collections import deque

from bits import bits2int

@dataclass
class Literal:
    version: int
    value: int

@dataclass
class Operator:
    version: int
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

def parse_literal(version: int, buffer: deque, subpacket: bool) -> Literal:
    number_bits = []
    consumed = 6
    while True:
        continuation, *number = shift(buffer, 5)
        number_bits.extend(number)
        consumed += 5
        if continuation == '0':
            break
    number = int(''.join(number_bits), base=2)
    result = Literal(version, number)
    print(f'Parsed {result=}')
    return result

def parse_packet(version: int, type_id: int, buffer: deque, subpacket: bool = False):
    # Literal
    if type_id == 4:
        lit = parse_literal(version, buffer, subpacket=subpacket)
        return lit
    # Operator 
    else:
        length_type_id, *_ = shift(buffer, 1)
        if length_type_id == '0':
            print('Parsing op with bits')
            bit_length = int(''.join(shift(buffer, 15)), base=2)
            new_bits = shift(buffer, bit_length)
            new_buffer = deque(new_bits)
            subpax = []
            while '1' in new_buffer:
                subpax.append(parse(new_buffer, subpacket=True))
            return Operator(version, subpax)
            print(f'Parsed {result=}')
        elif length_type_id == '1':
            print('Parsing op with subpax')
            n_subpackets = int(''.join(shift(buffer, 11)), base=2)
            return {'S': n_subpackets}
        else:
            raise ValueError

def parse(buffer: deque, subpacket: bool = False) -> list['Packet']:
    print(f'Parsing {"".join(buffer)}')
    header = shift(buffer, 6)
    version, type_id = parse_header(header)
    print(f'{(version, type_id)=}')
    packet = parse_packet(version, type_id, buffer, subpacket)
    return packet
