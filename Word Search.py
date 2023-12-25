def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def dfs(r, c, k):
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        temp = board[r][c]
        board[r][c] = '#'  

        # up, down, right, left
        found = dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1)

       
        board[r][c] = temp
        return found


    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):  
                return True

    return False


board = [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
word = "AAB"

exist(board, word)