from collections import defaultdict

#O(n)
def countKDifference(nums: list[int], k: int) -> int:
    seen = defaultdict(int)
    counter = 0
    for num in nums:
        counter += seen[num-k] + seen[num+k]
        seen[num] += 1
    return counter

#O(n^2)
def countKDifference(self, nums: List[int], k: int) -> int:
    n = len(nums)
    return len([i for i in range(n) for j in range(i+1, n) if abs(nums[i] - nums[j]) == k])

countKDifference(nums = [1,2,2,1], k = 1)