def reverseStr(s: str, k: int) -> str:
    s = [*s]
    n = len(s)
    for i in range(0, n, 2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)


reverseStr("abccdefghgh", 3)
#3
#abc cde fgh gh
#cba cde fgh hg

#bacd