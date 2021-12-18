from node import LeafNode, BranchNode

with open('test_input.txt', 'rt') as f:
    numbers = [BranchNode.from_line(l.strip()) for l in f.readlines()]

for n in numbers:
    print(n)
