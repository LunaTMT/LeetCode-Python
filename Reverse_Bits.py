def reverseBits( n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res<<1) + (n&1)
        n>>=1
    return res


reverseBits(n = 0b00000010100101000001111010011100)