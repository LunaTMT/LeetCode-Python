def kthDistinct(self, arr: List[str], k: int) -> str:
    count = Counter(arr)
    distinct = 0

    for item in count:
        if count[item] == 1:
            distinct += 1
        if distinct == k:
            return item
    return ""
