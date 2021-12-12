from collections import Counter


with open('input.txt', 'rt') as f:
    raw = [l.strip().split('-') for l in f.readlines()]
    conns = {}
    for a, b in raw:
        if a in conns:
            conns[a].append(b)
        else:
            conns[a] = [b]
        if b in conns:
            conns[b].append(a)
        else:
            conns[b] = [a]

path = ['start']
cant_visit = ['start']

def is_valid(path: list[str]):
    relkeys = [p for p in path if p.islower() and p != 'start']
    counter = Counter(relkeys)
    okay = True
    for v in counter.values():
        if v >= 2:
            if okay:
                okay = False
            else:
                return False
    return True

viable = []
def paths(path: list[str], cant_visit: list[str], has_double: bool) -> list[list[str]]:
    if path[-1] == 'end':
        viable.append(path)
        return
    accessible = [
        n for n in conns[path[-1]]
        if n not in cant_visit
    ]
    for a in accessible:
        new_has_double = has_double
        if a in path and a.islower():
            new_cant_visit = [n for n in path if n.islower()] + ['start']
            new_has_double = True
        elif has_double and a.islower():
            new_cant_visit = cant_visit + [a]
        else:
            new_cant_visit = cant_visit
        paths(path + [a], new_cant_visit, new_has_double)

paths(path, cant_visit, False)

print(len(viable))
