def reverseVowels(self, s: str) -> str:
    l, r = 0, len(s)-1
    s = [*s]
    vowels = "aeiouAEIOU"
    
    while l < r:
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
    return "".join(s)