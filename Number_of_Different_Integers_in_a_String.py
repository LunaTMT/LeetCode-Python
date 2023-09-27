def numDifferentIntegers(self, s: str) -> int:
    return len(set(int(i) for i in re.findall(r"\d+", s) if i.isnumeric()))

