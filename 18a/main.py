from node import LeafNode, BranchNode


def parse_number(line) -> BranchNode:
    assert line[0] == '['
    assert line[-1] == ']'
    line = line[1:-1]
    bracket_count = 0
    for i, c in enumerate(line):
        if c == '[':
            bracket_count += 1
        elif c == ']':
            bracket_count -= 1
        elif c == ',' and bracket_count == 0:
            left = line[:i]
            right = line[i+1:]
            if '[' in left:
                left = parse_number(left)
            else:
                left = LeafNode(parent=None, value=int(left))
            if '[' in right:
                right = parse_number(right)
            else:
                right = LeafNode(parent=None, value=int(right))
            node = BranchNode(parent=None, left=left, right=right)
            node.left.parent = node
            node.right.parent = node
            return node


with open('test_input.txt', 'rt') as f:
    numbers = [parse_number(l.strip()) for l in f.readlines()]

for n in numbers:
    print(n)
