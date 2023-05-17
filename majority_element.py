import math
def majorityElement(self, nums: list[int]) -> int:
    majority = math.floor(len(nums)/2)
    if len(nums) == 1: return nums[0]

    c = {} #counts

    for i in nums:
        if i in c:
            c[i] += 1
            if c[i] > majority: return i
        else:
            c[i] = 1
            
if __name__ == "__main__":
    majorityElement([1, 2])