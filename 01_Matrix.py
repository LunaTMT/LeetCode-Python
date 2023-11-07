def updateMatrix( mat: list[list[int]]) -> list[list[int]]:
    rows = len(mat)
    columns = len(mat[0])
    res = []

    def rec(sr, sc, r, c): 
        if not (0 <= r < rows) or not (0 <= c < columns): return
        
        if mat[r][c] == 0: 
            distance = min(abs(sr - r), abs(sc - c))
            if distance < mat[sr][sc]:
                mat[sr][sc] = distance
                return

        rec(sr, sc, r-1, c)
        rec(sr, sc, r+1, c)
        rec(sr, sc, r, c-1)
        rec(sr, sc, r, c+1)

        #distance = min(abs(r - closest[0]), abs(c - closest[1]))

    

    for sr in range(rows):
        row = []
        for sc in range(columns):
            if mat[sr][sc] == 0:
                row.append(0)
            else:
                rec(sr, sc, sr, sc)
        res.append(row)
    return res

updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]])