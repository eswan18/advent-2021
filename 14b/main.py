from collections import Counter
from itertools import repeat, chain

SENTINEL = '%'

with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]
template = lines[0]
rules = {
    tuple(l.split(' -> ')[0]): l.split(' -> ')[1]
    for l in lines[2:]
}

def main(template):
    for _ in range(5):
        template = [x for pair in zip(template, chain(repeat(SENTINEL, len(template)-1))) for x in pair] + [template[-1]]
        for i, pair in enumerate(zip(template[:-1:2], template[2::2])):
            x = rules.get(pair, SENTINEL)
            template[2*i+1] = x
        if SENTINEL in template:
            template.remove(SENTINEL)
    return template

template = main(template)

counter = Counter(template)
freqs = counter.values()
result = max(freqs) - min(freqs)

print(result)
