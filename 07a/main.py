with open('input.txt', 'rt') as f:
    crabs = [int(x) for x in f.readline().split(',')]

costs = [sum(abs(c - p) for c in crabs) for p in range(max(crabs))]
best_fuel = min(costs)
best_pos = costs.index(best_fuel)

print(best_fuel, best_pos)
