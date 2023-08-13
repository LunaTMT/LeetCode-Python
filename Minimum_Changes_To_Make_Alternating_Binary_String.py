def minOperations(s: str) -> int:

    n = len(s)
    t = s[::2].count('0') + s[1::2].count('1')
    return min(t, n - t)


minOperations(s ="01010")