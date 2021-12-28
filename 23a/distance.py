from functools import cache
from collections import defaultdict

_movements = defaultdict(set)
with open('mapping.txt', 'rt') as f:
    lines = (l.strip() for l in f.readlines())
for line in lines:
    node_a, node_b = line.split(',')
    _movements[node_a].add(node_b)
    _movements[node_b].add(node_a)

movements = dict(_movements)

@cache
def distance(_from: str, _to: str) -> int:
    reachable = movements[_from]
    if _to in reachable:
        return 1
    else:
        for i in range(2, 11):
            next_reachable = set()
            for n in reachable:
                print(f'Now can reach {n}')
                next_reachable = next_reachable.union(movements[n])
            reachable = next_reachable
            if _to in reachable:
                return i
