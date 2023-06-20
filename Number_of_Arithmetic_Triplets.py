from collections import Counter
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hash_ = Counter(nums)

        count = 0
        for i in nums:
            if i-diff in hash_ and i+diff in hash_:
                count += 1
            
        return count
