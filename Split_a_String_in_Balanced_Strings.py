def balancedStringSplit(s: str) -> int:

    l = r = 0
    res = 0
    for c in s:
        if l > 0 and r > 0 and c == "R":
            res += 1
            l = r = 0
            
        if c == "R":
            r += 1
        elif c == "L":
            l += 1
    return res

balancedStringSplit("RL RRLL RL RL")