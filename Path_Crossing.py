def isPathCrossing(self, path: str) -> bool:
    x, y = 0, 0
    positions = {(x, y)}
    
    for p in path:
        match p:
            case "N":
                y -= 1
            case "S":
                y += 1
            case "E":
                x += 1
            case "W":
                x -= 1
        if (x, y) in positions:
            return True
        else:
            positions.add((x, y))
    return False
            