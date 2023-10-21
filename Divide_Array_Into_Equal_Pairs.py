def divideArray(self, nums: List[int]) -> bool:
    """
    Symmetric difference
    """
    seen = set()
    for n in nums:
        seen ^= {n}
    return not seen
    
    #OR
    count = Counter(nums)
    for i in count:
        if count[i] % 2 == 1:
            return False
    return True