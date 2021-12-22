from __future__ import annotations
from dataclasses import dataclass

from cuboid import Cuboid, OutOfBoundsError, DEFAULT_CUBOID_RANGES 

C_Range = tuple[int, int]

FILENAME = 'input.txt'
cuboid = Cuboid()

@dataclass
class Step:
    text: str
    on: bool
    x: slice[int, int, None]
    y: slice[int, int, None]
    z: slice[int, int, None]

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
        x, y, z = (slice(*a) for a in (x, y, z))
        return cls(text=s, on=on, x=x, y=y, z=z)

    @property
    def cuboid_slice(self) -> tuple[slice, slice, slice]:
        return (self.x, self.y, self.z)

    def in_bounds(
        self,
        bounds: Tuple[C_Range, C_Range, C_Range] = DEFAULT_CUBOID_RANGES,
    ) -> bool:
        x_bound, y_bound, z_bound = bounds
        if self.x.start < x_bound[0] or self.x.stop > x_bound[1]:
            return False
        if self.y.start < y_bound[0] or self.y.stop > y_bound[1]:
            return False
        if self.z.start < z_bound[0] or self.z.stop > z_bound[1]:
            return False
        return True

    @property
    def cubes(self) -> Iterator[tuple[int, int, int]]:
        for x in range(self.x.start, self.x.stop+1):
            for y in range(self.y.start, self.y.stop+1):
                for z in range(self.z.start, self.z.stop+1):
                    yield (x, y, z)

with open(FILENAME, 'rt') as f:
    steps = [Step.from_string(l.strip()) for l in f.readlines()]

cubes = set()
for step in steps:
    if step.in_bounds():
        #cuboid[step.cuboid_slice] = step.on
        new_cubes = set(step.cubes)
        if step.on:
            cubes = cubes.union(new_cubes)
        else:
            cubes = cubes.difference(new_cubes)
    #print(cuboid.on_count)
    print(len(cubes))
