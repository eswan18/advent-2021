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

def num_from_segs(segs):
    segs = tuple(sorted(segs))
    num, *_ = [d.num for d in digit_segments if d.segments == segs]
    return num

len_digits = {
    n_segs: [d for d in digit_segments if d.n_segs == n_segs]
    for n_segs in range(8)
}

uniq_len_digits = {
    n_segs: digs[0].num
    for (n_segs, digs) in len_digits.items()
    if len(digs) == 1
}

running_sum = 0
for line in displays:
    signals, output = [x.split() for x in line]
    # Find the 1
    one, *_ = [s for s in signals if len(s) == 2]
    # Find the 7
    seven, *_ = [s for s in signals if len(s) == 3]
    # Whatever line is in 7 but not 1 is the 'A' segment
    A_seg, *_ = set(seven) - set(one)
    mapping = {A_seg: 'a'}
    # We don't know about CF yet
    CF_segs = tuple(one)

    # Whatever number has 6 segs but is missing one of CF is 6
    six, *_ = [s for s in signals if not all(cf in s for cf in CF_segs) and len(s) == 6]
    # The segment 6 is missing should be C
    C_seg, *_ = set('abcdefg') - set(six)
    # And we can figure out F by the other value of CF
    F_seg = CF_segs[0] if CF_segs[1] == C_seg else CF_segs[1]
    mapping[C_seg] = 'c'
    mapping[F_seg] = 'f'

    # The two remaining length-6 digits are 0 and 9
    zero_and_nine = [s for s in signals if len(s) == 6 and s != six]
    # The D and E segments are the ones they're missing.
    DE_segs = set('abcdefg') - set(zero_and_nine[0]).intersection(zero_and_nine[1])

    # The length-4 digit is 4
    four, *_ = [s for s in signals if len(s) == 4]
    # The segments in 4 but not 1 are B & D
    BD_segs = set(four) - set(one)

    # D is the segment in both BD and DE
    D_seg, *_ = BD_segs.intersection(DE_segs)
    mapping[D_seg] = 'd'
    # And we can use it to figure out B and E
    B_seg, *_ = BD_segs - set(D_seg)
    E_seg, *_ = DE_segs - set(D_seg)
    mapping[B_seg] = 'b'
    mapping[E_seg] = 'e'

    # We're missing just one letter: G
    G_seg, *_ = set('abcdefg') - mapping.keys()
    mapping[G_seg] = 'g'

    # Translate
    table = {ord(key): ord(val) for (key, val) in mapping.items()}
    output = [o.translate(table) for o in output]
    output_nums = [str(num_from_segs(o)) for o in output]

    display_num = int(''.join(output_nums))
    running_sum += display_num

print(running_sum)
