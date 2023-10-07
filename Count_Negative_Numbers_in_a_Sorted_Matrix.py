def countNegatives(grid: list[list[int]]) -> int:

    """
    This alogorithm uses binary search, O(mlogn)
    """ 
    def binary_search(row):
        start, end = 0, len(row)
        while start < end:
            mid = start + (end - start) // 2
            if row[mid] < 0:
                end = mid
            else:
                start = mid+1
        return len(row) - start
    return sum(binary_search(row) for row in grid)
    
    """
    O(m+n)
    Finding first negative instance and going to the next row
    """
    i, j = len(grid)-1, 0
    columns = len(grid[0])
    res = 0
    while i >= 0 and j < columns:
        if grid[i][j] < 0:
            res += (columns - j)
            i -= 1
            j = 0
        else:
            j += 1
    return res

    """
    O(n^2)
    Iterate through 2d matrix 
    return sum(1 for row in grid for item in row if item < 0)
    """

countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])