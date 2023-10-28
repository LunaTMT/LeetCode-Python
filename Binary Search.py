def search(nums: list[int], target: int) -> int:
    
    def bs(l, r):
        while l < r:
            m = r-l//2
            if nums[m] == target: 
                return m
            elif nums[m] < target:
                return bs(m+1, r) 
            else:
                return bs( l, m-1) 
        return -1
    return bs(0, len(nums-1))

search(nums = [-1,0,3,5,9,12], target = 9)