from collections import deque
def sortedSquares(nums: list[int]) -> list[int]:
    #Two pointers
    n = len(nums)
    A = n * [0]
    pL, pR = 0, n-1
    pW = pR

    L = nums[pL] ** 2
    R = nums[pR] ** 2

    while pW >= 0:
        if L > R:
            A[pW] = L
            pL += 1
            L = nums[pL] ** 2
        else:
            A[pW] = R
            pR -= 1
            R = nums[pR] ** 2
        pW -= 1
    return A
        
    #Deque 

    deq = deque(nums)
    n = len(nums)
    pL = 0
    pW = pR = n-1
    res = [0] * n

    while deq:
        L = nums[pL] ** 2
        R = nums[pR] ** 2
        if L > R:
            res[pW] = L
            pL += 1
            deq.popleft()
        else:
            res[pW] = R
            pR -= 1
            deq.pop()
        pW -= 1
    return res
        

sortedSquares(nums = [-4,-1,0,3,10])