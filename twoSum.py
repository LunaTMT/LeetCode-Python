class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bad solution 02/2023
        for idx_i, value_i in enumerate(nums):
            for idx_j, value_j in enumerate(nums):
                if idx_i != idx_j:
                    if value_i + value_j == target:
                        return [idx_i, idx_j]

    #06/2023
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            remainder = target - value
            
            if remainder in seen:
                return (seen[remainder], i)
            else:
                seen[value] = i
        return False
