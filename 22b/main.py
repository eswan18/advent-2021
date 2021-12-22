from __future__ import annotations
from dataclasses import dataclass, field

from cuboid import Cuboid, Bound

FILENAME = 'test_input.txt'


@dataclass(frozen=True)
class Step:
    text: str = field(repr=False)
    on: bool
    cuboid: Cuboid

    @classmethod
    def from_string(cls, s: str) -> Step:
        on_str, cuboid_str = s.split(' ')
        on = True if on_str == 'on' else False
        cuboid = Cuboid.from_string(cuboid_str)
        return cls(text=s, on=on, cuboid=cuboid)


with open(FILENAME, 'rt') as f:
    steps = [Step.from_string(l.strip()) for l in f.readlines()]

# Start by throwing out any cuboids that are fully covered by cuboids after them.
cuboids = []
for s in reversed(steps):
    if any(c.contains(s.cuboid) for c in cuboids):
        container = [c for c in cuboids if c.contains(s.cuboid)]
        c = container[0]
        print(f'{s.cuboid}\nis contained by\n{c}\n')
    else:
        cuboids.append(s.cuboid)

print(len(cuboids))
