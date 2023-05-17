class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
    
if __name__ == "__main__":
    numArray =  NumArray([-2, 0, 3, -5, 2, -1])
    numArray.sumRange(0, 2)