def allCellsDistOrder(self, R: int, C: int, rCenter: int, cCenter: int) -> List[List[int]]:
    """
    The problem is akward to understand but after looking at a solution it becomes 
    apparent what it is asking for.

    Create positions list (r, c) for the 2d matrix (range(R), range(C)

    sort by the distance function provided
    """
    
    def dist(coord):
        r, c = coord
        return abs(rCenter - r) + abs(cCenter - c)
    
    matrix = [(i,j) for i in range(R) for j in range(C)]
    return sorted(matrix, key=dist)