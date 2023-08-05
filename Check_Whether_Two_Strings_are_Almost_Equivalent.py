from collections import Counter

def checkAlmostEquivalent(w1: str, w2: str) -> bool:
    w1_count = Counter(w1)
    w2_count = Counter(w2)

    letters = set(w1).union(set(w2))
    for c in letters:
        if abs(w1_count[c] - w2_count[c]) > 3:
            return False
    return True

w1 = "abcdeef"
w2 = "abaaacc"
checkAlmostEquivalent(w1, w2)