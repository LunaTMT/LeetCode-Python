 def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        
        for i in range(n):
            l = 0
            r = n-1
        
            while l <= r:    
                image[i][l] = 1 if image[i][l] == 0 else 0                
                if l != r:
                    image[i][r] = 1 if image[i][r] == 0 else 0
                    image[i][l], image[i][r] = image[i][r], image[i][l]
                l += 1
                r -= 1

        return image

if __name__ == "__main__":
     flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])