def largeGroupPositions(self, s: str) -> List[List[int]]:
    letter = s[0]
    start = 0
    group = ""
    res = []
    for stop, c in enumerate(s):
        if c != letter:
            if len(group) >= 3:
                res += [[start, stop-1]]
            group = c
            letter = c
            start = stop
        else:
            group += c
    
    return res + [[start, stop]] if len(group) >= 3 else res