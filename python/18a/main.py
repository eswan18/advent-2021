from functools import reduce
from node import BranchNode

with open('input.txt', 'rt') as f:
    numbers = [BranchNode.from_line(l.strip()) for l in f.readlines()]

result = reduce(lambda x, y: x + y, numbers)
result.reduce()
print(result)
print(result.magnitude())
