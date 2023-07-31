def similarPairs(self, words: List[str]) -> int:
    words = [''.join(sorted(set(word))) for word in words]
    counter = Counter(words)
    res = 0
    for v in counter:
        count = counter[v]
        res += (count* (count-1))//2
    return res