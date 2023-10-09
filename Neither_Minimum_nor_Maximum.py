def findNonMinOrMax(nums: list[int]) -> int:
    """
    O(1)
    """
    return -1 if len(nums) < 3 else sum(nums[:3]) - min(nums[:3]) - max(nums[:3])
    
    return -1 if len(nums) < 3 else sorted(nums[:3])[1]
    """
    O(nlogn) solution
    """
    n = len(nums)

    if n == 2:
        return -1

    nums.sort()

    first = nums[0]
    for i in range(1, n):
        if nums[i] != first:
            return nums[i]
    return -1

