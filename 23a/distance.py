from __future__ import annotations

from functools import cache, reduce
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
rooms = {'l': 'A', 'p': 'A', 'm': 'B', 'q': 'B', 'n': 'C', 'r': 'C', 'o': 'D', 's': 'D'}

@cache
def shortest_path(_from: str, _to: str) -> tuple[str]:
    if _to == _from:
        return 0
    paths = [(_from,)]
    for i in range(1, 11):
        next_paths = []
        for path in paths:
            reachable_nodes = movements[path[-1]]
            if _to in reachable_nodes:
                return path + (_to,)
            next_paths.extend([path + (n,) for n in reachable_nodes])
        paths = next_paths

def distance(_from: str, _to: str) -> int:
    return len(shortest_path(_from, _to)) - 1

@cache
def n_away(node: str, n: int) -> set[str]:
    '''Get nodes n moves away from a given node.'''
    for i in range(11):
        if i == 0:
            reachable = {node}
        else:
            newly_reachable = reduce(set.union, (movements[n] for n in reachable))
            # Remove nodes that were already reachable.
            newly_reachable = newly_reachable - reachable
            # Update the reachable list
            reachable = reachable.union(newly_reachable)
        if n == i:
            return newly_reachable

def is_legal(_from: str, _to: str, color: str, locations: dict[str, Optional[str]]) -> bool:
    # If the amphipod is moving to a room where it doesn't belong.
    if _to in rooms:
        room = rooms[_to]
        if color != room and rooms != rooms[_from]:
            return False
    # If there's an amphipod in the way.
    path = shortest_path(_from, _to)
    for node in path:
        if locations[node] is not None:
            return False
    return True


