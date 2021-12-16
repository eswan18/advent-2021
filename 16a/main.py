from collections import deque

from bits import hex2bits
from parse import shift, parse, Operator, Literal

with open('input.txt', 'rt') as f:
    content = hex2bits(f.read().strip())
    buffer = deque(content)

results = []
while '1' in buffer:
    p = parse(buffer)
    results.append(p)
    print(f'found {p=}')
    # If you consumed a number of bytes that isn't divisible by four, consume a couple more.
    extra_bits = len(buffer) % 4
    if extra_bits:
        shift(buffer, extra_bits)

# Assume it's an operator
def sum_versions(node) -> int:
    if isinstance(node, Literal):
        return node.version
    else:
        return node.version + sum(sum_versions(p) for p in node.subpackets)

r_sum = 0
for r in results:
    r_sum += sum_versions(r)

print(r_sum)
