from __future__ import annotations
from dataclasses import dataclass, field

from cuboid import Cuboid, Bound

FILENAME = 'test_input.txt'

@dataclass
class Step:
    text: str = field(repr=False)
    on: bool
    cuboid: Cuboid

    @classmethod
    def from_string(cls, s: str) -> Step:
        on_str, slice_str = s.split(' ')
        on = True if on_str == 'on' else False
        x_str, y_str, z_str = slice_str.split(',')
        # Nothing to see here, just a normal, concise list comprehension.
        x, y, z = [
            tuple(int(a) for a in s.split('=')[1].split('..'))
            for s in slice_str.split(',')
        ]
        x, y, z = (Bound(*a) for a in (x, y, z))
        return cls(text=s, on=on, cuboid=Cuboid(x, y, z))

with open(FILENAME, 'rt') as f:
    steps = [Step.from_string(l.strip()) for l in f.readlines()]
for s in steps:
    print(s)
c = Cuboid(Bound(10, 12), Bound(10,12), Bound(10,12))
print(c.volume)
lksjdflksdjf

cubes = set()
for step in steps:
    new_cubes = set(step.cubes)
    if step.on:
        cubes = cubes.union(new_cubes)
    else:
        cubes = cubes.difference(new_cubes)
    print(len(cubes))
