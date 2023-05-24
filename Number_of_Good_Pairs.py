from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:

        res = 0
        for n in Counter(nums).values():
            if n > 1:
                n -= 1
                res += n*(n+1) / 2
        return int(res)
    
    #sum of first n integers
