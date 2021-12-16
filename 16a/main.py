from collections import deque

from bits import hex2bits
from parse import shift, parse_header, parse_content

with open('test_input_literal.txt', 'rt') as f:
    content = hex2bits(f.read().strip())
    buffer = deque(content)

while True:
    header = shift(buffer, 6)
    version, type_id = parse_header(header)
    print(f'{buffer=}')
    literal = parse_content(type_id, buffer)
    print(f'{literal=}')
    print(f'{buffer=}')
    break

assert len(buffer) == 0
