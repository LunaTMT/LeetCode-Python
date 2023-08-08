def findTheDifference(self, s: str, t: str) -> str:
    for c in set(t):
        if s.count(c) != t.count(c): return c