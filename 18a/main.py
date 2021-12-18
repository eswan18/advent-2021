from typing import Union


class Number:
    def __init__(
        self,
        left: Union['Number', int],
        right: Union['Number', int],
    ):
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'[{self.left!r}, {self.right!r}]'


def parse_number(line) -> Number:
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
                left = int(left)
            if '[' in right:
                right = parse_number(right)
            else:
                right = int(right)
            return Number(left, right)


with open('test_input.txt', 'rt') as f:
    numbers = [parse_number(l.strip()) for l in f.readlines()]

for n in numbers:
    print(repr(n))
