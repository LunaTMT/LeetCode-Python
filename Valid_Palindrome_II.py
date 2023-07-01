def validPalindrome(s: str) -> bool:        
    def validate(l, r, s, deleted=False):
        while l < r:
            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    return validate(l+1, r, s, True) or validate(l, r-1, s, True)
            else:
                l, r = l+1, r-1
        return True
    
    return validate(0, len(s)-1, s)

check = validPalindrome("abc")
print()
