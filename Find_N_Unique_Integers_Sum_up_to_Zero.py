def sumZero(self, n: int) -> List[int]:
    """
    simpler
    """
    return range(1 - n, n, 2)

    """
    OR
    """
    if n == 1:
        return [0]
    
    res = []
    R = n//2

    for i in range(1, R+1):
        res.append(i)
    
    if n%2 == 1:
        res.append(0)

    for j in range(-R, 0):
        res.append(j)
    
    return res


