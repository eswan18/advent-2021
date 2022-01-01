from collections import Counter

AFTER_0_VAL = 6
NEW_VAL = 8
DAYS = 256

with open('input.txt', 'rt') as f:
    fish = [int(x) for x in f.readline().split(',')]

fish = Counter(fish)

fish_days = [0 for _ in range(NEW_VAL + 1)]
for days in fish.keys():
    fish_days[days] = fish[days]

for d in range(DAYS):
    next_fish = [0 for _ in range(NEW_VAL + 1)]
    for i in range(NEW_VAL + 1):
        if i == NEW_VAL:
            next_fish[i] = fish_days[0]
        else:
            next_fish[i] = fish_days[i+1]
        if i == AFTER_0_VAL:
            next_fish[i] += fish_days[0]
    fish_days = next_fish

result = sum(fish_days)
print(result)
