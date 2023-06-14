def validPalindrome(s: str) -> bool:

    def validate(s, l, r, deleted):
        while l < r:
            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    return validate(s, l+1, r, True) or validate(s, l, r-1, True)
            else:
                l+=1
                r-=1
        return True 
    return validate(s, 0, len(s) - 1, False)

if __name__ == "__main__":
     validPalindrome("abca")