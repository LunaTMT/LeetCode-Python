from collections import deque

"""So hard to understand    """

def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    rows, columns = len(mat), len(mat[0])
    DIR = [(0,1),(1,0),(0,-1),(-1,0)] # RDLU

    q = deque([])
    for r in range(rows):
        for c in range(columns):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1  # Marked as not processed yet!

    while q:
        r, c = q.popleft()
        for a,b in DIR:
            nr,nc = a+r, b+c
            if nr < 0 or nr == rows or nc < 0 or nc == columns or mat[nr][nc] != -1: continue
            mat[nr][nc] = mat[r][c] + 1
            q.append((nr, nc))
    return mat

updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])