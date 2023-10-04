def maximizeSum(nums: list[int], k: int) -> int:
    return sum(max(nums) + i for i in range(k))
    
    """ or
    m = max(nums)
    return k*(2*m + k - 1) // 2
    """