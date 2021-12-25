import sys
sys.path.append('.')

from step import Step

lines = '''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10'''

steps = [Step.from_string(l.strip()) for l in lines.split('\n')]

layers = []

for s in reversed(steps):
    cuboid = s.cuboid
    if any(l.contains(cuboid) for l in layers):
        # Skip cuboids that are fully contained in a previous layer.
        continue

    volume = cuboid.uncovered_volume(layers=layers)
    cuboid.dynamic_data['covered_volume'] = volume
    cuboid.dynamic_data['on'] = s.on
    layers.append(cuboid)

total_on = sum(c.dynamic_data['covered_volume'] for c in layers if c.dynamic_data['on'])
assert total_on == 39


lines = '''on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19'''

steps = [Step.from_string(l.strip()) for l in lines.split('\n')]

layers = []

for s in steps:
    cuboid = s.cuboid
    print(f'Looking at cuboid {cuboid}')
    if any(l.contains(cuboid) for l in layers):
        # Skip cuboids that are fully contained in a previous layer.
        continue

    volume = cuboid.uncovered_volume(layers=layers)
    print(f'Covered volume: {volume}')
    
    cuboid.dynamic_data['covered_volume'] = volume
    cuboid.dynamic_data['on'] = s.on
    layers.append(cuboid)
    total_on = sum(c.dynamic_data['covered_volume'] for c in layers if c.dynamic_data['on'])
    print(f'Total on: {total_on}')

total_on = sum(c.dynamic_data['covered_volume'] for c in layers if c.dynamic_data['on'])
print(total_on)
assert total_on == 494804
