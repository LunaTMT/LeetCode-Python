def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
    most = max(candies)
    return [True if c+extra >= most else False for c in candies]