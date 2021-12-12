from collections import Counter
from dataclasses import dataclass


with open('input.txt', 'rt') as f:
    displays = [line.split('|') for line in f.readlines()]


@dataclass
class Digit:
    num: int
    segments: list[str]

    def __post_init__(self):
        self.segments = tuple(self.segments)
        self.n_segs = len(self.segments)


digit_segments = [
    Digit(0, 'abcefg'),
    Digit(1, 'cf'),
    Digit(2, 'acdeg'),
    Digit(3, 'acdfg'),
    Digit(4, 'bcdf'),
    Digit(5, 'abdfg'),
    Digit(6, 'abdefg'),
    Digit(7, 'acf'),
    Digit(8, 'abcdefg'),
    Digit(9, 'abcdfg'),
]

len_digits = {
    n_segs: [d for d in digit_segments if d.n_segs == n_segs]
    for n_segs in range(8)
}

uniq_len_digits = {
    n_segs: digs[0].num
    for (n_segs, digs) in len_digits.items()
    if len(digs) == 1
}


outputs = [d[1].split() for d in displays]

counts = Counter(len(o) for output in outputs for o in output)

uniq_dig_occurences = sum(counts[l] for l in uniq_len_digits.keys())
print(uniq_dig_occurences)
