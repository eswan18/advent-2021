from datetime import datetime
from functools import lru_cache
from collections import Counter
from itertools import repeat, chain

with open('test_input.txt', 'rt') as f:
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
        else:
            result = expand(expand(seq, steps-1))
    else:
        # The hard part.
        first_pair, remainder = seq[:2], seq[1:]
        first_pair_expanded = expand(first_pair, steps=steps)
        remainder_expanded = expand(remainder, steps=steps)
        result = first_pair_expanded[:-1] + remainder_expanded
    return result

N = 10
final_template = expand(template, N)
print(expand.cache_info())

counter = Counter(final_template)
freqs = counter.values()
result = max(freqs) - min(freqs)
print(result)
