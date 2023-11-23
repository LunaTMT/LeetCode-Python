from functools import reduce
from typing import List

"""def productExceptSelf(self, nums: List[int]) -> List[int]: 
    nums = [1] + nums + [1]
    
    def accumulate_sums(acc, num):
        acc.append(acc[-1] * num) if acc else acc.append(num)
        return acc

    pre = reduce(accumulate_sums, nums, [])[:-2]
    post = reduce(accumulate_sums, nums[::-1], [])[::-1][2:]
    return (a*b for a, b in zip(pre, post))"""


"""
I dont understand this at all
def productExceptSelf(nums: List[int]) -> List[int]:
    length=len(nums)
    sol=[1]*length
    pre = 1
    post = 1
    for i in range(length):
        sol[i] *= pre
        pre *= nums[i]
        sol[length-i-1] *= post
        post *= nums[length-i-1]
    return(sol)
"""
#makes sense
def productExceptSelf(self, nums: List[int]) -> List[int]: 
    n = len(nums)
    prefix = 1
    res = [1] * n

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res

productExceptSelf(nums = [1,2,3,4])