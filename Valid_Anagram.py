def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

    #OR
    
    s = sorted([*s])
    t = sorted([*t])

    return s == t