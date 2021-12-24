from __future__ import annotations
from dataclasses import dataclass, field
from itertools import combinations

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

# Start by throwing out any steps with cuboids that are fully covered by steps after
# them.
layers: list[Cuboid] = []
on = 0
off = 0

for s in reversed(steps[:4]):
    cuboid = s.cuboid
    print(f'Looking at cuboid {cuboid}')
    if any(l.contains(cuboid) for l in layers):
        # Skip cuboids that are fully contained in a previous layer.
        continue

    # Find the spaces where this cuboid overlaps with other, already-seen layers -- that
    # volume shouldn't be included in the volume it covers.
    overlapping_cuboids = [
        l for l in (l.common(cuboid) for l in layers) if l is not None
    ]
    naive_overlapping_volume = sum(oc.volume for oc in overlapping_cuboids)
    # Overlapping areas may overlap with each other, causing the overlap to be double-
    # (or triple-, or ...) counted.
    redundant_overlap_volume = sum(
        a.overlap(b) for a, b in combinations(overlapping_cuboids, 2)
    )
    overlapping_volume = naive_overlapping_volume - redundant_overlap_volume
    if overlapping_cuboids:
        print('It overlaps with cuboids:')
        for c in overlapping_cuboids:
            print(f'- {c}')
        print(f'Naively, its overlapping volume is {naive_overlapping_volume}')
        print(f'But after adjustment, its overlapping volume is {overlapping_volume}')
    
    # Figure out how much volume this new cuboid covers.
    covered_volume = cuboid.volume - overlapping_volume
    print(
        f'The *new* volume covered by this cuboid is {covered_volume}, which is {s.on}'
    )

    cuboid.dynamic_data['covered_volume'] = covered_volume
    cuboid.dynamic_data['on'] = s.on
    layers.append(cuboid)

# Do the rest of our work with only the steps worth keeping.
total_on = sum(c.dynamic_data['covered_volume'] for c in layers if c.dynamic_data['on'])
print(total_on)
