from datetime import datetime
from functools import lru_cache
from collections import Counter
from itertools import repeat, chain

with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]
template = lines[0]
rules = {
    tuple(l.split(' -> ')[0]): l.split(' -> ')[1]
    for l in lines[2:]
}

@lru_cache(maxsize=10_000_000)
def expand(seq: str, steps: int = 1) -> str:
    if steps == 1:
        if len(seq) < 2:
            raise ValueError
        elif len(seq) == 2:
            a, b = seq
            return a + rules.get((a,b), '') + b
        else:
            new_seq = ''
            for pair in zip(seq[:-1], seq[1:]):
                pair_str = ''.join(pair)
                new_seq += expand(pair_str)[:2]
            new_seq += seq[-1]
            return new_seq
    else:
        return expand(expand(seq, steps-1))

N = 10
final_template = expand(template, N)

counter = Counter(final_template)
freqs = counter.values()
result = max(freqs) - min(freqs)
print(result)
