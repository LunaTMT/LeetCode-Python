from collections import Counter

def checkAlmostEquivalent(w1: str, w2: str) -> bool:
        w1 = Counter(w1)
        w2 = Counter(w2)
        d1 = (w1 - w2)
        d2 = (w2 - w1)
        diff = d1 + d2
        return all(v <= 3 for v in diff.values())


w1 = "abcdeef"
w2 = "abaaacc"
checkAlmostEquivalent(w1, w2)