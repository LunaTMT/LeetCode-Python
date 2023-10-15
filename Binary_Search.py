"""
Binary search works upon sorted arrays

p, q, r = start, mid, end

We take the midpoint of the array and ask ourselves whether our target is larger or smaller than
the value currently at the midpoint.

If it is larger we set p = mid and recalculate q

the midpoint is calculated as follows:
(p + r) // 2
"""

#Itertive
def search(A: list[int], target: int) -> int:
        p, r = 0, len(A)-1
        while p <= r:
            q = (p+r) // 2
            if target == A[q]:
                return q
            elif target > A[q]:
                p = q + 1
            else:
                r = q - 1
        
        return -1

def search_Recusive(A, target, p, q, r):
    while p <= r:
        q = (p+r) // 2
        if target == A[q]:
            return q
        elif target > A[q]:
            return search_Recusive(A, target, q+1, 0, r)         
        else:
            return search_Recusive(A, target, p, 0, q-1)     
    return -1


A = [-1,0,3,5,9,12]

print(search(A, target = 2))

print(search_Recusive(A, target = 2, p=0, q=0, r=len(A)-1))