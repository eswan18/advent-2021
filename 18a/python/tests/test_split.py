import sys
sys.path.append('.')

import copy

from node import BranchNode

in_out = [
    ('[[[[10,8],1],2],3]', '[[[[[5,5],8],1],2],3]'),
    ('[[6,[4,[3,13]]],1]', '[[6,[4,[3,[6,7]]]],1]'),
]

def test_split():
    for x, y in in_out:
        b = BranchNode.from_line(x)
        old = copy.deepcopy(b)
        b.reduce()
        try:
            assert str(b) == y
        except:
            print(f'FAILED: {old} -> {b}')
            print(f'But should be {y}')
            raise
        else:
            print(f'PASSED: {old} -> {b}')

test_split()
