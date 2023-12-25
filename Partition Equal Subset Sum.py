def canPartition(self, nums: List[int]) -> bool:
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = {0}

    for n in nums:
        new = set() 
        for i in dp:
            new_val = n + i
            if new_val == target:
                return True
            if new_val < target:
                new.add(new_val)
        dp |= new  
    return False
    