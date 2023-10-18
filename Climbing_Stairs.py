
"""
Fibonacci seq using memoizationg
can also use 
lcu_cache from functools
"""
def climbStairs(n: int) -> int:
    memo = {}
    return helper(n, memo)

def helper(n, memo):
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = climbStairs(n-1) + climbStairs(n-2)
    return memo[n]

"""
Fibonacci seq using DP
"""
def climbStairs(self, n: int) -> int:
    if n in (0,1):
        return 1

    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

"""
Fibonacci 2 variables, space optimisation
"""
def climbStairs(self, n: int) -> int:
    if n in (0,1):
        return 1

    prev, curr = 1, 1
    for i in range(2, n+1):
        temp = curr
        curr += prev 
        prev = temp
    return curr


climbStairs(4)