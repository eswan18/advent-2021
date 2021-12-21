from itertools import cycle
from typing import Iterator

with open('input.txt', 'rt') as f:
    p1_str, p2_str = [l.strip() for l in f.readlines()]

pos = {
    'p1': int(p1_str.split(': ')[1]),
    'p2': int(p2_str.split(': ')[1])
}
scores = {'p1': 0, 'p2': 0}

total_n_rolls = 0
def roll_dice() -> Iterator[int]:
    global total_n_rolls 
    dice = 1
    while True:
        if dice == 101:
            dice = 1
        total_n_rolls += 1
        yield dice
        dice += 1


dice = roll_dice()
turns = 0
for player in cycle(('p1', 'p2')):
    roll = sum(next(dice) for _ in range(3))
    pos[player] += roll
    while pos[player] > 10:
        pos[player] = pos[player] - 10
    scores[player] += pos[player]
    if scores[player] >= 1000:
        other_player = 'p1' if player == 'p2' else 'p2'
        loser_score = scores[other_player]
        break
print(f'{loser_score=}')
print(f'{total_n_rolls=}')
result = loser_score * total_n_rolls
print(f'{result=}')
