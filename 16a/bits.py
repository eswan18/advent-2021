def hex2bits(code: str) -> str:
    s = format(int(code, base=16), '0b')
    over_4 = len(s) % 4
    if over_4:
        fill = 4 - over_4
        s = '0' * fill + s
    return s

def bits2int(code: str) -> int:
    return int(code, base=2)
