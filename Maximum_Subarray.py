def maxSubArray(self, nums: List[int]) -> int:
    ans = -inf
    n = len(nums)
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            ans = max(ans, sum_)
    return ans

# or

    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub