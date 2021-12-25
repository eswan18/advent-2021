from __future__ import annotations

from step import Step
from cuboid import Cuboid

FILENAME = 'input.txt'


with open(FILENAME, 'rt') as f:
    steps = [Step.from_string(l.strip()) for l in f.readlines()]

# Start by throwing out any steps with cuboids that are fully covered by steps after
# them.
layers: list[Cuboid] = []

for s in reversed(steps):
    cuboid = s.cuboid
    print(f'Looking at cuboid {cuboid}')
    if any(l.contains(cuboid) for l in layers):
        # Skip cuboids that are fully contained in a previous layer.
        continue

    volume = cuboid.uncovered_volume(layers=layers)
    cuboid.dynamic_data['new_volume'] = volume
    cuboid.dynamic_data['on'] = s.on
    layers.append(cuboid)

# Do the rest of our work with only the steps worth keeping.
total_on = sum(c.dynamic_data['new_volume'] for c in layers if c.dynamic_data['on'])
print(total_on)
