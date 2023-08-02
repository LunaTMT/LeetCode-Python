def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    s1_set = set(s1)
    s2_set = set(s2)
    
    res = []
    for word in (s1_set.union(s2_set) - s1_set.intersection(s2_set)):
        if s1.count(word) == 1 or s2.count(word) == 1:
            res += [word]
    return res