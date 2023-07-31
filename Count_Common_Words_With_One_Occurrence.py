def countWords(self, w1: List[str], w2: List[str]) -> int:
    w1 = Counter(w1)
    w2 = Counter(w2)

    res = 0
    
    for word in set(w1):
        if word in w2 and w1[word] == 1 and w2[word] == 1:
            res += 1
    return res