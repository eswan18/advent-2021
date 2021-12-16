from collections import deque

from bits import hex2bits
from parse import shift, parse, Operator, Literal

#with open('test_input_literal.txt', 'rt') as f:
#with open('test_input_op_3sub.txt', 'rt') as f:
with open('test_input.txt', 'rt') as f:
    content = hex2bits(f.read().strip())
    buffer = deque(content)
print(''.join(list(buffer)))

result = parse(buffer)

# Assume it's an operator
def sum_versions(node) -> int:
    if isinstance(node, Literal):
        return node.version
    else:
        return node.version + sum(sum_versions(p) for p in node.subpackets)

print(sum_versions(result))
