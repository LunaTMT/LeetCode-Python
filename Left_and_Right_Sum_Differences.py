def leftRightDifference(self, nums: List[int]) -> List[int]:
    L = 0
    R = sum(nums[1:])
    res = [R]
    for i in range(1, len(nums)):
        L += nums[i-1]
        R -= nums[i]
        res.append(abs(L-R))
    return res