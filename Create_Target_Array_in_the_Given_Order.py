def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
    n = len(nums)
    arr = []

    for i in range(n):
        if index[i] == len(arr):
            arr.append(nums[i])
        else:
            arr = arr[:index[i]] + [nums[i]] + arr[index[i]:]
    return arr

createTargetArray(nums = [4,2,4,3,2], index = [0,0,1,3,1])

#[2,2,4,4,3]