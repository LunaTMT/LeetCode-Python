def minSubsequence(self, nums: List[int]) -> List[int]:
    nums.sort(reverse=1)
    total = sum(nums)
    ss = []
    ss_sum = 0
    
    for i in nums:
        ss.append(i)
        
        total -= i
        ss_sum += i

        if ss_sum > total:
            break
    return ss