def canPlaceFlowers(fb: list[int], n: int) -> bool:
    if n == 0: return True
    
    #To ensure we dont go out of bounds + flowerless spaces at both ends outside list
    fb = [0] + fb +[0] 
    for i, e in enumerate(fb[1:-1], 1):
        
        if n == 0:
            return True

        elif [fb[i-1], e, fb[i+1]] == [0, 0, 0]: #Adjacent checking
            fb[i] = 1
            n -= 1
    
    return True if n == 0 else False


if __name__ == "__main__":
    canPlaceFlowers([1,0,0,0,1,0,1], 1)