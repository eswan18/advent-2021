from collections import deque

from bits import hex2bits
from parse import shift, parse, Operator, Literal

with open('input.txt', 'rt') as f:
    content = hex2bits(f.read().strip())
    buffer = deque(content)

result = parse(buffer)

def sum_versions(node) -> int:
    if isinstance(node, Literal):
        return node.version
    else:
        return node.version + sum(sum_versions(p) for p in node.subpackets)

r_sum = sum_versions(result)

print(r_sum)
