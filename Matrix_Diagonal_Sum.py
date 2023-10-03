def diagonalSum(self, arr: List[List[int]]) -> int:
    n = len(arr)
    mid = n // 2
    res = sum(arr[i][i] + arr[i][n-1-i] for i in range(n))
    
    if n % 2 == 1:
        res -= arr[mid][mid]
    return res