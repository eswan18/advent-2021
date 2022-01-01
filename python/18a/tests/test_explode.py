import sys
sys.path.append('.')

import copy

from node import BranchNode

in_out = [
    ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
    ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
    ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
    ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
    ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
]

def test_explode():
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

test_explode()
