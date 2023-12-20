
def uniquePaths(m: int, n: int) -> int:
        curr_row = [1] * n
        prev_row = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                curr_row[j] = curr_row[j - 1] + prev_row[j]    
            curr_row, prev_row = prev_row, curr_row
        
        return prev_row[-1]

uniquePaths(m = 3, n = 7)


def uniquePaths(self, rows: int, cols: int) -> int:
    dp = [[1 if (c == 0 or r == 0) else 0 for c in range(cols)] for r in range(rows)]     
    
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    for row in dp:
        print(row)

    return dp[-1][-1]