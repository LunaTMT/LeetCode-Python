def arrayPairSum(self, nums: list[int]) -> int:
    nums.sort()
    return sum(nums[i] for i in range(0, len(nums), 2))