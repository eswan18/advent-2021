def hex2bits(code: str) -> str:
    return format(int(code, base=16), 'b')

def bits2int(code: str) -> int:
    return int(code, base=2)
