def maxSubArray(nums: list[int]) -> int:
    
    
    dp = [[0]*len(nums) for i in range(2)]
    dp[0][0], dp[1][0] = nums[0], nums[0]
    for i in range(1, len(nums)):
        dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
        dp[0][i] = max(dp[0][i-1], dp[1][i])
    return dp[0][-1]


    """
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub
    """
    """
    ans = -inf
    n = len(nums)
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            ans = max(ans, sum_)
    return ans"""

maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])