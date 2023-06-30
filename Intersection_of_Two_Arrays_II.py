def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        l1 = l2 = 0
        res = []
        while l1 < len(nums1) and l2 < len(nums2):
            n1 = nums1[l1]
            n2 = nums2[l2]
            
            if n1 < n2:
                l1 += 1
            elif n2 < n1:
                l2 += 1
            else: 
                res.append(n1)
                l1, l2 = l1 + 1, l2 + 1
            
        return res
                