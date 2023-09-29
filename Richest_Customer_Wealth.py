def maximumWealth(self, arr: List[List[int]]) -> int:
    return max(sum(i) for i in arr)