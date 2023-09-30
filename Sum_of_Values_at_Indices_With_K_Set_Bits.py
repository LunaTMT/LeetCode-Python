def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
    return sum([nums[i] for i in range(len(nums)) if bin(i).count('1') == k])

"""
OR

     res = 0
        for i, num in enumerate(nums):
            if i.bit_count() == k:
                res += num
        return res
"""
    
