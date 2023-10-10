def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
    max_ = 0
    row = 0
    for i, r in enumerate(mat):
        ones = r.count(1)
        if ones > max_:
            max_ = ones
            row = i
    return (row, max_)

    """
    OR
    """

    ones = []
    for i, r in enumerate(mat):
        ones.append([i, r.count(1)])
    ones.sort(key=lambda x:[-x[1],x[0]])
    return ones[0]