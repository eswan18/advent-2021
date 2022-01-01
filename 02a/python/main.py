from collections import defaultdict


with open('input.txt', 'rt') as f:
    lines = (line.strip() for line in f.readlines())

d = defaultdict(lambda: 0)

def parse(line):
    direction, amt = line.split()
    amt = int(amt)
    d[direction] += amt

# Force execution of the generator.
[_ for _ in map(parse, lines)]

result = (d['down'] - d['up']) * (d['forward'] - d['back'])
print(result)
