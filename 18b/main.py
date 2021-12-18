from itertools import product
from node import BranchNode

with open('input.txt', 'rt') as f:
    numbers = [BranchNode.from_line(l.strip()) for l in f.readlines()]

high_mag = 0
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        s = (numbers[i] + numbers[j]).magnitude()
        if s > high_mag:
            high_mag = s
        s = (numbers[j] + numbers[i]).magnitude()
        if s > high_mag:
            high_mag = s

print(high_mag)
