def frequencySort(self, A: List[int]) -> List[int]:
    count = Counter(A)
    return sorted(A, key=lambda x: (count[x], -x))