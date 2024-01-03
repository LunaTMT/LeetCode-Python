from typing import List

def rob(nums: List[int]) -> int:
    curr, prev = 0,0
    for n in nums:
        curr, prev =  max(prev+n, curr), curr
    return curr

rob(nums = [2,7,9,3,1])