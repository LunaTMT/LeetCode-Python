def minTimeToType(word: str) -> int:
    res, current = len(word), "a"
    
    for c in word:
        right = abs(ord(c) - ord(current))
        left = 26 - right
        res += min(left, right)
        current = c 
    return res


minTimeToType("zjpc")