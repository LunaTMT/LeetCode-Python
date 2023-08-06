def titleToNumber(self, s: str) -> int:
    return sum((26**power) * (ord(c) - 64) for power, c in enumerate(reversed(s)))