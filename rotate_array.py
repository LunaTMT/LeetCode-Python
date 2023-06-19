def rotate(self, nums: List[int], k: int) -> None:
        
    def rotate_section(l, r):
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    
    k %= len(nums)

    rotate_section(0, len(nums)-1)
    rotate_section(0, k-1)
    rotate_section(k, len(nums)-1)