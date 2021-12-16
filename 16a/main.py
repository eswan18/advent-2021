from collections import deque

from bits import hex2bits
from parse import shift, parse

#with open('test_input_literal.txt', 'rt') as f:
with open('test_input_op_2sub.txt', 'rt') as f:
    content = hex2bits(f.read().strip())
    buffer = deque(content)
print(''.join(list(buffer)))

parse(buffer)
