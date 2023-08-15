def rearrangeCharacters(self, s: str, target: str) -> int:
    s = {c : s.count(c) for c in set(target)}
    target = {c : target.count(c) for c in set(target)}
    return min((s[t] // target[t] for t in target.keys()))
    