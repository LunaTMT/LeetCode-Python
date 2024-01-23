def rotate(self, nums, k):
    n = len(nums)
    k %= n
    # Reverse the entire array
    nums.reverse()

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Reverse the remaining n-k elements
    nums[k:] = reversed(nums[k:])
