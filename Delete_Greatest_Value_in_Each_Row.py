def deleteGreatestValue(grid: list[list[int]]) -> int:
    for row in grid: row.sort()
    return sum(max(col) for col in zip(*grid))

deleteGreatestValue(grid = [[1,2,4],[3,3,1]])