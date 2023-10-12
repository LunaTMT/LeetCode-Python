def mergeSimilarItems(self, a1: List[List[int]], a2: List[List[int]]) -> List[List[int]]:
    count = Counter()
    for v, w in a1 + a2:
        count[v] += w
    return sorted(count.items())