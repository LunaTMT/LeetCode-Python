def replaceDigits(self, s: str) -> str:
    s = [*s]
    for i in range(1, len(s), 2):
        s[i] = chr(ord(s[i-1]) + int(s[i]))
    return "".join(s)