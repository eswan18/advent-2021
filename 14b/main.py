import sys
from datetime import datetime
from functools import lru_cache, reduce
from collections import Counter
from itertools import product

sys.setrecursionlimit(10000)


with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]
template = lines[0]
rules = {
    tuple(l.split(' -> ')[0]): l.split(' -> ')[1]
    for l in lines[2:]
}

@lru_cache(maxsize=10_000_000)
def expand(seq: str, steps: int = 1) -> str:
    if len(seq) < 2:
        raise ValueError
    elif len(seq) == 2:
        if steps == 1:
            a, b = seq
            result = a + rules.get((a,b), '') + b
        elif steps % 2 == 1:
            result = expand(expand(seq, steps-1))
        else:
            result = expand(expand(seq, steps=steps/2), steps=steps/2)
    else:
        # The hard part.
        first_pair, remainder = seq[:2], seq[1:]
        first_pair_expanded = expand(first_pair, steps=steps)
        remainder_expanded = expand(remainder, steps=steps)
        result = first_pair_expanded[:-1] + remainder_expanded
    return result

# for every possible letter combo, compute 20 generations
letters = set(l for tup in rules.keys() for l in tup)
combos = ((x, y) for x, y in product(letters, letters))
rule20s = {
    combo: expand(''.join(combo), 20)[:-1]
    for combo in combos
}
rule20counts = {
    key: Counter(value)
    for key, value in rule20s.items()
}

temp20 = ''.join(rule20s[pair] for pair in zip(template[:-1], template[1:])) + template[-1]

print('Done with computing 20 iterations')
c = 0
def loud_add(x, y):
    global c
    c += 1
    return x + y
counter = reduce(loud_add, (rule20counts[pair] for pair in zip(temp20[:-1], temp20[1:])))
counter += Counter(temp20[-1])

freqs = counter.values()
result = max(freqs) - min(freqs)
print(f'{result=}')
