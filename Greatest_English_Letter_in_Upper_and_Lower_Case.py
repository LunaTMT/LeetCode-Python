def greatestLetter(self, s: str) -> str:
    s = set(s)

    for i in range(90, 54, -1):
        c = chr(i)
        if c.lower() in s and c in s:
            return c
    return ""