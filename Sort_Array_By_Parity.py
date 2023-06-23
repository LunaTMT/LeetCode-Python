def sortArrayByParity( nums: list[int]) -> list[int]:
    l, r = 0, len(nums)-1
    
    while l < r:    
        if nums[l] % 2 == 1:
            if nums[r] % 2 == 1:
                while r > l:
                    r -= 1
                    if nums[r] % 2 == 0:
                        break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        else:
            l += 1

    return nums


        

if __name__ == "__main__":
    sortArrayByParity([0, 2])
