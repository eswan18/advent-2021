from collections import Counter


with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]
template = lines[0]
rules = {
    tuple(l.split(' -> ')[0]): l.split(' -> ')[1]
    for l in lines[2:]
}

for _ in range(10):
    pairs = zip(template, template[1:])
    insertions = []
    for index, pair in enumerate(pairs):
        if pair in rules:
            insertions.append(rules[pair])
        else:
            insertions.append('')
    # Insertions will have one fewer element.
    insertions.append('')
    new_str = ''.join(i + j for i, j in zip(template, insertions))
    template = new_str

counter = Counter(template)
freqs = counter.values()
result = max(freqs) - min(freqs)

print(result)
