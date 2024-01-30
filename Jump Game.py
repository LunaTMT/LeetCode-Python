def canJump(nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

canJump(nums = [2,3,1,1,4])