class Solution:
    def pacificAtlantic(self, arr: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(arr), len(arr[0])
        atl, pac = set(), set()

        def dfs(r, c, visit, previousHeight):
            if ((r, c) in visit or  
            r < 0 or c < 0 or 
            r >= ROWS or c >= COLS or
            arr[r][c] < previousHeight):
                return
            
            visit.add((r, c))
            dfs(r + 1, c, visit, arr[r][c])
            dfs(r - 1, c, visit, arr[r][c])
            dfs(r, c + 1, visit, arr[r][c])
            dfs(r, c - 1, visit, arr[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, arr[0][c])
            dfs(ROWS-1, c, atl, arr[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, arr[r][0])
            dfs(r, COLS-1, atl, arr[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append((r, c))
        return res