def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    MAD = min((abs(arr[i] - arr[i-1]) for i in range(1, n)))
    return [[arr[i-1], arr[i]] for i in range(1, n) if arr[i] - arr[i-1] == MAD]
            