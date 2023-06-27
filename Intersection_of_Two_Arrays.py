def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()

    print(nums1, nums2)
    
    if len(nums1) < len(nums2):
        smallest = nums1
        largest  = nums2
    else:
        smallest = nums2
        largest  = nums1

    l = r = 0
    res = []
    while l < len(smallest):
        left  = smallest[l]
        right = largest[r]

        if left == right :
            res.append(left)
            l += 1
            r += 1

        elif left < right:
            l += 1
        else:
            r += 1

    return res

if __name__ == "__main__":
    intersection([1], [1, 1])