def floodFill(image: list[list[int]], sr: int, sc: int, colour: int) -> list[list[int]]:

    def dfs(x, y, startColour):
        if not (0 <= x < len(image)): return   
        if not (0 <= y < len(image[0])): return
        if image[x][y] == colour or image[x][y] != startColour: return

        image[x][y] = colour

        dfs(x-1, y, startColour)
        dfs(x+1, y, startColour)
        dfs(x, y-1, startColour)
        dfs(x, y+1, startColour)
    dfs(sr, sc, image[sr][sc])
    return image

floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)