class Solution:
    def sortColors(self, nums: list[int]) -> None:
        #RWB - 012
        #Bucket sort - but this is not one pass

        l, r = 0, len(nums)-1
        i = 0

        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        while(i <= r):
            if nums[i] == 0:
                swap(l, i)
                l += 1
                #swap with left pointer pos and increase L

            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
                #swap with right pointer pos and decrease R
                
            i += 1