def arrayPairSum(nums: list[int]) -> int:
    nums.sort()
    return sum(nums[i] for i in range(0, len(nums), 2))

    
    return sum(sorted(nums)[::2])

arrayPairSum([1,4,3,2])