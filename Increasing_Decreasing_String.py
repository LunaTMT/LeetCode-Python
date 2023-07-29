def sortString(self, s: str) -> str:
    s = [*s]
    s.sort()
    count = Counter(s)
    res = ""

    while any(count.values()):
        for c in count:
            if count[c] != 0:
                res += c
                count[c] -= 1
            
        for c in reversed(count):
            if count[c] != 0:
                res += c
                count[c] -= 1
    return res