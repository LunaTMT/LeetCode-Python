class Solution:
    
    #2 log(n)
    def search(self, nums: List[int], target: int) -> int:
        
        def find_pivot(s, e):
            if s <= e:
                k = (s + e) // 2

                if k > 0 and nums[k] < nums[k - 1]:
                    return k  
                elif nums[k] >= nums[s] and nums[k] > nums[e]:
                    return find_pivot(k + 1, e)
                else:
                    return find_pivot(s, k - 1)
            return 0  

        def bs(s, e):
                if s <= e:
                    m = (s + e) // 2

                    if target == nums[m]:
                        return m
                    elif target > nums[m]:
                        return bs(m + 1, e)
                    else:
                        return bs(s, m - 1)
                return -1
        
        s = 0
        e = len(nums)-1
        k = find_pivot(s, e)

        if k == 0 or target < nums[0]:
            return bs(k, e)
        else:
            return bs(0, k-1)


    #log(n)
    def search(self, nums: List[int], target: int) -> int:
        def bs(s, e):
            if s <= e:
                m = (s + e) // 2
                start = nums[s]
                mid = nums[m]
                end = nums[e]

                if target == mid:
                    return m

                if start <= mid:
                    if start <= target <= mid:
                        return bs(s, m - 1)
                    else:
                        return bs(m + 1, e)
                else:
                    if mid < target <= end:
                        return bs(m + 1, e)
                    else:
                        return bs(s, m - 1)
            return -1

        return bs(0, len(nums) - 1)
        
