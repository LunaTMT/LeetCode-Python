def runningSum(self, nums: List[int]) -> List[int]:
    res = []
    sums = 0
    for i in nums:
        sums += i
        res.append(sums)
    return res