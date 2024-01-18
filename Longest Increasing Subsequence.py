from bisect import bisect_left

def lengthOfLIS(nums: list[int]) -> int:
    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)
        else:
            idx = bisect_left(sub, x)  # Find the index of the first element >= x
            sub[idx] = x  # Replace that number with x
    return len(sub)

lengthOfLIS([10,9,2,5,3,7,101,18])