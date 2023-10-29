def findFinalValue(self, nums: List[int], target: int) -> int:
    nums = set(nums)
    while target in nums:
        target *= 2
    return target