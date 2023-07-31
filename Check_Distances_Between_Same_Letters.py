def checkDistances(s: str, distance: list[int]) -> bool:
    done = set()
    
    for i, c in enumerate(s):
        if c not in done:
            for j in range(i+1, len(s)):
                if s[j] == c:
                    break
            if ((j-1)-i) != distance[ord(c)-97]:
                return False
        done.add(c)
    return True

checkDistances("abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])