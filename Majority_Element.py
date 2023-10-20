def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    return nums[n//2]
    
    count = defaultdict(int)
    n = len(nums)
    for i in nums:
        count[i] += 1
        if count[i] > n//2:
            return i