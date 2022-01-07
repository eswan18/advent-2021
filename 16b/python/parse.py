from dataclasses import dataclass
from collections import deque

from bits import bits2int

@dataclass
class Literal:
    version: int
    value: int

    def eval(self) -> int:
        return self.value

@dataclass
class Operator:
    version: int
    type_id: int
    subpackets: list[Literal]

    def eval(self) -> int:
        if self.type_id == 0:
            return sum(s.eval() for s in self.subpackets)
        elif self.type_id == 1:
            p = 1
            for s in self.subpackets:
                p *= s.eval()
            return p
        elif self.type_id == 2:
            return min(s.eval() for s in self.subpackets)
        elif self.type_id == 3:
            return max(s.eval() for s in self.subpackets)
        elif self.type_id == 5:
            val_a = self.subpackets[0].eval()
            val_b = self.subpackets[1].eval()
            return int(val_a > val_b)
        elif self.type_id == 6:
            val_a = self.subpackets[0].eval()
            val_b = self.subpackets[1].eval()
            return int(val_a < val_b)
        elif self.type_id == 7:
            val_a = self.subpackets[0].eval()
            val_b = self.subpackets[1].eval()
            return int(val_a == val_b)


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

def parse_literal(version: int, buffer: deque) -> Literal:
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

def parse_operator(version: int, type_id: int, buffer: deque) -> Operator:
    length_type_id, *_ = shift(buffer, 1)
    if length_type_id == '0':
        print('Parsing op with bits')
        bit_length = int(''.join(shift(buffer, 15)), base=2)
        print(bit_length)
        new_bits = shift(buffer, bit_length)
        new_buffer = deque(new_bits)
        subpax = []
        while '1' in new_buffer:
            subpax.append(parse(new_buffer))
        return Operator(version, type_id, subpax)
        print(f'Parsed {result=}')
    elif length_type_id == '1':
        print('Parsing op with subpax')
        n_subpax = int(''.join(shift(buffer, 11)), base=2)
        subpax = []
        for _ in range(n_subpax):
            subpax.append(parse(buffer))
        return Operator(version, type_id, subpax)
    else:
        raise ValueError

def parse_packet(version: int, type_id: int, buffer: deque):
    # Literal
    if type_id == 4:
        lit = parse_literal(version, buffer)
        return lit
    # Operator 
    else:
        op = parse_operator(version, type_id, buffer)
        return op

def parse(buffer: deque) -> list['Packet']:
    print(f'Parsing {"".join(buffer)}')
    header = shift(buffer, 6)
    version, type_id = parse_header(header)
    print(f'{(version, type_id)=}')
    packet = parse_packet(version, type_id, buffer)
    return packet
