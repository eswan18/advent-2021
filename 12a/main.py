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

viable = []
def paths(path: list[str]) -> list[list[str]]:
    if path[-1] == 'end':
        viable.append(path)
        return
    accessible = [
        n for n in conns[path[-1]]
        if n.isupper() or n not in path
    ]
    [paths(path + [a]) for a in accessible]

paths(path)

print(len(viable))
