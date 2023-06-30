def backspaceCompare(s: str, t: str) -> bool:
    s = [*s]
    t = [*t]

    def remove_hash_tag(s):
        remove = 0
        r = len(s)-1
        while remove >= 0:
            if s[r] == "#":
                remove += 1
                s.pop(r)
            
            elif remove > 0:
                remove -= 1
                s.pop(r)

            r -= 1  
        return s
        
    return remove_hash_tag(s) == remove_hash_tag(t)

backspaceCompare("a#c", "b")
            
