
def targetIndices(nums, target):
    "O(n)"
    idx = cnt = 0
    for num in nums:
        idx += num < target
        cnt += num == target
    return list(range(idx, idx+cnt))

    "O(nlog(n))"
    nums.sort()
    return (i for i in range(len(nums)) if nums[i] == target)

targetIndices(nums = [1,2,5,2,3], target = 2)