AFTER_0_VAL = 6
NEW_VAL = 8
DAYS = 80

with open('input.txt', 'rt') as f:
    fish = [int(x) for x in f.readline().split(',')]

for d in range(DAYS):
    new_fish = 0 
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = AFTER_0_VAL
            new_fish += 1
        else:
            fish[i] -= 1
    new_fish = [NEW_VAL for _ in range(new_fish)]
    fish.extend(new_fish)

result = len(fish)
print(result)
