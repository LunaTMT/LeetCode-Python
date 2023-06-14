
def removeDuplicates(nums: list[int]) -> int:
    unique = ""
    idx = 0

    for e in nums:
        if e != unique:
            unique = e
            nums[idx] = unique
            idx += 1
    return idx
  
if __name__ == "__main__":
    removeDuplicates([1,1,2])