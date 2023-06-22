def firstPalindrome(self, words: List[str]) -> str:

    #For the sake of using pointers
    pali = False
    for word in words:
        l, r = 0, len(word)-1
        
        while l <= r:
            if word[l] != word[r]:
                pali = False
                break
            
            pali = True
            l, r = l+1, r-1
        
        if pali: return word

    return ""

    #Ez solution
    for word in words:
        if word == word[::-1]: return word
    return ""