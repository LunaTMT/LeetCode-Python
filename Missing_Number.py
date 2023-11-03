def missingNumber(self, nums: List[int]) -> int:    
    
    return reduce(lambda x, y: x^y, list(range(len(nums)+1)) + nums)
    reduce(lambda acc, x: acc ^ x[0] ^ x[1], enumerate(nums), len(nums))
    
    #Gauss
    n = len(nums)
    return (n*(n+1)//2) - sum(nums)