def squareIsWhite(coord: str) -> bool:
    letter = (ord(coord[0]) - 96)
    number = int(coord[1])
    
    if not letter % 2:
        return True if number % 2 else False
    return False if number % 2 else True
