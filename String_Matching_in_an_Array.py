def stringMatching(self, words: List[str]) -> List[str]:
    res = []
    for i, w1 in enumerate(words):
        for j, w2 in enumerate(words):
            if w1 in w2 and i != j:
                res.append(w1)
                break
    return res