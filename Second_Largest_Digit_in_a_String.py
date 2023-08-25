def secondHighest(self, s: str) -> int:
    found = set()
    res = []
    for c in set(s):
        if c.isdigit() and c not in found:
            found.add(c)
    return int(sorted(found)[-2]) if len(found) > 1 else -1
