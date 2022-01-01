from itertools import cycle, combinations_with_replacement
from collections import namedtuple, Counter
from functools import cache
from typing import Iterator

with open('input.txt', 'rt') as f:
    p1_str, p2_str = [l.strip() for l in f.readlines()]


roll_freq = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

Universe = namedtuple('Universe', 'p1_pos,p2_pos,p1_score,p2_score,next_up')

start = Universe(
    p1_pos=int(p1_str.split(': ')[1]),
    p2_pos=int(p2_str.split(': ')[1]),
    p1_score=0,
    p2_score=0,
    next_up='p1'
)


@cache
def advance_by_roll(u: Universe, roll: int) -> Universe:
    player = u.next_up
    if player == 'p1':
        new_pos = u.p1_pos + roll
        while new_pos > 10:
            new_pos -= 10
        new_score = u.p1_score + new_pos
        return Universe(
            p1_pos=new_pos,
            p2_pos=u.p2_pos,
            p1_score=new_score,
            p2_score=u.p2_score,
            next_up='p2',
        )
    else:  # player == 'p2':
        new_pos = u.p2_pos + roll
        while new_pos > 10:
            new_pos -= 10
        new_score = u.p2_score + new_pos
        return Universe(
            p1_pos=u.p1_pos,
            p2_pos=new_pos,
            p1_score=u.p1_score,
            p2_score=new_score,
            next_up='p1',
        )

@cache
def get_winners(universe) -> Counter:
    if universe.p1_score >= 21:
        return Counter({'p1': 1})
    elif universe.p2_score >= 21:
        return Counter({'p2': 1})
    results = Counter()
    for roll, freq in roll_freq.items():
        new_universe = advance_by_roll(universe, roll)
        result = get_winners(new_universe)
        result = multiply(result, freq)
        results += result
    return results

def multiply(c: Counter, m: int):
    c_new = Counter()
    for _ in range(m):
        c_new += c
    return c_new

print(get_winners(start))
