from collections import deque

def pivotIndex(nums: list[int]) -> int:
    nums = [0] + nums + [0]
    left = nums[:1]
    right = deque(nums[2:])
    
    for i in range(1, len(nums)-1):
        if sum(left) == sum(right): return i
        else:
            left.append(nums[i])
            right.popleft()

if __name__ == "__main__":
    pivotIndex([1,7,3,6,5,6])