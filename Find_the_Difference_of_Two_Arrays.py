def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    
    a = set(nums1)
    b = set(nums2)
    return (list(a-b), list(b-a))

    #OR the slower 
    # return [[i for i in set(nums1) if i not in nums2], [j for j in set(nums2) if j not in nums1]]
       
