def floodFill(self, image: List[List[int]], sr: int, sc: int, colour: int) -> List[List[int]]:
    start_colour = image[sr][sc]

    def fill(r, c):
        if not (0 <= r < len(image)) or not(0 <= c < len(image[0])):
            return

        if image[r][c] == colour or image[r][c] != start_colour:
            return
        
        image[r][c] = colour

        fill(r-1, c)
        fill(r+1, c)
        fill(r, c-1)
        fill(r, c+1)
    
    fill(sr, sc)
    return image
