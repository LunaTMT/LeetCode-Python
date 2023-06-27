
from collections import deque


def findTheArrayConcVal(nums: list[int]) -> int:
    nums = deque(nums)

    res = 0
    while nums:
        
        try:
            v1 = str(nums[0])
            v2 = str(nums[-1])
            nums.pop()
            nums.popleft()
            res += int(v1 + v2)
        except:
            res += int(v1)
            break
            
    return res

if __name__ == "__main__":
    findTheArrayConcVal([5,14,13,8,12])