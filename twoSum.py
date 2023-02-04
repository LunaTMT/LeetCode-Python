class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx_i, value_i in enumerate(nums):
            for idx_j, value_j in enumerate(nums):
                if idx_i != idx_j:
                    if value_i + value_j == target:
                        return [idx_i, idx_j]