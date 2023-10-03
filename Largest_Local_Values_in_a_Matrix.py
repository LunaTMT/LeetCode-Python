def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    res =[]
    print(res)
    for i in range(n-2):
        row = []
        for j in range(n-2):
            row.append(max(max(grid[i+x][j:j+3]) for x in range(3)))
        res.append(row)
            

largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])