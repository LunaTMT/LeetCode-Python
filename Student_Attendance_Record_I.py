def checkRecord(self, s: str) -> bool:
    l = 0
    a = 0
    for c in s:
        if c == "L":
            l += 1
        elif c == "A":
            a += 1
            l = 0
        else: 
            l = 0
        if a == 2 or l == 3:
            return False
    return True