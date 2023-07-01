def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
    R1 = m-1
    R2 = n-1
    i = (m+n)-1

    while R1 >= 0 and R2 >= 0:
        if nums1[R1] > nums2[R2]:
            nums1[i] = nums1[R1]
            R1 -= 1
        else:
            nums1[i] = nums2[R2]
            R2 -= 1
        i -= 1

    if R2 >= 0:
        nums1[:R2+1] = nums2[:R2+1]
