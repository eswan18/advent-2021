from itertools import count


with open('input.txt', 'rt') as f:
    lines = [line.strip() for line in f.readlines()]

def most_common(it):
    it = list(it)
    ones = it.count('1')
    zeros = it.count('0')
    if ones >= zeros:
        return '1'
    else:
        return '0'

# Oxygen
values = lines.copy()
for i in count():
    col = [v[i] for v in values]
    keep = most_common(col)
    values = [v for v in values if v[i] == keep]
    if len(values) <= 1:
        break
oxygen, *_ = values
oxygen_int = int(oxygen, base=2)


# CO2
values = lines.copy()
for i in count():
    col = [v[i] for v in values]
    keep = '1' if most_common(col) == '0' else '0'
    values = [v for v in values if v[i] == keep]
    if len(values) <= 1:
        break
co2, *_ = values
co2_int = int(co2, base=2)

result = oxygen_int * co2_int
print(result)
