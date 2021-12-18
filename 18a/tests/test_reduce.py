import sys
sys.path.append('.')

import copy

from node import BranchNode

in_out = [
    ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'),
    (
        '[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]',
        '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'
    ),
    (
        '[[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]],[[[[4,2],2],6],[8,7]]]',
        '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
    ),
]

def test_reduce():
    for x, y in in_out:
        b = BranchNode.from_line(x)
        old = copy.deepcopy(b)
        b.fully_reduce()
        try:
            assert str(b) == y
        except:
            print(f'FAILED: {old} -> {b}')
            print(f'But should be {y}')
            raise
        else:
            print(f'PASSED: {old} -> {b}')

test_reduce()
