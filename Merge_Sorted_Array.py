nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
m = 3
n = 3

R1 = m-1
R2 = n-1
i = (m+n)-1

while R1 >= 0 and R2 >= 0:
    n1_val = nums1[R1]
    n2_val = nums2[R2]
    

    if n1_val > n2_val:
        nums1[i] = n1_val
        R1 -= 1
    else:
        nums1[i] = n2_val
        R2 -= 1
    i -= 1

if R2 >= 0:
    nums1[:R2] = nums2[:R2]

print()