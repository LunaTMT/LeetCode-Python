#bad solution

def countBinarySubstrings(s: str) -> int:

    l = r = 0
    
    current_count = 0
    opposite_count = 0
    res = 0
    while l < len(s)-1:
        current = s[l]
        
        try:
            while s[r] == current:
                current_count += 1
                r += 1
        except:
            pass
        
        l = r

        try:
            while s[r] != current:
                opposite_count += 1
                r += 1
        except:
            pass

        
        r = l

        res += min(current_count, opposite_count)
        current_count = opposite_count = 0


if __name__ == "__main__":
    countBinarySubstrings("00110011")
