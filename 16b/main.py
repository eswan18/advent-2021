from collections import deque

from bits import hex2bits
from parse import shift, parse, Operator, Literal

with open('input.txt', 'rt') as f:
    content = hex2bits(f.read().strip())
    buffer = deque(content)

result = parse(buffer)

print(result.eval())
