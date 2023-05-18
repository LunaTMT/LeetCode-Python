def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    n = len(nums)
    range_ = set([i for i in range(1, n+1)])
    return range_.difference(set(nums))
     