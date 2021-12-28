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
nodes = set(movements.keys())

@cache
def distance(_from: str, _to: str) -> int:
    if _to == _from:
        return 0

    reachable = movements[_from]
    if _to in reachable:
        return 1
    else:
        for i in range(2, 11):
            next_reachable = set()
            for n in reachable:
                next_reachable = next_reachable.union(movements[n])
            reachable = next_reachable
            if _to in reachable:
                return i
