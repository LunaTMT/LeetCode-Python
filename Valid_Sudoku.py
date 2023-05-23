
#DIGUSTING CODE


def check_duplicates(lists):
    for list_ in lists:
        count = {i:list_.count(i) for i in set(list_)}
        for k, v in count.items(): 
            if v > 1 and k != ".":
                return True
    return False

def check_row(r):
    count = {i:r.count(i) for i in set(r)}
    for k, v in count.items(): 
        if v > 1 and k != ".":
            return True
    return False
    


def isValidSudoku(board: list[list[str]]) -> bool:

    cubes = { "0": [],
                "3": [],
                "6": []}
    
    columns = {  "0": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": []}
    
    
    for i in range(9): #row
        if check_row(board[i]): return False
        
        for j in range(9):
            j_str = str(j)
            if j in (0, 3, 6): cubes[j_str] += (board[i][j:j+3])
            columns[j_str].append(board[i][j])

        if i in (2, 5, 8):
            if check_duplicates(cubes.values()): return False
            cubes = { "0": [],
                     "3": [],
                     "6": []}
            
    if check_duplicates(columns.values()): return False
    return True    

if __name__ == "__main__":
    board = [[".",".",".",".",".",".","5",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             ["9","3",".",".","2",".","4",".","."],
             [".",".","7",".",".",".","3",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".","3","4",".",".",".","."],
             [".",".",".",".",".","3",".",".","."],
             [".",".",".",".",".","5","2",".","."]]
    isValidSudoku(board)
