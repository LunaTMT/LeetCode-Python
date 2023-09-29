def countPairs(nums: list[int], target: int) -> int:
    nums.sort()

    l = 0
    r = len(nums)-1
    res = 0
    while l < r:
        if nums[l] + nums[r] < target:
            res += r-l
            l += 1
        else:
            r -= 1
    return res


countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2)