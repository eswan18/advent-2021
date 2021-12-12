from functools import cache

with open('input.txt', 'rt') as f:
    crabs = [int(x) for x in f.readline().split(',')]

@cache
def cost(distance):
    return sum(x for x in range(distance+1))

costs = [sum(cost(abs(c - p)) for c in crabs) for p in range(max(crabs))]
best_fuel = min(costs)
best_pos = costs.index(best_fuel)

print(best_fuel, best_pos)
