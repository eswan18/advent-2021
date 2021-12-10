from collections import defaultdict


with open('input.txt', 'rt') as f:
    lines = (line.strip() for line in f.readlines())

aim = depth = horizontal = 0

def parse(line):
    global aim, depth, horizontal
    direction, amt = line.split()
    amt = int(amt)
    if direction == 'down':
        aim += amt
    elif direction == 'up':
        aim -= amt
    elif direction == 'forward':
        horizontal += amt
        depth += (aim * amt)
    else:
        raise ValueError

# Force execution of the generator.
[_ for _ in map(parse, lines)]

result = depth * horizontal
print(result)
