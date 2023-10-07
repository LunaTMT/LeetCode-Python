def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    sequence = set([i for i in range(1, len(nums)+1)])
    nums = set(nums)
    return sequence - nums