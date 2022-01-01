with open('input.txt', 'rt') as f:
    lines = (line.strip() for line in f.readlines())

cols = zip(*lines)
def most_common(it):
    it = list(it)
    ones = it.count('1')
    zeros = it.count('0')
    if ones > zeros:
        return '1'
    else:
        return '0'

gamma = ''.join(most_common(c) for c in cols)
gamma_int = int(gamma, base=2)

bin_len = len(gamma)
inverter = int('1' * bin_len, base=2)
epsilon_int = gamma_int ^ inverter

result = gamma_int * epsilon_int
print(result)
