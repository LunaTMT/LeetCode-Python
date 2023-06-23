def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    l = r = 0
    res = []
    while l != len(nums1) and r != len(nums2):
    
        if nums1[l][0] < nums2[r][0]:
            res += [nums1[l]]
            l += 1
        elif nums1[l][0] > nums2[r][0]:
            res += [nums2[r]]
            r += 1
        else:
            res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
            l += 1
            r += 1  

    if l < len(nums1):
        res += nums1[l:]
    else:
        res += nums2[r:]

    return res
