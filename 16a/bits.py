def hex2bits(code: str) -> str:
    # Leading zeroes caused a terrible bug.
    n_zero = 0
    while code.startswith('0'):
        n_zero += 1
        code = code[1:]
    s = format(int(code, base=16), '0b')
    over_4 = len(s) % 4
    if over_4:
        fill = 4 - over_4
        s = '0' * fill + s
    for _ in range(n_zero):
        s = '0000' + s
    return s

def bits2int(code: str) -> int:
    return int(code, base=2)
